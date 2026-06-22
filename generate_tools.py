#!/usr/bin/env python3
"""Generate individual tool pages from tools data."""

import html
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).parent
TOOLS_DIR = ROOT / "tools"
GITHUB_UA = "LeadScaper-docs-generator"

TOOLS = [
    {
        "slug": "ai-find-customer",
        "name": "AI_Find_Customer",
        "layer": 1,
        "layer_name": "Поиск компаний",
        "id": "1.1",
        "role": "Поиск компаний через AI-агентов по ключевым словам, отрасли, геолокации",
        "sources": "Google, B2B-платформы",
        "platform": None,
        "url": "https://github.com/xiongQvQ/AI_Find_Customer",
        "url_label": "GitHub",
        "github": "xiongQvQ/AI_Find_Customer",
        "description": "AI-powered B2B lead hunting system built with FastAPI, LangGraph, and React for automated company research, keyword generation, web search, lead extraction, and contact discovery.",
        "stars": 107,
        "language": "Python",
    },
    {
        "slug": "github-lead-signals",
        "name": "GitHub Lead Signals",
        "layer": 1,
        "layer_name": "Поиск компаний",
        "id": "1.2",
        "role": "Поиск компаний по технологическому стеку (GitHub активности)",
        "sources": "GitHub API",
        "platform": None,
        "url": "https://apify.com/lizzyyy2/github-lead-signals-ai",
        "url_label": "Apify",
        "github": None,
        "description": "Apify Actor for discovering companies and developers by tech stack using GitHub activity signals and AI analysis. Finds organizations based on repository patterns, languages, and developer engagement.",
        "stars": None,
        "language": "—",
    },
    {
        "slug": "clutch-profile-scraper",
        "name": "Clutch Profile Scraper",
        "layer": 1,
        "layer_name": "Поиск компаний",
        "id": "1.3",
        "role": "Сбор компаний из B2B-каталога",
        "sources": "Clutch.co",
        "platform": None,
        "url": "https://github.com/sajdakabir/clutch-profile-scraper",
        "url_label": "GitHub",
        "github": "sajdakabir/clutch-profile-scraper",
        "description": "A Python tool that extracts company profile URLs from Clutch.co for market research and lead generation. Handles pagination and saves structured data.",
        "stars": 0,
        "language": "Python",
    },
    {
        "slug": "trendscan",
        "name": "TrendScan",
        "layer": 1,
        "layer_name": "Поиск компаний",
        "id": "1.4",
        "role": "Поиск трендовых компаний",
        "sources": "Crunchbase, LinkedIn, Twitter/X",
        "platform": None,
        "url": "https://github.com/brightdata/trendscan",
        "url_label": "GitHub",
        "github": "brightdata/trendscan",
        "description": "TrendScan is a multi-source company intelligence platform for automated collection and AI-powered analysis of company data from Crunchbase, LinkedIn, Reddit, and Twitter/X.",
        "stars": 4,
        "language": "Python",
    },
    {
        "slug": "icp-researcher",
        "name": "ICP Researcher",
        "layer": 1,
        "layer_name": "Поиск компаний",
        "id": "1.5",
        "role": "Определение Ideal Customer Profile и поиск по нему",
        "sources": "Веб-поиск, LinkedIn, Crunchbase",
        "platform": None,
        "url": "https://github.com/thekiln-dev/icp-researcher",
        "url_label": "GitHub",
        "github": "thekiln-dev/icp-researcher",
        "description": "ICP Researcher tool helps you instantly understand your company's ICP inside out.",
        "stars": 0,
        "language": "—",
    },
    {
        "slug": "coldreach-scraper",
        "name": "ColdReach-Scraper",
        "layer": 2,
        "layer_name": "Сбор контактов",
        "id": "2.1",
        "role": "Скрапинг сайта: контакты, миссия, услуги",
        "sources": "Сайт компании",
        "platform": None,
        "url": "https://github.com/sspomeroy-banyanlabs/ColdReach-Scraper",
        "url_label": "GitHub",
        "github": "sspomeroy-banyanlabs/ColdReach-Scraper",
        "description": "Automated company website scraping to identify high-value partnership opportunities and business development prospects.",
        "stars": 0,
        "language": "Python",
    },
    {
        "slug": "lead-generator",
        "name": "lead-generator",
        "layer": 2,
        "layer_name": "Сбор контактов",
        "id": "2.2",
        "role": "Поиск LinkedIn-профилей сотрудников и обогащение email",
        "sources": "LinkedIn, Apollo.io",
        "platform": None,
        "url": "https://github.com/Anudeepreddynarala/lead-generator",
        "url_label": "GitHub",
        "github": "Anudeepreddynarala/lead-generator",
        "description": "Lead scraper with LinkedIn people search, Apollo.io email enrichment, blacklist support, and CSV export.",
        "stars": 1,
        "language": "Python",
    },
    {
        "slug": "linkedin-scraper",
        "name": "linkedIn_scraper",
        "layer": 2,
        "layer_name": "Сбор контактов",
        "id": "2.3",
        "role": "Сбор профилей ЛПР с AI-генерацией «болевых точек»",
        "sources": "LinkedIn",
        "platform": None,
        "url": "https://github.com/haytham10/linkedIn_scraper",
        "url_label": "GitHub",
        "github": "haytham10/linkedIn_scraper",
        "description": "A comprehensive solution for automated LinkedIn lead generation and AI-powered lead analysis. Scrapes LinkedIn profiles, extracts key information, and uses Google's Gemini AI to generate personalized outreach insights.",
        "stars": 3,
        "language": "Python",
    },
    {
        "slug": "the-3rd-eye",
        "name": "The 3rd Eye",
        "layer": 2,
        "layer_name": "Сбор контактов",
        "id": "2.4",
        "role": "Сбор цифрового следа из всех соцсетей",
        "sources": "Twitter, LinkedIn, Instagram, Facebook, Telegram",
        "platform": None,
        "url": "https://github.com/Ordinary0x/The-3rd-Eye",
        "url_label": "GitHub",
        "github": "Ordinary0x/The-3rd-Eye",
        "description": "Modular OSINT framework on an agent-based, graph-driven architecture. Automates public information discovery, identity correlation, and exposure analysis across multiple platforms with LangGraph.",
        "stars": 11,
        "language": "Python",
    },
    {
        "slug": "business-researcher",
        "name": "Business Researcher",
        "layer": 2,
        "layer_name": "Сбор контактов",
        "id": "2.5",
        "role": "Глубокое исследование: финансы, структура, рынок",
        "sources": "Tavily API, веб-поиск",
        "platform": None,
        "url": "https://github.com/bgunyel/business-researcher",
        "url_label": "GitHub",
        "github": "bgunyel/business-researcher",
        "description": "AI module to research people and companies.",
        "stars": 2,
        "language": "Python",
    },
    {
        "slug": "automated-decision-making-discovery",
        "name": "Automated-Decision-Making-Discovery",
        "layer": 3,
        "layer_name": "Анализ данных",
        "id": "3.1",
        "role": "Выявление ЛПР (CEO, CTO, Head of X) с валидацией контактов",
        "sources": "Веб-поиск, LinkedIn, AI",
        "platform": None,
        "url": "https://github.com/chibbss/Automated-Decision-Making-Discovery",
        "url_label": "GitHub",
        "github": "chibbss/Automated-Decision-Making-Discovery",
        "description": "Automated CrewAI workflow that researches companies, discovers decision makers (CEO, CTO), validates contacts, and generates outbound messaging strategies.",
        "stars": 0,
        "language": "Python",
    },
    {
        "slug": "owasp-social-osint-agent",
        "name": "OWASP SocialOSINTAgent",
        "layer": 3,
        "layer_name": "Анализ данных",
        "id": "3.2",
        "role": "Анализ текста и изображений из соцсетей, создание отчётов",
        "sources": "X, Reddit, GitHub, YouTube",
        "platform": None,
        "url": "https://github.com/bm-github/owasp-social-osint-agent",
        "url_label": "GitHub",
        "github": "bm-github/owasp-social-osint-agent",
        "description": "AI-powered OSINT framework for multi-platform social media intelligence gathering using OpenAI-compatible APIs. Features vision analysis, network mapping, and dual web/CLI interfaces.",
        "stars": 82,
        "language": "Python",
    },
    {
        "slug": "obsei",
        "name": "Obsei",
        "layer": 3,
        "layer_name": "Анализ данных",
        "id": "3.3 / 4.4",
        "role": "Анализ тональности и классификация сообщений; мониторинг упоминаний",
        "sources": "X, Reddit, Facebook, отзывы",
        "platform": "X, Reddit, Facebook",
        "url": "https://github.com/obsei/obsei",
        "url_label": "GitHub",
        "github": "obsei/obsei",
        "description": "Obsei is a low code AI powered automation tool. It can be used in various business flows like social listening, AI based alerting, brand image analysis, comparative study and more.",
        "stars": 1412,
        "language": "Python",
    },
    {
        "slug": "company-research-agent-tavily",
        "name": "Company Research Agent (Tavily)",
        "layer": 3,
        "layer_name": "Анализ данных",
        "id": "3.4",
        "role": "Глубокий анализ и генерация отчётов в PDF/Markdown",
        "sources": "Tavily API, Anthropic API",
        "platform": None,
        "url": "https://github.com/BunsDev/company-research-agent-tavily",
        "url_label": "GitHub",
        "github": "BunsDev/company-research-agent-tavily",
        "description": "An agentic company research tool powered by LangGraph and Tavily that conducts deep diligence on companies using a multi-agent framework with Gemini and GPT-4.",
        "stars": 1,
        "language": "—",
    },
    {
        "slug": "agent-x-tuitbot",
        "name": "Agent-X (TuitBot)",
        "layer": 4,
        "layer_name": "Вовлечение в соцсетях",
        "id": "4.1",
        "role": "Мониторинг ключевых слов, AI-ответы на посты с одобрением",
        "sources": "X (Twitter)",
        "platform": "X (Twitter)",
        "url": "https://github.com/aramirez087/TuitBot",
        "url_label": "GitHub",
        "github": "aramirez087/TuitBot",
        "description": "A cross-platform Rust CLI autonomous growth agent for X (Twitter) designed to help founders, indie hackers, and businesses grow their accounts organically. Discovers conversations by keywords, drafts replies, and queues them for approval.",
        "stars": 3,
        "language": "Rust",
    },
    {
        "slug": "redsignal",
        "name": "RedSignal",
        "layer": 4,
        "layer_name": "Вовлечение в соцсетях",
        "id": "4.2",
        "role": "Поиск «тёплых» лидов, AI-фильтрация релевантности",
        "sources": "Reddit",
        "platform": "Reddit",
        "url": "https://github.com/ivucicev/redsignal",
        "url_label": "GitHub",
        "github": "ivucicev/redsignal",
        "description": "Reddit monitoring and lead generation tool. Watches subreddits for keyword matches, filters noise with AI, and helps you draft replies and track leads.",
        "stars": 19,
        "language": "JavaScript",
    },
    {
        "slug": "n8n-workflow",
        "name": "n8n workflow",
        "layer": 4,
        "layer_name": "Вовлечение в соцсетях",
        "id": "4.3",
        "role": "Мультиплатформенный мониторинг и уведомления",
        "sources": "Reddit, LinkedIn, X, Instagram",
        "platform": "Reddit, LinkedIn, X, Instagram",
        "url": "https://n8n.io/workflows/10251-cross-platform-brand-monitoring-and-analysis-with-anysite-api-and-gpt/",
        "url_label": "n8n",
        "github": None,
        "description": "Cross-platform brand monitoring workflow for Reddit, LinkedIn, X, and Instagram. Collects posts by keywords, analyzes engagement and sentiment with GPT, and sends automated email reports.",
        "stars": None,
        "language": "—",
    },
    {
        "slug": "awesome-n8n-templates",
        "name": "awesome-n8n-templates",
        "layer": 4,
        "layer_name": "Вовлечение в соцсетях",
        "id": "—",
        "role": "Коллекция готовых шаблонов автоматизации для соцсетей и мониторинга",
        "sources": "Reddit, LinkedIn, X, Instagram",
        "platform": None,
        "url": "https://github.com/enescingoz/awesome-n8n-templates",
        "url_label": "GitHub",
        "github": "enescingoz/awesome-n8n-templates",
        "description": "280+ free n8n automation templates — ready-to-use workflows for Gmail, Telegram, Slack, Discord, social media, AI agents, and more. The largest open-source n8n template collection.",
        "stars": 23188,
        "language": "—",
    },
]

LAYER_COLORS = {1: "var(--layer-1)", 2: "var(--layer-2)", 3: "var(--layer-3)", 4: "var(--layer-4)"}


def fetch_github_meta(repo: str) -> dict:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={"Accept": "application/vnd.github+json", "User-Agent": GITHUB_UA},
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.load(resp)
    return {
        "description": data.get("description") or "",
        "stars": data.get("stargazers_count"),
        "language": data.get("language") or "—",
    }


def fetch_github_readme_html(repo: str) -> str:
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/readme",
        headers={"Accept": "application/vnd.github.html", "User-Agent": GITHUB_UA},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw = resp.read().decode("utf-8")
    # Keep article body only; drop github anchor icons
    raw = re.sub(r"<svg[^>]*>.*?</svg>", "", raw, flags=re.S)
    match = re.search(r"<article[^>]*>(.*)</article>", raw, flags=re.S)
    if match:
        return match.group(1).strip()
    return raw.strip()


def read_existing_readme(slug: str) -> str | None:
    path = TOOLS_DIR / f"{slug}.html"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(r'<div class="readme-content">\s*(.*?)\s*</div>\s*\n\s*</section>', text, re.S)
    return match.group(1).strip() if match else None


def enrich_tool(tool: dict, local_only: bool = False) -> dict:
    enriched = dict(tool)
    if local_only:
        existing = read_existing_readme(tool["slug"])
        if existing:
            enriched["readme_html"] = existing
            enriched.setdefault("short_description", tool.get("description", ""))
            return enriched
    if tool.get("github"):
        try:
            meta = fetch_github_meta(tool["github"])
            enriched["stars"] = meta["stars"]
            enriched["language"] = meta["language"]
            if meta["description"]:
                enriched["short_description"] = meta["description"]
            readme = fetch_github_readme_html(tool["github"])
            enriched["readme_html"] = readme
            print(f"  ✓ README {tool['github']} ({len(readme)} chars)")
        except Exception as exc:
            print(f"  ✗ {tool['github']}: {exc}")
            enriched["readme_html"] = f"<p>{html.escape(tool['description'])}</p>"
    else:
        enriched["readme_html"] = f"<p>{html.escape(tool['description'])}</p>"
    enriched.setdefault("short_description", tool.get("description", ""))
    return enriched


def render_tool(tool: dict) -> str:
    name = html.escape(tool["name"])
    slug = html.escape(tool["slug"])
    url = html.escape(tool["url"])
    url_label = html.escape(tool["url_label"])
    layer = tool["layer"]
    tid = html.escape(tool["id"])
    sources = html.escape(tool["sources"])
    readme_html = tool.get("readme_html", f"<p>{html.escape(tool['description'])}</p>")
    source_tag = html.escape(tool.get("github") and "GitHub" or tool["url_label"])

    stats = []
    if tool.get("github"):
        stats.append(f'<div class="tool-stat"><span class="tool-stat-label" data-i18n="ui.repo"></span><span class="tool-stat-value">{html.escape(tool["github"])}</span></div>')
    if tool.get("stars") is not None:
        stats.append(f'<div class="tool-stat"><span class="tool-stat-label" data-i18n="ui.stars"></span><span class="tool-stat-value">{tool["stars"]:,}</span></div>')
    if tool.get("language"):
        stats.append(f'<div class="tool-stat"><span class="tool-stat-label" data-i18n="ui.language"></span><span class="tool-stat-value">{html.escape(tool["language"])}</span></div>')
    stats.append(f'<div class="tool-stat"><span class="tool-stat-label" data-i18n="ui.dataSource"></span><span class="tool-stat-value">{sources}</span></div>')
    if tool.get("platform"):
        stats.append(f'<div class="tool-stat"><span class="tool-stat-label" data-i18n="ui.platform"></span><span class="tool-stat-value">{html.escape(tool["platform"])}</span></div>')

    stats_html = "\n          ".join(stats)

    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} — LeadScaper</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
</head>
<body class="tool-page" data-tool-slug="{slug}">
  <header class="site-header">
    <div class="header-inner">
      <a class="logo" href="../index.html">
        <span class="logo-icon">✦</span>
        LeadScaper
      </a>
      <div class="header-actions">
        <div class="lang-switch" role="group" aria-label="Language">
          <button class="lang-btn active" type="button" data-lang="ru">RU</button>
          <button class="lang-btn" type="button" data-lang="en">EN</button>
        </div>
      </div>
    </div>
  </header>

  <div class="layout tool-page">
    <main class="main">
      <a class="back-link" href="../index.html" data-i18n="ui.back"></a>

      <div class="hero-card hero-card-accent tool-hero">
        <div class="tool-icon">{html.escape(tid.split("/")[0].strip())}</div>
        <div class="tool-hero-body">
          <div class="hero-stat-label" data-i18n-tool-layer data-layer="{layer}"></div>
          <h1 class="hero-stat-value tool-hero-title">{name}</h1>
          <p class="hero-stat-sub" data-i18n-tool-role></p>
          <a class="btn-external" href="{url}" target="_blank" rel="noopener" data-i18n-open data-source="{url_label}">
            Open on {url_label} →
          </a>
        </div>
      </div>

      <section class="panel">
        <div class="panel-head">
          <div class="panel-tag">{source_tag}</div>
          <h2 class="panel-title" data-i18n="ui.description"></h2>
        </div>

        <div class="tool-stats">
          {stats_html}
        </div>

        <div class="readme-content">
          {readme_html}
        </div>
      </section>

      <footer data-i18n="ui.footer"></footer>
    </main>
  </div>
  <script src="../i18n.js"></script>
</body>
</html>
"""


def main():
    local_only = "--local" in sys.argv
    TOOLS_DIR.mkdir(exist_ok=True)
    for tool in TOOLS:
        print(f"{'Rendering' if local_only else 'Fetching'} {tool['slug']}...")
        enriched = enrich_tool(tool, local_only=local_only)
        path = TOOLS_DIR / f"{tool['slug']}.html"
        path.write_text(render_tool(enriched), encoding="utf-8")
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
