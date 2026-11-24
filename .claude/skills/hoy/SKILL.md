---
name: hoy
description: Armar la sesión de gym del día para Manuel. Usar cuando invoca /hoy o pregunta qué toca hoy / qué entrena — confirma que la rutina de Hevy tiene los objetivos cargados y devuelve el día A/B/Extra con pesos, reps y RPE.
---

# /hoy — la sesión del día

La sesión ya vive en la rutina de Hevy (el coach la carga tras cada `/log`). `/hoy` es la
verificación y el respaldo.

1. Cargá la skill **`manuel-training`** y ejecutá su **Protocolo de arranque**. Si aparece un
   workout sin registrar, registralo primero (flujo de `/log`) — así la sesión de hoy sale con
   los objetivos correctos.
2. Determiná qué toca HOY con el calendario de `CURRENT_PLAN.md`:
   - Si hoy no es día de gym → decilo en una línea y tirá la próxima sesión con fecha.
   - Semana de **deload** → 2 series por ejercicio, -10% de peso, RPE 5-6.
3. **Chequeá la rutina de Hevy** (`get_user_routines`) contra "Próximo objetivo" del plan,
   incluida la pierna del día. Si difiere, corregila (`HEVY.md`) y avisá en una línea.
4. Output para mirar EN el gym desde el celu:
   - Título: `[A/B/Extra] — [fecha] · Meso N sem X/6 · [acumulación/pico/deload]`
   - `📲 Cargada en Hevy: abrí "[rutina]"`.
   - Tabla: Ejercicio | Peso | Series×Reps | RPE cap — en el orden real de la rutina.
   - Máximo 3 bullets de consignas del momento. Nada más.
5. No toca archivos salvo que haya registrado una sesión o corregido una rutina/cache de
   semana (eso sí se commitea y pushea).
