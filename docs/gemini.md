# Find your next customers with Gemini CLI and Leadbase

Describe your ideal customers and turn the research into an editable lead list with sources. Find DACH companies, research relevant professional contacts and enrich records you already have. New Leadbase workspaces start with 200 free credits.

## Install

```sh
gemini extensions install https://github.com/leadbaseio/leadbase-plugin
```

Restart Gemini CLI after installation. Open `/mcp` and run `/mcp auth leadbase` to sign in to your Leadbase account and select your workspace. Each person authorizes their own account through Leadbase. The extension contains no credentials and runs no local server.

## Try a focused search

> Find 10 kitchen retailers in Germany with their company website, location and supporting sources. Create a private Leadbase sheet so I can review the list.

Or work with an existing sheet:

> Enrich the Website column in my selected Leadbase sheet. Show the estimated credits first, then research the missing values and include sources.

Follow progress, inspect the evidence and open the sheet to review, edit and export the results. MCP UI support depends on the client. The Leadbase sheet link remains available for the full editable workspace.

## Shared foundation

This extension connects to the same hosted MCP service as the Claude, Codex and Cursor bundles. Gemini loads the existing `get-started` and `research-list` skills from `skills/`. It does not need access to your GitHub repositories.

Authentication uses OAuth discovery, with read and write access for the workspace you select and renewal access for your connection. Research and enrichment use your Leadbase credits. Ask for estimates and a small sample before a large run.

- [Start with Leadbase](https://www.leadbase.io)
- [Leadbase connection guide](https://www.leadbase.io/en/docs/settings/mcp)
- [Gemini CLI extensions](https://geminicli.com/docs/extensions/)
