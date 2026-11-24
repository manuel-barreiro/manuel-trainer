---
name: resumen
description: Resumen del entrenamiento de Manuel. Usar cuando invoca /resumen o pregunta cómo viene / cómo vamos / hacia dónde va el plan — estado del bloque, tendencias por ejercicio y próximos hitos (deload, cierre, rotación, viajes).
---

# /resumen — cómo venimos y hacia dónde vamos

1. Cargá la skill **`manuel-training`** y ejecutá su **Protocolo de arranque**.
2. Leé `CURRENT_PLAN.md` y `SESSION_HISTORY.md` (bloque actual). Para las tendencias usá
   `get_user_exercise_history` (IDs en `HEVY.md`) desde el inicio del bloque, solo para los
   compuestos y para lo que esté consolidando o en atención — no para todo. Para comparar con
   el bloque anterior, buscá su "RESUMEN" en `docs/archive/SESSION_HISTORY-hasta-2026-10.md`.
3. Estructura fija de la respuesta:
   - **📍 Dónde estamos:** Meso N, semana X/6, fase (acumulación/pico/deload), qué se
     hizo y qué falta de la semana en curso.
   - **📈 Cómo venimos** — por ejercicio, en tres grupos (listar solo lo que tiene
     novedad, no lo neutro):
     - ✅ Progresando — con el salto concreto del bloque (ej. "Row 57.5 → 67.5").
     - 🔁 Consolidando — qué le falta para subir (ej. "Bench: 3×9 con la 3ª a ≤8").
     - 🚩 Atención — estancados o fuera de cap, con la acción ya decidida en el plan.
   - **🎯 Hacia dónde vamos:** los próximos hitos en orden con fechas: resto del
     bloque, deload, cierre + rotación de accesorios (pools de `EXERCISE_LIBRARY.md`),
     arranque del meso siguiente con los cambios ya decididos (ej. rear delt, regla
     0-1 RIR), viajes/parates anotados.
   - **⚠️ Flags** solo si existen: fatiga acumulada, sueño, sesiones sin registrar.
4. Read-only. Sin preguntas al final: cierre limpio.
