# Process Nervous System (PNS)

## OpenClaw Bootstrap Runbook

**Status:** Draft v0.2\
**Purpose:** A conversational onboarding, migration, and self-bootstrap document for installing, adapting, and extending PNS inside a user's OpenClaw environment.

---

## 1. What PNS Is

**PNS** stands for **Process Nervous System**.

PNS is not a conventional software product with one rigid installation path. It is a **portable runbook + convention layer** for turning OpenClaw into a more structured, self-documenting, workflow-aware project system.

A user should be able to paste this document into their OpenClaw agent and have that agent:

1. understand the purpose of PNS,
2. validate the user's current OpenClaw environment,
3. interview the user about preferred architecture, workflow, security posture, and model strategy,
4. create the necessary local workspace files immediately,
5. stand up the relevant skills, docs, hooks, helper scripts, cron jobs, and optional additional agents,
6. checkpoint onboarding progress to disk as it goes,
7. leave behind a usable, legible, locally owned nervous system that can evolve with the user.

PNS is therefore both:

- a **method** for structuring project work, and
- a **bootstrap spec** for teaching an OpenClaw instance how to implement that method in its own native environment.

PNS should be treated as **forkable, inspectable, local-first text infrastructure**.

---

## 2. Why This Exists

PNS begins from a simple observation:

OpenClaw is unusually strong at **conversational setup, iterative adaptation, file-based local ownership, agent routing, and environment-aware self-modification**.

That makes it a better host for this kind of methodology than a static IDE-centric install flow.

The point is not to faithfully clone another method.\
The point is to **translate the useful parts into OpenClaw-native primitives**, improve what can be improved, and let each user's agent adapt the details to the live environment.

PNS should preserve the good parts of structured agentic development:

- phased planning,
- explicit artifacts,
- context hygiene,
- guided next-step recommendations,
- implementation loops,
- review and retrospection,
- optional role separation,
- local documentation as source of truth,
- better chain-of-custody around what happened and why.

But PNS should avoid dead weight:

- bloated always-injected prompt files,
- brittle assumptions about tool names,
- one-size-fits-all architecture,
- frozen workflows that ignore how fast OpenClaw changes,
- vague “framework” installs that collapse when interrupted halfway through.

---

## 3. Core PNS Principles

### 3.1 Conversational first

PNS should be installed and configured through a short guided conversation, not a giant wall of manual setup steps.

### 3.2 Local ownership

The user's workspace is the product. PNS should create local files, docs, and skills the user can inspect, edit, version, and fork.

### 3.3 Validate against reality

OpenClaw changes quickly. The agent must verify assumptions against the **current local environment** and **current OpenClaw docs** before deciding implementation details.

### 3.4 Native before emulation

When OpenClaw has a first-class tool or capability, use it. Do not recreate native OpenClaw functionality with awkward wrapper hacks.

### 3.5 Skills for instruction, tools for execution

PNS behavior should usually live in **skills and local documentation**, while actual work should prefer **native OpenClaw tools**, plus hooks, plugins, helper scripts, or cron when appropriate.

### 3.6 Explicit artifacts

Project state should live in files, not only in model memory.

### 3.7 Fresh context boundaries

Major workflow transitions should encourage fresh sessions or clean phase boundaries so the agent does not drag stale context forever.

### 3.8 One system, many anatomies

PNS should support both:

- a **single-agent nervous system**, and
- a **multi-agent nervous system**.

The user chooses based on preference, complexity, trust, and how much separation they want.

### 3.9 Checkpoint relentlessly

Onboarding and reconfiguration should be resumable. PNS should checkpoint progress, rationale, and pending steps to disk as it goes.

### 3.10 Playful naming, serious utility

PNS should be useful first. The branding may wink. The workflow may flirt a little. But the system must remain legible, trustworthy, and genuinely helpful.

---

## 4. Desired User Experience

A good PNS install should feel like this:

1. The user pastes this document into OpenClaw.
2. The agent recognizes it as a bootstrap spec.
3. The agent inspects the workspace and OpenClaw environment.
4. The agent creates the minimum PNS skeleton and onboarding progress files immediately.
5. The agent asks a short sequence of high-value onboarding questions.
6. The agent proposes a PNS architecture adapted to the user's actual setup.
7. The agent checkpoints each onboarding step to disk.
8. The agent creates or updates the local PNS docs, folders, skills, helper scripts, and optional automations.
9. The agent explains how the user will actually work with PNS day to day.
10. The agent leaves the user with a clear “next step” entrypoint.

If the user gets distracted, switches sessions, or later wants to re-architect the system, onboarding should be safely re-runnable.

The user should finish onboarding with the feeling:

> “My OpenClaw now has a structured process layer that understands how I like to work, I own the whole thing, and I can resume or reconfigure it without starting from scratch.”

---

## 5. What the Agent Must Understand When Reading This Document

If you are the user's OpenClaw agent and the user has provided this document, interpret it as:

- a request to **bootstrap or adapt PNS locally**,
- a request to **adapt implementation to the current OpenClaw environment**,
- a request to **co-design the setup conversationally with the user**,
- a request to **leave behind local documentation and reusable structure**,
- a request to **prefer transparent file-based implementation over hidden magic**,
- a request to **make onboarding resumable and safe to rerun**.

Do **not** assume that every feature in this document must be installed immediately.

Instead:

- inspect,
- validate,
- scaffold,
- checkpoint,
- ask,
- propose,
- install the smallest coherent useful version first,
- then expand.

---

## 6. Bootstrap Behavior Contract

When bootstrapping or adapting PNS, the agent should follow this order.

### Phase A — Orient

1. Confirm that the user wants to initialize, resume, repair, migrate, or adapt PNS in the current OpenClaw setup.
2. Inspect current workspace files and existing skills, hooks, scripts, docs, and project state.
3. Check current OpenClaw capabilities relevant to PNS.
4. Identify whether a partial PNS install already exists.
5. Determine whether this is:
   - a first install,
   - a resumed onboarding,
   - a repair run,
   - a migration from single-agent to multi-agent,
   - a migration from multi-agent to single-agent,
   - or a targeted reconfiguration.

### Phase B — Scaffold Immediately

Before deeper onboarding, create the minimal PNS skeleton so the process can survive interruption. At minimum, create:

- `PNS.md`
- `pns/docs/pns-overview.md`
- `pns/docs/pns-operator-guide.md`
- `pns/docs/pns-architecture.md`
- `pns/docs/pns-use-cases.md`
- `pns/docs/pns-reference.md`
- `pns/docs/model-playbooks.md`
- `pns/state/onboarding-progress.md`
- `pns/state/active-projects.md`
- `pns/state/workflow-map.md`
- `pns/state/decisions.md`
- `pns/state/security-posture.md`
- `pns/state/chain-of-custody.md`
- `pns/notes/onboarding-notes.md`

These may start as minimal stubs, but they must exist early.

### Phase C — Validate

Validate implementation assumptions against the live environment. This includes, where relevant:

- current OpenClaw docs,
- available native tools,
- skill locations and precedence,
- tool policy and deny/allow boundaries,
- agent and workspace layout,
- sandboxing and exec approval posture,
- whether hooks, cron, plugins, ACP, session spawning, or sub-agents are available and appropriate.

If a documented approach is outdated or no longer appropriate, adapt the plan and explain why.

### Phase D — Checkpoint

After every meaningful bootstrap step, update `pns/state/onboarding-progress.md` with:

- current phase,
- completed steps,
- pending steps,
- unresolved questions,
- chosen architecture direction so far,
- any blockers or warnings,
- the exact next recommended action.

This file is the source of truth for resuming onboarding.

### Phase E — Interview

Ask the user a brief but meaningful onboarding questionnaire. Do not bury them in framework jargon. Focus on:

- what they want PNS to help with,
- whether they prefer one agent or multiple,
- how much structure they want,
- their desired security posture,
- whether they want optional external harnesses via ACP,
- whether they want automation like hooks or cron from day one,
- which models they want to use for which tasks.

### Phase F — Propose

Present a concrete recommended setup with tradeoffs. Example dimensions:

- single-agent vs multi-agent,
- lean vs full artifact set,
- native-only vs ACP-enabled,
- minimal automation vs hooks and cron,
- relaxed personal-use security vs hardened shared-ingress setup,
- simple model routing vs task-specific model routing.

### Phase G — Install or Migrate

Create or update the files, docs, skills, scripts, and optional automations. Keep names consistent and local documentation clear. If the user is changing architecture, perform migration rather than reinstalling blindly.

### Phase H — Hydrate

Fill in the initial docs using the user's stated preferences, use cases, model choices, and security posture. Do not leave empty ceremonial files unless a placeholder truly helps.

### Phase I — Teach

Explain how to use PNS in practice:

- how to start a project,
- how to ask for next steps,
- how to inspect state,
- how to resume onboarding,
- how to rerun onboarding to change implementation,
- how to add or change capabilities later.

---

## 7. Determinism, Resumability, and Momentum

PNS should behave like a robust onboarding system, not a one-shot prompt.

### 7.1 The onboarding progress file is mandatory

`pns/state/onboarding-progress.md` should be created at the beginning and updated throughout onboarding.

It should record:

- install status,
- phase status,
- architecture decision status,
- security decision status,
- model routing decision status,
- file creation status,
- skill creation status,
- automation creation status,
- pending user answers,
- migration status if applicable,
- next step.

### 7.1.1 Recommended progress file shape

Use a predictable structure so onboarding can be resumed by a fresh session with minimal ambiguity. A strong default shape is:

```md
# Onboarding Progress

## Status
- install_mode: first_install | resume | repair | extend | reconfigure | migrate
- overall_status: todo | in_progress | blocked | done
- current_phase: orient | scaffold | validate | interview | propose | install | hydrate | teach
- next_step: <single authoritative next action>

## Decisions
- architecture: undecided | single_agent | multi_agent | hybrid
- security_posture: undecided | personal | personal_high_capability | shared_or_remote | sensitive_workflows
- acp_mode: undecided | none | optional | primary_for_specific_flows
- automation_level: undecided | none | light | proactive
- model_strategy: undecided | simple | task_specific

## Checkpoints
- [ ] workspace inspected
- [ ] minimal skeleton created
- [ ] live environment validated
- [ ] onboarding interview completed
- [ ] architecture proposed
- [ ] security posture documented
- [ ] model playbooks created
- [ ] core skills installed
- [ ] optional automations configured
- [ ] operator guide hydrated

## Open Questions
- <question and owner>

## Warnings / Blockers
- <blocking issue or none>

## Migration Notes
- source_shape: <if applicable>
- target_shape: <if applicable>
- backups_created: yes | no
- customizations_requiring_review: <list>

## Last Update
- timestamp: <iso8601>
- updated_by: <agent/session identifier if available>
```

The important part is not this exact wording. The important part is that the file has a stable schema, explicit statuses, and one canonical `next_step`.

### 7.2 Onboarding must be safely re-runnable

If the user reruns onboarding, the agent should first inspect existing PNS state and determine whether to:

- resume,
- repair,
- extend,
- reconfigure,
- or migrate.

The default behavior should be conservative: reuse good existing work, patch missing pieces, and avoid duplicating files or blowing away user customizations.

### 7.3 Migration invariants

When PNS changes architecture or rewires core implementation, the agent should obey these invariants:

1. Never delete or overwrite user-authored files without first creating a clearly named backup or patch plan.
2. Never duplicate skills with conflicting names when an update, rename, or compatibility note would be cleaner.
3. Never silently replace the user's `AGENTS.md`, `SOUL.md`, `USER.md`, or equivalent persona files; propose succinct edits instead.
4. Always checkpoint migration intent before making changes and checkpoint migration outcome immediately after.
5. Always update `PNS.md`, `pns/docs/pns-reference.md`, and `pns/state/onboarding-progress.md` to reflect the new installed reality.
6. Always document any intentionally preserved legacy behavior so future agents can understand why it still exists.
7. Prefer additive migration over destructive reinstall unless the user explicitly wants a reset.

### 7.4 Install the skeleton before custom detail

The minimum file structure should be created before deep customization so the system can survive context loss or user interruption.

### 7.5 Prefer helper scripts for repeatable steps

If certain PNS flows benefit from deterministic helper scripts, generate them and document them clearly rather than relying on purely improvised model behavior every time.

---

## 8. PNS Onboarding Interview

The onboarding interview should be short, adaptive, and conversational. It should usually fit in a small number of high-value questions, with follow-ups only when needed.

The agent should gather at least the following:

### 8.1 Use case profile

Ask what kinds of work the user wants PNS to support. Examples:

- solo coding projects,
- product planning,
- Discord bots,
- local automation,
- OpenClaw skills, plugins, or internal OpenClaw extensions,
- remote repository work unrelated to OpenClaw itself,
- content and research pipelines,
- mixed technical and creative work,
- long-lived agentic projects,
- life automation and soft-skills assistant use,
- finance, trading, or research workflows.

### 8.2 Workflow strictness

Ask whether the user prefers:

- a lightweight guiding system,
- a more explicit artifact-driven process,
- or a fairly opinionated multi-phase workflow.

### 8.3 Architecture preference

Ask whether the user wants:

- **single-agent PNS**,
- **multi-agent PNS**,
- or a **hybrid PNS**.

If they are unsure, recommend one. A good default is usually **single-agent first**, unless they already know they want strong persona, workspace, or security separation.

### 8.4 Security posture

Ask how exposed or sensitive their OpenClaw setup is. Examples:

- personal-use only,
- personal-use but high-capability,
- shared-ingress or remotely reachable,
- handles sensitive repos, credentials, or financial workflows.

Then tailor PNS within the currently documented OpenClaw security boundaries.

### 8.5 ACP preference

Ask whether the user wants PNS to optionally route implementation work to external ACP-compatible harnesses such as Codex or Claude Code.

Explain this in plain language:

- native OpenClaw is simpler,
- ACP can be useful if they want thread-bound or harness-specific coding flows,
- it is optional,
- it should be documented carefully if enabled.

### 8.6 Automation preference

Ask whether they want:

- no automation yet,
- helpful defaults,
- or a more proactive system using hooks and or cron.

### 8.7 Model strategy

Ask which models or providers they want to use for which PNS tasks. Examples:

- planning,
- coding,
- reviews,
- research,
- summarization,
- low-cost routine tasks,
- higher-intelligence planning tasks.

### 8.8 Domain preferences and knowledge sources

Ask about domain-specific preferences that should shape setup. Examples:

- preferred UI framework or design system,
- preferred coding stack,
- preferred research sources,
- repo hosting patterns,
- local knowledge sources such as Obsidian, markdown vaults, or vector-backed memory,
- existing MCP servers, shared skills, or toolchains they already trust.

This helps PNS build the right local knowledge surfaces early instead of improvising later.

---

## 9. Recommended PNS Architectures

### 9.1 Single-Agent PNS

Best for most users at first.

Characteristics:

- one OpenClaw agent,
- one main workspace,
- PNS docs and skills installed locally,
- optional hooks, scripts, and cron,
- strongest conversational continuity,
- lowest setup complexity.

Use this when the user wants simplicity and flexibility.

### 9.2 Multi-Agent PNS

Best for users who want hard separation between process roles, domains, or trust boundaries.

Possible roles include:

- **pns-core** — default front door and orchestrator,
- **pns-architect** — structure, planning, systems thinking,
- **pns-builder** — implementation and execution,
- **pns-aftercare** — review, cleanup, retrospective, docs hygiene.

This naming scheme is intentionally half-serious. It should remain understandable even when it is being a little bit cheeky.

Use multi-agent PNS when the user wants:

- separate workspaces,
- distinct identities or channels,
- cleaner context isolation,
- different tool or sandbox policies per agent,
- optional ACP delegation patterns,
- stronger chain-of-custody around who did what.

### 9.3 Hybrid PNS

A single main agent with optional spawned sub-agents, session tools, or ACP sessions for special tasks.

This is often the most practical power-user setup.

### 9.4 Workflow-oriented recommendations

#### Building OpenClaw skills, hooks, plugins, or internal extensions

A hybrid or multi-agent setup is often useful here because the user may want stronger auditability, testing discipline, and separation between orchestration and implementation.

#### General remote-repo software work

A single-agent or hybrid setup is often enough. The main need is usually good planning, chain-of-custody, and repeatable flow support rather than OpenClaw-specific architecture.

#### Soft-skills assistant and life automation use

A lighter single-agent PNS is usually the right fit. The system should emphasize use-case docs, memory hygiene, routines, and safety boundaries more than software-heavy artifacts.

#### Finance, trading, and research workflows

A more structured setup is often justified. PNS should emphasize logging, decision tracking, model routing, validation, and careful security posture.

---

## 10. PNS Local File Layout

The exact layout may vary, but a strong default is:

```text
PNS.md
pns/
  docs/
    pns-overview.md
    pns-operator-guide.md
    pns-architecture.md
    pns-use-cases.md
    pns-style.md
    pns-reference.md
    model-playbooks.md
    knowledge-sources.md
  state/
    onboarding-progress.md
    active-projects.md
    workflow-map.md
    backlog.md
    decisions.md
    security-posture.md
    chain-of-custody.md
  skills/
    pns-bootstrap/
      SKILL.md
    pns-help/
      SKILL.md
    pns-plan/
      SKILL.md
    pns-build/
      SKILL.md
    pns-review/
      SKILL.md
  scripts/
    optional helper scripts...
  templates/
    project-template.md
    brief-template.md
    plan-template.md
    review-template.md
  hooks/
    optional...
  notes/
    onboarding-notes.md
```

If multi-agent PNS is used, each relevant workspace may contain its own local PNS docs and skills, with some shared reference material copied or generated as needed.

---

## 11. PNS Core Documents

The bootstrap should generate and hydrate these documents.

### `PNS.md`

The local top-level nervous system contract. This should be short and high-signal. It explains what this instance of PNS is for, how it is configured, and how to enter the workflow.

### `pns/docs/pns-overview.md`

Human-readable overview of this user's local PNS.

### `pns/docs/pns-operator-guide.md`

How the user should work with their PNS day to day.

### `pns/docs/pns-architecture.md`

Current architecture choice, rationale, and extension notes.

### `pns/docs/pns-use-cases.md`

What kinds of projects and requests this local PNS is designed to support.

### `pns/docs/pns-style.md`

Tone, naming conventions, artifact strictness, and how playful or serious the local branding should be.

### `pns/docs/pns-reference.md`

A locally generated technical reference that summarizes the live implementation choices made during onboarding. This is not merely a copy of this document. It should reflect the actual installed reality.

### `pns/docs/model-playbooks.md`

A concise local reference describing how the user's chosen models should be prompted for different PNS tasks. This should summarize the provider guidance actually relevant to this user's setup, not dump huge vendor docs into every session.

### `pns/docs/knowledge-sources.md`

A living inventory of the local and remote knowledge surfaces PNS relies on for a given user or project. Examples:

- official framework docs,
- repo-local reference files,
- installed MCP servers,
- shared or local skills,
- internal notes or vaults,
- memory folders,
- data sources used for research or finance workflows.

This file should make project mise-en-place explicit and easy to refresh.

### `pns/state/onboarding-progress.md`

The canonical resumability ledger for onboarding, repair, and migration.

### `pns/state/active-projects.md`

Current projects and their status.

### `pns/state/workflow-map.md`

The phases and transitions used in this local PNS instance.

### `pns/state/backlog.md`

Optional rolling backlog for PNS itself.

### `pns/state/decisions.md`

A durable decision log for major PNS changes.

### `pns/state/security-posture.md`

The user's chosen security stance, OpenClaw-specific constraints, and any active hardening decisions.

### `pns/state/chain-of-custody.md`

A concise record of where major actions, decisions, and outputs came from. This may be complemented by hooks, helper scripts, git history, and provider-native traces where available.

---

## 12. PNS Workflow Model

PNS should preserve the general strengths of a structured development method while adapting it to OpenClaw.

A strong default flow is:

1. **Signal** — clarify intent, scope, and context.
2. **Shape** — decide the plan, artifacts, architecture, or approach.
3. **Build** — implement or execute in manageable units.
4. **Check** — review output against goals and constraints.
5. **Aftercare** — clean up state, document decisions, and decide what comes next.

These names can be adjusted locally. The point is that the system should have an obvious rhythm.

If the user wants a more direct mapping to traditional software workflows, that is fine. PNS should support both plain and playful naming.

PNS may also define named **flows** for specific repeatable patterns. These flows may use helper scripts where that improves determinism.

---

## 13. Selective Skill Surface

PNS should suggest a base skill surface, but it should **not** blindly implement every possible workflow as a skill.

The rule is:

> Implement the smallest skill set that improves OpenClaw's native experience without duplicating first-class tools.

PNS should primarily use skills as **behavioral entrypoints** and **instruction surfaces**.

Suggested core skills:

### `pns-bootstrap`

Used when installing, resuming, repairing, or reconfiguring PNS. Reads local docs, validates environment assumptions, interviews the user, checkpoints onboarding state, and updates local PNS files.

### `pns-help`

The “what should I do next?” entrypoint. Inspects current PNS state and recommends the next sensible step. It should also detect incomplete onboarding and help the user resume.

### `pns-plan`

Used for scoping, planning, artifact generation, and implementation prep.

### `pns-build`

Used for implementation or execution work. Should prefer native OpenClaw tools and available local capabilities.

### `pns-review`

Used for review, documentation, refactoring recommendations, retrospection, and readiness checks.

Optional skills:

- `pns-research`
- `pns-docs`
- `pns-route`
- `pns-aftercare`
- `pns-project-init`
- `pns-ui`

The exact skill set may be smaller or larger depending on the user's needs.

### 13.1 UI and frontend flow support

UI and frontend work is a special case worth treating explicitly. Raw model output is often weak at sophisticated modern design unless the agent has better visual and framework-specific support.

When a project includes significant UI work, PNS may install or recommend a dedicated `pns-ui` flow that:

- asks the user which UI framework, component library, and design system they prefer,
- builds or refreshes a small local knowledge pack for that stack,
- uses OpenClaw's browser and web tooling to fetch current docs and visually inspect running output,
- prefers framework-native MCP servers or agent skills when high-quality support exists,
- records implementation conventions and review criteria in local PNS docs.

Examples include component-library-specific MCP servers or shared skills for frameworks such as HeroUI when those tools materially improve implementation quality.

### 13.2 Domain accelerators

PNS can define additional domain-oriented flows, but only when they provide real leverage. Good candidates are workflows where structured artifacts, knowledge refresh, validation, and chain-of-custody are clearly useful. Examples:

- UI or frontend design and implementation,
- plugin or skill development for OpenClaw,
- research workflows,
- finance or trading workflows,
- long-lived content pipelines.

A bad candidate is a “flow” that merely renames a native OpenClaw tool without adding process value.

---

## 14. Implementation Rules for Skills

When creating PNS skills, follow these rules:

1. Keep skill instructions concise and purposeful.
2. Store skills locally in the workspace when they are specific to the user's local PNS.
3. Prefer reusable docs for long reference material.
4. Do not stuff giant always-needed instructions into every context surface.
5. Tell the agent when to read reference docs, not to memorize everything.
6. Prefer native OpenClaw tools for actual actions.
7. Keep user-owned files legible and editable.
8. When repeatability matters, pair skills with documented helper scripts.
9. Log meaningful actions to local chain-of-custody artifacts when appropriate.

---

## 15. Hooks, Cron, Plugins, Helper Scripts, and Knowledge Surfaces

PNS should use additional OpenClaw mechanisms when they genuinely improve the system.

### Hooks

Hooks are appropriate for event-driven nervous system behavior, such as:

- saving state on session reset,
- maintaining a lightweight memory snapshot,
- updating a local decision log,
- triggering onboarding helpers,
- auto-refreshing certain reference files,
- maintaining a chain-of-custody ledger.

### Cron

Cron is appropriate for scheduled or recurring PNS support, such as:

- daily status rollups,
- reminder prompts,
- periodic project check-ins,
- maintenance tasks for local docs or queues.

### Plugins or bundles

Plugins or mapped bundle content may be useful when the user wants a more advanced extension surface or interoperable package format. Use them when they clearly help. Do not introduce them for ceremony alone.

### Helper scripts

Helper scripts are appropriate when a flow benefits from repeatability, logging, or deterministic state transitions. Examples:

- scaffolding PNS files,
- rotating or normalizing status docs,
- collecting flow logs,
- validating artifact completeness,
- checking chain-of-custody metadata,
- translating project state into summary views.

### Knowledge surfaces and mise-en-place

For many domains, especially frontend, research, trading, and OpenClaw-extension work, clean high-signal context is one of PNS's biggest advantages.

PNS should therefore encourage project-level knowledge preparation at project start or resume. Depending on the project, that may include:

- refreshing official docs,
- capturing repo-local conventions,
- noting installed MCP servers or shared skills,
- mapping trusted data sources,
- linking memory folders or knowledge stores,
- summarizing stack-specific rules into small local reference files.

The goal is not to hoard context. The goal is to keep the right context legible, local, and refreshable.

## 16. Security and Trust Boundaries

Security is part of onboarding, not a later afterthought.

During onboarding or reconfiguration, the agent should inspect the current documented OpenClaw security surfaces and align PNS to them rather than hacking around them.

The agent should:

1. assess the user's practical threat model,
2. document it in `pns/state/security-posture.md`,
3. recommend the smallest sensible hardening moves,
4. keep PNS inside currently documented OpenClaw boundaries.

Important topics to inspect and document may include:

- sandboxing posture,
- workspace scoping,
- tool allow and deny policy,
- exec approval posture,
- elevated mode usage,
- multi-agent trust boundaries,
- ACP exposure,
- plugin trust,
- channel or remote-ingress exposure.

If the user's OpenClaw environment is shared, remotely reachable, or otherwise exposed beyond personal local use, PNS should lean more conservative.

---

## 17. ACP and External Harnesses

PNS should explicitly offer the user the option to integrate external ACP-compatible coding harnesses.

This should be framed as an optional capability, not a requirement.

Potential reasons to enable ACP in a PNS setup:

- the user already likes Codex or Claude Code,
- they want thread-bound coding sessions,
- they want to delegate implementation work to a specific harness,
- they want stronger workflow separation between orchestration and execution.

Potential reasons to skip ACP at first:

- simpler setup,
- fewer moving parts,
- native OpenClaw is enough,
- the user can always add ACP later,
- some ACP lifecycle details may warrant more careful documentation.

If ACP is enabled, document clearly:

- what harnesses are available,
- how PNS should decide when to route work there,
- what remains in the main OpenClaw agent,
- how state should be documented back into local PNS files,
- any lifecycle limitations or caveats relevant to session recovery.

---

## 18. Model Strategy and Prompting Profiles

Many OpenClaw users have multiple models or providers available. PNS should treat model selection as part of system design.

During onboarding, the agent should ask which models the user wants to use for which categories of work. Examples:

- planning,
- orchestration,
- coding,
- code review,
- research,
- writing,
- summarization,
- cheap routine work,
- high-stakes reasoning.

The agent should then:

1. identify the relevant official prompting guidance for the chosen models,
2. summarize only the high-value rules relevant to the user's tasks,
3. save those summaries in `pns/docs/model-playbooks.md`,
4. compare them against the user's `AGENTS.md`, `SOUL.md`, and `USER.md` where applicable,
5. suggest any succinct, high-value additions the user may want to make.

PNS should not inject large provider prompt guides wholesale into every session. Instead, it should keep concise local playbooks and tell agents where to read deeper reference material when needed.

---

## 19. Naming Philosophy

Branding matters because it helps users remember, reuse, and talk about the system. PNS sounds like a male-anatomy joke and therefore presents an effective mnemonic durability strategy. Also it is funny.

PNS should have a naming style that is:

- memorable,
- slightly mischievous,
- not so horny that it becomes unreadable,
- legible in docs,
- funny when spoken,
- useful even after the joke lands.

A good rule is:

> **Wink, don’t wedge.**

The joke should be there if you notice it. The system should still look like a real system.

Suggested naming palette:

- **Signal**
- **Pulse**
- **Spine**
- **Build**
- **Thrust**
- **Check**
- **Aftercare**
- **Release**

Not every install needs all of these. Choose the level of camp the user wants.

---

## 20. What PNS Should Borrow, and What It Should Change

PNS should preserve the useful structural ideas of a disciplined agentic workflow system:

- guided next-step logic,
- project inspection,
- resumable process state,
- explicit phase transitions,
- artifact creation,
- implementation loops,
- review and readiness practices,
- extension through modular behavior.

But PNS should adapt these ideas to OpenClaw-native strengths:

- conversational onboarding,
- live environment validation,
- per-agent workspaces,
- skill-first instruction surfaces,
- hooks, helper scripts, and cron when useful,
- optional ACP integration,
- user-owned local reference docs,
- easier iterative self-modification,
- more legible migration and recovery behavior.

In short:

**Do not cargo-cult another system. Translate its strengths into OpenClaw.**

---

## 21. Bootstrap Deliverables

A successful PNS onboarding should leave behind:

1. a top-level `PNS.md`,
2. local PNS docs reflecting the user's real setup,
3. an onboarding progress file that enables resumption,
4. a minimal useful skill set,
5. any chosen hooks, scripts, cron, or config changes,
6. architecture notes,
7. use-case notes,
8. security posture notes,
9. model playbooks,
10. a clear first operational entrypoint,
11. a recommendation for how to expand later.

If multi-agent PNS is chosen, onboarding should also leave behind:

- documented agent roles,
- workspace mapping notes,
- routing or binding notes if relevant,
- cross-agent state conventions,
- any sandbox or tool-boundary differences between agents.

---

## 22. Post-Install Entry Prompt

At the end of onboarding, the agent should give the user a very clear next move. For example:

- “PNS is installed. Ask `pns-help` what to do next.”
- “Your PNS is ready. Start by describing the first project you want it to manage.”
- “Your single-agent PNS is active. The next useful step is to initialize your first tracked workflow.”
- “Your onboarding paused safely. Use `pns-bootstrap` to resume from the recorded next step.”

---

## 23. PNS Self-Improvement Rule

PNS should be able to improve itself over time.

Whenever the user asks to extend, repair, migrate, or refine PNS, the agent should:

1. inspect the current local implementation,
2. compare it against the current OpenClaw environment,
3. inspect `pns/state/onboarding-progress.md` and related state files,
4. propose the smallest coherent upgrade,
5. checkpoint the planned changes,
6. update the local docs so the installed system stays legible.

PNS is not a fossil. It is a living local process layer.

---

## 24. First-Boot Instruction to the Agent

If you are the user's OpenClaw agent and this document is being used to initialize or adapt PNS, begin by doing the following:

1. Inspect the current workspace for existing PNS-related files, skills, hooks, scripts, and project state.
2. Create the minimal PNS skeleton and onboarding progress files immediately.
3. Validate current OpenClaw capabilities and implementation assumptions before proposing setup steps.
4. Ask the user a brief onboarding interview covering use case, desired structure, security posture, architecture, ACP preference, automation preference, and model strategy.
5. Recommend either single-agent, multi-agent, or hybrid PNS.
6. Create or update the initial local PNS docs, skills, and any helper infrastructure.
7. Hydrate those docs with the user's actual answers.
8. Update `pns/state/onboarding-progress.md` after each meaningful step.
9. Explain how the user should operate the system from here, including how to resume or rerun onboarding later.

Do not over-install.\
Do not overcomplicate.\
Create a real nervous system, not ceremonial framework tax.

---

## 25. Closing Position

PNS should feel less like “installing a framework” and more like **teaching your OpenClaw how you want to think, plan, build, recover, and reconfigure**.

The joke in the name is allowed.\
The utility is mandatory.

The system should be memorable enough that people talk about it, flexible enough that they fork it, and grounded enough that their own agent can keep it alive as OpenClaw evolves.

That is the goal.

