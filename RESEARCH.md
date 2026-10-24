# What makes a good agent skill

Notes from reading the format spec, Anthropic's authoring guidance and six public skill repos before writing anything here. Everything below is a summary in my own words. Where a repo is quoted, it is a few words at most, and each repo's license is listed with it.

Read on 2026-10-24.

## 1. The format

Primary sources:

- Agent Skills specification: https://agentskills.io/specification (spec repo https://github.com/agentskills/agentskills, Apache-2.0)
- Anthropic, skill authoring best practices: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Claude Code skills documentation: https://code.claude.com/docs/en/skills
- anthropics/skills, including `skills/skill-creator`: https://github.com/anthropics/skills

### Folder and file

A skill is a folder with a `SKILL.md` file in it. The file opens with YAML frontmatter and continues as ordinary Markdown. Anything else in the folder is optional. The spec suggests three conventional subfolders: `scripts/` for code the agent runs, `references/` for documents it reads when needed, and `assets/` for templates and static files used in the output.

### Frontmatter rules

Two fields are required.

`name` is 1 to 64 characters of lowercase letters, digits and hyphens. It cannot start or end with a hyphen or contain two hyphens in a row, and it has to match the folder name. Anthropic's platform also rejects XML tags and the reserved words "anthropic" and "claude".

`description` is 1 to 1,024 characters, has no XML tags, and should say both what the skill does and when to use it.

Optional fields in the spec are `license`, `compatibility` (up to 500 characters, only if the skill needs a particular environment), `metadata` (a string-to-string map) and `allowed-tools` (experimental). Claude Code adds its own fields on top, such as `disable-model-invocation`, `argument-hint` and `paths`. Those don't work on other platforms, so a skill meant to be shared should not depend on them.

### How the description decides when a skill runs

At startup the agent loads only each skill's name and description, about 100 tokens each. It reads the body only after the description has matched the request. If the description doesn't use the words people type, the body never loads.

What the sources agree on:

- Write it in the third person. The description is injected into the system prompt, and "I can help you" or "you can use this" phrasing confuses the agent about who is speaking.
- Say what the skill does, then when to use it, in the words users type. "Helps with marketing" will never be picked from a list of 100 skills.
- Anthropic's skill-creator says models tend to under-trigger skills, so a description should be a little pushy. It should name situations where the user needs the skill even if they never say its name.
- Claude Code cuts the description (plus an optional `when_to_use` field) at 1,536 characters in its skill listing. The spec's 1,024 limit is the one that matters for portability.

The sources disagree on one point. Anthropic's docs want the description to cover what the skill does as well as when to use it. The superpowers repo argues for "when" only, because in its testing an agent that saw a workflow summary in the description followed the summary and skipped the body. Both points hold up, so I take the middle: say what the skill produces (the deliverable) and when to use it, but never list the steps in the description.

### Progressive disclosure and length

Skills load in three stages: metadata always, the SKILL.md body when the skill triggers, and other files only when the body points to them. In practice:

- Keep the SKILL.md body under 500 lines. The spec recommends under about 5,000 tokens.
- Put long detail in `references/` and say in SKILL.md exactly when to read each file ("read references/x.md before step 4").
- Link files one level deep. Anthropic notes that when a reference file links to another reference file, the agent may only preview the second one with a partial read. Every reference should therefore be linked straight from SKILL.md.
- Give reference files over 100 lines a short contents list at the top so a partial read still shows what is there.
- Use forward slashes in paths and give files names that describe their contents (`ad-math.md`, not `ref2.md`).

### Writing the body

From Anthropic's guide:

- Assume the agent is already smart. Only write down what it doesn't already know. Every paragraph costs context once the skill loads.
- Match how strict the instructions are to how fragile the task is. Open tasks get a goal and heuristics. Fragile tasks get exact steps.
- Give one default and say when to switch ("Use X; if Y, use Z"). A list of five equal options leaves the agent to guess.
- Use one term for one thing all the way through.
- Include concrete input and output examples. They teach style and level of detail better than adjectives.
- For multi-step work, give a checklist the agent can copy and tick off. Build in a feedback loop (draft, check against the list, fix, check again).
- Leave out dated advice, or put it in a clearly marked "old way" section.

The skill-creator adds two notes. Prefer explaining why a rule exists over shouting MUST in capitals, since a model that understands the reason handles the edge cases better. And if every test run has the agent writing the same helper from scratch, bundle that helper in `scripts/`.

### Testing a skill

Anthropic recommends writing evaluations before the documentation. Run the agent on real tasks without the skill, note where it goes wrong, write the minimum instructions that fix those failures, then rerun. Its checklist asks for at least three evaluation scenarios and a test on each model you expect people to use. The skill-creator automates this. It runs each test prompt with and without the skill, grades the outputs against assertions, and separately tunes the description with about 20 trigger queries (8 to 10 that should trigger and 8 to 10 near misses that should not), split into training and held-out sets.

The near-miss idea is the useful part for a marketing library. "Write my welcome emails" should trigger the email skill and not the landing-page skill, even though both are copywriting.

## 2. Six public repos

### anthropics/skills (Apache-2.0 for most skills; the docx, pdf, pptx and xlsx skills are source-available, not open source)

https://github.com/anthropics/skills

Structure: `skills/<name>/SKILL.md` with optional `scripts/`, `references/` and `assets/`, plus a `template/` folder and a `.claude-plugin/marketplace.json` that groups skills into installable plugins.

What is good: the document skills keep SKILL.md as a router and push format detail into separate files, and they ship real scripts for the steps that have to be exact. skill-creator is the best worked example of a testing loop anywhere I looked.

What is weak: many of the creative skills are mostly taste and principles with very little procedure. The brand-guidelines skill pads its body with a keyword list, which belongs in the description.

### coreyhaines31/marketingskills (MIT)

https://github.com/coreyhaines31/marketingskills

The largest marketing collection I found: more than 50 skills under `skills/<name>/`, each with `references/` and an `evals/evals.json`. It also has a plugin manifest and validation scripts.

What is good: almost every skill starts by reading a shared product-context file, so the user explains their business once and every skill reuses it. Descriptions list many real user phrasings and point to sibling skills for near misses ("for email copy, see emails"). The copywriting skill makes the agent diagnose the input first: a blank brief, a draft with a real voice, or a one-line fix each get a different amount of rewriting. It also keeps a list of AI tells to avoid. Claims have to be supportable, and a refused claim has to name the evidence that would allow it. Shipping evals with each skill is a habit worth copying.

What is weak: descriptions run close to the 1,024 limit and read like keyword lists. Bodies run 300 to 480 lines, with long stretches of advice bullets that the model mostly knows already. Most skills open with a "you are an expert" persona line, which adds nothing. Some numbers are given without a source. The README spends a lot of space on partner promotion.

### obra/superpowers (MIT)

https://github.com/obra/superpowers

A software-development method packaged as about 15 skills (planning, test-driven development, debugging, code review), with plugin manifests for many agents.

What is good: it treats skill writing as test-driven development. Run a pressure scenario without the skill, record exactly how the agent cuts corners, then write the skill to close those gaps. Its discipline skills name the excuses an agent will make and answer each one. Its verification skill is built around one hard gate: no claim of success without fresh evidence.

What is weak: the tone is heavy on capitals and absolute rules ("Iron Law", "delete means delete"), which works for coding discipline but would read as hectoring in a marketing skill. Skills depend on each other ("required background"), so a single skill copied on its own loses context.

### vercel-labs/agent-skills (MIT per the README; GitHub detects no license file)

https://github.com/vercel-labs/agent-skills

Engineering skills for React, Next.js and deployment. The large ones keep a short SKILL.md index and one file per rule in `rules/`, each rule with an impact rating and a before/after code pair.

What is good: the rule-per-file layout with priority tiers (critical down to low) lets the agent load only the rules it needs and tells it what to fix first. Paired wrong-and-right examples are the clearest teaching format in any of these repos.

What is weak: two of the review skills are only a pointer to fetch rules from a URL at run time, so the skill does nothing offline and its behavior changes without a version bump. At least one skill's `name` (`vercel-react-best-practices`) does not match its folder (`react-best-practices`), which breaks the spec rule. Zip archives sit in the repo next to the source folders.

### trailofbits/skills (CC-BY-SA-4.0)

https://github.com/trailofbits/skills

Security research and audit skills, each packaged as a plugin under `plugins/<name>/skills/<skill>/`, with a strong contributor guide and CI that validates metadata.

What is good: the house rules are sharp. Skills should add behavior the model doesn't already have instead of pasting reference material, and should explain trade-offs and say why an anti-pattern is wrong. How strict a skill is should match how risky the task is. Audit skills must include a "rationalizations to reject" section. The guide also points to three reference skills at basic, intermediate and advanced levels for contributors to copy.

What is weak: the plugin-per-skill nesting is deep and heavy for anyone who just wants to drop one folder into their skills directory. Some skills assume particular local tools are installed.

### getsentry/skills (Apache-2.0)

https://github.com/getsentry/skills

Sentry's internal engineering skills. Trail of Bits points to its security-review skill as a model.

What is good: the GitHub Actions review skill opens with explicit scope and out-of-scope lists and a threat model that says what not to report. A confidence table decides what gets reported, and a routing table maps what the agent finds to the one reference file it should load. Every finding needs five named parts or it gets downgraded.

What is weak: it is written for a narrow expert audience and assumes a lot of context. The description stuffs in many trigger phrases and loses readability.

## 3. Why skills fail

Patterns I saw across these repos and the guidance:

1. The description never fires. "Marketing helper" or "SEO best practices" is too vague to beat the agent's default of answering directly. It needs the words users type and the deliverable they want.
2. Advice with no procedure. A wall of principles ("know your audience", "be specific") is something the model already believes, so repeating it doesn't change the output. A numbered procedure with points where the agent has to choose does.
3. No inputs. If the skill doesn't say what to ask for first, the agent invents the business, the audience and the numbers, and the output reads as generic.
4. No defined output. Without a template or a described deliverable, every run returns a different shape, and nobody can check it.
5. No example. The agent guesses the level of detail. One short worked example settles it.
6. No checks. Without a final list to run before handing work over, made-up statistics, invented testimonials and broken promises slip through.
7. Overlap. Two skills that both claim "copywriting" fight over the same requests. Descriptions need clear edges and should point to the sibling skill.
8. Bloat. A 600-line SKILL.md full of background buries the steps that matter, and it costs context on every run.
9. Hidden dependencies. A skill that only works if another skill, a paid tool or a remote URL is present will break for most people who copy it.

## 4. Rules for this repo

1. One folder per skill at `skills/<name>/`. The folder name and `name` field match, in lowercase with hyphens, and are named after the deliverable a marketer would ask for (`landing-page-copy`, `welcome-emails`).
2. Each description is third person and under 1,024 characters. It says what the skill produces and when to use it, in phrases a user would type, and names the near-miss sibling skill where one exists. It never lists the procedure.
3. Frontmatter uses only spec fields (`name`, `description`, and `metadata` for the version), so the skills work in any agent that supports the format.
4. SKILL.md stays under 250 lines. Long tables, interview guides, scoring sheets and templates go in `references/`, and code goes in `scripts/`. Each file is linked one level deep from SKILL.md, with a line saying when to open it.
5. Every SKILL.md has the same working parts in the same order: what to ask the user first, a numbered procedure, decision rules with real numbers where the evidence has them, the output format, a short worked example, and a final check list the agent runs before handing work over.
6. No persona lines and no explaining what the model already knows. Cut any sentence that would fit another skill unchanged.
7. Never invent facts about the user's business. Testimonials, numbers, prices, features and customer quotes come from the user or get marked as gaps.
8. Study numbers keep their source and year ("Backlinko's 2019 study of 12 million outreach emails found..."), and secondhand figures name the original study where it's known. They are context for a decision, never a promise.
9. Product-neutral. Examples use made-up businesses of different kinds: a shop, a local service, a newsletter, an app, a B2B tool.
10. Nothing copied from other repos or from source articles. Structure ideas are borrowed; all text is written fresh.
11. Plain writing: second person, specific, mixed sentence length, no em dashes, no emojis, no filler labels. Every file is checked against a banned-phrase list before it ships.
12. Each skill is tested on a realistic made-up task, and fixed for whatever that run showed was unclear or missing.
