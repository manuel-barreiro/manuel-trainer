# manuel-trainer

Coach de hipertrofia personal de Manuel (subagente de Claude Code + skill + datos).

## Estructura
- `.claude/agents/manuel-trainer.md` — el coach (punto de entrada).
- `.claude/skills/manuel-training/SKILL.md` — las reglas de programación.
- `PROFILE.md` — perfil estable del atleta.
- `CURRENT_PLAN.md` — plan vivo (rutinas + estado del mesociclo). **Fuente de verdad.**
- `SESSION_HISTORY.md` — historial de sesiones.
- `EXERCISE_LIBRARY.md` — catálogo de ejercicios.

## Cómo usarlo desde el celular
1. Tener este repo en GitHub (privado).
2. Abrir `claude.ai/code`, elegir el repo `manuel-trainer`.
3. Escribir, por ejemplo: *"registrá esta sesión"* y pegar el log de Hevy.
4. El agente parsea, actualiza los `.md` y te dice qué ajustar. Cada cambio se commitea.

## Flujo del mesociclo
Bloque de 6 semanas → sesión a sesión ajusta pesos → semana 6 deload → cierre +
armamos el próximo A/B/Extra juntos.
