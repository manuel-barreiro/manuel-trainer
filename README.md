# manuel-trainer

Coach de hipertrofia personal de Manuel (subagente de Claude Code + skill + datos).

## Estructura
- `.claude/agents/manuel-trainer.md` — el coach (punto de entrada).
- `.claude/skills/manuel-training/SKILL.md` — las reglas de programación.
- `PROFILE.md` — perfil estable del atleta.
- `NUTRITION.md` — target proteico, distribución y restricciones alimentarias.
- `CURRENT_PLAN.md` — plan vivo (rutinas + estado del mesociclo). **Fuente de verdad.**
- `SESSION_HISTORY.md` — historial de sesiones.
- `EXERCISE_LIBRARY.md` — catálogo de ejercicios + pools de rotación por slot.
- `TEORIA.md` — base teórica del sistema.
- `scripts/hevy_sync.py` — trae las últimas sesiones desde la API de Hevy (Hevy Pro).

## Cómo usarlo desde el celular

> Regla de oro: **todo pasa por este repo, rama `main`** (el agente sincroniza y pushea
> solo — ver Protocolo de arranque en la skill). Un chat suelto sin el repo no persiste
> nada; siempre abrir la sesión sobre `manuel-trainer`.

**Flujo oficial (paste manual — sin Hevy Pro, decisión 01/09/2026):**
1. Al terminar el workout en Hevy: Share → copiar como texto.
2. Abrir `claude.ai/code`, elegir el repo `manuel-trainer`.
3. Escribir *"registrá esta sesión"* y pegar el log. Sirve pegar varios workouts juntos
   si se acumularon sesiones sin registrar.
4. El agente parsea, actualiza los `.md` y te dice qué ajustar. Cada cambio se commitea
   y pushea a `main`.
5. Opcional: una rutina programada (*"/schedule un agente que cada mañana de gym me
   prepare la sesión del día"*) — no necesita la API: lee el plan del repo y te deja
   los pesos/reps objetivo listos antes de llegar al gym.

**Flujo con API** (`scripts/hevy_sync.py`): dormido — solo aplica si algún día hay
Hevy Pro (key en hevy.com/settings → `~/.config/hevy/api-key`), y elimina el paste.

## Flujo del mesociclo
Bloque de 6 semanas → sesión a sesión ajusta pesos → semana 6 deload → cierre +
rotación de 2-3 accesorios por rutina (pools en `EXERCISE_LIBRARY.md`) + próximo
A/B/Extra armado juntos.
