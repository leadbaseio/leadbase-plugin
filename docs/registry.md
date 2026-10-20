# Official MCP Registry

The canonical registry name is `io.leadbase/leadbase`. The namespace is verified through an MCP TXT proof at the apex of `leadbase.io`. Authentication uses a publisher signing key, separate from end-user Leadbase OAuth.

## What is published

`server.json` contains public discovery metadata and the existing Streamable HTTP endpoint, `https://www.leadbase.io/api/mcp`. It has no local package, credentials or private application source. Its website links to setup documentation. The public plugin bundle is identified separately in publisher metadata because it is not the server implementation.

The service requires Leadbase OAuth and workspace access. Research consumes the connected workspace's credits. Interactive sheets depend on the host's MCP Apps support; other clients receive structured results and a Leadbase link.

## Validate and publish

1. Run the package validation commands from the README. CI validates the registry manifest against the pinned official schema and checks that its version and endpoint match the shared bundle.
2. Review the public metadata and merge only after package validation passes. Existing marketplace review submissions are separate and must not be cancelled or replaced for a registry publication.
3. Use the official `mcp-publisher` CLI from https://github.com/modelcontextprotocol/registry/releases. Verify the release checksum before execution. Version 1.8.1 was used for the initial publication.
4. Authenticate using the existing `leadbase.io` DNS signing key according to https://modelcontextprotocol.io/registry/authentication. Keep the key and publisher token in an owner-only directory outside any repository. Never commit them, put them in a workflow, or print them in logs. Retain the existing public DNS proof for future releases; do not create another key or replace the proof as part of an ordinary update.
5. From that private publisher directory, run `mcp-publisher publish /absolute/path/to/leadbase-plugin/server.json` against the production registry. No npm package or GitHub repository access is needed.
6. Read back the exact version and latest entry through the registry API, checking the name, version, active status, icon and remote URL. Publishing is complete only once that read-back matches the submitted manifest.

Read-back endpoint: https://registry.modelcontextprotocol.io/v0.1/servers/io.leadbase%2Fleadbase/versions/latest

The registry stores discovery metadata. A registry entry does not imply approval by OpenAI, Anthropic, xAI, Cursor or any other client, and downstream galleries decide independently whether to include it.
