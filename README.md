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

**Flujo con API (Hevy Pro — cero copy-paste):**
1. Generar una API key en hevy.com/settings (sección developer) y guardarla en
   `~/.config/hevy/api-key` (o env var `HEVY_API_KEY`).
2. Abrir `claude.ai/code`, elegir el repo, y decir: *"sync con Hevy y decime qué toca
   hoy"*. El agente corre `scripts/hevy_sync.py`, registra lo que falte, actualiza
   pesos y te tira la sesión del día.
3. Opcional: una rutina programada (*"/schedule un agente que cada día de gym haga el
   sync de Hevy y me prepare la sesión"*) deja el trabajo hecho antes de llegar al gym.

**Flujo manual (sin Hevy Pro):**
1. Abrir `claude.ai/code`, elegir el repo `manuel-trainer`.
2. Escribir *"registrá esta sesión"* y pegar el log de Hevy.
3. El agente parsea, actualiza los `.md` y te dice qué ajustar. Cada cambio se commitea
   y pushea a `main`.

## Flujo del mesociclo
Bloque de 6 semanas → sesión a sesión ajusta pesos → semana 6 deload → cierre +
rotación de 2-3 accesorios por rutina (pools en `EXERCISE_LIBRARY.md`) + próximo
A/B/Extra armado juntos.
