---
name: excalidraw-asset-pipeline
description: Generate, render, and organize Excalidraw diagrams and asset libraries. Use when creating course diagrams, rendering scenes to PNG, building master libraries, or scaffolding a new course.
---

# Excalidraw Asset Pipeline

## Use this skill when

- The user wants to create or edit Excalidraw diagram generators.
- The user wants to render `.excalidraw` scenes to PNG.
- The user wants to build or audit Excalidraw libraries.
- The user wants to scaffold a new course from the existing pattern.

## Repository layout

- `generators/<slug>/generated/` - generated `.excalidraw` scenes
- `generators/common/` - shared drawing kit, tokens, and styles
- `assets/` - classified files and libraries
- `tools/renderer/` - light/dark PNG renderer
- `tools/library_builder/` - normalizer, classifier, builder
- `tools/brand/` - brand validation and audit

## Course slugs

Course directories use URL-safe slugs. Display names stay in file content and metadata.

Examples:
- `building-agents-that-never-sleep`
- `cloud-computing-101-master-the-fundamentals`
- `designing-modern-web-scale-distributed-services`
- `software-developers-roadmap-to-excellence`
- `web-application-software-architecture-101`

## Common commands

Render a course:

```sh
cd tools/renderer
node render_all.mjs "../../generators/<slug>/generated"
```

Build master library:

```sh
python3 tools/library_builder/builder.py
```

Validate brand tokens:

```sh
python3 tools/brand/validate.py
```

Run tests:

```sh
python3 -m unittest tests.test_library_builder
```

## Generating a full course from a summary

When the user provides a course summary or list of prompts:

1. Scaffold the course with `tools/new_course.py`.
2. Create one scene module per topic in `generator/`.
3. Use `from ekit import *` and brand tokens for every element.
4. Save each scene with a numbered, descriptive filename.
5. Render the course with `tools/render_course.py`.

Do not hand-edit generated `.excalidraw` files.

## Generation pattern

Each course has:

- `generator/generate.py` or scene modules
- `generator/ekit.py` shim importing `generators/common`
- `generated/*.excalidraw`

Always build scenes with the shared kit:

```python
from ekit import *
new()
title("Course Title", 60, 40)
box(60, 140, 220, 90, "Concept")
save("001 Scene Name")
```

Use `BG`, `INK`, `ACC`, `CON`, `BDR`, and other tokens from `generators/common/tokens.py`. Do not hardcode colors or raw Excalidraw JSON unless necessary.

## Safety

- Do not commit generated PNGs unless requested.
- Do not modify `assets/libraries/master.index.json` by hand; regenerate or script updates.
- Keep `.codegraph/` untracked.
