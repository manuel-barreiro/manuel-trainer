# Auditoría de sistema y UX — 2026-09-01

**Disparador:** pedido de Manuel: auditar mesociclos, rotación, pesos y RPE máximos,
mejorar la UX del flujo Hevy → agente, e implementar mejoras de forma autónoma.

> Nota de honestidad: una primera versión de esta auditoría (31/08, en un clone local
> desactualizado) diagnosticó "sistema congelado desde junio". Era falso: el sistema vivo
> estaba en `origin/main`, al día hasta el 31/08. Lo que sí estaba roto: (a) la auditoría
> científica de junio (`cd997e3`) **nunca se había pusheado**, así que el sistema operó
> junio-agosto con reglas pre-auditoría; (b) el clone local nunca hizo fetch. Esta versión
> reemplaza a la anterior con los hallazgos corregidos.

## Hallazgos

### 1. Divergencia de ramas (causa raíz real)
`main` local tenía la auditoría científica (junio) sin pushear; `origin/main` tenía todo
el historial vivo (Meso 1 cerrado 04/07, Meso 2 completo hasta 31/08, NUTRITION.md,
TEORIA.md, protocolo de arranque) sin la auditoría. Dos fuentes de verdad paralelas
durante 3 meses. **Resuelto:** merge + este commit. El "Protocolo de arranque" que el
propio sistema desarrolló (sync con origin/main + semana derivada de fechas + push
inmediato) es la vacuna correcta; se le sumó detección de staleness (>10 días sin
sesión ✅ sin viaje anotado → traer sesiones antes de recomendar).

### 2. Reglas pre-auditoría que corrieron todo el Meso 2
El remoto operaba con: deload "-10-20% NO opcional", ramp MEV→MRV como mandato,
rotación "cada 2-5 bloques", estancamiento a 2+ sesiones, aislamientos a RPE 8, y
"pierna la cubre el fútbol" sin matiz. La auditoría de junio (aprobada por Manuel)
corrige todo eso. **Aplicada ahora sobre el estado real**, con un matiz nuevo:

- **RPE de aislamientos (última serie 0-1 RIR): EN PAUSA hasta Meso 3.** La práctica de
  agosto desarrolló una disciplina de cap ≤8 que resolvió el grinding crónico, y el
  bloque está en semana 5 (pico) con 🚩 de fatiga (30/08: 6 de 8 ejercicios con la 3ª
  a 8.5). Cambiar la regla en pico sería exactamente el error que el cap vino a arreglar.
  Arranca post-deload con el cuerpo fresco.
- **Rotación:** al cierre del Meso 2 (~13/09) se rotan 2-3 accesorios por rutina desde
  los ROTATION POOLS nuevos (Kassiano 2025, Baz-Valle 2019 — costo cero, mejora
  motivación). El "NINGUNA rotación porque es el bloque 2" del plan venía de la regla
  vieja. Excepción práctica documentada: un accesorio rindiendo a mitad de progresión
  puede quedarse.
- **Estancamiento:** umbral 3 sesiones + respuesta graduada (el remoto ya convergió a
  esto en la práctica: OHP "estancado tras 3 intentos" → reajuste de reps, no deload).
- **Deload híbrido** (-10%, revisable ±1 semana, nunca saltear 2 seguidos) y **ramp de
  volumen opcional** — reemplazan al texto viejo.
- **Nota honesta del fútbol** restaurada (no presentar fútbol como equivalente de
  entrenar pierna).

### 3. Lo que el sistema aprendió solo y ahora es regla escrita
La práctica de agosto descubrió patrones valiosos que quedaron canonizados en la skill:
"el techo de reps no vale si se sale del cap" (anti-grinding), ≥1 día de descanso entre
sesiones de gym (el pico de RPE del 15-17/08 fue por 3 días seguidos), y carries sin RPE
por diseño de Hevy.

### 4. UX
El flujo actual (paste de Hevy en claude.ai/code sobre el repo) FUNCIONA — el historial
de agosto lo prueba. Mejoras implementadas:
- **`scripts/hevy_sync.py`:** API oficial de Hevy (`api.hevyapp.com/v1/workouts`, header
  `api-key`, requiere Hevy Pro; key en hevy.com/settings → developer). Imprime las
  sesiones en el formato de paste que la skill ya parsea. Elimina el copy-paste; el
  paste manual queda de fallback.
- README con los dos flujos + opción de rutina programada (/schedule) para dejar la
  sesión del día preparada.
- Regla de oro explícita: toda sesión de Claude opera sobre el repo, rama `main`.

### 5. Higiene de doble progresión
Regla 0 nueva: cada slot tiene rango piso-techo; los números fijos solo valen como paso
de consolidación explícito (el plan de Meso 2 los usa bien: "consolidar 3×9 → 3×10").

## Pendiente (decisiones de Manuel, no urgentes)
- Cierre del Meso 2 (~13/09): elegir qué 2-3 accesorios por rutina rotar de los pools.
- Meso 3: sumar rear delt/face pull (hueco real, ya anotado) y activar la regla de
  0-1 RIR en la última serie de aislamientos.
- Definir a mediados de septiembre el plan pre-viaje USA (05-24/10): bloque corto
  Meso 3 + viaje como break largo (ya esbozado en CURRENT_PLAN).
- Si quiere el flujo sin copy-paste: generar la API key de Hevy.
