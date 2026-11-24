# Conector de Hevy — Implementation Plan (2026-11-24)

**Goal:** Reemplazar el flujo de paste manual por el conector oficial de Hevy para Claude
(`mcp.hevy.com`, funciona sin Hevy Pro): `/log` sin paste, y el coach escribe la próxima
sesión directamente en las rutinas de Hevy.

**Architecture:** Hevy es la fuente de verdad de **lo hecho** (series, reps, RPE). El repo es
la fuente de verdad de **lo prescripto y el porqué** (plan, reglas, lecturas). Las rutinas de
Hevy son el canal de entrega de la prescripción.

**Tech Stack:** Markdown + herramientas `mcp__Hevy__*` del conector. Sin código ejecutable.

**Hallazgos que condicionan el diseño (probados el 24/11 contra la cuenta real):**
- `get_user_workouts` trae peso/reps/RPE por serie, supersets, notas, ID y `routine_id`.
- `get_user_exercise_history` trae un ejercicio por rango de fechas en una llamada.
- `update_hevy_routine` REEMPLAZA la rutina entera (no hace patch).
- Hevy pisa la rutina con lo hecho al terminar un workout → hay que reescribirla tras cada log.
- Cuenta free: máximo 4 rutinas y 7 ejercicios custom. Había 4; Manuel borró "PIERNA + CORE"
  el 24/11 → quedan 3. Igual, nunca crear rutinas sin pedido.
- No hay webhooks, ni escritura de workouts, ni borrado de rutinas.
- Gotchas reportados por la comunidad (ioandev/hevy, claude-hevy-coach), no verificados con el
  conector oficial: un `rep_range` con inicio ≠ fin puede dejar las reps en blanco para
  siempre; Hevy rechaza objetivos de RPE en rutinas. → Reps fijas por serie y RPE en la nota.

---

## File Structure

| Archivo | Cambio |
|---|---|
| `HEVY.md` | **Nuevo.** IDs de rutinas y ejercicios, reglas de lectura/escritura, gotchas. |
| `EQUIPMENT.md` | **Nuevo.** Saltos de peso reales del gym por equipo. |
| `.claude/skills/manuel-training/SKILL.md` | Registro vía conector; formato nuevo de sesión; sync de rutinas. |
| `.claude/skills/log/SKILL.md` | `/log` sin paste (paste queda de fallback). |
| `.claude/skills/hoy/SKILL.md` | Verifica que la rutina de Hevy tenga los objetivos; tabla de respaldo. |
| `.claude/skills/resumen/SKILL.md` | Tendencias desde `get_user_exercise_history`. |
| `.claude/agents/manuel-trainer.md` | Sin lista de tools restringida (necesita las de Hevy). |
| `CURRENT_PLAN.md` | Reescrito: solo estado vivo del Meso 4. Lo viejo → archivo. |
| `SESSION_HISTORY.md` | Solo bloque actual + re-entrada. Lo anterior → archivo. |
| `docs/archive/` | **Nuevo.** `CURRENT_PLAN-2026-11-24.md` y `SESSION_HISTORY-hasta-2026-10.md`. |
| `TEORIA.md` | Alineado con las reglas auditadas de la skill. |
| `README.md` | Flujo nuevo. |
| `scripts/hevy_sync.py` | Eliminado (lo reemplaza el conector). |

## Tasks

- [x] **1. `HEVY.md`** — mapa de IDs (3 rutinas + folder + ~25 ejercicios) y reglas del conector.
- [x] **2. `EQUIPMENT.md`** — consolidar los saltos de peso dispersos en el plan; marcar lo no confirmado.
- [x] **3. Archivar** — mover `SESSION_HISTORY.md` desde el Meso 3 hacia atrás y el
      `CURRENT_PLAN.md` completo a `docs/archive/` (sin borrar nada).
- [x] **4. `CURRENT_PLAN.md` nuevo** — estado, calendario Meso 4, tablas por rutina con
      columnas `Último | Próximo objetivo | Rango | Cap | Consigna`.
- [x] **5. Skills y agente** — reescribir registro, `/log`, `/hoy`, `/resumen`, tools del agente.
- [x] **6. `TEORIA.md`** — deload híbrido -10%, ramp opcional, rotación por bloque, aislamientos
      última serie 9-10.
- [x] **7. README + borrar `hevy_sync.py`.**
- [x] **8. Primera escritura en Hevy** — cargar los objetivos de B (mié 25/11), A (vie 27/11) y
      Extra (dom 29/11) con reps fijas, notas con el cap de RPE y la pierna del día correcta.
      Verificar releyendo con `get_user_routines`.
- [ ] **9. Validar en el gym (mié 25/11)** — ¿se ven bien pesos, reps y notas al abrir la rutina?
      ¿qué queda en la rutina después de terminar el workout? Ajustar `HEVY.md` con lo aprendido.
- [ ] **10. (Opcional, después del 9) Tarea programada** — corrida nocturna los días de gym que
      haga `/log` sola y mande push. Falta verificar que las escrituras a Hevy corran sin aprobación.

## Correcciones post-auditoría (24/11, sesión nueva de solo lectura)
- Protocolo de ramas para sesiones en la nube (commit en la rama asignada + push a `main`).
- Caps de RPE definidos por tipo de ejercicio; regla de lastre en dominadas; carries objetivos.
- Pico (sem 5) y deload (2 series) definidos igual en skill, plan, `HEVY.md` y `TEORIA.md`.
- `routine.notes` deja de usarse (no se puede verificar); todo ejercicio lleva nota.
- `/resumen` aclara su excepción al solo-lectura; `TEORIA.md` §2, §9 y TL;DR actualizados.

## Decisiones de entrenamiento pendientes de Manuel (NO incluidas en este cambio)
1. Probar 3:00 de descanso en compuestos (hipótesis: la 3ª serie a 9 es descanso corto).
2. Decidir subida de peso por las dos primeras series, tolerando 8.5 en la última.
3. +3 series semanales de tríceps directo.
4. Protocolo de mantenimiento para viajes/fiestas (Meso 4 cierra el 13/12).
