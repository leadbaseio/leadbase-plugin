"""Validate the shared package without credentials or a running Leadbase account."""

import json
import re
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads((ROOT / path).read_text())


def contained(path):
    relative = Path(path)
    assert not relative.is_absolute() and ".." not in relative.parts, path
    target = ROOT / relative
    assert target.exists() and not target.is_symlink(), path
    assert target.resolve().is_relative_to(ROOT), path
    return target


portable = read("plugin.json")
for filename in ("plugin.json", "mcp.json"):
    schema = read(f"schemas/{filename}")
    Draft202012Validator.check_schema(schema)
    Draft202012Validator(schema).validate(read(filename))

manifests = [portable, read(".claude-plugin/plugin.json"), read(".cursor-plugin/plugin.json")]
for field in ("name", "version", "license", "homepage", "repository"):
    assert len({manifest[field] for manifest in manifests}) == 1, f"Manifest drift: {field}"
assert re.fullmatch(r"\d+\.\d+\.\d+", portable["version"]), "Use a release version"
for manifest in manifests:
    assert not manifest.get("apps"), "Do not publish private app bindings"
    assert not manifest.get("extensions", {}).get("com.openai", {}).get("apps")

legacy_servers = read(".mcp.json")["mcpServers"]
portable_servers = read("mcp.json")["mcpServers"]
assert set(legacy_servers) == set(portable_servers) == {"leadbase"}
for servers, transport in ((legacy_servers, "http"), (portable_servers, "streamable-http")):
    assert servers["leadbase"] == {
        "type": transport,
        "url": "https://www.leadbase.io/api/mcp",
    }, "MCP endpoint, transport or credential configuration changed"

cursor = manifests[2]
assert contained(cursor["mcpServers"]) == ROOT / ".mcp.json"
assert contained(cursor["skills"]) == ROOT / "skills"
contained(cursor["logo"])
contained(manifests[1]["icon"])
for skill in (ROOT / "skills").iterdir():
    assert skill.is_dir() and not skill.is_symlink(), skill
    text = (skill / "SKILL.md").read_text()
    frontmatter = text.split("---", 2)
    assert len(frontmatter) == 3 and not frontmatter[0].strip(), skill
    assert re.search(rf"^name: {re.escape(skill.name)}$", frontmatter[1], re.M), skill
    assert re.search(r"^description: \S.+$", frontmatter[1], re.M), skill

interface = portable["extensions"]["com.openai"]["interface"]
assert len(interface["displayName"]) <= 30
assert len(interface["shortDescription"]) <= 30
assert len(interface["longDescription"]) <= 4000
prompts = interface["defaultPrompt"]
assert 1 <= len(prompts) <= 3 and len(set(prompts)) == len(prompts)
assert all(prompt.strip() and len(prompt) <= 128 and "\n" not in prompt for prompt in prompts)
for field in ("logo", "logoDark", "composerIcon", "composerIconDark"):
    contained(interface[field])
for field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
    assert interface[field].startswith("https://www.leadbase.io")

print("Package valid: portable + Claude + Cursor, shared skills, matching MCP service and contained assets.")
