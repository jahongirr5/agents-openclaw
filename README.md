# agents-openclaw

Personal OpenClaw workspace for **Mario 🗿**.

This repo holds the local brain, rules, memory, and custom skills behind the assistant setup. It is meant to keep the workspace organized, reproducible, and easy to extend.

## What is inside

- **AGENTS.md**: workspace rules, safety boundaries, operating style
- **SOUL.md**: persona, tone, and character
- **IDENTITY.md**: short identity card for the assistant
- **USER.md**: durable user preferences and behavior rules
- **MEMORY.md**: long-term private memory and stable facts
- **memory/**: dated notes, heartbeat state, and ongoing logs
- **skills/**: custom and installed skills used by the workspace
- **media/**: staged local media files used during tasks

## Purpose

This workspace is used to:

- run a personalized OpenClaw assistant setup
- store durable instructions and memory safely
- manage custom skills and automations
- keep day-to-day assistant state versioned in Git

## Repo structure

```text
.
├── AGENTS.md
├── IDENTITY.md
├── MEMORY.md
├── README.md
├── SOUL.md
├── SUBAGENT-POLICY.md
├── USER.md
├── memory/
├── media/
└── skills/
```

## Local setup

1. Install and configure **OpenClaw**.
2. Point the agent workspace to this folder.
3. Add required secrets through the OpenClaw secret store.
4. Start the Gateway and verify the agent is healthy.
5. Use Git to keep changes tracked and backed up.

## Notes

- This repo may contain private local assistant configuration and memory structure.
- Secrets should **never** be committed in plaintext.
- Use protected secrets and SecretRefs wherever possible.

## Status

Current setup already includes:

- OpenClaw workspace initialized
- Notion skill connected and tested
- Obsidian vault basic structure prepared
- Git remote linked to GitHub

## Future improvements

- cleaner vault templates
- better daily workflow notes
- more custom skills
- automated backup and sync flow

---

Built around a local-first assistant workflow, direct, practical, and a little stone-faced.
