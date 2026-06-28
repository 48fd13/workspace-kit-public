# Active Runs

Current in-progress runs.

Folder name:

```text
YYYY-MM-DD-topic-slug/
```

Workflow run shape:

```text
YYYY-MM-DD-topic-slug/
├── RUN.md
├── input/
├── output/
└── final/
```

Pipeline run shape:

```text
YYYY-MM-DD-topic-slug/
├── RUN.md
├── input/
├── stages/
│   ├── 00_stage-name.md
│   └── 01_stage-name.md
└── final/
```

Use `output/` for one-pass workflow working output. Use `stages/` for pipeline stage handoffs.

Ask before moving or clearing active run folders.
