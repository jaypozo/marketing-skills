# Marketing skills

Thirteen skills for AI agents, each covering one marketing job. A skill is a folder with a `SKILL.md` file in the open [Agent Skills](https://agentskills.io/specification) format, so it works in Claude Code, Claude.ai and other agents that read the format.

Each one asks for the facts it needs, works through numbered steps with decision rules, and checks its output against a list before handing it over. None of them makes up customer quotes, testimonials, statistics or deadlines. When a fact is missing and the agent can't ask (for example, when it runs without anyone to reply), it writes `[CONFIRM: ...]` in the draft instead of guessing.

## The skills

| Skill | What it does |
| --- | --- |
| [buyer-research](skills/buyer-research/SKILL.md) | Turns reviews, support tickets and interviews into a buyer brief: triggers, objections, the customer's own words. |
| [landing-page-copy](skills/landing-page-copy/SKILL.md) | Writes or rewrites a landing or sales page from customer evidence, with a check on every claim. |
| [lead-magnet](skills/lead-magnet/SKILL.md) | Picks the right page, designs a small resource for the reader's next step and writes the signup path. |
| [welcome-emails](skills/welcome-emails/SKILL.md) | Writes the email sequence after someone signs up, with timing, exit rules and pre-send tests. |
| [keyword-map](skills/keyword-map/SKILL.md) | Groups the searches customers make, assigns each group to one page and writes briefs for the gaps. |
| [demo-video](skills/demo-video/SKILL.md) | Plans a product demo or tutorial: script, recording setup, edit notes, packaging and short clips. |
| [product-launch](skills/product-launch/SKILL.md) | Plans a small launch on two or three channels, with owners, dates, drafts and a retrospective. |
| [conversion-diagnosis](skills/conversion-diagnosis/SKILL.md) | Finds where a funnel leaks and why, and sizes any A/B test against the traffic available. |
| [partner-outreach](skills/partner-outreach/SKILL.md) | Finds partners who serve the same customers, qualifies them and drafts short pitches. |
| [paid-ads-test](skills/paid-ads-test/SKILL.md) | Works out whether ads can pay for a product before spending, then designs a small capped test. |
| [on-page-seo](skills/on-page-seo/SKILL.md) | Diagnoses one page from Search Console data and the live results, then fixes it. |
| [ai-search-visibility](skills/ai-search-visibility/SKILL.md) | Audits how AI assistants describe a brand, traces wrong answers to their sources and plans fixes. |
| [local-seo](skills/local-seo/SKILL.md) | Fixes the business profile, listings, location pages and review routine for a local business. |

The skills point to each other where one hands off to another. landing-page-copy works best with a brief from buyer-research, for example. Each one also works on its own.

## Install

### Claude Code

Add this repository as a plugin marketplace, then install the plugin:

```text
/plugin marketplace add jaypozo/marketing-skills
/plugin install marketing-skills@marketing-skills
```

Or copy the skills you want into your skills folder, either for all projects or for one project:

```bash
git clone https://github.com/jaypozo/marketing-skills.git
cp -r marketing-skills/skills/buyer-research ~/.claude/skills/
# or, for one project only
cp -r marketing-skills/skills/buyer-research .claude/skills/
```

Claude picks a skill when your request matches its description. You can also call one directly by name, for example `/buyer-research`.

### Claude.ai

Zip a single skill folder (the folder that contains `SKILL.md`) and upload it in the Skills section of your Claude.ai settings. Skills need to be turned on for your plan.

### Other agents

Any agent that supports the Agent Skills format can use these folders as they are. Many read `~/.agents/skills/` or a project-level skills folder; check your agent's documentation for its path. Copy the skill folders there.

Two skills include a small Python script with no dependencies (`conversion-diagnosis/scripts/sample_size.py` and `paid-ads-test/scripts/ad_math.py`). They need Python 3.8 or later wherever the agent runs commands. Everything else is plain Markdown.

## How the skills are built

[RESEARCH.md](RESEARCH.md) covers the format rules, notes on six other public skill repositories, and the rules every skill here follows. In short:

- `skills/<name>/SKILL.md` holds the procedure and stays under 250 lines. Longer detail lives in `references/`, linked straight from `SKILL.md`.
- Each description says what the skill produces and when to use it, in the words people type.
- The frontmatter uses only fields from the open spec, so nothing is tied to one product.

Study figures quoted in the skills keep their source and are there as context. They aren't targets or promises.

## Contributing

Open an issue or a pull request. A new skill or a change should keep to the rules at the end of RESEARCH.md. Test it once on a realistic task before you submit it, and say in the pull request what the test showed.

## License

MIT. See [LICENSE](LICENSE).
