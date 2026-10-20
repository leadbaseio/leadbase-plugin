# Connect to Leadbase from MCP.so

MCP.so is a discovery directory. It does not replace the Leadbase service or issue Leadbase credentials. A listing request is separate from publication, approval or successful authentication in your chosen client.

Use these connection details in a client that supports remote Streamable HTTP MCP and OAuth:

| Field | Value |
| --- | --- |
| Server name | `leadbase` |
| Endpoint | `https://www.leadbase.io/api/mcp` |
| Transport | Streamable HTTP |
| Authentication | OAuth sign-in with your Leadbase account |
| Official registry identity | `io.leadbase/leadbase` |

Complete the host's browser sign-in and select an accessible workspace. Do not put a password, access token or API key in a public configuration or conversation. The public plugin bundle is optional for clients that can connect directly to a remote server.

Transport spelling depends on the host: Claude and Cursor use `http` in their compatibility configuration, Cline's extension uses `streamableHttp`, and Agent Plugins 1.0 uses `streamable-http`. Use the [shared connection files](../README.md#connect-your-account) or [Cline instructions](cline.md) for your client instead of copying one transport label everywhere.

After connecting, check accessible sheets and your workspace balance before requesting research. For a small test, ask for two companies with official websites and sources, follow progress, read the structured evidence, and open the returned Leadbase sheet link. Research uses existing workspace credits and plan limits. MCP.so does not provide free Leadbase research credits.

Interactive sheets depend on the client's MCP Apps support. Text clients receive structured results and a Leadbase link; you can review and edit the same sheet on Leadbase according to your permissions.

This repository contains the MIT integration bundle, not the private hosted server implementation. Directory review does not require access to private application code.

[Leadbase MCP documentation](https://www.leadbase.io/en/docs/settings/mcp) · [Support](https://www.leadbase.io/en/contact)
