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

This is the shared Leadbase plugin bundle, not a Claude-only integration. Every format uses the same two skills and hosted MCP service. The bundle contains no private application source.

| Host | Package entry point | Connection |
| --- | --- | --- |
| Codex and Agent Plugins 1.0 clients | `plugin.json` | `mcp.json` (Streamable HTTP) |
| Cursor | `.cursor-plugin/plugin.json` | `.mcp.json` (HTTP compatibility format) |
| Claude | `.claude-plugin/plugin.json` | `.mcp.json` (HTTP compatibility format) |
| Grok Bot and compatible MCP clients | Host-supported plugin import or MCP server URL | `https://www.leadbase.io/api/mcp` |

Both MCP files describe the same OAuth-protected endpoint using the transport spelling required by their format. Packaging compatibility is separate from marketplace approval and authenticated host testing. Existing OpenAI and Claude submissions retain their original identities and submitted versions; this repository does not replace those submissions automatically.

For a local Cursor test, copy this bundle into `~/.cursor/plugins/local/leadbase-research` and reload a test window. Open **Customize** and verify the two skills and the `leadbase` MCP server. Authenticate through the host's OAuth flow. Local plugin imports must be allowed by your account or team. To test another compatible client, use its local plugin installation flow or add the HTTPS MCP endpoint below. A marketplace listing is subject to the platform's review.

You need a Leadbase account and access to a workspace. Add this plugin, connect the Leadbase connector and complete the OAuth sign-in flow. Choose the workspace you want to use. No API key or password belongs in a conversation. The plugin and the Leadbase connector use the same endpoint, so you only need one connection.

Research consumes your workspace's existing Leadbase credits. Plan limits apply. Connecting, opening sheets or checking your balance does not request paid research. Buy or manage your plan on the Leadbase website. The plugin does not purchase credits or send outreach.

## Try it

“Find 5 independent coffee roasters in Berlin with their official websites. Save one company per row in a new sheet and show it.”

“Fill empty headquarters cells for every company in this sheet using official sources. Keep existing values.”

“Open my Leadbase workspace and show the progress of my latest research.”

## Sheets and results

Hosts with MCP Apps support can display the interactive Leadbase sheet. Text-only clients receive structured results and a Leadbase link. Available display modes depend on the host. Live progress is separate from completed results, and execution completion is separate from final credit settlement. Coverage varies; results may be incomplete or lack sufficient evidence. Review the supplied sources before acting on findings.

## Data and permissions

This bundle contains two research workflow skills and a reference to the hosted Leadbase MCP server at https://www.leadbase.io/api/mcp. It uses the same server, account permissions and sheet editor as Leadbase's Codex integration. It runs no local server, shell hooks, background scripts or package installers.

When a connected client calls a tool, the requested arguments and relevant sheet context are sent to Leadbase. Leadbase stores sheets and research results in your workspace and uses service providers for research and hosting as described in its privacy policy. The bundle itself adds no separate storage or telemetry. Only context sent through tool calls is received; the plugin does not independently read your conversation history. Read and write permissions are enforced by the connected account. Sharing, deletion and paid research remain explicit actions.

See the [privacy policy](https://www.leadbase.io/en/legal/privacy) for data processing, service providers, retention and deletion requests. The [service terms](https://www.leadbase.io/en/legal/terms) govern your Leadbase account.

## License

The files in this public plugin bundle are available under the [MIT License](LICENSE). The hosted Leadbase service and private application source are separate and are not licensed by this repository. Leadbase accounts remain subject to the service terms. The MIT license does not grant trademark rights. Vendored schemas retain their included upstream license.

## Help

Maintainers can validate all manifests, shared endpoint configuration, skills and asset paths with `python -m pip install -r requirements-validation.txt` followed by `python scripts/validate-package.py`. The same check runs in GitHub Actions with read-only repository permissions. Official schemas are pinned in `schemas/`; their upstream license is included there. No validation code runs during plugin installation.

[Setup and usage documentation](https://www.leadbase.io/en/docs/settings/mcp) · [Support](https://www.leadbase.io/en/contact) · [Deutsch](README.de.md)
