# OpenClaw Automation System

AI-powered automation gateway running on macOS with Telegram integration.

## What I Built

- **Local Gateway:** OpenClaw running on Apple M2 (8GB RAM) via Node.js/nvm
- **AI Backend:** OpenAI GPT-4o-mini API ($5 prepaid tier, ~5,000+ messages)
- **Mobile Interface:** Telegram bot for on-the-go access and notifications
- **Security:** API keys stored locally, never committed to Git

## Why I Built This

- **Reselling Business:** Automate price monitoring (Supreme, Pokemon, FB Marketplace)
- **Pololu Internship:** Error decoding and documentation assistance
- **College Apps:** Activity tracking and essay proofreading

## Current Status

- [x] Gateway running locally
- [x] Telegram bot connected and paired
- [x] OpenAI API integration working
- [x] Supreme drop monitor (basic scraper built, testing selectors)
- [ ] Arduino error decoder (in progress)
- [ ] Daily activity logger (planned)

## Setup

### Prerequisites
- Node.js (installed via nvm in user space — no admin required)
- OpenClaw CLI
- Telegram bot (via @BotFather)

### Installation
1. Clone this repo
2. Copy template to your local OpenClaw config:
   ```bash

cp config.template.json ~/.openclaw/openclaw.json

## Automations

### Supreme Drop Monitor
- **File:** `supreme_monitor.py`
- **What it does:** Checks Supreme's new releases page for items and prices
- **How to run:** `python supreme_monitor.py`
- **Status:** Basic scraper built, needs real HTML selectors from live site
- **Next step:** Connect to OpenClaw scheduler to run daily at 8 AM