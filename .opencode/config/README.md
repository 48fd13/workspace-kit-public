# OpenCode generated config

`.opencode/opencode.json` is the generated runtime config used by OpenCode. Do not hand-edit permission maps there.

Edit the source files in this directory instead:

- `base.json` stores the non-generated OpenCode config.
- `permissions/*.json` stores reusable bash permission fragments and per-agent profile assignments.

After editing source config or permissions, regenerate the runtime config:

```sh
python3 .opencode/scripts/build-config.py
```

Then run `python3 verify-opencode-setup.py` to catch stale generated config and effective permission regressions.
