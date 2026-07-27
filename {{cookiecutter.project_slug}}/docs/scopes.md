# Scopes

{{ cookiecutter.project_name }} splits its permission checks into **scopes**: named checkpoints passed to `@panel_config.permission_required(scope)` (for views) and `scope=` (for panel tools, in `tools.py`). Every scope inherits the panel-wide `ALLOWED_GROUPS`/`REQUIRE_SUPERUSER` rule by default; a scope only behaves differently once you add an entry for it under `SCOPE_PERMISSIONS` in `{{ cookiecutter.package_name|upper }}_SETTINGS`.

Both views and tools are enforced through the **exact same mechanism**: the same `SCOPE_PERMISSIONS` dict, the same `ALLOWED_GROUPS`/`REQUIRE_SUPERUSER` keys, the same resolution order. There is no separate permission system for AI agents. See the [Permissions and Scopes guide](https://djangocontrolroom.com/guides/control-room-permissions-and-scopes) for the full model.

## Design: separate scopes per actor type

Give **humans (admin UI views)** and **AI agents (MCP tools)** distinct scopes, even where a tool surfaces the same underlying data as a view. This lets you grant staff full browsing access in the admin while denying (or separately restricting) automated/agent access to the same data, or vice versa, without one setting accidentally controlling both. In practice this means:

- Name view scopes after what they protect, e.g. `widget_list`, `widget_detail`.
- Name tool scopes the same way, but prefixed with `agent_`, e.g. `agent_widget_list`.

## Scaffolded scopes

This template ships two example scopes out of the box. Rename them (and add more) as you build out your panel:

| Scope | Type | Protects | Default behavior |
|---|---|---|---|
| `index` | View | `index` view (`views.py`) | Any staff user |
| `agent_hello_world` | Tool | `hello_world` MCP tool (`tools.py`) | Any staff user the MCP endpoint authenticates as |

## Example: independent human vs. agent access

```python
{{ cookiecutter.package_name|upper }}_SETTINGS = {
    # Panel-wide default: any staff member can browse the admin UI
    'ALLOWED_GROUPS': [],

    'SCOPE_PERMISSIONS': {
        # Restrict a single tool to a dedicated group, even though staff
        # can access the equivalent admin view freely.
        'agent_hello_world': {'ALLOWED_GROUPS': ['ai-agents-readonly']},
    },
}
```

Any scope not mentioned in `SCOPE_PERMISSIONS` simply falls back to the panel-wide rule, so you only ever need to write down the exceptions.

See [Configuration](configuration.md#panel-tools-mcp) for the rest of the panel's settings, including what each MCP tool does.
