# Auditoría científica de la lógica deportiva de manuel-trainer

**Fecha:** 2026-06-10
**Objetivo:** Validar contra evidencia peer-reviewed la lógica de programación del agente
`manuel-training` (deload, mesociclo, doble progresión, RPE, rotación, estancamiento) y
aplicar los ajustes que la evidencia justifique al perfil de Manuel.

## Contexto

Manuel es advanced-intermediate (9 años entrenando, 25 años, 1.90 m / 94 kg), objetivo
hipertrofia. Entrena 4 días de tren superior en gym (split A/B + Extra) y juega fútbol
3×/semana (martes, jueves, partido el sábado), por lo que no programa pierna en gym salvo
Leg Extension. La queja que dispara esta auditoría: el ciclo de 6 semanas le parecía corto
para rotar ejercicios y no quería hacer siempre lo mismo. Decisión de Manuel: aplicar lo que
diga la evidencia, no su preferencia de variedad por sí sola.

## Método

Deep research con verificación adversarial (3 votos por claim, 25 claims confirmados,
0 refutados). Fuentes primarias clave: Coleman et al. 2024 (PeerJ), Bell et al. 2025 (NSCA
SCJ) y 2023 (Delphi), Rogerson/Bell 2024 (Sports Med Open, n=246), Pelland et al. 2025
(Sports Med, meta-regresión n=2058), Plotkin et al. 2022 (PeerJ), Refalo et al. 2024
(J Sports Sci), Robinson et al. 2024 (Sports Med) y 2025 (IJSC), Kassiano et al. 2022 (JSCR)
y 2025 (n=70).

## Veredictos por regla

| # | Regla actual | Veredicto | Acción |
|---|---|---|---|
| 1 | Mesociclo 6 sem + deload obligatorio sem 6 | Parcialmente válida | Cambio 1 (híbrido) |
| 2 | Deload: ~50% series, -10-20% carga, RPE 5-6, misma frecuencia | Validada | Ajuste menor (carga -10%) |
| 3 | Ramp de volumen MEV→MRV | Parcialmente válida | Cambio 5 (opcional) |
| 4 | Doble progresión (+2.5 barra / +2 mancuerna) | Validada | Sin cambios |
| 5 | RPE 7-8 compuestos / 8 aislamientos | Validada con matiz | Cambio 3 (aislamientos 0-1 RIR) |
| 6 | Rotación: accesorios cada 2-5 bloques, compuestos fijos | Validada | Cambio 2 (rotar cada bloque) |
| 7 | Estancamiento: 2+ sesiones sin progresar → deload/ajuste | Razonable, no validada directa | Cambio 4 (umbral robusto) |

### Detalle de evidencia

- **Regla 1 (parcial):** la cadencia de 6 semanas cae en la práctica normativa (deloads cada
  4-8 sem; media observada 5,6 ± 2,3 sem en 246 atletas). Pero el único RCT dedicado
  (Coleman 2024) muestra que el deload programado **no mejora la hipertrofia** — su valor es
  gestión de fatiga, no supercompensación. El consenso Delphi (100% acuerdo) avala enfoques
  preplaneado, reactivo o híbrido. Ese RCT testeó *cese completo*, no deload activo, así que
  argumenta contra layoffs totales, no contra el deload activo del programa.
- **Regla 2 (validada):** la prescripción coincide punto por punto con Bell 2025 (40-60%
  volumen, ~10% carga, frecuencia sin cambios) y la práctica de atletas (Rogerson 2024). El
  único exceso leve: -20% de carga supera el consenso de ~10%. Ajuste: fijar -10%.
- **Regla 3 (parcial):** el dose-response de volumen es real y casi lineal para hipertrofia
  (Pelland 2025, prob. posterior ~100% pendiente positiva), lo que hace defendible terminar
  con más volumen. Pero **ningún estudio compara ramp vs volumen constante igualado**: el
  modelo RP es extrapolación plausible, no protocolo validado.
- **Regla 4 (validada):** Plotkin 2022 — progresar reps o carga produce hipertrofia similar.
  Los incrementos +2.5/+2 kg son los mínimos prácticos. Sin cambios.
- **Regla 5 (validada con matiz):** 1-2 RIR ≈ fallo para hipertrofia (Refalo 2024); el fallo
  no ayuda a la fuerza y puede perjudicarla levemente (Robinson 2025). Pero la meta-regresión
  (Robinson 2024) sugiere un pequeño beneficio hipertrófico al acercarse al fallo →
  capturarlo solo en aislamientos de bajo costo de fatiga (0-1 RIR), manteniendo compuestos a
  RPE 7-8.
- **Regla 6 (validada):** Kassiano 2022 — la variación *sistemática* mejora/no perjudica;
  la *aleatoria por sesión* perjudica; los compuestos prioritarios se mantienen fijos por
  especificidad. Kassiano 2025 (n=70) y Baz-Valle 2019: rotar accesorios sistemáticamente
  tiene **costo cero** en ganancias y mejora la motivación. Rotar cada bloque (6 sem) está
  perfectamente soportado siempre que la variante cubra el mismo músculo/función.
- **Regla 7 (razonable, no validada directa):** ningún estudio testea el umbral exacto. El
  marco de deload reactivo (Delphi, Bell 2025) lo legitima. Riesgo: 2 sesiones puede dar
  falsos positivos por el ruido del fútbol (partido del sábado afectando el lunes). Más
  robusto: 3 sesiones (o 2 con caída clara) + respuesta graduada (bajar peso del ejercicio
  antes que deload completo).

### Brechas de evidencia (cuestiones abiertas, sin claim verificado)

- No hubo evidencia verificada sobre **interferencia fútbol ↔ hipertrofia** ni sobre si el
  fútbol sustituye el entrenamiento de pierna para hipertrofia. Tratado como decisión de
  prioridades de Manuel, documentada con honestidad (Cambio 6).
- Los hallazgos de proximidad al fallo y deload provienen mayormente de tren inferior; su
  transferencia exacta al tren superior de Manuel es extrapolación razonable, no directa.

## Cambios aprobados

**Cambio 1 — Deload híbrido (Regla 1).**
La semana 6 de deload pasa de "obligatorio" a *default revisable*. Al llegar, el agente
evalúa readiness (progresión del bloque, tendencia de RPE, sueño, calendario de fútbol) y
puede proponer adelantarlo o estirarlo ±1 semana. Regla de seguridad: **no saltear el deload
dos bloques seguidos**. Marco: deload reactivo/híbrido (Coleman 2024; Delphi 2023; Bell 2025).

**Cambio 2 — Rotación de accesorios cada bloque (Regla 6).**
La rotación de accesorios pasa de "cada 2-5 bloques" a **cada bloque (al cierre de las 6
semanas)**. Default: rotar **2-3 accesorios por rutina** (A/B/Extra), no todos. Regla dura: la
variante nueva debe cubrir el **mismo músculo/función** (ej. Hammer Curl → Incline DB Curl OK;
→ Face Pull NO) y se re-establece la progresión desde el piso del rango. **Compuestos fijos**
sin cambios (Bench, OHP, Barbell Row, Dominadas). Soporte: Kassiano 2022/2025, Baz-Valle 2019.

**Cambio 3 — Aislamientos más cerca del fallo (Regla 5).**
RPE objetivo de aislamientos (curls, laterales, extensions, pushdowns, wrist curl) sube de
RPE 8 a **RPE 9-10 (0-1 RIR) en la última serie**. Compuestos siguen en RPE 7-8, nunca al
fallo. Soporte: Robinson 2024 (dose-response), Refalo 2024, Robinson 2025.

**Cambio 4 — Estancamiento con umbral robusto (Regla 7).**
Trigger pasa de "2+ sesiones" a **3 sesiones sin progresar (o 2 con caída clara, no solo
meseta)**. Respuesta graduada: primero **bajar 5-10% el peso del ejercicio**; deload completo
solo si el estancamiento es multi-ejercicio. El agente considera el calendario de fútbol al
interpretar un RPE alto (partido del sábado → posible fatiga el lunes). Soporte: marco
reactivo + Coleman 2024 (no gatillar deload por meseta de un solo lift).

**Cambio 5 — Ramp de volumen opcional (Regla 3).**
El "MEV→MRV" deja de ser mandato. Sumar series dentro del bloque es **opcional y guiado por
rendimiento**: si al mismo peso caen las reps o trepa el RPE, no se suman series. Soporte:
Pelland 2025 (dose-response real pero sin validación del ramp vs constante).

**Cambio 6 — Nota honesta sobre el fútbol (brecha de evidencia).**
Documentar en la skill que cubrir pierna con fútbol es una **decisión de prioridades válida de
Manuel**, pero que el fútbol no aporta el estímulo de tensión mecánica progresiva que maximiza
la hipertrofia de pierna. Sin cambio de programación; solo que el agente no lo presente como
equivalente.

## Validado sin cambios

- Prescripción del deload: ~50% de series, RPE 5-6, misma frecuencia (solo se fija carga a
  -10%).
- Doble progresión con incrementos +2.5 kg barra / +2 kg mancuerna y la regla de
  consolidación de RPE.
- RPE 7-8 en compuestos, nunca al fallo.
- Mesociclo de 6 semanas como duración del bloque.
- Compuestos fijos por varios bloques (especificidad).

## Archivos a modificar

- `.claude/skills/manuel-training/SKILL.md` — secciones Mesociclo, Rotación, RPE objetivo,
  Detección de estancamiento; nueva nota sobre fútbol.
- `CURRENT_PLAN.md` — RPE objetivo de aislamientos (a 9-10), nota de rotación al cierre del
  bloque, nota de deload híbrido.

## Fuera de alcance

- No se reescriben las rutinas A/B/Extra actuales (el bloque está en curso, semana 1 de 6).
- No se cambia la decisión de no programar pierna pesada (preferencia de Manuel).
- Nutrición sigue fuera de alcance (solo registrar creatina).
