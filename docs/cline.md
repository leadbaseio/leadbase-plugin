# Leadbase in Cline

Use Cline's native remote MCP connection. It connects to the same Leadbase service, workspace and sheets as the other plugin formats. No local Leadbase server, proxy, API key or private GitHub repository access is required.

## Cline CLI

With Cline installed, run:

```sh
cline mcp install leadbase --transport http https://www.leadbase.io/api/mcp
```

Confirm the prefilled name, **Remote (HTTP)** transport and URL. Choose **OAuth**, leave the client ID empty for dynamic registration, and complete the browser sign-in. Choose the intended Leadbase workspace and approve the requested permissions. Do not paste passwords or tokens into the agent conversation.

For a separate test configuration, use Cline's global `--config` and `--data-dir` flags. Keep the resulting OAuth tokens private; they are local client credentials and do not belong in this public repository.

## Cline extension

Open Cline's MCP server settings and add a remote HTTP server named `leadbase` at:

```text
https://www.leadbase.io/api/mcp
```

Authenticate through the host's OAuth action. If editing the extension's MCP settings directly, its Streamable HTTP transport spelling is:

```json
{
  "mcpServers": {
    "leadbase": {
      "type": "streamableHttp",
      "url": "https://www.leadbase.io/api/mcp"
    }
  }
}
```

Merge the `leadbase` entry into your existing settings; preserve other servers. CLI and extension configuration paths differ. Use the CLI command for CLI installation rather than copying extension settings into it.

## Verify the connection

1. Ask Cline to list your accessible Leadbase sheets and check your workspace credit balance. These actions do not start paid research.
2. With sufficient credits, ask: “Find 2 independent coffee roasters in Berlin with their official websites. Save one company per row in a new private sheet and include sources.”
3. Follow the returned research operation until it reaches a terminal state. Read every result page needed for the requested count, and inspect the returned evidence URLs. Execution completion and final credit settlement are separate.
4. Open the returned Leadbase sheet link and verify the rows. Only edit or archive the sheet created for this test.

Research consumes existing workspace credits and is subject to plan and permission limits. Review evidence before relying on results. Keep sharing and deletion explicit, and require confirmation before unrequested paid work.

The catalog entry does not promise an embedded sheet in every Cline version. Clients supporting MCP Apps may render it; otherwise use structured tool results and the editable sheet on Leadbase.

If OAuth fails, use the server's OAuth action to reconnect, confirm the HTTPS endpoint, and update Cline. Never work around a redirect error by disabling PKCE, certificate checks or authorization. Report the error through [Leadbase support](https://www.leadbase.io/en/contact), without including tokens.

[Official Cline catalog](https://github.com/cline/marketplace) · [Leadbase setup documentation](https://www.leadbase.io/en/docs/settings/mcp)
