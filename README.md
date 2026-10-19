# Leadbase

Find leads. Build your list.

Turn a research request into companies, professional contacts, products or public posts in a sheet you can review and edit. Leadbase finds information on the web, saves available sources and keeps your results in the same workspace you use at [leadbase.io](https://www.leadbase.io).

## What you can do

- Build a new list with one result per row.
- Fill missing details in existing rows or an entire column, preserving populated cells.
- Follow research progress and inspect available sources.
- Browse, search, filter and edit accessible sheets according to your permissions.
- Check your plan and credit balance without starting research.

## Connect your account

You need a Leadbase account and access to a workspace. Add this plugin, connect the Leadbase connector and complete the OAuth sign-in flow. Choose the workspace you want to use. No API key or password belongs in a conversation. The plugin and the Leadbase connector use the same endpoint, so you only need one connection.

Research consumes your workspace's existing Leadbase credits. Plan limits apply. Connecting, opening sheets or checking your balance does not request paid research. Buy or manage your plan on the Leadbase website. The plugin does not purchase credits or send outreach.

## Try it

“Find 5 independent coffee roasters in Berlin with their official websites. Save one company per row in a new sheet and show it.”

“Fill empty headquarters cells for every company in this sheet using official sources. Keep existing values.”

“Open my Leadbase workspace and show the progress of my latest research.”

## Sheets and results

Supported Claude surfaces can display the interactive Leadbase sheet through MCP Apps. Text-only clients receive structured results and a Leadbase link. Available display modes depend on the host. Live progress is separate from completed results, and execution completion is separate from final credit settlement. Coverage varies; results may be incomplete or lack sufficient evidence. Review the supplied sources before acting on findings.

## Data and permissions

This bundle contains two research workflow skills and a reference to the hosted Leadbase MCP server at https://www.leadbase.io/api/mcp. It uses the same server, account permissions and sheet editor as Leadbase's Codex integration. It runs no local server, shell hooks, background scripts or package installers.

When Claude calls a tool, the requested arguments and relevant sheet context are sent to Leadbase. Leadbase stores sheets and research results in your workspace and uses service providers for research and hosting as described in its privacy policy. The bundle itself adds no separate storage or telemetry. Only context sent through tool calls is received; the plugin does not independently read your conversation history. Read and write permissions are enforced by the connected account. Sharing, deletion and paid research remain explicit actions.

See the [privacy policy](https://www.leadbase.io/en/legal/privacy) for data processing, service providers, retention and deletion requests. The [service terms](https://www.leadbase.io/en/legal/terms) govern your Leadbase account.

## Help

[Setup and usage documentation](https://www.leadbase.io/en/docs/settings/mcp) · [Support](https://www.leadbase.io/en/contact) · [Deutsch](README.de.md)
