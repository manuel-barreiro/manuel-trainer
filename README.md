# manuel-trainer

Coach de hipertrofia personal de Manuel (subagente de Claude Code + skill + datos).

## Estructura
- `.claude/agents/manuel-trainer.md` — el coach (punto de entrada).
- `.claude/skills/manuel-training/SKILL.md` — las reglas de programación.
- `PROFILE.md` — perfil estable del atleta.
- `NUTRITION.md` — target proteico, distribución y restricciones alimentarias.
- `CURRENT_PLAN.md` — lo **prescripto**: estado del mesociclo y próximo objetivo por ejercicio.
- `SESSION_HISTORY.md` — lecturas del coach por sesión + ID de Hevy (bloque actual).
- `HEVY.md` — IDs y reglas del conector de Hevy.
- `EQUIPMENT.md` — pesos y saltos reales del gym.
- `EXERCISE_LIBRARY.md` — catálogo de ejercicios + pools de rotación por slot.
- `TEORIA.md` — base teórica del sistema.
- `docs/archive/` — historial y planes de bloques anteriores.

## Cómo funciona

**Hevy guarda lo que hiciste; el repo guarda lo que el coach prescribe y por qué; las rutinas
de Hevy te muestran la próxima sesión.** Requiere el conector de Hevy conectado en Claude
(funciona sin Hevy Pro).

1. Entrenás con la rutina de Hevy (A, B o Extra): ya tiene pesos y reps objetivo, y el cap
   de RPE en la nota de cada ejercicio.
2. Al terminar, abrís Claude sobre el repo `manuel-trainer` y escribís `/log` — sin pegar
   nada. Podés sumar contexto ("dormí mal", "usé la otra polea").
3. El coach lee el workout, decide la progresión, guarda la lectura, y **reescribe la rutina
   en Hevy** con el próximo objetivo.
4. La próxima vez que vayas al gym, abrís Hevy y listo.

| Comando | Qué hace |
|---|---|
| `/log` | Registra lo que falte desde Hevy, actualiza el plan y las rutinas, te dice qué cambia. |
| `/hoy` | Confirma que la rutina de hoy está cargada en Hevy y te la muestra (respaldo). |
| `/resumen` | Cómo venimos (tendencias por ejercicio) y hacia dónde vamos. |

> Regla de oro: **todo pasa por este repo, rama `main`.** Un chat suelto sin el repo no
> persiste nada. Si el conector no está disponible, el paste manual sigue funcionando.

## Flujo del mesociclo
Bloque de 6 semanas → sesión a sesión ajusta pesos → semana 6 deload → cierre +
rotación de 2-3 accesorios por rutina (pools en `EXERCISE_LIBRARY.md`) + próximo
A/B/Extra armado juntos.
