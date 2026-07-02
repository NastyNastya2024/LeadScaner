#!/usr/bin/env python3
"""Generate locales/ru.json and locales/en.json for the LeadScaper static site."""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent
LOCALES_DIR = ROOT / "locales"

sys.path.insert(0, str(ROOT))
from generate_tools import TOOLS  # noqa: E402

TOOL_SLUGS = [
    "ai-find-customer",
    "github-lead-signals",
    "clutch-profile-scraper",
    "trendscan",
    "icp-researcher",
    "coldreach-scraper",
    "lead-generator",
    "linkedin-scraper",
    "the-3rd-eye",
    "business-researcher",
    "automated-decision-making-discovery",
    "owasp-social-osint-agent",
    "obsei",
    "company-research-agent-tavily",
    "agent-x-tuitbot",
    "redsignal",
    "n8n-workflow",
    "awesome-n8n-templates",
]

RU = {
    "meta": {"title": "LeadScaper — Архитектура платформы"},
    "ui": {
        "settings": "Настройки",
        "back": "← Назад к архитектуре",
        "description": "Описание",
        "openOn": "Открыть на {source} →",
        "details": "Подробнее",
        "repo": "Репозиторий",
        "stars": "Stars",
        "language": "Язык",
        "dataSource": "Источник данных",
        "platform": "Платформа",
        "active": "Active",
        "footer": "LeadScaper Platform — Architecture Documentation",
        "layerLabel": "Слой {n} · {name}",
    },
    "nav": {
        "label": "Навигация",
        "overview": "Обзор",
        "layer1": "Слой 1 — Поиск",
        "layer2": "Слой 2 — Сбор",
        "layer3": "Слой 3 — Анализ",
        "layer4": "Слой 4 — Вовлечение",
        "fullArch": "Архитектура",
        "dataFlow": "Data Flow",
        "tech": "Техстек",
        "links": "Все инструменты",
        "financialModel": "Финансовая модель",
        "chatgtm": "ChatGTM / AI-GTM",
    },
    "model": {
        "metaTitle": "LeadScaper — Финансовая модель",
        "tag": "Financial Model",
        "title": "Финансовая модель",
        "subtitle": "Конфигурации системы, unit economics, ICP, конкуренты и RU-источники данных. Все расчёты в ₽.",
        "tocLabel": "Содержание",
        "loading": "Загрузка модели…",
        "downloadMd": "Скачать .md",
        "backArch": "Архитектура",
    },
    "chatgtm": {
        "metaTitle": "LeadScaper — ChatGTM / AI-GTM анализ",
        "tag": "ChatGTM Reference",
        "title": "ChatGTM × LeadScaper",
        "subtitle": "Разбор AI-GTM workflow Cursor, конкуренты, боли ICP, инструментарий РФ и финансовый прогноз.",
        "tocLabel": "Содержание",
        "loading": "Загрузка анализа…",
        "downloadMd": "Скачать .md",
        "backArch": "Архитектура",
        "backModel": "Финмодель",
    },
    "hero": {
        "label": "LeadScaper Platform",
        "title": "4 слоя",
        "desc": "Многослойная AI-платформа для автоматического поиска B2B-клиентов, сбора данных о компаниях и ЛПР, мониторинга соцсетей и генерации персонализированных предложений.",
        "cta": "→ Исследовать архитектуру",
        "agents": "Agents",
    },
    "overview": {
        "tag": "Overview",
        "title": "Общая концепция",
        "desc": "Четыре последовательных слоя обработки данных — от поиска компаний до вовлечения в соцсетях.",
    },
    "pipeline": [
        {"num": "Слой 1", "title": "Поиск<br>Компаний"},
        {"num": "Слой 2", "title": "Сбор<br>Контактов"},
        {"num": "Слой 3", "title": "Анализ<br>Данных"},
        {"num": "Слой 4", "title": "Действие<br>Вовлечение"},
    ],
    "layers": {
        "1": {
            "tag": "Слой 1 · Discovery",
            "title": "Поиск компаний",
            "desc": "Найти все возможные компании-клиенты по заданным критериям.",
            "archTitle": "",
        },
        "2": {
            "tag": "Слой 2 · Enrichment",
            "title": "Сбор контактов и соцсетей",
            "desc": "Для каждой найденной компании собрать контакты, соцсети и публичные данные.",
            "archTitle": "Архитектура слоя 2",
        },
        "3": {
            "tag": "Слой 3 · Analysis",
            "title": "Анализ и генерация инсайтов",
            "desc": "Анализ данных для поиска триггерных слов, ЛПР и генерации персонализированных сообщений.",
            "archTitle": "Архитектура слоя 3",
        },
        "4": {
            "tag": "Слой 4 · Engagement",
            "title": "Вовлечение в соцсетях",
            "desc": "Автоматический мониторинг и вовлечение аудитории по триггерным словам.",
            "archTitle": "Архитектура слоя 4",
        },
    },
    "tools": {
        "ai-find-customer": {
            "desc": "Поиск компаний через AI-агентов по ключевым словам, отрасли, геолокации",
            "meta": "Google, B2B-платформы",
        },
        "github-lead-signals": {
            "desc": "Поиск компаний по технологическому стеку (GitHub активности)",
            "meta": "GitHub API",
        },
        "clutch-profile-scraper": {
            "desc": "Сбор компаний из B2B-каталога",
            "meta": "Clutch.co",
        },
        "trendscan": {
            "desc": "Поиск трендовых компаний",
            "meta": "Crunchbase, LinkedIn, X",
        },
        "icp-researcher": {
            "desc": "Определение Ideal Customer Profile и поиск по нему",
            "meta": "Веб-поиск, LinkedIn",
        },
        "coldreach-scraper": {
            "desc": "Скрапинг сайта: контакты, миссия, услуги",
            "meta": "Сайт компании",
        },
        "lead-generator": {
            "desc": "Поиск LinkedIn-профилей сотрудников и обогащение email",
            "meta": "LinkedIn, Apollo.io",
        },
        "linkedin-scraper": {
            "desc": "Сбор профилей ЛПР с AI-генерацией «болевых точек»",
            "meta": "LinkedIn",
        },
        "the-3rd-eye": {
            "desc": "Сбор цифрового следа из всех соцсетей",
            "meta": "Соцсети",
        },
        "business-researcher": {
            "desc": "Глубокое исследование: финансы, структура, рынок",
            "meta": "Tavily API",
        },
        "automated-decision-making-discovery": {
            "desc": "Выявление ЛПР (CEO, CTO, Head of X) с валидацией контактов",
            "meta": "LinkedIn, AI",
        },
        "owasp-social-osint-agent": {
            "desc": "Анализ текста и изображений из соцсетей, создание отчётов",
            "meta": "X, Reddit, GitHub",
        },
        "obsei": {
            "desc": "Анализ тональности и классификация сообщений",
            "meta": "X, Reddit, Facebook",
        },
        "obsei-l4": {
            "desc": "Анализ тональности упоминаний",
            "meta": "X, Reddit, Facebook",
        },
        "company-research-agent-tavily": {
            "desc": "Глубокий анализ и генерация отчётов в PDF/Markdown",
            "meta": "Tavily, Anthropic",
        },
        "agent-x-tuitbot": {
            "desc": "Мониторинг ключевых слов, AI-ответы на посты с одобрением",
            "meta": "X (Twitter)",
        },
        "redsignal": {
            "desc": "Поиск «тёплых» лидов, AI-фильтрация релевантности",
            "meta": "Reddit",
        },
        "n8n-workflow": {
            "desc": "Мультиплатформенный мониторинг и уведомления",
            "meta": "Multi-platform",
        },
        "awesome-n8n-templates": {
            "desc": "Коллекция готовых шаблонов автоматизации для соцсетей и мониторинга",
            "meta": "Reddit, LinkedIn, X, Instagram",
        },
    },
    "arch": {
        "tag": "Architecture",
        "title": "Полная архитектурная схема",
        "desc": "Взаимодействие слоёв, оркестрации и хранилища данных.",
        "ui": "User Interface — Dashboard / Reports / Notifications",
        "orch": "Orchestration Layer — CrewAI / LangGraph / n8n",
        "data": "Data Lake & CRM — PostgreSQL / SQLite + HubSpot / Salesforce",
        "l1": "Слой 1 — Поиск",
        "l2": "Слой 2 — Сбор",
        "l3": "Слой 3 — Анализ",
        "l4": "Слой 4 — Вовлечение",
    },
    "flow": {
        "tag": "Data Flow",
        "title": "Процесс обработки данных",
        "steps": [
            "Поиск компаний (Слой 1)",
            "Обогащение данными (Слой 2)",
            "Анализ и генерация инсайтов (Слой 3)",
            "Запись в CRM (PostgreSQL / Salesforce)",
            "Мониторинг соцсетей по триггерным словам (Слой 4)",
            "AI-фильтрация и классификация (Obsei + OWASP)",
            "Генерация персонализированных сообщений (Agent-X / RedSignal)",
            "Вовлечение и отправка в CRM",
        ],
    },
    "tech": {
        "tag": "Tech Stack",
        "title": "Технические рекомендации",
        "col1": "Компонент",
        "col2": "Технология",
        "col3": "Назначение",
        "rows": [
            {"name": "Orchestration", "purpose": "Управление агентами и потоками данных"},
            {"name": "Backend API", "purpose": "REST API для взаимодействия с клиентами"},
            {"name": "Frontend", "purpose": "Дашборд для просмотра результатов"},
            {"name": "Database", "purpose": "Хранение компаний, контактов, отчётов"},
            {"name": "Queue", "purpose": "Асинхронная обработка задач"},
            {"name": "AI/LLM", "purpose": "Анализ, генерация сообщений"},
            {"name": "Search APIs", "purpose": "Поиск данных о компаниях"},
            {"name": "Cron/Scheduler", "purpose": "Регулярный запуск мониторинга"},
            {"name": "Notifications", "purpose": "Уведомления о новых лидах"},
        ],
    },
    "links": {
        "tag": "All Tools",
        "title": "Все инструменты",
        "cat1": "Слой 1 — Поиск компаний",
        "cat2": "Слой 2 — Сбор контактов",
        "cat3": "Слой 3 — Анализ данных",
        "cat4": "Слой 4 — Вовлечение",
    },
}

EN = {
    "meta": {"title": "LeadScaper — Platform Architecture"},
    "ui": {
        "settings": "Settings",
        "back": "← Back to architecture",
        "description": "Description",
        "openOn": "Open on {source} →",
        "details": "Details",
        "repo": "Repository",
        "stars": "Stars",
        "language": "Language",
        "dataSource": "Data source",
        "platform": "Platform",
        "active": "Active",
        "footer": "LeadScaper Platform — Architecture Documentation",
        "layerLabel": "Layer {n} · {name}",
    },
    "nav": {
        "label": "Navigation",
        "overview": "Overview",
        "layer1": "Layer 1 — Discovery",
        "layer2": "Layer 2 — Enrichment",
        "layer3": "Layer 3 — Analysis",
        "layer4": "Layer 4 — Engagement",
        "fullArch": "Architecture",
        "dataFlow": "Data Flow",
        "tech": "Tech Stack",
        "links": "All Tools",
        "financialModel": "Financial Model",
        "chatgtm": "ChatGTM / AI-GTM",
    },
    "model": {
        "metaTitle": "LeadScaper — Financial Model",
        "tag": "Financial Model",
        "title": "Financial Model",
        "subtitle": "System configurations, unit economics, ICP, competitors, and RU data sources. All figures in ₽.",
        "tocLabel": "Contents",
        "loading": "Loading model…",
        "downloadMd": "Download .md",
        "backArch": "Architecture",
    },
    "chatgtm": {
        "metaTitle": "LeadScaper — ChatGTM / AI-GTM Analysis",
        "tag": "ChatGTM Reference",
        "title": "ChatGTM × LeadScaper",
        "subtitle": "Cursor AI-GTM workflow breakdown, competitors, ICP pains, RU tooling, and financial forecast.",
        "tocLabel": "Contents",
        "loading": "Loading analysis…",
        "downloadMd": "Download .md",
        "backArch": "Architecture",
        "backModel": "Financial model",
    },
    "hero": {
        "label": "LeadScaper Platform",
        "title": "4 Layers",
        "desc": "A multi-layer AI platform for automated B2B lead discovery, company and decision-maker enrichment, social monitoring, and personalized outreach generation.",
        "cta": "→ Explore architecture",
        "agents": "Agents",
    },
    "overview": {
        "tag": "Overview",
        "title": "Core Concept",
        "desc": "Four sequential data-processing layers — from company discovery to social engagement.",
    },
    "pipeline": [
        {"num": "Layer 1", "title": "Company<br>Discovery"},
        {"num": "Layer 2", "title": "Contact<br>Enrichment"},
        {"num": "Layer 3", "title": "Data<br>Analysis"},
        {"num": "Layer 4", "title": "Engagement<br>Actions"},
    ],
    "layers": {
        "1": {
            "tag": "Layer 1 · Discovery",
            "title": "Company Discovery",
            "desc": "Find all potential target companies that match your criteria.",
            "archTitle": "",
        },
        "2": {
            "tag": "Layer 2 · Enrichment",
            "title": "Contact & Social Enrichment",
            "desc": "For each discovered company, collect contacts, social profiles, and public data.",
            "archTitle": "Layer 2 Architecture",
        },
        "3": {
            "tag": "Layer 3 · Analysis",
            "title": "Analysis & Insight Generation",
            "desc": "Analyze data to surface trigger keywords, decision makers, and personalized messaging.",
            "archTitle": "Layer 3 Architecture",
        },
        "4": {
            "tag": "Layer 4 · Engagement",
            "title": "Social Engagement",
            "desc": "Automated monitoring and audience engagement driven by trigger keywords.",
            "archTitle": "Layer 4 Architecture",
        },
    },
    "tools": {
        "ai-find-customer": {
            "desc": "Discover companies via AI agents using keywords, industry, and geolocation",
            "meta": "Google, B2B platforms",
        },
        "github-lead-signals": {
            "desc": "Find companies by technology stack (GitHub activity signals)",
            "meta": "GitHub API",
        },
        "clutch-profile-scraper": {
            "desc": "Collect companies from a B2B directory",
            "meta": "Clutch.co",
        },
        "trendscan": {
            "desc": "Discover trending companies",
            "meta": "Crunchbase, LinkedIn, X",
        },
        "icp-researcher": {
            "desc": "Define Ideal Customer Profile and search against it",
            "meta": "Web search, LinkedIn",
        },
        "coldreach-scraper": {
            "desc": "Scrape company websites: contacts, mission, services",
            "meta": "Company website",
        },
        "lead-generator": {
            "desc": "Find employee LinkedIn profiles and enrich emails",
            "meta": "LinkedIn, Apollo.io",
        },
        "linkedin-scraper": {
            "desc": "Collect decision-maker profiles with AI-generated pain points",
            "meta": "LinkedIn",
        },
        "the-3rd-eye": {
            "desc": "Aggregate digital footprint across social networks",
            "meta": "Social networks",
        },
        "business-researcher": {
            "desc": "Deep research: finances, structure, market",
            "meta": "Tavily API",
        },
        "automated-decision-making-discovery": {
            "desc": "Identify decision makers (CEO, CTO, Head of X) with contact validation",
            "meta": "LinkedIn, AI",
        },
        "owasp-social-osint-agent": {
            "desc": "Analyze text and images from social media; generate reports",
            "meta": "X, Reddit, GitHub",
        },
        "obsei": {
            "desc": "Sentiment analysis and message classification",
            "meta": "X, Reddit, Facebook",
        },
        "obsei-l4": {
            "desc": "Sentiment analysis for brand mentions",
            "meta": "X, Reddit, Facebook",
        },
        "company-research-agent-tavily": {
            "desc": "Deep analysis and PDF/Markdown report generation",
            "meta": "Tavily, Anthropic",
        },
        "agent-x-tuitbot": {
            "desc": "Keyword monitoring with AI-generated replies pending approval",
            "meta": "X (Twitter)",
        },
        "redsignal": {
            "desc": "Find warm leads with AI relevance filtering",
            "meta": "Reddit",
        },
        "n8n-workflow": {
            "desc": "Cross-platform monitoring and notifications",
            "meta": "Multi-platform",
        },
        "awesome-n8n-templates": {
            "desc": "Curated automation templates for social media and monitoring",
            "meta": "Reddit, LinkedIn, X, Instagram",
        },
    },
    "arch": {
        "tag": "Architecture",
        "title": "Full Architecture Diagram",
        "desc": "How layers, orchestration, and data storage interact.",
        "ui": "User Interface — Dashboard / Reports / Notifications",
        "orch": "Orchestration Layer — CrewAI / LangGraph / n8n",
        "data": "Data Lake & CRM — PostgreSQL / SQLite + HubSpot / Salesforce",
        "l1": "Layer 1 — Discovery",
        "l2": "Layer 2 — Enrichment",
        "l3": "Layer 3 — Analysis",
        "l4": "Layer 4 — Engagement",
    },
    "flow": {
        "tag": "Data Flow",
        "title": "Data Processing Pipeline",
        "steps": [
            "Company discovery (Layer 1)",
            "Data enrichment (Layer 2)",
            "Analysis and insight generation (Layer 3)",
            "CRM write-back (PostgreSQL / Salesforce)",
            "Social monitoring by trigger keywords (Layer 4)",
            "AI filtering and classification (Obsei + OWASP)",
            "Personalized message generation (Agent-X / RedSignal)",
            "Engagement and CRM sync",
        ],
    },
    "tech": {
        "tag": "Tech Stack",
        "title": "Technical Recommendations",
        "col1": "Component",
        "col2": "Technology",
        "col3": "Purpose",
        "rows": [
            {"name": "Orchestration", "purpose": "Agent and data-flow orchestration"},
            {"name": "Backend API", "purpose": "REST API for client integrations"},
            {"name": "Frontend", "purpose": "Dashboard for reviewing results"},
            {"name": "Database", "purpose": "Store companies, contacts, and reports"},
            {"name": "Queue", "purpose": "Asynchronous task processing"},
            {"name": "AI/LLM", "purpose": "Analysis and message generation"},
            {"name": "Search APIs", "purpose": "Company data discovery"},
            {"name": "Cron/Scheduler", "purpose": "Scheduled monitoring runs"},
            {"name": "Notifications", "purpose": "Alerts for new leads"},
        ],
    },
    "links": {
        "tag": "All Tools",
        "title": "All Tools",
        "cat1": "Layer 1 — Company Discovery",
        "cat2": "Layer 2 — Contact Enrichment",
        "cat3": "Layer 3 — Data Analysis",
        "cat4": "Layer 4 — Engagement",
    },
}

LAYER_NAMES_EN = {
    1: "Company Discovery",
    2: "Contact Enrichment",
    3: "Data Analysis",
    4: "Social Engagement",
}

TOOL_ROLES_EN = {
    "ai-find-customer": "Discover companies via AI agents using keywords, industry, and geolocation",
    "github-lead-signals": "Find companies by technology stack (GitHub activity signals)",
    "clutch-profile-scraper": "Collect companies from a B2B directory",
    "trendscan": "Discover trending companies",
    "icp-researcher": "Define Ideal Customer Profile and search against it",
    "coldreach-scraper": "Scrape company websites: contacts, mission, services",
    "lead-generator": "Find employee LinkedIn profiles and enrich emails",
    "linkedin-scraper": "Collect decision-maker profiles with AI-generated pain points",
    "the-3rd-eye": "Aggregate digital footprint across social networks",
    "business-researcher": "Deep research: finances, structure, market",
    "automated-decision-making-discovery": "Identify decision makers (CEO, CTO, Head of X) with contact validation",
    "owasp-social-osint-agent": "Analyze text and images from social media; generate reports",
    "obsei": "Sentiment analysis, message classification, and mention monitoring",
    "company-research-agent-tavily": "Deep analysis and PDF/Markdown report generation",
    "agent-x-tuitbot": "Keyword monitoring with AI-generated replies pending approval",
    "redsignal": "Find warm leads with AI relevance filtering",
    "n8n-workflow": "Cross-platform monitoring and notifications",
    "awesome-n8n-templates": "Curated automation templates for social media and monitoring",
}

TOOL_ABOUT_RU = {
    "github-lead-signals": (
        "<p><strong>GitHub Lead Signals</strong> — Apify Actor для поиска B2B-клиентов по технологическим "
        "сигналам из GitHub. Инструмент анализирует публичную активность разработчиков и организаций: "
        "репозитории, стек языков, паттерны коммитов и вовлечённость — и с помощью AI выявляет компании, "
        "которые уже используют или внедряют нужные технологии.</p>"
        "<p>Это эффективный способ находить продуктовые команды, SaaS-стартапы и dev-tools компании "
        "для outbound-продаж, интеграций и партнёрств — без ручного просмотра GitHub.</p>"
        "<h2>Что делает</h2>"
        "<ul>"
        "<li>Ищет организации и разработчиков по технологическому стеку</li>"
        "<li>Анализирует паттерны репозиториев и языки программирования</li>"
        "<li>Оценивает активность и вовлечённость через AI</li>"
        "<li>Формирует списки компаний для обогащения в пайплайне LeadScaper</li>"
        "</ul>"
        "<h2>Источник данных</h2>"
        "<p>GitHub API через платформу Apify — готовый облачный Actor без собственной инфраструктуры.</p>"
    ),
    "ai-find-customer": (
        "<p><strong>AI_Find_Customer</strong> (AI Hunter) — открытая система автоматизированного поиска "
        "B2B-клиентов для внешней торговли и B2B-продаж на базе FastAPI, LangGraph, мультиагентного "
        "пайплайна и поддержки нескольких LLM.</p>"
        "<p>Укажите сайт компании, загрузите документы о продукте или введите ключевые слова и целевой "
        "рынок — система самостоятельно проанализирует компанию, сгенерирует поисковые запросы, "
        "выполнит веб-поиск, извлечёт лиды и найдёт контактные данные.</p>"
        "<h2>Ключевые возможности</h2>"
        "<ul>"
        "<li>Мультиагентный пайплайн: Insight → KeywordGen → Search → LeadExtract → Evaluate</li>"
        "<li>Два типа моделей: reasoning-модель для ReAct-решений, стандартная — для извлечения и генерации</li>"
        "<li>Гибкий ввод: URL сайта, PDF/Excel/CSV/Word/Markdown/TXT или ключевые слова</li>"
        "<li>Многоканальный поиск: Google Search, Google Maps, B2B-площадки</li>"
        "<li>Извлечение контактов: email, телефон, адрес, ссылки на соцсети</li>"
        "<li>AI-генерация email-цепочек из 3 писем на основе ICP и инсайтов с сайта</li>"
        "<li>Real-time прогресс через SSE; интеграция с Langfuse для мониторинга затрат</li>"
        "<li>Поддержка OpenAI, Anthropic, OpenRouter, Groq, GLM, Moonshot, MiniMax через LiteLLM</li>"
        "</ul>"
        "<h2>Стек</h2>"
        "<p>Backend: FastAPI + LangGraph. Frontend: React + Vite. Хранение: SQLite/JSON.</p>"
    ),
}

TOOL_ABOUT_EN = {
    "github-lead-signals": (
        "<p><strong>GitHub Lead Signals</strong> is an Apify Actor for B2B prospecting based on GitHub "
        "technology signals. It analyzes public developer and organization activity—repositories, language "
        "stacks, commit patterns, and engagement—and uses AI to surface companies already using or adopting "
        "your target technologies.</p>"
        "<p>It is a practical way to find product teams, SaaS startups, and dev-tool vendors for outbound "
        "sales, integrations, and partnerships—without manually browsing GitHub.</p>"
        "<h2>What it does</h2>"
        "<ul>"
        "<li>Discovers organizations and developers by tech stack</li>"
        "<li>Analyzes repository patterns and programming languages</li>"
        "<li>Scores activity and engagement with AI</li>"
        "<li>Exports company lists for enrichment in the LeadScaper pipeline</li>"
        "</ul>"
        "<h2>Data source</h2>"
        "<p>GitHub API via Apify—a ready-to-run cloud Actor with no infrastructure to maintain.</p>"
    ),
    "ai-find-customer": (
        "<p><strong>AI_Find_Customer</strong> (AI Hunter) is an open-source automated B2B lead discovery "
        "system for export and B2B sales, built on FastAPI, LangGraph, a multi-agent pipeline, and "
        "multi-model LLM support.</p>"
        "<p>Provide your company website, product documents, or keywords plus a target market—the system "
        "automatically analyzes the company, generates search queries, runs web search, extracts leads, "
        "and discovers contact details.</p>"
        "<h2>Key features</h2>"
        "<ul>"
        "<li>Multi-agent pipeline: Insight → KeywordGen → Search → LeadExtract → Evaluate</li>"
        "<li>Dual-model setup: a reasoning model for ReAct decisions, a standard model for extraction and generation</li>"
        "<li>Flexible input: website URL, PDF/Excel/CSV/Word/Markdown/TXT files, or keywords alone</li>"
        "<li>Multi-channel search: Google Search, Google Maps, B2B platforms</li>"
        "<li>Contact discovery: email, phone, address, social links</li>"
        "<li>AI email sequences: 3-step outreach drafts based on ICP and website insights</li>"
        "<li>Real-time progress via SSE; Langfuse integration for cost observability</li>"
        "<li>Models via LiteLLM: OpenAI, Anthropic, OpenRouter, Groq, GLM, Moonshot, MiniMax</li>"
        "</ul>"
        "<h2>Stack</h2>"
        "<p>Backend: FastAPI + LangGraph. Frontend: React + Vite. Storage: SQLite/JSON.</p>"
    ),
}


def build_tools_page(locale: dict, lang: str) -> dict:
    """Build toolsPage section from generate_tools.TOOLS."""
    about_map = TOOL_ABOUT_RU if lang == "ru" else TOOL_ABOUT_EN
    tools_page = {}
    for tool in TOOLS:
        slug = tool["slug"]
        if lang == "ru":
            entry = {
                "role": tool["role"],
                "layerName": tool["layer_name"],
            }
        else:
            entry = {
                "role": TOOL_ROLES_EN[slug],
                "layerName": LAYER_NAMES_EN[tool["layer"]],
            }
        if slug in about_map:
            entry["about"] = about_map[slug]
        tools_page[slug] = entry
    return tools_page


def validate_locale(locale: dict, lang: str) -> None:
    """Ensure all required tool slugs are present."""
    missing_tools = [s for s in TOOL_SLUGS if s not in locale["tools"]]
    if missing_tools:
        raise ValueError(f"{lang}: missing tools entries: {missing_tools}")

    missing_page = [s for s in TOOL_SLUGS if s not in locale["toolsPage"]]
    if missing_page:
        raise ValueError(f"{lang}: missing toolsPage entries: {missing_page}")

    if len(locale["pipeline"]) != 4:
        raise ValueError(f"{lang}: pipeline must have 4 items")

    if len(locale["flow"]["steps"]) != 8:
        raise ValueError(f"{lang}: flow.steps must have 8 items")

    if len(locale["tech"]["rows"]) != 9:
        raise ValueError(f"{lang}: tech.rows must have 9 items")


def build_locale(base: dict, lang: str) -> dict:
    locale = json.loads(json.dumps(base))
    locale["toolsPage"] = build_tools_page(locale, lang)
    validate_locale(locale, lang)
    return locale


def write_locale(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    LOCALES_DIR.mkdir(exist_ok=True)

    ru = build_locale(RU, "ru")
    en = build_locale(EN, "en")

    ru_path = LOCALES_DIR / "ru.json"
    en_path = LOCALES_DIR / "en.json"

    write_locale(ru_path, ru)
    write_locale(en_path, en)

    print(f"Wrote {ru_path} ({len(json.dumps(ru)):,} bytes)")
    print(f"Wrote {en_path} ({len(json.dumps(en)):,} bytes)")
    print(f"Tools: {len(ru['tools'])} | toolsPage: {len(ru['toolsPage'])}")


if __name__ == "__main__":
    main()
