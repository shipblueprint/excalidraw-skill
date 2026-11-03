# Excalidraw Asset Pipeline

OpenCode skill and tooling for branded Excalidraw diagrams: scaffold a course, author scenes with the shared kit, render PNGs, and build libraries.

![Example render](docs/screenshot.png)

## TL;DR

- Scaffold a course: `python3 tools/new_course.py "Course Name"`
- Generate scenes: `python3 generators/<slug>/generator/generate.py`
- Render PNGs: `python3 tools/render_course.py <slug>`
- Build master library: `python3 tools/library_builder/builder.py`
- Install skill: `bash tools/install_skill.sh`

## Skill

Skill location: `.opencode/skills/excalidraw-asset-pipeline/SKILL.md`

Use it to scaffold courses, generate branded starter scenes, and render output without hardcoding paths.

## Commands

- `make new NAME="Course Name"`
- `make render SLUG=course-slug`
- `make build`
- `make validate`
- `make test`
- `make install-skill`

## Layout

- `generators/<slug>/` - course generators
- `generators/common/` - shared drawing kit and brand tokens
- `templates/course/` - scaffold template
- `tools/` - renderer, library builder, brand tools
- `assets/` - classified files and libraries

## Generated output

Generated scenes and PNGs are ignored by Git. Regenerate them from the course generators and shared kit.
