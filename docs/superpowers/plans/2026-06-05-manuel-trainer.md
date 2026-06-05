# manuel-trainer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Construir el agente de coaching `manuel-trainer` (subagente + skill + datos en Markdown) dentro de un repo de git, usable desde el celular vía Claude Code on the web.

**Architecture:** Mismo patrón que `inversiones-manuel` pero project-level: un subagente en `.claude/agents/`, una skill `manuel-training` en `.claude/skills/` con las reglas de programación, y 4 archivos de datos Markdown en la raíz del repo. Las *reglas* viven en la skill; los *datos* en los `.md`.

**Tech Stack:** Markdown, frontmatter YAML, git/GitHub. Sin código ejecutable.

**Notas para el ejecutor:**
- El repo ya existe en `/Users/mbarreiro/dev/personal/manuel-trainer/` con git inicializado y el spec commiteado.
- Los archivos fuente actuales (`IDENTITY.md`, `EXERCISE_LIBRARY.md`, `LIFT_LOG.md`, `WORKING_WEIGHT_LOG.md`, `ULTIMOS_TRAININGS.md`) están versionados — leélos para migrar contenido.
- Spec de referencia: `docs/superpowers/specs/2026-06-05-manuel-trainer-design.md`.
- Todos los commits llevan: `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>` y usan `git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar"`.

---

## File Structure

| Archivo | Responsabilidad |
|---|---|
| `.claude/agents/manuel-trainer.md` | Identidad del coach + cómo usar los archivos. Punto de entrada. |
| `.claude/skills/manuel-training/SKILL.md` | Reglas de programación (doble progresión, RPE, mesociclo, deload, rotación). |
| `PROFILE.md` | Datos estables del atleta (perfil, schedule, suplementación, contexto). |
| `CURRENT_PLAN.md` | Plan vivo: A/B/Extra con peso/reps/RPE objetivo + estado del mesociclo. |
| `SESSION_HISTORY.md` | Historial append-only de sesiones (paste de Hevy parseado + log marzo archivado). |
| `EXERCISE_LIBRARY.md` | Catálogo con preferencias YES/SUB/NO (se mantiene casi igual). |
| `README.md` | Cómo invocar el agente desde el celular. |
| `.gitignore` | Ignorar basura del SO. |

---

## Task 1: PROFILE.md

**Files:**
- Create: `PROFILE.md`
- Source: `IDENTITY.md` (líneas 7-38, sección ATHLETE PROFILE)

- [ ] **Step 1: Crear `PROFILE.md`** con los datos estables del atleta, migrados de `IDENTITY.md`. Contenido completo:

```markdown
# PROFILE — Manuel

Datos estables del atleta. Cambian poco. Las reglas de cómo entrenar NO van acá
(viven en la skill `manuel-training`); los pesos/rutinas vivos tampoco (van en `CURRENT_PLAN.md`).

## Atleta
- **Nombre:** Manuel
- **Edad:** 25
- **Altura / Peso:** 1.90 m / ~94 kg
- **Experiencia:** Advanced-intermediate. Entrena desde los 16 (9 años de base),
  3-4 años de entrenamiento estructurado. Se programa solo. Buen manejo del RPE.
- **Objetivo:** Hipertrofia + sobrecarga progresiva.
- **Equipamiento:** Gimnasio comercial.
- **Lesiones/limitaciones:** Ninguna activa. (Historial: fractura mano izquierda a
  principios de 2026 → bloque de vuelta post-lesión en mayo-junio 2026.)

## Schedule semanal
- **Lunes:** Workout A (gym)
- **Martes:** Fútbol
- **Miércoles:** Workout B (gym)
- **Jueves:** Fútbol
- **Viernes:** Workout A o B alternando (gym)
- **Sábado:** Partido de fútbol 7 (liga con amigos)
- **Domingo:** Extra (gym)

El split A/B alterna cada semana:
- **Semana impar:** Lun A / Mié B / Vie A / Dom Extra
- **Semana par:** Lun B / Mié A / Vie B / Dom Extra

## Recuperación y contexto
- **Sueño:** 7.5+ hs consistentes. Llega bien recuperado al Extra del domingo.
- **Suplementación:** 5 g de creatina monohidrato diarios (consistente).
- **Trabajo:** Desde casa, 8-10 hs/día sentado.
- **Fútbol 3×/semana** (martes, jueves, sábado) → cubre el volumen de tren inferior.
  NO se programa pierna en el gym salvo Leg Extension en superset.
```

- [ ] **Step 2: Verificar el archivo**

Run: `head -5 PROFILE.md && echo "..." && wc -l PROFILE.md`
Expected: muestra el encabezado `# PROFILE — Manuel` y un conteo > 25 líneas.

- [ ] **Step 3: Commit**

```bash
git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  add PROFILE.md && git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  commit -m "Add PROFILE.md (datos estables del atleta)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 2: CURRENT_PLAN.md

**Files:**
- Create: `CURRENT_PLAN.md`
- Source: `IDENTITY.md` (CURRENT WORKING WEIGHTS, líneas 60-90) + `ULTIMOS_TRAININGS.md` (rutinas reales de junio)

**Contexto:** Este es el archivo más importante — la fuente de verdad operativa. Refleja
el **Mesociclo 1** arrancando con la rutina de junio 2026 (post-lesión). Los pesos salen
de la última sesión con detalle de cada día en `ULTIMOS_TRAININGS.md` (no de los de marzo,
que son pre-lesión y quedan archivados en el historial).

- [ ] **Step 1: Crear `CURRENT_PLAN.md`**. Contenido completo:

```markdown
# CURRENT PLAN — Manuel

> Fuente de verdad operativa. El agente lee esto PRIMERO para saber en qué punto del
> mesociclo está Manuel. Se actualiza después de cada sesión (working weights) y al
> cerrar cada bloque (rutinas nuevas).

## Estado del mesociclo
- **Mesociclo:** 1 (vuelta post-lesión → reconstrucción)
- **Semana:** 1 de 6
- **Inicio del bloque:** 2026-06-05
- **Deload programado:** Semana 6
- **Próximo cierre de bloque:** ~mediados de julio 2026 (armar A/B/Extra nuevos)

## Working weights actuales (junio 2026)
NO son máximos de 1 rep. No calcular porcentajes. Progresar solo vía RPE / doble progresión.

| Ejercicio | Peso actual | Última act. |
|---|---|---|
| Incline DB Press | 22 kg | 03/06/2026 |
| Chin-Up | BW | 03/06/2026 |
| Leg Extension | 70 kg | 03/06/2026 |
| OH Single Carry | 18 kg (3×50") | 25/05/2026 |
| Hammer Curl | 12.5 kg | 03/06/2026 |
| Bench Press | 75 kg | reconstruyendo (pre-lesión 75 kg) |
| Lat Pulldown | 70 kg | 19/04/2026 |
| Lateral Raise (DB) | 12 kg | 19/04/2026 |
| Bicep Curl | 25-26 kg | 19/04/2026 |
| Tricep Pushdown | 25 kg | 19/04/2026 |
| Wrist Curl | 12 kg | 19/04/2026 |
| Suitcase Carry | 18 kg (3×50") | 22/05/2026 |
| Weighted Dips | BW (sin lastre, reconstruyendo) | 22/05/2026 |

## Rutinas del bloque (Mesociclo 1)

### Workout A
| Ejercicio | Peso | Reps objetivo | RPE objetivo |
|---|---|---|---|
| Incline DB Press | 22 kg | 3×10-12 | 7-8 |
| Chin-Up | BW | 3×8 (ver nota) | 7-8 |
| Leg Extension | 70 kg | 3×13-15 | 8 |
| OH Single Carry | 18 kg | 3×50" | 7-8 |
| Hammer Curl | 12.5 kg | 3×12 | 8 |
| Ab Wheel | BW | 3×10 | 7-8 |

### Workout B
| Ejercicio | Peso | Reps objetivo | RPE objetivo |
|---|---|---|---|
| OHP (o Shoulder Press DB si no hay barra) | reconstruir | 3×6-8 | 7-8 |
| Barbell Row (o Cable Row V-grip) | reconstruir | 3×8-10 | 7-8 |
| Leg Curl / Leg Extension | 70 kg | 3×13 | 8 |
| Suitcase Carry | 18 kg | 3×50" | 7-8 |
| Weighted Dips | BW → lastre | 3×8-10 | 7-8 |
| Hanging Leg Raise | BW | 3×10 | 7-8 |

### Extra (Domingo)
| Ejercicio | Peso | Reps objetivo | RPE objetivo |
|---|---|---|---|
| Bench Press | 75 kg (reconstruir) | 3×6-8 | 7-8 |
| Lat Pulldown | 70 kg | 3×8-10 | 7-8 |
| Lateral Raise (DB) + Leg Extension | 12 kg / 70 kg | 3×12-15 | 8 |
| Bicep Curl | 25 kg | 3×10-12 | 8 |
| Tricep Pushdown | 25 kg | 3×10-12 | 8 |
| Wrist Curl | 12 kg | 3×15-20 | 8 |

## Decisiones abiertas
1. **Chin-Up** corre hot (RPE 9-10 última serie), 3 sesiones sin progresar. Patrón
   histórico, no solo post-lesión. Opción recomendada: bajar a 3×6 BW y reconstruir
   desde RPE manejable. **Pendiente de confirmar con Manuel.**
2. **OH Single Carry** sin RPE loggeado hace varias sesiones → el agente debe pedirlo.

## Notas del bloque
- Bench e isolations reconstruyendo desde baseline post-lesión (por debajo de pre-lesión).
- Press progresando limpio (Incline DB 20→22 kg en semana 2 del bloque rehab).
- Tracción/bíceps siempre más calientes que el empuje — patrón conocido.
```

- [ ] **Step 2: Verificar**

Run: `grep -c "RPE objetivo" CURRENT_PLAN.md`
Expected: `3` (una por cada rutina A/B/Extra).

- [ ] **Step 3: Commit**

```bash
git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  add CURRENT_PLAN.md && git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  commit -m "Add CURRENT_PLAN.md (plan vivo, Mesociclo 1)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 3: SESSION_HISTORY.md

**Files:**
- Create: `SESSION_HISTORY.md`
- Source: `ULTIMOS_TRAININGS.md` (sesiones junio, copiar íntegro) + `IDENTITY.md` (LIFT LOG marzo, líneas 107-234, archivar)

- [ ] **Step 1: Crear `SESSION_HISTORY.md`** con esta estructura. El bloque "BLOQUE ACTUAL"
  se copia íntegro del contenido de `ULTIMOS_TRAININGS.md` (de la línea `## ✅ Extra` en
  adelante). El bloque "ARCHIVO — MARZO 2026" copia el LIFT LOG de `IDENTITY.md` (líneas
  107-234). Encabezado completo:

```markdown
# SESSION HISTORY — Manuel

> Historial append-only. Nunca borrar entradas viejas. Cada sesión nueva se agrega
> ARRIBA del bloque actual (más reciente primero). Formato de cada sesión:
>
> ## [✅/⚠️] [Día] — [Fecha] (Mesociclo N, semana X)
> | Ejercicio | Peso | Reps | RPE |
> 🔗 link de Hevy
>
> ✅ = detalle set-por-set verificado · ⚠️ = solo resumen/patrones

---

# BLOQUE ACTUAL — Mesociclo 1 (vuelta post-lesión)

<!-- Copiar acá el contenido de ULTIMOS_TRAININGS.md desde "## ✅ Extra — Domingo 19/04/2026"
     hasta el final ("Fin del registro"), incluyendo PATRONES y DECISIONES ABIERTAS. -->

---

# ARCHIVO — MARZO 2026 (pre-lesión, referencia histórica)

<!-- Copiar acá el LIFT LOG de IDENTITY.md (Workout A T1-T7, Workout B T1-T7, Extra T1-T3)
     + la sección NOTES & ADJUSTMENTS LOG. Es contexto histórico, no operativo. -->
```

- [ ] **Step 2: Migrar el contenido real.** Leer `ULTIMOS_TRAININGS.md` e `IDENTITY.md` y
  pegar el contenido en los dos placeholders `<!-- -->`, reemplazándolos. El resultado NO
  debe contener ningún comentario `<!-- -->`.

- [ ] **Step 3: Verificar que no quedan placeholders**

Run: `grep -c "<!--" SESSION_HISTORY.md`
Expected: `0`

Run: `grep -c "hevy.com/workout" SESSION_HISTORY.md`
Expected: `>= 4` (los links de las sesiones de junio).

- [ ] **Step 4: Commit**

```bash
git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  add SESSION_HISTORY.md && git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  commit -m "Add SESSION_HISTORY.md (historial junio + archivo marzo)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 4: EXERCISE_LIBRARY.md (limpieza menor)

**Files:**
- Modify: `EXERCISE_LIBRARY.md`

El archivo ya está bien. Solo se actualiza la nota de cabecera para que apunte a la skill
en vez de a "tu Claude PT" genérico.

- [ ] **Step 1: Reemplazar las líneas 5-7** (el bloque "Use this file to tell your Claude PT...")
  por:

```markdown
Catálogo de ejercicios con el status de Manuel. El agente `manuel-trainer` lo usa al
armar sesiones y al rotar accesorios entre mesociclos. Marcá cada ejercicio:
```

- [ ] **Step 2: Verificar que sigue íntegro**

Run: `grep -c "\[YES\]" EXERCISE_LIBRARY.md`
Expected: el mismo conteo que antes del cambio (los status no se tocan).

- [ ] **Step 3: Commit**

```bash
git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  add EXERCISE_LIBRARY.md && git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  commit -m "Tweak EXERCISE_LIBRARY.md header (apunta al agente)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 5: Eliminar archivos obsoletos

**Files:**
- Delete: `IDENTITY.md`, `LIFT_LOG.md`, `WORKING_WEIGHT_LOG.md`, `ULTIMOS_TRAININGS.md`

Su contenido ya fue migrado (Tasks 1-3). Se eliminan para evitar duplicación/confusión.

- [ ] **Step 1: Confirmar que el contenido migró** antes de borrar

Run: `ls PROFILE.md CURRENT_PLAN.md SESSION_HISTORY.md`
Expected: los 3 existen (si falta alguno, NO borrar y volver a la tarea correspondiente).

- [ ] **Step 2: Borrar los 4 archivos obsoletos**

```bash
git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  rm IDENTITY.md LIFT_LOG.md WORKING_WEIGHT_LOG.md ULTIMOS_TRAININGS.md
```

- [ ] **Step 3: Verificar el estado del directorio**

Run: `ls *.md`
Expected: solo `CURRENT_PLAN.md  EXERCISE_LIBRARY.md  PROFILE.md  SESSION_HISTORY.md`

- [ ] **Step 4: Commit**

```bash
git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  commit -m "Remove archivos obsoletos (migrados a PROFILE/CURRENT_PLAN/SESSION_HISTORY)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 6: Skill `manuel-training`

**Files:**
- Create: `.claude/skills/manuel-training/SKILL.md`

Esta skill es la fuente de verdad de las REGLAS. El agente la carga primero.

- [ ] **Step 1: Crear `.claude/skills/manuel-training/SKILL.md`**. Contenido completo:

```markdown
---
name: manuel-training
description: Use when Manuel asks about his gym training — registrar/parsear una sesión de Hevy, ajustar pesos o progresión, armar la sesión del día (A/B/Extra), gestionar el mesociclo de 6 semanas y el deload, o rotar ejercicios al cerrar un bloque.
---

# Entrenamiento de Manuel

Sos el coach de hipertrofia de Manuel. Directo, basado en evidencia, sin vueltas.
Hablás como un entrenador que entrena de verdad, en español argentino. Esto es
coaching educativo de un atleta que se programa solo — no des órdenes médicas.

## Fuentes de verdad (leer SIEMPRE al empezar)
- `PROFILE.md` — quién es, schedule, contexto.
- `CURRENT_PLAN.md` — **el plan vivo**: en qué semana del mesociclo está, working
  weights, rutinas A/B/Extra, decisiones abiertas. LEÉ ESTO PRIMERO.
- `SESSION_HISTORY.md` — historial; para detectar tendencias y estancamientos.
- `EXERCISE_LIBRARY.md` — qué ejercicios puede/prefiere/evita (YES/SUB/NO).

## Sistema de programación
**Doble progresión:**
1. Arrancar en el piso del rango de reps con el RPE objetivo.
2. Sumar reps cada sesión hasta que TODAS las series lleguen al techo del rango con
   el RPE objetivo.
3. Logrado el techo: subir peso y volver al piso del rango.

**RPE objetivo:**
- Compuestos: RPE 7-8 (2-3 reps en reserva). NUNCA al fallo en compuestos.
- Aislamientos/accesorios: RPE 8 (1-2 reps en reserva).

**Incrementos al progresar:**
- Compuestos con barra (tren superior): +2.5 kg
- Mancuernas/cables accesorios: +2 kg
- Carries: +2 kg cuando se siente cómodo
- Dominadas: llegar a 3×12 limpio antes de agregar 2.5 kg de lastre

## Mesociclo (6 semanas) + deload
- El bloque dura **6 semanas**: el volumen/RPE rampea hacia arriba (MEV → MRV).
- **Semana 6 = deload:** mismas rutinas y frecuencia, ~50% del volumen (mitad de
  series), -10-20% de peso, lejos del fallo (RPE 5-6). El deload NO es opcional —
  es lo que permite que el bloque siguiente progrese.
- Al cerrar el bloque: resumen (qué progresó, qué se estancó) y armar el próximo
  A/B/Extra JUNTO a Manuel.

## Rotación de ejercicios (de la evidencia: RP, Helms, Kassiano 2022)
- **Compuestos fijos** (Bench, OHP, Barbell Row, Dominadas/Chin-up): NO se rotan.
  La especificidad manda para fuerza; mantenerlos por varios bloques.
- **Accesorios:** rotar 1-2 por grupo muscular cada 2-5 bloques, no antes.
- **Nunca** rotar ejercicios cada sesión: peor progresión y más fatiga. La variación
  tiene que ser sistemática, no aleatoria.

## Detección de estancamiento (autorregulación)
Mirar `SESSION_HISTORY.md` y avisar cuando:
- Un compuesto no mejora reps/RPE en 2+ sesiones con buen sueño/nutrición → deload o
  ajuste de peso.
- El RPE en el mismo peso "trepa" sesión a sesión → fatiga acumulándose.
- Caso conocido: el **Chin-Up** corre hot (RPE 9-10 última serie) crónicamente →
  proponer bajar a 3×6 BW y reconstruir desde RPE manejable.

## Cómo parsear un paste de Hevy
Manuel pega texto de Hevy con este formato:
```
Workout A
Wednesday, Jun 03, 2026 at 7:46pm

Incline Bench Press (Dumbbell)
Set 1: 22 kg x 10 @ 8 rpe
...
```
Pasos al recibir un paste:
1. Identificar día (A/B/Extra), fecha, y cada ejercicio con sus series (peso × reps @ RPE).
2. Agregar la sesión ARRIBA del bloque actual en `SESSION_HISTORY.md` con el formato del archivo
   (marcar ✅ si tiene detalle set-por-set).
3. Comparar contra `CURRENT_PLAN.md` y decidir por ejercicio: **subir peso / sumar reps /
   mantener** según doble progresión y RPE objetivo. Actualizar working weights si subió.
4. **Flaggear datos faltantes** (ej. el OH Single Carry suele venir sin RPE → pedirlo).
5. Avanzar el contador de semana del mesociclo si corresponde; avisar si toca deload (semana 6).
6. Confirmarle a Manuel qué se registró y la recomendación, con el porqué, en 2-4 líneas.

## Fuera de alcance
- No programar sentadilla/peso muerto/pierna pesada (lo cubre el fútbol 3×/semana).
  Único trabajo de pierna en gym: Leg Extension en superset.
- Carries son fijos en la programación — no sustituir.
- Nutrición: solo registrar la creatina (5 g/día), nada más.
```

- [ ] **Step 2: Validar el frontmatter YAML**

Run: `head -4 .claude/skills/manuel-training/SKILL.md`
Expected: muestra `---`, `name: manuel-training`, `description: ...`, `---`.

- [ ] **Step 3: Commit**

```bash
git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  add .claude/skills/manuel-training/SKILL.md && \
  git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  commit -m "Add skill manuel-training (reglas de programación)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 7: Subagente `manuel-trainer`

**Files:**
- Create: `.claude/agents/manuel-trainer.md`

- [ ] **Step 1: Crear `.claude/agents/manuel-trainer.md`**. Contenido completo:

```markdown
---
name: manuel-trainer
description: Coach de hipertrofia de Manuel. Usar para registrar una sesión (pegale el log de Hevy), ajustar pesos/progresión, pedirle la sesión del día ("hoy toca A"), o gestionar el mesociclo de 6 semanas y el deload. Reconstruyendo post-lesión (junio 2026).
tools: Bash, Read, Skill, Edit, Write, Glob, Grep
color: orange
---

Sos el **coach de hipertrofia de Manuel**. Directo, basado en evidencia, sin fluff —
hablás como un entrenador que entrena de verdad, en español argentino.

## Lo primero, SIEMPRE
1. Cargá la skill **`manuel-training`** (Skill tool). Tiene el sistema de programación,
   RPE objetivo, mesociclo/deload y reglas de rotación. Es tu fuente de verdad de las reglas.
2. Leé **`CURRENT_PLAN.md`** para saber en qué semana del mesociclo está Manuel, sus
   working weights y las decisiones abiertas.

## Qué hacés
- **Registrar una sesión:** Manuel pega el log de Hevy → parseás, lo guardás en
  `SESSION_HISTORY.md`, actualizás working weights en `CURRENT_PLAN.md` si subió, y le
  decís qué progresar (subir/sumar reps/mantener) con el porqué. Flaggeá datos faltantes.
- **Armar la sesión del día:** "hoy toca A" → tirale A/B/Extra con peso, reps y RPE
  objetivo según dónde viene en la progresión (de `CURRENT_PLAN.md`).
- **Gestionar el mesociclo:** llevá la cuenta de la semana del bloque, avisá cuándo toca
  deload (semana 6), y al cerrar el bloque hacé el resumen y armá el próximo A/B/Extra
  junto a Manuel (compuestos fijos, accesorios rotables).

## Mantenimiento y límites
- Después de cada cambio en los `.md`, dejá todo commiteado (Manuel loggea desde el cel
  vía Claude Code on the web; el commit es lo que persiste el historial).
- Si Manuel pide algo fuera del marco (otra lógica, pierna pesada, nutrición), seguí las
  reglas de la skill y avisá explícitamente que se sale de ahí.
- No inventes pesos ni RPE que Manuel no haya reportado: si falta un dato, pedilo.
```

- [ ] **Step 2: Validar el frontmatter YAML**

Run: `head -6 .claude/agents/manuel-trainer.md`
Expected: muestra `---`, `name: manuel-trainer`, `description:`, `tools:`, `color:`, `---`.

- [ ] **Step 3: Commit**

```bash
git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  add .claude/agents/manuel-trainer.md && \
  git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  commit -m "Add subagente manuel-trainer

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 8: README.md + .gitignore

**Files:**
- Create: `README.md`, `.gitignore`

- [ ] **Step 1: Crear `.gitignore`**:

```
.DS_Store
*.swp
```

- [ ] **Step 2: Crear `README.md`**:

```markdown
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
```

- [ ] **Step 3: Commit**

```bash
git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  add README.md .gitignore && \
  git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  commit -m "Add README y .gitignore

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

## Task 9: Verificación end-to-end del agente

**Objetivo:** confirmar que el agente carga la skill, lee el plan, parsea un paste de Hevy
de prueba y propone un ajuste coherente — sin romper nada.

- [ ] **Step 1: Verificar la estructura completa del repo**

Run: `git ls-files | sort`
Expected (sin archivos obsoletos):
```
.claude/agents/manuel-trainer.md
.claude/skills/manuel-training/SKILL.md
.gitignore
CURRENT_PLAN.md
EXERCISE_LIBRARY.md
PROFILE.md
README.md
SESSION_HISTORY.md
docs/superpowers/plans/2026-06-05-manuel-trainer.md
docs/superpowers/specs/2026-06-05-manuel-trainer-design.md
```

- [ ] **Step 2: Verificar que ningún archivo referencia los borrados**

Run: `grep -rl "IDENTITY.md\|ULTIMOS_TRAININGS.md\|LIFT_LOG.md\|WORKING_WEIGHT_LOG.md" --include="*.md" . | grep -v docs/`
Expected: sin resultados (los docs/ sí pueden mencionarlos como histórico; el resto no).

- [ ] **Step 3: Prueba funcional del agente.** Invocar al subagente `manuel-trainer` con el
  Agent tool y este prompt de prueba (un paste de Hevy real de Manuel):

```
Registrá esta sesión:

Workout A
Wednesday, Jun 03, 2026 at 7:46pm

Incline Bench Press (Dumbbell)
Set 1: 22 kg x 10 @ 8 rpe
Set 2: 22 kg x 10 @ 8.5 rpe
Set 3: 22 kg x 10 @ 9 rpe

Chin Up
Set 1: 8 reps @ 8 rpe
Set 2: 8 reps @ 9 rpe
Set 3: 8 reps @ 10 rpe

Hammer Curl (Dumbbell)
Set 1: 12.5 kg x 12 @ 7 rpe
Set 2: 12.5 kg x 12 @ 8 rpe
Set 3: 12.5 kg x 12 @ 8.5 rpe
```

Expected: el agente (a) carga la skill `manuel-training`, (b) lee `CURRENT_PLAN.md`,
(c) reconoce que es Workout A del 03/06, (d) propone un ajuste coherente — ej. Incline DB
llegó al techo (3×10 @ RPE ≤8 los dos primeros) → evaluar subir; Chin-Up hot (RPE 10) →
señalar el patrón / proponer 3×6. NO debe inventar ejercicios ni pesos.

- [ ] **Step 4: Revisar el cambio del agente y commitear** la sesión de prueba si quedó
  registrada (o revertirla si preferís no ensuciar el historial):

```bash
git -c user.name="Manuel" -c user.email="manuel.barreiro@flashpass.com.ar" \
  status
```
Decidir con Manuel: dejar la sesión de prueba (ya estaba en el historial de junio, así que
probablemente sea un duplicado a revertir con `git checkout -- SESSION_HISTORY.md`).

---

## Task 10: Push a GitHub

**Objetivo:** dejar el repo en GitHub para abrirlo desde el celular.

- [ ] **Step 1: Crear el repo remoto (privado) y pushear**

Run:
```bash
gh repo create manuel-trainer --private --source=. --remote=origin --push
```
Expected: crea el repo, agrega el remoto `origin` y sube `main`.

Si `gh` no está autenticado, avisarle a Manuel que corra `! gh auth login` en la sesión.

- [ ] **Step 2: Verificar**

Run: `git remote -v && git log --oneline -1`
Expected: `origin` apuntando al repo de GitHub y el último commit visible.

- [ ] **Step 3: Confirmarle a Manuel** la URL del repo y los pasos para abrirlo desde
  `claude.ai/code` en el celular (del README).

---

## Self-Review (completado por el autor del plan)

- **Cobertura del spec:** §3 arquitectura → Tasks 6,7. §4 reorg archivos → Tasks 1-5.
  §5 ciclo de trabajo → skill (Task 6) + agente (Task 7). §6 reglas → Task 6. §8 primer
  mesociclo → Task 2. §10 setup móvil → Tasks 8,10. §11 invocación → Task 9. ✅ todo cubierto.
- **Placeholders:** los `<!-- -->` de Task 3 son instrucciones de migración con verificación
  explícita (Step 3 chequea que queden en 0). No hay TODOs sin resolver.
- **Consistencia de nombres:** skill `manuel-training`, agente `manuel-trainer`, archivos
  `PROFILE/CURRENT_PLAN/SESSION_HISTORY/EXERCISE_LIBRARY` — usados consistentemente en todas
  las tareas y en el agente/skill.
```
