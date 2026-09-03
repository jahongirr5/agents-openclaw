# SUBAGENT-POLICY.md - Subagent & Task Delegation Policy

Core Directive: Keep the main chat session instantly responsive. Anything requiring multi-step processing, file modifications, or background execution should be offloaded to a subagent.

---

## Delegation Boundaries

### Handle Directly in Main Session
- Conversational replies, quick answers, and clarifying questions
- Brief file reads or context lookups that complete in under 2 seconds
- Simple acknowledgments and status checks

### Delegate to a Subagent
- Web searches, external API calls, and internet research
- File modifications, multi-file edits, and batch operations
- Complex data transformations, log analysis, and system scripts
- Any task with a potential execution delay or risk of failure

---

## Coding, Debugging & Investigation Delegation

All coding, debugging, and structural troubleshooting work is routed through subagents to keep the main session unblocked:

- **Simple Fixes**: Single-line config updates, minor script tweaks, or appending patterns -> Handled directly by a lightweight subagent.
- **Medium / Major Development**: Multi-file refactoring, new features, or system troubleshooting -> Delegated to the coding agent CLI.

Model and provider routing rules are managed centrally in `config/model-routing.json`.

---

## Delegation Announcements

When spawning a subagent, provide a brief, professional confirmation using this format:

`[model] via [provider/tool]`

**Examples**:
- *"Spawning subagent with Claude-3.5-Sonnet to search documentation."*
- *"Delegating task to DeepSeek-Coder via Coding CLI."*

---

## Failure Handling & Recovery

1. **Isolation**: Subagent errors must never crash or block the main chat session.
2. **Transient Retry**: If a subagent encounters a network timeout or rate limit, retry once automatically.
3. **Proactive Reporting**: If both attempts fail, report the error details directly in the main session so the user is aware.

---

## Execution Environment

- **Workspace Path**: `C:\Users\johann\.openclaw\workspace\`
- **Shell**: Windows PowerShell
- **Rule**: Run subagents silently in the background. Synthesize and deliver the final deliverable directly upon completion.