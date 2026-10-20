<img src="assets/icon.png" width="64" height="64" alt="Leadbase logo">

# Leadbase: AI Lead Generation and Contact Enrichment

**Your next customer list starts with one sentence.**

Tell your AI assistant which companies or decision-makers you want to reach. Leadbase turns that request into a researched, editable prospect list with sources, ready for your team to qualify and use.

Find target accounts, research professional contacts and enrich the details that make a lead worth pursuing. Work inside a compatible AI assistant or open the same persistent sheet in Leadbase. Keep your research, evidence and next questions together as your list develops.

**Try your own target market with 200 free credits in every new workspace.**

[Start free](https://www.leadbase.io/auth/signup) · [See pricing](https://www.leadbase.io/pricing) · [Connection guide](https://www.leadbase.io/en/docs/settings/mcp) · [Read in German](README.de.md)

> Find 10 solar installation companies in Bavaria that serve commercial customers. Include their websites, evidence of commercial projects and relevant professional contacts. Save the companies in a new Leadbase sheet.

## Contents

- [What is Leadbase?](#what-is-leadbase)
- [Why teams choose Leadbase](#why-teams-choose-leadbase)
- [Features and practical benefits](#features-and-practical-benefits)
- [DACH lead generation](#dach-lead-generation)
- [Who uses Leadbase?](#who-uses-leadbase)
- [From your first request to a qualified list](#from-your-first-request-to-a-qualified-list)
- [Research questions that reveal customer fit](#research-questions-that-reveal-customer-fit)
- [Example prompts](#example-prompts)
- [Connect your account](#connect-your-account)
- [Live sheets and source evidence](#live-sheets-and-source-evidence)
- [Pricing and free credits](#pricing-and-free-credits)
- [Considering an Apollo alternative?](#considering-an-apollo-alternative)
- [Frequently asked questions](#frequently-asked-questions)
- [Data and permissions](#data-and-permissions)
- [About this public plugin bundle](#about-this-public-plugin-bundle)
- [Glossary](#glossary)
- [Support and useful links](#support-and-useful-links)

## What is Leadbase?

Leadbase is an AI lead generation, company research and contact enrichment platform. It helps you discover accounts, understand why they fit your offer and bring the results into a sheet you can continue working with.

The Leadbase MCP server connects that research workflow to compatible AI assistants, including ChatGPT, Claude, Claude Code, Codex, Cursor and Cline. Describe the result in ordinary language, then let your assistant use Leadbase to create a list, research existing records or retrieve findings and supporting sources.

Think of the output as a working prospect list. Each company, person, product or public content item has its own row. Research fields become columns. Your team can inspect the evidence, correct a value, add a qualification question and export the shortlist when it is ready.

This repository provides the shared integration bundle for those workflows. A single hosted service connects your assistant to your existing Leadbase workspace and sheets.

## Why teams choose Leadbase

### Describe the customer you actually want

Your ideal customer may be a regional manufacturer, a specialist installer or an agency serving one particular market. Describe the services, business model, location and evidence that make an account relevant. Turn your ideal customer profile into a research brief your assistant can act on.

### Understand why an account belongs on your list

A company name is a starting point. Add the details that explain fit: a relevant service, a commercial customer focus, a public hiring signal or a branch network. Keep the explanation and available source links beside the account, so a teammate can understand your reasoning when reviewing the list.

### Bring company research and contact research together

Build your account shortlist, then research the professional roles that matter for your offer. You can also create a dedicated people list when the person is your starting point. Keep the company context close to the contact, so your next conversation starts with something relevant.

### Keep the work useful after the first answer

Your list stays in an editable Leadbase sheet. Revisit it, enrich another field, filter the results or export the accounts you want to pursue. The first research request becomes a foundation for the next one.

## Features and practical benefits

| Capability | What you can do | Why it helps |
| --- | --- | --- |
| AI company discovery | Describe target businesses by region, offer and relevant criteria | Build a list around your actual market |
| Professional contact research | Research people by company, role and business context | Identify relevant decision-makers for an account |
| New company and people lists | Save each requested entity as its own result row | Get a usable list structure from the start |
| Existing-list enrichment | Add missing details and new research fields to your sheet | Improve the records your team already has |
| Whole-column enrichment | Research a defined field across existing rows | Apply the same qualification question consistently |
| Custom account qualification | Ask questions about services, customers or public signals | Evaluate fit using criteria specific to your offer |
| Readable source evidence | Inspect available supporting links with the findings | Check and cite the facts behind your shortlist |
| Persistent research sheets | Return to the same saved results | Continue research without recreating the list |
| Interactive sheet editing | Edit cells, search and filter in the sheet | Turn research into a practical working dataset |
| Research progress | Follow the operation and retrieve completed findings | See how the request is progressing |
| CSV export | Export the reviewed sheet | Move a shortlist into your downstream workflow |
| Hosted MCP connection | Connect a supported client through OAuth | Use Leadbase from an existing AI workflow |
| Workspace access controls | Work with sheets your connected account can access | Keep research within the intended workspace |
| Product and public web research | Collect structured products, suppliers or content | Reuse the workflow beyond sales prospecting |

## DACH lead generation

Leadbase is useful for teams researching companies in **Germany, Austria and Switzerland**, including German SMEs, regional service providers and craft businesses. Start with a specific territory and the kind of customer your offer is built for.

For a DACH prospecting project, you might describe:

- Solar installers in Bavaria with evidence of commercial projects.
- HVAC service companies in Austria that offer maintenance contracts.
- Swiss manufacturers advertising a relevant public job opening.
- Independent kitchen retailers in Germany with multiple showrooms.
- Industrial service providers in a defined German sales territory.

These are research briefs you can adapt to your own market. Decide which details would make the result useful, then include those fields in your request. For a local sales campaign, that could be the business address and service area. For account-based sales, it could be customer segments, relevant services and professional roles.

Leadbase also supports research outside DACH. Specify the country, language context and target criteria when researching another region.

## Who uses Leadbase?

| Team or role | A useful starting task | The result to work toward |
| --- | --- | --- |
| Founders | Find businesses matching a new product's ideal customer profile | A focused first prospect list |
| SDR and BDR teams | Research target accounts and the professional roles involved | Accounts with context for relevant outreach preparation |
| Account executives | Add business-fit evidence to named accounts | A better-informed account review |
| Sales operations | Enrich missing company fields in an existing sheet | More useful data for the next workflow |
| Agencies | Research prospects for a specific service or client niche | A shortlist tailored to the campaign |
| Consultants | Map a regional market and classify relevant providers | A structured market overview |
| Partnership teams | Find distributors, agencies or complementary businesses | Potential partners with a clear reason for relevance |
| Recruiting businesses | Research employers and professional decision-makers | Company context for business development |
| Procurement teams | Compare suppliers or products against requirements | A source-linked supplier or product shortlist |

## From your first request to a qualified list

### 1. Define the result

Start with the entity you want: companies, professional contacts, products or public content. Add the number of results, geographic scope and fields that matter. A clear brief gives your assistant a concrete outcome to work toward.

> Find 10 independent coffee roasters in Berlin. Include the company name, official website, location and evidence that they supply cafes or restaurants. Save one company per row in a new private sheet.

### 2. Connect the intended workspace

Complete the Leadbase sign-in flow in your supported client and choose the workspace you want to use. You can ask the assistant to show your accessible sheets or check the credit balance before starting research.

### 3. Follow progress and inspect the findings

Research can continue after the first tool response. Ask your assistant to follow the operation, retrieve its results and show the sheet. Review the source links for the criteria that matter to your decision.

### 4. Add your qualification questions

Once the list exists, enrich the same rows with another field. For example, research whether each roaster offers wholesale supply, training or equipment support. Your list becomes more useful as the questions become more specific to your offer.

### 5. Review and use the shortlist

Edit values, filter your sheet and export the accounts you want to pursue. Keep the sheet for follow-up research when your campaign develops or a teammate needs more context.

### New rows or enrichment?

Use **new-list research** when you want additional entities, such as 50 new companies or 20 professional contacts. Each entity becomes a new result row.

Use **enrichment** when the entities already exist in your sheet and you want to learn something else about them. You can research selected records or an entire column. The standard column workflow preserves populated values and skips cells already undergoing research.

## Research questions that reveal customer fit

The most valuable field is often the one that reflects how you sell. Before adding a research column, ask which answer would change your decision about an account.

| Research question | What it helps you assess | Useful evidence to request |
| --- | --- | --- |
| Does this company serve commercial customers? | Fit for a B2B offer | A service page or commercial project example |
| Does it offer installation and maintenance? | Fit for a recurring-service workflow | Service descriptions and maintenance pages |
| Does it operate multiple locations? | Potential operational complexity | Official branch or location pages |
| Is it hiring for a relevant role? | A public signal connected to your offer | Current job posting and publication context |
| Which customer industries does it mention? | Relevance to your vertical | Customer pages or case studies |
| Does it offer the product category we support? | Product or supplier fit | Official product and category pages |
| Who appears responsible for the relevant function? | A starting point for contact research | Professional role and profile evidence |

Request both the conclusion and the supporting source. A finding such as “commercial projects mentioned on the services page” is easier to review when the source stays attached to the account. Where the evidence does not answer the question, keep that uncertainty visible in the sheet.

## Example prompts

Copy a prompt, replace the market and criteria with your own, and start with a focused request. These examples describe research tasks; the available evidence and contact data determine the findings.

### Company search and B2B prospecting

1. **Regional sales:** “Find 10 industrial cleaning companies in North Rhine-Westphalia that work with manufacturing customers. Include official websites and the source for the customer focus.”
2. **Craft businesses:** “Find 10 electrical installation businesses in Hamburg. Research whether they offer commercial building services. Save one company per row.”
3. **Specialist services:** “Find 5 Austrian HVAC companies with a maintenance offering. Include the relevant service page for each company.”
4. **Market mapping:** “Create a company list of Swiss packaging manufacturers. Include location, product focus and official website.”

### Decision-makers and professional contacts

5. **Account contacts:** “For the companies in this sheet, research the most relevant professional contact for facilities management. Include role and available profile sources.”
6. **People list:** “Create a new list of professional contacts responsible for partnerships at German B2B software companies. Save one person per row with company context.”
7. **Founder research:** “Research the founders of these agencies and add available professional profile links to the existing rows.”

### Existing-list and column enrichment

8. **Company details:** “Fill the empty headquarters cells in this sheet using official company sources. Keep existing values.”
9. **Qualification:** “Research whether each company in this sheet serves commercial customers. Add a short explanation and supporting source.”
10. **Locations:** “For the selected companies, research their branch locations using the official websites.”
11. **Public hiring signals:** “Check whether these companies have a current public job posting for a service technician. Include the job URL and what you found.”
12. **Follow-up research:** “Add a field explaining which of these suppliers offer maintenance contracts. Use the same sheet.”

### Suppliers, products and public content

13. **Supplier discovery:** “Find 5 suppliers of reusable transport packaging in Germany. Include their product focus and source websites.”
14. **Product research:** “Create a shortlist of commercial air purifiers. Include manufacturer, product name, published specifications and source URL.”
15. **Content research:** “Find public posts about commercial solar installation in Germany. Save each relevant post as a row with author, topic and source link.”
16. **Competitor research:** “Research the public service offerings of the companies in this sheet. Add the service categories and supporting pages.”

### Working with your results

17. **Progress:** “Show the progress of my latest Leadbase research and open the corresponding sheet.”
18. **Evidence review:** “Read the source evidence behind these qualification results and cite the links in your summary.”
19. **Workspace overview:** “Show my accessible Leadbase sheets and check the workspace credit balance.”
20. **Next research step:** “Summarize which accounts have evidence of commercial projects and suggest one useful follow-up field. Wait for my choice before starting it.”

## Connect your account

The hosted Leadbase MCP endpoint is:

```text
https://www.leadbase.io/api/mcp
```

Use a client that supports remote MCP over Streamable HTTP and the Leadbase OAuth sign-in flow. Choose your workspace during authorization. If you already have the Leadbase connection in that client, reuse it.

### Choose your client

| Client | How to connect | Where to learn more |
| --- | --- | --- |
| ChatGPT | Use the available Leadbase connection or the client's supported custom MCP connection flow | [Leadbase connection guide](https://www.leadbase.io/en/docs/settings/mcp) |
| Claude | Use the Leadbase connector where available, or add the endpoint through supported connector settings | [Leadbase connection guide](https://www.leadbase.io/en/docs/settings/mcp) |
| Claude Code | Add the remote HTTP MCP server and complete sign-in | [Command below](#claude-code) |
| Codex and Agent Plugins 1.0 clients | Use the supported plugin installation flow with this bundle | [Portable manifest](plugin.json) and [MCP configuration](mcp.json) |
| Cursor | Use the supported plugin import flow or add the remote MCP server | [Cursor manifest](.cursor-plugin/plugin.json) and [HTTP configuration](.mcp.json) |
| Cline | Add a native remote HTTP connection and authorize with OAuth | [Cline setup guide](docs/cline.md) |
| Gemini CLI | Install the shared extension, then authorize your Leadbase workspace | [Gemini setup guide](docs/gemini.md) |
| Other compatible clients | Add the hosted endpoint using the client's remote MCP settings | [General connection guide](https://www.leadbase.io/en/docs/settings/mcp) |

Direct MCP connections and plugin bundles use the same Leadbase service. Public marketplace availability follows each host's publication process; the connection instructions also cover clients with a supported direct setup.

### Claude Code

Add the hosted server:

```sh
claude mcp add --transport http leadbase https://www.leadbase.io/api/mcp
```

Then open `/mcp` in Claude Code and complete the Leadbase authentication flow. See the [official Claude Code MCP documentation](https://code.claude.com/docs/en/mcp) for client configuration and scope options.

### HTTP configuration example

For clients using the Claude and Cursor compatibility format, the shared configuration is:

```json
{
  "mcpServers": {
    "leadbase": {
      "type": "http",
      "url": "https://www.leadbase.io/api/mcp"
    }
  }
}
```

Merge the `leadbase` entry into your existing client configuration. Transport labels differ by format: this bundle's portable configuration uses `streamable-http`, while the Cline extension uses `streamableHttp`. Follow the guide for your client when configuring the connection.

### Verify your first connection

Ask your assistant to list your accessible sheets and check the workspace balance. Then request a small research task using your own market, inspect the results and open the sheet. Complete sign-in in the host's authorization window; keep credentials out of prompts and public configuration files.

## Live sheets and source evidence

### A working sheet inside your research workflow

Leadbase saves results in persistent sheets. You can open a sheet, edit cells, search, filter and export the data. Add another research field when you need more context, or return later to continue with the same accounts.

Hosts with MCP Apps support can display the interactive Leadbase sheet inside the assistant. Other clients can read structured tool results and provide the link to the same sheet in Leadbase. Embedded display modes, full-screen views and sidebar pinning follow the host's available features.

### Evidence your assistant can read and cite

Available sources are included with research findings, so an assistant can retrieve the evidence and cite the relevant links in an answer. Your team can inspect the source pages when checking a qualification decision.

For a useful handoff, ask for a concise conclusion, the supporting URL and any context needed to understand it. “Offers commercial maintenance” with the corresponding service page is more actionable than a standalone label.

### Progress that stays connected to the result

Research status and saved findings let you follow an operation and inspect its results. For a larger request, the assistant should retrieve every result page needed for the requested scope. A research operation's completion and final credit settlement are separate states, so ask for the settled usage when reviewing cost.

## Pricing and free credits

**Every new Leadbase workspace starts with 200 free credits.** Use them to test your own target market before choosing a paid plan.

Start with a focused task: a small company list, a contact research request or a qualification field on existing rows. Review the result quality and credit usage, then expand the workflow that fits your team.

The public plugin bundle is free to use under its MIT license. Research runs on the hosted Leadbase service using your workspace credits and plan limits. The price of a task depends on the tools and research requested. Check the [current pricing](https://www.leadbase.io/pricing) for plan details and usage examples.

[Create your first workspace](https://www.leadbase.io/auth/signup)

## Considering an Apollo alternative?

If your evaluation starts with “Can this tool build the list my team actually needs?”, test Leadbase against a real brief from your market.

Bring a target account description, one qualification question and a set of fields your team would use. Assess the relevance of the companies, the usefulness of the evidence and how easily you can continue working with the results. For DACH prospecting, try a concrete regional or specialist-business use case.

The [Leadbase and Apollo comparison](https://www.leadbase.io/alternatives/leadbase-vs-apollo) explains the product's approach to natural-language targeting and custom account research. Explore the [comparison hub](https://www.leadbase.io/alternatives) for other evaluation starting points.

## Frequently asked questions

### What can I use the Leadbase plugin for?

Use it for B2B lead generation, company discovery, professional contact research, existing-list enrichment and custom account qualification. The same research workflow supports supplier discovery, product research and public web content.

### Who is Leadbase for?

Leadbase helps founders, sales teams, agencies, consultants and researchers who need relevant accounts and useful business context. It is especially helpful when the criteria that define a good prospect need their own research questions.

### Can I try Leadbase for free?

Yes. Every new workspace starts with 200 free credits. Create a workspace and try a focused task before selecting a paid plan.

### Is the plugin free?

The public integration bundle is available under the MIT license. Research uses the hosted Leadbase service and your workspace credits. Your account's plan and usage terms apply to that service.

### How do I control research costs?

Start with a small, clearly defined request, check the balance and review usage before expanding. Specify the number of results and the fields you actually need. Current plan details and examples are on the [pricing page](https://www.leadbase.io/pricing).

### How do I create my first company list?

Describe the company type, region, result count and required fields. Ask Leadbase to save each company as a row in a new sheet. For example, request ten installers in one region with official websites and evidence of the service you care about.

### Can I find companies in Germany, Austria and Switzerland?

Yes. Specify the DACH country or region and the business criteria that matter. Research regional service providers, SMEs, craft businesses and other target accounts, then qualify them in the sheet.

### Can I research markets outside DACH?

Yes. Define the country or region and your research brief. Include any language or location context that helps identify the intended market.

### Can I find small businesses and specialist providers?

You can describe a specialist business type and request evidence of the relevant service or customer focus. Start with a narrow geography and a small sample to evaluate how the results fit your niche.

### Can I use my own lead qualification criteria?

Yes. Add questions about services, customer industries, business locations or other public information relevant to your offer. Request the supporting source alongside each answer so the qualification can be reviewed.

### Can I research buying signals or hiring activity?

You can ask for public evidence relevant to your campaign, such as a current role advertised on a company's website. Define the signal precisely and request its source and timing context. A public signal is one input for your assessment of an account.

### Can Leadbase research decision-makers?

Yes. Research professional contacts by company, role and business context. Ask for relevant role information, available professional profile links and business contact details appropriate to the task.

### Can I create a people list instead of a company list?

Yes. Ask for professional contacts as the result type. Each person becomes a result row, with company context and the fields you request.

### Does every result include an email address or phone number?

Contact details depend on availability and the requested lookup. Ask for the fields relevant to your workflow and review what was returned for each contact. Company research, contact discovery and contact-detail lookups serve different purposes.

### Can I enrich an existing list?

Yes. Use the companies or contacts already in your Leadbase sheet and add missing details or new research fields. The results stay associated with those records.

### Can I enrich an entire column?

Yes. Research a defined field across existing rows or limit the task to selected records. Standard column enrichment preserves populated values and skips cells with active research.

### Can I continue researching the same list later?

Yes. Sheets are persistent. Open the same sheet and request another field, review the existing evidence or refine the shortlist as your requirements develop.

### Can my assistant read and cite the sources?

Yes. Available source evidence is returned with the research findings. Ask the assistant to read it and include the relevant links in its summary.

### Are the results editable?

Yes. The Leadbase sheet supports cell editing, search, filtering and export according to your account permissions. Changes and follow-up research use the same working sheet.

### Will the sheet appear inside my AI assistant?

Clients supporting MCP Apps can render the interactive sheet. Other clients receive structured results and a Leadbase link. Open that link to continue working in the Leadbase app.

### Does Leadbase work with ChatGPT and Claude?

Leadbase supports compatible MCP connections from these assistants. Use the host's supported connection flow and the [Leadbase setup guide](https://www.leadbase.io/en/docs/settings/mcp). Directory publication and embedded UI features are specific to each host.

### Can I use Leadbase in Claude Code, Codex, Cursor or Cline?

Yes, through their supported MCP or plugin workflows. This repository includes shared connection configuration and client-specific plugin manifests. The [connection section](#connect-your-account) links to the relevant entry points.

### Do I need to run a local server?

Use the hosted HTTPS MCP endpoint. The bundle supplies the integration configuration and research skills, while Leadbase runs the research service.

### Do I need an API key for the OAuth connection?

Complete the client's Leadbase sign-in flow and choose your workspace. The standard OAuth connection uses that authorization rather than a key pasted into chat.

### Can I export results for my CRM or sales workflow?

Yes. Review and edit the sheet, then export the shortlist as CSV for your downstream workflow. The research plugin's sheet export is the handoff described here; any separate CRM integration has its own setup.

### Can I research products, suppliers or public posts?

Yes. Specify the result type, scope and fields. A product list might include published specifications and manufacturer links; a supplier list might include service regions and capabilities; a content list might include author, topic and source URL.

### Why consider Leadbase as an Apollo alternative?

Evaluate whether its research workflow, custom qualification fields and editable sheets fit your sales process. Use a small real task from your target market and compare the usefulness of the shortlist. The [comparison page](https://www.leadbase.io/alternatives/leadbase-vs-apollo) provides more context.

### Is this repository only for Claude?

It is the shared Leadbase integration bundle. The portable, Claude and Cursor manifests reference the same service and shared skills. Compatible clients can connect directly to the hosted endpoint.

### Does connecting give the plugin access to my private code?

The Leadbase bundle connects to its declared research service. It contains no local code-scanning tool or shell hooks. Leadbase receives the arguments and relevant context a connected client sends in tool calls. Your GitHub permissions and any separate code integrations are managed independently.

### What should I do if a connection fails?

Check the endpoint, complete the client's OAuth reconnect flow and confirm access to the intended workspace. The [setup documentation](https://www.leadbase.io/en/docs/settings/mcp) and [support team](https://www.leadbase.io/en/contact) can help with client-specific issues. Share a concise error description without credentials.

## Data and permissions

The public bundle contains two research workflow skills and a reference to the hosted Leadbase MCP server. It uses your connected account's workspace and sheet permissions. It runs no local server, shell hooks, background scripts or package installers.

When a client calls a tool, the requested arguments and relevant sheet context are sent to Leadbase. Leadbase stores sheets and results in your workspace and uses service providers for research and hosting as described in its [privacy policy](https://www.leadbase.io/en/legal/privacy). The bundle adds no separate storage or telemetry and does not independently read your conversation history.

Research, sharing and deletion follow explicit tool actions and account permissions. The research plugin does not send outreach or purchase credits. Review source evidence and use professional contact information according to applicable requirements and your organization's policies. The [service terms](https://www.leadbase.io/en/legal/terms) govern your Leadbase account.

## About this public plugin bundle

This is the shared, public integration foundation for Leadbase clients. It contains plugin manifests, connection configuration, two workflow skills, brand assets and validation tools.

| File or directory | Purpose |
| --- | --- |
| [plugin.json](plugin.json) | Portable Agent Plugins 1.0 manifest |
| [mcp.json](mcp.json) | Portable Streamable HTTP connection |
| [.claude-plugin/plugin.json](.claude-plugin/plugin.json) | Claude plugin manifest |
| [.cursor-plugin/plugin.json](.cursor-plugin/plugin.json) | Cursor plugin manifest |
| [.mcp.json](.mcp.json) | Shared HTTP compatibility configuration |
| [skills/get-started](skills/get-started/SKILL.md) | Account connection and first-task guidance |
| [skills/research-list](skills/research-list/SKILL.md) | Research, enrichment and evidence workflow |
| [server.json](server.json) | Official MCP Registry manifest for `io.leadbase/leadbase` |
| [docs](docs) | Client setup and registry publishing guides |
| [assets](assets) | Leadbase icons, including light and dark SVG assets |
| [scripts/validate-package.py](scripts/validate-package.py) | Shared package validation |

### For maintainers

Validate the package with:

```sh
python -m pip install -r requirements-validation.txt
python scripts/validate-package.py
```

The same check runs in GitHub Actions with read-only repository permissions. It validates manifests, the shared endpoint, skills and contained asset paths. Official schemas and their upstream license are included in [schemas](schemas).

Client-specific instructions are available for [Cline](docs/cline.md) and [MCP.so connections](docs/mcp-so.md). Maintainers can read the [registry publishing guide](docs/registry.md) for the domain-verified `io.leadbase/leadbase` identity.

### License

The public bundle is available under the [MIT License](LICENSE). The hosted Leadbase service and private application source remain separate from that license. Service terms apply to Leadbase accounts. The MIT license does not grant trademark rights; vendored schemas retain their included upstream license.

## Glossary

| Term | Meaning in a Leadbase workflow |
| --- | --- |
| B2B lead generation | Discovering companies and professional contacts relevant to your offer |
| Sales prospecting | Building and researching a target list for your sales process |
| Ideal customer profile or ICP | Business characteristics describing a good-fit account |
| Account qualification | Researching whether a company meets your chosen criteria |
| Contact enrichment | Adding relevant professional information to a contact record |
| Company enrichment | Adding business details and research fields to a company record |
| Firmographics | Company characteristics such as location, industry and size |
| DACH | Germany, Austria and Switzerland |
| Source evidence | Supporting URLs and context behind a research finding |
| Research sheet | A persistent, editable table containing your records and findings |
| MCP | Model Context Protocol, used by compatible assistants to call Leadbase tools |
| MCP Apps | Host support for an interactive interface alongside MCP tools |
| OAuth | The account authorization flow used to connect your workspace |

## Support and useful links

- [Start free with Leadbase](https://www.leadbase.io/auth/signup)
- [Plans, credits and pricing](https://www.leadbase.io/pricing)
- [MCP connection and usage documentation](https://www.leadbase.io/en/docs/settings/mcp)
- [Leadbase and Apollo comparison](https://www.leadbase.io/alternatives/leadbase-vs-apollo)
- [Product comparisons](https://www.leadbase.io/alternatives)
- [Contact the Leadbase team](https://www.leadbase.io/en/contact)
- [Privacy policy](https://www.leadbase.io/en/legal/privacy)
- [Service terms](https://www.leadbase.io/en/legal/terms)
- [German documentation in this repository](README.de.md)

**Bring your target market. Build your first researched list.**

[Create your workspace and start with 200 free credits](https://www.leadbase.io/auth/signup).
