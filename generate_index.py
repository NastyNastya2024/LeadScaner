#!/usr/bin/env python3
"""Generate index.html with i18n data attributes."""

import html
from pathlib import Path

from generate_tools import TOOLS

ROOT = Path(__file__).parent
OUT = ROOT / "index.html"

# Layer 4 lists Obsei again with a shorter description
OBEI_L4_KEY = "obsei-l4"

LAYER_TOOL_ORDER = {
    1: ["ai-find-customer", "github-lead-signals", "clutch-profile-scraper", "trendscan", "icp-researcher"],
    2: ["coldreach-scraper", "lead-generator", "linkedin-scraper", "the-3rd-eye", "business-researcher"],
    3: [
        "automated-decision-making-discovery",
        "owasp-social-osint-agent",
        "obsei",
        "company-research-agent-tavily",
    ],
    4: ["agent-x-tuitbot", "redsignal", "n8n-workflow", OBEI_L4_KEY],
}

TOOLS_BY_SLUG = {t["slug"]: t for t in TOOLS}


def tool_row(slug: str, tool_id: str) -> str:
    if slug == OBEI_L4_KEY:
        tool = TOOLS_BY_SLUG["obsei"]
        name = html.escape(tool["name"])
        href = "tools/obsei.html"
        desc_key = f"tools.{OBEI_L4_KEY}.desc"
        meta_key = f"tools.{OBEI_L4_KEY}.meta"
    else:
        tool = TOOLS_BY_SLUG[slug]
        name = html.escape(tool["name"])
        href = f"tools/{slug}.html"
        desc_key = f"tools.{slug}.desc"
        meta_key = f"tools.{slug}.meta"

    return f"""        <div class="tool-row">
          <div class="tool-icon">{html.escape(tool_id)}</div>
          <div><div class="tool-name"><a href="{href}">{name}</a></div><div class="tool-meta" data-i18n="{meta_key}"></div></div>
          <div class="tool-desc-col" data-i18n="{desc_key}"></div>
          <a class="btn-soft" href="{href}" data-i18n="ui.details"></a>
        </div>"""


def layer_section(n: int) -> str:
    rows = "\n".join(
        tool_row(slug, TOOLS_BY_SLUG["obsei" if slug == OBEI_L4_KEY else slug]["id"])
        for slug in LAYER_TOOL_ORDER[n]
    )
    arch = ""
    if n == 2:
        arch = """
      <h3 data-i18n="layers.2.archTitle"></h3>
      <div class="diagram">
        <div class="diagram-label">Company URL List</div>
        <div class="diagram-row">
          <div class="diagram-box highlight">ColdReach-Scraper<br><small style="color:var(--text-muted)">Website</small></div>
          <div class="diagram-box highlight">The 3rd Eye<br><small style="color:var(--text-muted)">Social</small></div>
          <div class="diagram-box highlight">lead-generator<br><small style="color:var(--text-muted)">LinkedIn</small></div>
        </div>
        <div class="diagram-arrow">↓</div>
        <div class="diagram-row"><div class="diagram-box highlight">Aggregated Profile — Company DB</div></div>
      </div>"""
    elif n == 3:
        arch = """
      <h3 data-i18n="layers.3.archTitle"></h3>
      <div class="diagram">
        <div class="diagram-label">Data Ingest — Company profiles + Social media + OSINT</div>
        <div class="diagram-arrow">↓</div>
        <div class="diagram-label">Parallel Analysis Pipeline</div>
        <div class="diagram-row">
          <div class="diagram-box">Decision Maker</div>
          <div class="diagram-box">Social OSINT</div>
          <div class="diagram-box">Sentiment</div>
          <div class="diagram-box">Report Gen</div>
          <div class="diagram-box">Pain Points</div>
        </div>
        <div class="diagram-arrow">↓</div>
        <div class="diagram-row"><div class="diagram-box highlight">Unified Output — DMs, pain points, sentiment, PDF</div></div>
      </div>"""
    elif n == 4:
        arch = """
      <h3 data-i18n="layers.4.archTitle"></h3>
      <div class="diagram">
        <div class="diagram-label">Trigger Keywords</div>
        <div class="diagram-arrow">↓</div>
        <div class="diagram-row">
          <div class="diagram-box highlight">Agent-X</div>
          <div class="diagram-box highlight">RedSignal</div>
          <div class="diagram-box highlight">n8n Workflow</div>
        </div>
        <div class="diagram-arrow">↓</div>
        <div class="diagram-row"><div class="diagram-box">AI Filter — Obsei + OWASP</div></div>
        <div class="diagram-arrow">↓</div>
        <div class="diagram-row">
          <div class="diagram-box">Send DM</div>
          <div class="diagram-box">Schedule Reply</div>
          <div class="diagram-box">Create Task</div>
          <div class="diagram-box">Add to CRM</div>
        </div>
      </div>"""

    layer1_badge = ""
    if n == 1:
        layer1_badge = ' <span class="badge-active" data-i18n="ui.active"></span>'

    return f"""    <section id="layer-{n}" class="panel">
      <div class="panel-head">
        <div class="panel-tag" data-i18n="layers.{n}.tag"></div>
        <h2 class="panel-title" data-i18n="layers.{n}.title"></h2>
        <p class="section-desc"><span data-i18n="layers.{n}.desc"></span>{layer1_badge}</p>
      </div>
      <div class="tool-list">
{rows}
      </div>{arch}
    </section>"""


def pipeline_steps() -> str:
    parts = []
    for i in range(4):
        parts.append(
            f"""        <div class="pipeline-step">
          <div class="pipeline-num" data-i18n="pipeline.{i}.num"></div>
          <div class="pipeline-title" data-i18n="pipeline.{i}.title" data-i18n-html="true"></div>
          <div class="pipeline-bar"></div>
        </div>"""
        )
    return "\n".join(parts)


def flow_steps() -> str:
    parts = []
    for i in range(8):
        parts.append(
            f"""        <div class="flow-step"><span class="flow-num">{i + 1}</span><span class="flow-text" data-i18n="flow.steps.{i}"></span></div>"""
        )
    return "\n".join(parts)


def tech_rows() -> str:
    tech_badges = [
        '<span class="badge">CrewAI</span> <span class="badge">LangGraph</span>',
        '<span class="badge">Python (FastAPI)</span>',
        '<span class="badge">Streamlit</span> <span class="badge">Next.js</span>',
        '<span class="badge">PostgreSQL</span> <span class="badge">SQLite</span>',
        '<span class="badge">Celery</span> <span class="badge">Redis</span>',
        '<span class="badge">OpenAI</span> <span class="badge">Anthropic</span> <span class="badge">Gemini</span>',
        '<span class="badge">Tavily</span> <span class="badge">Exa.ai</span> <span class="badge">Google Search</span>',
        '<span class="badge">APScheduler</span> <span class="badge">Celery Beat</span>',
        '<span class="badge">Slack</span> <span class="badge">Telegram</span> <span class="badge">Email</span>',
    ]
    parts = []
    for i, badges in enumerate(tech_badges):
        parts.append(
            f"""            <tr><td data-i18n="tech.rows.{i}.name"></td><td>{badges}</td><td data-i18n="tech.rows.{i}.purpose"></td></tr>"""
        )
    return "\n".join(parts)


def links_grid(slugs: list[str]) -> str:
    return "\n".join(
        f'        <div class="link-item"><a href="tools/{slug}.html">{html.escape(TOOLS_BY_SLUG[slug]["name"])}</a></div>'
        for slug in slugs
    )


def render() -> str:
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>LeadScaper — Platform Architecture</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="site-header">
    <div class="header-inner">
      <div class="header-start">
        <button class="menu-toggle" type="button" aria-label="Menu" aria-expanded="false" aria-controls="site-nav">
          <span></span>
          <span></span>
          <span></span>
        </button>
        <a class="logo" href="#overview">
          <span class="logo-icon">✦</span>
          LeadScaper
        </a>
      </div>
      <div class="header-actions">
        <div class="lang-switch" role="group" aria-label="Language">
          <button class="lang-btn active" type="button" data-lang="ru">RU</button>
          <button class="lang-btn" type="button" data-lang="en">EN</button>
        </div>
      </div>
    </div>
  </header>

  <div class="layout">
    <aside class="sidebar" id="site-nav">
      <div class="sidebar-label" data-i18n="nav.label"></div>
      <ul class="sidebar-nav">
        <li><a href="#overview" class="active" data-i18n="nav.overview"></a></li>
        <li><a href="#layer-1" data-i18n="nav.layer1"></a></li>
        <li><a href="#layer-2" data-i18n="nav.layer2"></a></li>
        <li><a href="#layer-3" data-i18n="nav.layer3"></a></li>
        <li><a href="#layer-4" data-i18n="nav.layer4"></a></li>
        <li><a href="#full-arch" data-i18n="nav.fullArch"></a></li>
        <li><a href="#data-flow" data-i18n="nav.dataFlow"></a></li>
        <li><a href="#tech" data-i18n="nav.tech"></a></li>
        <li><a href="#links" data-i18n="nav.links"></a></li>
      </ul>
    </aside>

    <main class="main">

    <div class="stats-row">
      <div class="hero-card">
        <div>
          <div class="hero-stat-label" data-i18n="hero.label"></div>
          <div class="hero-stat-value" data-i18n="hero.title"></div>
          <p class="hero-stat-sub" data-i18n="hero.desc"></p>
          <a class="btn-dark" href="#layer-1" data-i18n="hero.cta"></a>
        </div>
      </div>
      <div class="stat-pill">
        <div class="stat-pill-value">18</div>
        <div class="stat-pill-label" data-i18n="hero.agents"></div>
      </div>
    </div>

    <section id="overview" class="panel">
      <div class="panel-head">
        <div class="panel-tag" data-i18n="overview.tag"></div>
        <h2 class="panel-title" data-i18n="overview.title"></h2>
        <p class="section-desc" data-i18n="overview.desc"></p>
      </div>
      <div class="pipeline">
{pipeline_steps()}
      </div>
    </section>

{layer_section(1)}

{layer_section(2)}

{layer_section(3)}

{layer_section(4)}

    <section id="full-arch" class="panel">
      <div class="panel-head">
        <div class="panel-tag" data-i18n="arch.tag"></div>
        <h2 class="panel-title" data-i18n="arch.title"></h2>
        <p class="section-desc" data-i18n="arch.desc"></p>
      </div>
      <div class="arch-bar" data-i18n="arch.ui"></div>
      <div class="diagram-arrow">↓</div>
      <div class="arch-bar muted" data-i18n="arch.orch"></div>
      <div class="arch-grid">
        <div class="arch-layer">
          <strong data-i18n="arch.l1"></strong>
          <ul>
            <li><a href="tools/ai-find-customer.html">AI_Find_Customer</a></li>
            <li><a href="tools/github-lead-signals.html">GitHub Lead Signals</a></li>
            <li><a href="tools/clutch-profile-scraper.html">Clutch Scraper</a></li>
            <li><a href="tools/trendscan.html">TrendScan</a></li>
            <li><a href="tools/icp-researcher.html">ICP Researcher</a></li>
          </ul>
        </div>
        <div class="arch-layer">
          <strong data-i18n="arch.l2"></strong>
          <ul>
            <li><a href="tools/coldreach-scraper.html">ColdReach</a></li>
            <li><a href="tools/lead-generator.html">lead-generator</a></li>
            <li><a href="tools/linkedin-scraper.html">LinkedIn Scraper</a></li>
            <li><a href="tools/the-3rd-eye.html">The 3rd Eye</a></li>
            <li><a href="tools/business-researcher.html">Business Researcher</a></li>
          </ul>
        </div>
        <div class="arch-layer">
          <strong data-i18n="arch.l3"></strong>
          <ul>
            <li><a href="tools/automated-decision-making-discovery.html">Decision Maker</a></li>
            <li><a href="tools/owasp-social-osint-agent.html">OWASP OSINT</a></li>
            <li><a href="tools/obsei.html">Obsei</a></li>
            <li><a href="tools/company-research-agent-tavily.html">Tavily Agent</a></li>
          </ul>
        </div>
        <div class="arch-layer">
          <strong data-i18n="arch.l4"></strong>
          <ul>
            <li><a href="tools/agent-x-tuitbot.html">Agent-X</a></li>
            <li><a href="tools/redsignal.html">RedSignal</a></li>
            <li><a href="tools/n8n-workflow.html">n8n</a></li>
            <li><a href="tools/obsei.html">Obsei</a></li>
          </ul>
        </div>
      </div>
      <div class="diagram-arrow">↓</div>
      <div class="arch-bar muted" data-i18n="arch.data"></div>
    </section>

    <section id="data-flow" class="panel">
      <div class="panel-head">
        <div class="panel-tag" data-i18n="flow.tag"></div>
        <h2 class="panel-title" data-i18n="flow.title"></h2>
      </div>
      <div class="flow">
{flow_steps()}
      </div>
    </section>

    <section id="tech" class="panel">
      <div class="panel-head">
        <div class="panel-tag" data-i18n="tech.tag"></div>
        <h2 class="panel-title" data-i18n="tech.title"></h2>
      </div>
      <div class="table-wrap">
        <table>
          <thead><tr><th data-i18n="tech.col1"></th><th data-i18n="tech.col2"></th><th data-i18n="tech.col3"></th></tr></thead>
          <tbody>
{tech_rows()}
          </tbody>
        </table>
      </div>
    </section>

    <section id="links" class="panel">
      <div class="panel-head">
        <div class="panel-tag" data-i18n="links.tag"></div>
        <h2 class="panel-title" data-i18n="links.title"></h2>
      </div>
      <div class="link-cat" data-i18n="links.cat1"></div>
      <div class="links-grid">
{links_grid(LAYER_TOOL_ORDER[1])}
      </div>
      <div class="link-cat" data-i18n="links.cat2"></div>
      <div class="links-grid">
{links_grid(LAYER_TOOL_ORDER[2])}
      </div>
      <div class="link-cat" data-i18n="links.cat3"></div>
      <div class="links-grid">
{links_grid(LAYER_TOOL_ORDER[3])}
      </div>
      <div class="link-cat" data-i18n="links.cat4"></div>
      <div class="links-grid">
{links_grid(LAYER_TOOL_ORDER[4][:3] + ["awesome-n8n-templates"])}
      </div>
    </section>

    <footer data-i18n="ui.footer"></footer>
    </main>
  </div>
  <script src="i18n.js"></script>
  <script src="app.js"></script>
</body>
</html>
"""


def main():
    OUT.write_text(render(), encoding="utf-8")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
