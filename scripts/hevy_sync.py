#!/usr/bin/env python3
"""Trae las últimas sesiones desde la API de Hevy y las imprime en el formato
de "paste de Hevy" que la skill manuel-training ya sabe parsear.

Uso:
    python3 scripts/hevy_sync.py --days 14
    python3 scripts/hevy_sync.py --limit 5

API key (requiere Hevy Pro, se genera en hevy.com/settings → developer):
  - env var HEVY_API_KEY, o
  - archivo ~/.config/hevy/api-key (una línea con la key)

Solo stdlib. Si algo falla, imprime el error a stderr y sale con código != 0
para que el agente le pida a Manuel el paste manual como fallback.
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

API_BASE = "https://api.hevyapp.com/v1"
PAGE_SIZE = 10  # máximo que permite la API


def get_api_key() -> str:
    key = os.environ.get("HEVY_API_KEY", "").strip()
    if key:
        return key
    key_file = Path.home() / ".config" / "hevy" / "api-key"
    if key_file.exists():
        key = key_file.read_text().strip()
        if key:
            return key
    sys.exit(
        "ERROR: no hay API key de Hevy. Configurá HEVY_API_KEY o guardala en "
        "~/.config/hevy/api-key (se genera con Hevy Pro en hevy.com/settings)."
    )


def fetch_page(api_key: str, page: int) -> dict:
    url = f"{API_BASE}/workouts?page={page}&pageSize={PAGE_SIZE}"
    req = urllib.request.Request(url, headers={"api-key": api_key})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR: la API de Hevy devolvió HTTP {e.code} ({e.reason}) en {url}")
    except urllib.error.URLError as e:
        sys.exit(f"ERROR: no se pudo conectar a la API de Hevy: {e.reason}")


def parse_time(value: str) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def format_set(i: int, s: dict) -> str:
    parts = []
    weight = s.get("weight_kg")
    reps = s.get("reps")
    duration = s.get("duration_seconds")
    if weight is not None:
        w = int(weight) if float(weight).is_integer() else weight
        parts.append(f"{w} kg")
    if reps is not None:
        parts.append(f"x {reps}" if parts else f"{reps} reps")
    if duration:
        parts.append(f"{duration}s")
    if not parts:
        parts.append("(sin datos)")
    line = f"Set {i}: " + " ".join(parts)
    rpe = s.get("rpe")
    if rpe is not None:
        r = int(rpe) if float(rpe).is_integer() else rpe
        line += f" @ {r} rpe"
    return line


def format_workout(w: dict) -> str:
    start = parse_time(w.get("start_time", ""))
    when = start.strftime("%A, %b %d, %Y at %-I:%M%p").replace("AM", "am").replace(
        "PM", "pm"
    ) if start else "(fecha desconocida)"
    out = [w.get("title") or "Workout", when, ""]
    for ex in w.get("exercises", []):
        out.append(ex.get("title") or "(ejercicio sin nombre)")
        for i, s in enumerate(ex.get("sets", []), start=1):
            out.append(format_set(i, s))
        notes = (ex.get("notes") or "").strip()
        if notes:
            out.append(f"Nota: {notes}")
        out.append("")
    return "\n".join(out).rstrip()


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--days", type=int, default=14, help="traer sesiones de los últimos N días")
    ap.add_argument("--limit", type=int, default=0, help="cortar en N sesiones (0 = sin tope)")
    args = ap.parse_args()

    api_key = get_api_key()
    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days)

    workouts: list[dict] = []
    page = 1
    while True:
        data = fetch_page(api_key, page)
        batch = data.get("workouts", [])
        if not batch:
            break
        stop = False
        for w in batch:
            start = parse_time(w.get("start_time", ""))
            if start and start < cutoff:
                stop = True
                break
            workouts.append(w)
            if args.limit and len(workouts) >= args.limit:
                stop = True
                break
        if stop or page >= int(data.get("page_count", page)):
            break
        page += 1

    if not workouts:
        print(f"No hay sesiones en los últimos {args.days} días.")
        return

    # Más viejas primero, para registrarlas en orden cronológico.
    workouts.reverse()
    print("\n\n---\n\n".join(format_workout(w) for w in workouts))


if __name__ == "__main__":
    main()
