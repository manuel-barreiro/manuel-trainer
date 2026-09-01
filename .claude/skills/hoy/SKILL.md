---
name: hoy
description: Armar la sesión de gym del día para Manuel. Usar cuando invoca /hoy o pregunta qué toca hoy / qué entrena — devuelve el día A/B/Extra que corresponde con pesos, reps objetivo y RPE listos para el gym.
---

# /hoy — la sesión del día

1. Cargá la skill **`manuel-training`** y ejecutá su **Protocolo de arranque** (sync
   con main, semana por fechas, staleness).
2. Determiná qué toca HOY con el calendario del bloque en `CURRENT_PLAN.md` (patrón
   semana impar/par) cruzado con la última sesión registrada:
   - Si hoy no es día de gym → decilo en una línea y tirá la próxima sesión con fecha.
   - Si es **semana de deload** → aplicá la prescripción (~50% series, -10% peso,
     RPE 5-6) sobre la rutina que corresponde.
3. Si falta registrar la sesión anterior, avisalo en UNA línea ("me falta el log del
   [día] — pegalo con /log cuando puedas") y armá la sesión igual con lo último
   conocido; no bloquees.
4. Output pensado para mirar EN el gym desde el celu:
   - Título: `[Día A/B/Extra] — [fecha] · Meso N sem X/6 · [foco: acumulación/pico/deload]`
   - Tabla: Ejercicio | Peso | Series×Reps objetivo | RPE cap — con el orden real de la
     rutina (ej. Pull-Up SIEMPRE 1º en el Extra).
   - Máximo 3 bullets de consignas del momento sacadas de `CURRENT_PLAN.md`
     (consolidaciones, pesos a retomar, "no cazar PRs", etc.). Nada más.
5. Read-only: no toques archivos, salvo corregir el cache de semana si está mal
   (eso sí se commitea y pushea, per protocolo).
