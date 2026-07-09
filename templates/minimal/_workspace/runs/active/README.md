# Active Runs

Active runs plus finished runs awaiting explicit archive.

Folder name:

```text
YYYY-MM-DD-topic-slug/
```

Standalone task or workflow run shape:

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
└── final/
```

Keep status `active` through drafting and review. Explicit finish creates run-final content plus a durable workspace output and sets status to `finished`. Ask before archiving, moving, or clearing run folders.
