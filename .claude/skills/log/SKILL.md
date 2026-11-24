---
name: log
description: Registrar una sesión de gym de Manuel. Usar cuando invoca /log o pide loggear/registrar un workout. Lee el workout desde Hevy (sin paste), guarda la lectura, actualiza CURRENT_PLAN, reescribe las rutinas de Hevy con el próximo objetivo, commitea y responde qué progresar.
---

# /log — registrar sesión

1. Cargá la skill **`manuel-training`** y ejecutá su **Protocolo de arranque** (sync con
   main, semana por fechas, workouts sin registrar). Leé `HEVY.md`.
2. **No hace falta paste.** Traé los workouts de Hevy y registrá todos los que no tengan su
   ID en `SESSION_HISTORY.md`, en orden cronológico. Si no hay ninguno nuevo, decilo en una
   línea (con fecha y rutina del último registrado) y terminá.
   - Lo que Manuel escriba junto al comando ("dormí mal", "usé la otra polea") es contexto:
     anotalo en la sesión y usalo al leer el RPE.
   - Si Manuel pega un texto de Hevy o el conector no está disponible → fallback de paste
     (ver skill madre).
3. Seguí **"Cómo registrar una sesión"** de la skill madre, completo: lectura →
   `SESSION_HISTORY.md` → `CURRENT_PLAN.md` → **rutinas de Hevy** → verificación.
4. **Commit + push en el momento.**
5. Respuesta, corta y para leer en el celu:
   - `✅ Registrado [rutina] [fecha] — Meso N, semana X/6`
   - Una línea por ejercicio SOLO si cambia algo (sube peso, consolida, alerta).
   - `📲 Hevy actualizado: [rutinas]` — o, si falló la escritura, decirlo explícito.
   - Cierre: qué sesión toca la próxima y cuándo; si viene deload/cierre de bloque, avisarlo.
   - Flags (datos faltantes, fatiga, RPE trepando) al final, si los hay.
6. **Recovery (opcional):** datos de Bevel/Fitbit Air van en una línea de contexto de la
   sesión. Nunca pedirlos ni decidir una progresión por ellos.
