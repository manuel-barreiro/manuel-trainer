# HEVY — conector, IDs y reglas

> El conector oficial de Hevy (`mcp.hevy.com`) funciona **sin Hevy Pro**. Herramientas:
> `mcp__Hevy__*`. Hevy es la fuente de verdad de **lo hecho**; el repo, de **lo prescripto**.
> Si las herramientas no están disponibles en la sesión, el fallback es el paste manual.

## Rutinas (cuenta free: máximo 4 — NUNCA crear rutinas nuevas, siempre actualizar)

| Rutina | `routine_id` |
|---|---|
| Workout A | `45fa4768-8b79-42b9-92c4-7052b592c260` |
| Workout B | `19b43832-0c0c-433c-af40-6a1a40f26639` |
| Workout Extra | `c1970ae6-a80f-46fe-80aa-52670417de05` |
| PIERNA + CORE (vieja, sin usar desde mayo; sirve de banco de pruebas) | `0451bd69-70df-4ed0-aab4-c86915a01373` |

Folder "Abril 2026": `folder_id` **2646352** (A, B y Extra viven ahí).

## Ejercicios (`exercise_template_id`)

| Ejercicio | ID | Tipo |
|---|---|---|
| Incline Bench Press (Dumbbell) | `07B38369` | peso × reps |
| Chin Up | `29083183` | BW reps |
| Pull Up | `1B2B1E7C` | BW reps |
| Seated Cable Row - V Grip (Cable) | `0393F233` | peso × reps |
| Lying Leg Curl (Machine) | `B8127AD1` | peso × reps |
| Leg Extension (Machine) | `75A4F6C4` | peso × reps |
| OH Single Carry *(custom)* | `11eebf4e-ed14-436e-a7c6-c1a478cf4c70` | peso × tiempo |
| Suitcase Carry *(custom)* | `598a3316-ea6d-447d-8544-9883d05cec33` | peso × tiempo |
| Seated Incline Curl (Dumbbell) | `8BAB2735` | peso × reps |
| Rear Delt Reverse Fly (Dumbbell) | `E5988A0A` | peso × reps |
| Ab Wheel | `99D5F10E` | BW reps |
| Overhead Press (Barbell) | `7B8D84E8` | peso × reps |
| Pendlay Row (Barbell) | `018ADC12` | peso × reps |
| Single Arm Lateral Raise (Cable) | `DE68C825` | peso × reps |
| Lateral Raise (Dumbbell) | `422B08F1` | peso × reps |
| Triceps Dip (Weighted) | `10347BAC` | lastre × reps |
| Hanging Leg Raise | `F8356514` | BW reps |
| Bench Press (Barbell) | `79D0BB3A` | peso × reps |
| Preacher Curl (Barbell) | `4F942934` | peso × reps |
| Overhead Triceps Extension (Cable) | `B5EFBF9C` | peso × reps |
| Seated Palms Up Wrist Curl | `1006DF48` | peso × reps |
| Crunch (Weighted) | `D928C232` | peso × reps |
| Oblique Crunch | `DBE341AA` | BW reps |
| Face Pull *(candidato de rotación)* | `BE640BA0` | peso × reps |

Un ejercicio que no esté acá: `search_hevy_exercises` y agregarlo a esta tabla. Custom nuevos
solo como último recurso (límite free: 7) y avisándole a Manuel.

## Leer (qué herramienta para qué)

- **Sesiones nuevas:** `get_user_workouts` con `page=1, pageSize=3` (subir a 10 solo si hay
  staleness). Una sesión está registrada si su ID aparece en `SESSION_HISTORY.md`.
- **Tendencia de un ejercicio:** `get_user_exercise_history` con el ID y un rango de fechas.
  Pedir solo los ejercicios que hacen falta — no paginar todo el historial de workouts.
- **Zona horaria:** Hevy devuelve UTC. Manuel está en Argentina (UTC-3): restar 3 h antes de
  decidir el día de la semana (un workout que empieza 00:30 UTC es del día anterior).
- Los carries vienen con `duration_seconds` y sin RPE (por diseño). El cable row viene en
  54.4 kg porque el stack está en libras (120 lb).
- Series con `type: "warmup"` no cuentan para la progresión.

## Escribir (reglas duras)

1. **Solo `update_hevy_routine`** sobre A, B o Extra. Reemplaza la rutina entera: mandar
   SIEMPRE todos los ejercicios, en orden, con `title`, `folder_id: 2646352`, `superset_id` y
   `rest_seconds` tal como están (leer antes con `get_user_routines`), cambiando solo lo que
   corresponde.
2. **Reps fijas por serie, nunca `rep_range`.** El objetivo es concreto (ej. 8/8/7). Riesgo
   reportado por la comunidad: un rango con inicio ≠ fin deja las reps en blanco para siempre y
   solo se arregla creando otra rutina — y no hay cupo. Si algún día se quiere probar, primero
   en "PIERNA + CORE".
3. **El RPE no va en las series** (Hevy lo rechaza en rutinas): va en `notes` del ejercicio,
   corto y accionable. Ej.: `Obj 8/8/7 · cortar la 3ª en RPE 8`.
4. **Pierna del día:** el slot de pierna de la rutina se cambia según el DÍA de la próxima
   sesión de esa rutina (Lun/Vie = Leg Curl · Mié/Dom = Leg Extension), manteniendo posición
   y superset.
5. **Cuándo:** después de cada `/log`, reescribir la rutina recién registrada (Hevy la pisó
   con lo hecho) y cualquier otra que comparta un ejercicio cuyo objetivo cambió (pierna, o un
   ajuste del plan). Después de escribir, releer con `get_user_routines` y verificar.
6. **Deload:** la semana 6 se carga con 2 series, -10% de peso y nota `DELOAD · RPE 5-6`.
7. `routine.notes` (nota general): `Coach · [fecha de carga] · Meso N sem X · próxima: [día fecha]`.
8. No usar `create_hevy_routine`, `create_hevy_plan` ni `create_hevy_routine_folder` salvo
   pedido explícito de Manuel.

## Verificado el 24/11/2026
- `update_hevy_routine` aceptó A, B y Extra con reps fijas, notas por ejercicio, carries por
  `duration_seconds`, cambio de ejercicio de pierna y supersets intactos.
- La respuesta NO devuelve `routine.notes` (nota general): no se sabe si se guarda. No
  depender de ella; lo importante va en la nota de cada ejercicio.

## Pendiente de validar (ver plan 2026-11-24, tareas 9-10)
- Qué queda en la rutina (notas, reps) después de terminar un workout y aceptar "update routine".
- Si una tarea programada puede escribir en Hevy sin aprobación manual.
