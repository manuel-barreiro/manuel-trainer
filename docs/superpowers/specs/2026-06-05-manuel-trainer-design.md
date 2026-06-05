# Diseño: agente `manuel-trainer`

**Fecha:** 2026-06-05
**Autor:** Manuel + Claude
**Estado:** Aprobado en brainstorming, pendiente de plan de implementación

---

## 1. Propósito

Un coach de hipertrofia personalizado para Manuel que reemplace el flujo actual
(pegar logs de Hevy en un chat desprolijo del proyecto de Claude.ai). El agente:

- Registra y parsea las sesiones que Manuel pega desde Hevy.
- Ajusta pesos/progresión según su sistema de doble progresión y RPE objetivo.
- Arma la sesión del día cuando se le pide ("hoy toca A").
- Gestiona el mesociclo de 6 semanas con deload y cierre de bloque.
- Es usable **desde el celular** (donde Manuel siempre loggea).

## 2. Decisiones tomadas en brainstorming

| Decisión | Elección | Motivo |
|---|---|---|
| Ingesta de datos | **Paste manual de Hevy** | Cero fricción; Hevy ya es la base de datos real |
| Almacenamiento | **Archivos Markdown** | Claude razona perfecto sobre texto; versionable; suficiente para 1 usuario |
| Acceso móvil | **Repo en GitHub + Claude Code on the web** | Independiente de que la Mac esté prendida; historial versionado |
| Forma del agente | **Subagente + skill + datos** (project-level) | Mismo patrón que `inversiones-manuel`, pero dentro del repo |

## 3. Arquitectura

Tres piezas, todas **dentro del repo `manuel-trainer/`** (project-level, no
`~/.claude/`), para que viajen al sandbox cloud y funcionen desde el celular:

```
manuel-trainer/                         ← repo de git (raíz que se abre en claude.ai/code)
├── .claude/
│   ├── agents/
│   │   └── manuel-trainer.md           ← identidad de coach + cómo usar los archivos
│   └── skills/
│       └── manuel-training/
│           └── SKILL.md                ← las REGLAS (know-how de programación)
├── PROFILE.md                          ← datos estables del atleta
├── CURRENT_PLAN.md                     ← plan vivo (fuente de verdad operativa)
├── SESSION_HISTORY.md                  ← historial append-only de sesiones
├── EXERCISE_LIBRARY.md                 ← catálogo con preferencias YES/SUB/NO
├── README.md                           ← cómo invocarlo desde el cel
└── docs/superpowers/specs/             ← este spec
```

**Separación clave:** las *reglas* (cómo progresar) viven en la skill; los *datos*
(qué se levantó) viven en los `.md`. Hoy están mezclados en `IDENTITY.md` y por eso
queda desprolijo.

## 4. Reorganización de los archivos de datos

Estado actual: 5 archivos con duplicación y dos templates vacíos. Se consolida a 4:

| Archivo nuevo | Sale de | Rol |
|---|---|---|
| `PROFILE.md` | IDENTITY (perfil, schedule, suplementación, contexto) | Datos estables del atleta |
| `CURRENT_PLAN.md` | IDENTITY (working weights) + ULTIMOS_TRAININGS (rutinas junio) | Plan vivo: A/B/Extra con peso/reps/RPE objetivo + semana del bloque + fecha de deload |
| `SESSION_HISTORY.md` | ULTIMOS_TRAININGS + lift log de marzo (archivado) | Historial append-only; acá cae cada paste de Hevy parseado |
| `EXERCISE_LIBRARY.md` | (se mantiene) | Catálogo con YES/SUB/NO |

**Se eliminan:** `LIFT_LOG.md` y `WORKING_WEIGHT_LOG.md` (templates vacíos que
reemplaza `CURRENT_PLAN.md`). `IDENTITY.md` queda absorbido por `PROFILE.md` +
`CURRENT_PLAN.md` + la skill. El log de marzo se conserva archivado dentro de
`SESSION_HISTORY.md` (no se pierde nada).

## 5. El ciclo de trabajo

```
INICIO DE BLOQUE  →  armar juntos A/B/Extra (Mesociclo N, semana 1 de 6)
       │
SESIÓN A SESIÓN  →  "hoy toca A" → sesión con pesos/RPE objetivo
       │              pegás el log de Hevy → parsea, guarda en historial,
       │              actualiza working weights y dice: subir / sumar reps / mantener
       │              (+ flags de datos faltantes, ej. RPE del OH Carry sin loggear)
       │
SEMANA 6 / DELOAD →  descarga (mismas rutinas, ~50% volumen, -10-20% peso)
       │
CIERRE DE BLOQUE →  resumen del mesociclo (qué progresó, qué se estancó) →
                    armar juntos el próximo A/B/Extra (accesorios rotados,
                    compuestos fijos) → arranca Mesociclo N+1
```

## 6. Reglas que codifica la skill (de la evidencia investigada)

Basado en RP (Israetel/Hoffmann), Helms (Muscle & Strength Pyramid) y la review
de Kassiano et al. 2022 sobre variación de ejercicios:

- **Doble progresión** con RPE objetivo: compuestos 7-8 (2-3 RIR), aislamientos 8
  (1-2 RIR), nunca al fallo en compuestos. (Ya es el sistema de Manuel.)
- **Mesociclo de 6 semanas:** volumen/RPE rampea hacia arriba (MEV→MRV), semana 6
  es deload (mismas rutinas, ~50% volumen, -10-20% peso, lejos del fallo).
- **Compuestos fijos** (Bench, OHP, Barbell Row, Dominadas/Chin-up) — no se rotan;
  la especificidad manda. **Solo se rotan accesorios** entre bloques.
- **No rotar ejercicios cada sesión** (peor progresión, más fatiga). Variación
  sistemática, no aleatoria.
- **Detección de estancamiento:** ej. Chin-Up que viene "hot" (RPE 9-10) 3 sesiones
  sin progresar → propone bajar a 3×6 BW y reconstruir (decisión abierta #1 de Manuel).
- **Contexto post-lesión:** Manuel viene de una fractura en la mano izquierda;
  arranca reconstruyendo desde el baseline de junio 2026, NO desde los pesos de marzo.

## 7. Incrementos de progresión (del sistema actual de Manuel)

- Compuestos con barra (tren superior): +2.5 kg
- Mancuernas / cables accesorios: +2 kg
- Carries: +2 kg cuando se siente cómodo
- Dominadas: llegar a 3×12 limpio antes de agregar 2.5 kg de lastre

## 8. Primer mesociclo

Se trata la rutina actual de junio 2026 (post-lesión) como **Mesociclo 1, semana 1**.
Las rutinas A/B/Extra vigentes salen de `ULTIMOS_TRAININGS.md`:

- **A:** Incline DB Press · Chin-Up · Leg Extension · OH Single Carry · Hammer Curl · Ab Wheel
- **B:** OHP (o sustituto) · Row · Leg Curl/Extension · Suitcase Carry · Weighted Dips · Hanging Leg Raise
- **Extra:** Bench · Lat Pulldown · Lateral Raise + Leg Extension · Bicep Curl · Tricep Pushdown · Wrist Curl

(El detalle exacto de pesos de arranque se confirma al construir `CURRENT_PLAN.md`.)

## 9. Fuera de alcance (YAGNI)

- API de Hevy, Google Sheets, base de datos (se eligió paste + Markdown).
- Programación de pierna/sentadilla/peso muerto (lo cubre el fútbol 3×/semana).
- Nutrición más allá de registrar la creatina (5 g/día).
- Remote Control / uso desde la Mac (se eligió solo el camino repo+web).

## 10. Setup móvil (parte de la implementación)

1. `git init` en `manuel-trainer/`, primer commit.
2. Crear repo en GitHub (privado) y push.
3. Abrir el repo desde `claude.ai/code` en el navegador del celular.
4. Invocar el agente: "che, registrá esta sesión" + paste de Hevy.
5. Cada cambio (sesión nueva, working weights) se commitea al repo.

## 11. Cómo se invoca

Igual que `inversiones-manuel`: se llama al subagente `manuel-trainer` con el Agent
tool, o conversando dentro del repo. El agente, como primer paso, carga la skill
`manuel-training` (fuente de verdad de las reglas) y lee `CURRENT_PLAN.md` para
saber en qué punto del mesociclo está Manuel.
