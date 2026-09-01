---
name: log
description: Registrar una sesión de gym de Manuel. Usar cuando invoca /log, pega un log/paste de Hevy, o pide loggear/registrar un workout. Parsea, guarda en SESSION_HISTORY, actualiza CURRENT_PLAN, commitea y responde qué progresar.
---

# /log — registrar sesión

1. Cargá la skill **`manuel-training`** y ejecutá su **Protocolo de arranque** completo
   (sync con main, semana recalculada por fechas, chequeo de staleness).
2. El paste de Hevy viene en los args del comando o en el mismo mensaje. Si no está,
   pedilo en una línea y esperá. **Varios workouts en un solo paste es válido:**
   procesalos en orden cronológico, uno por uno.
3. Seguí al pie de la letra **"Cómo parsear un paste de Hevy"** de la skill madre
   (registro arriba del bloque en `SESSION_HISTORY.md`, decisión por ejercicio según
   doble progresión y caps, working weights y semana en `CURRENT_PLAN.md`).
4. **Commit + push a `main` en el momento** (regla del protocolo).
5. Respuesta, corta y para leer en el celu:
   - `✅ Registrado [día] [fecha] — Meso N, semana X/6`
   - Una línea por ejercicio SOLO si cambia algo (sube peso, consolida, alerta);
     lo que sigue igual no se lista.
   - Cierre: qué sesión toca la próxima y cuándo; si viene deload/cierre de bloque,
     avisarlo acá.
   - Flags (datos faltantes, fatiga, RPE trepando) al final, si los hay.
