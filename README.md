#WHS Daily Safety Tips Bot

A lightweight, automated Slack bot that posts a rotating Workplace Health & Safety (WHS) tip once per day into a selected Slack channel. 
The bot is designed to reinforce safe habits, raise daily awareness, and support safety culture inside operational and logistics teams.

This project runs entirely on **GitHub Actions**—no servers, no endpoints, and no maintenance required. 
It simply executes once per day at the configured time, sends one WHS tip via Slack, and repeats the next day.

---

## :wrench: How It Works

GitHub Actions triggers the workflow on a schedule (using cron).
The workflow installs dependencies, runs a small Python script, and sends a message to Slack.
The Python script selects a WHS tip based on the current date (clean daily rotation).
The bot posts one message to the Slack channel using only the low-risk `chat:write` scope.
---
