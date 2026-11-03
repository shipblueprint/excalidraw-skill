# Excalidraw Asset Pipeline

## Structure

- `assets/classified/` - topic folders of individual Excalidraw files
- `assets/libraries/by-topic/` - topic-grouped Excalidraw libraries
- `assets/` - legacy libs, brand-recolor libs, all-in-one library
- `docs/` - spec and animation guidelines
- `generators/` - course and hand-drawn diagram generators
- `tests/` - tests
- `tools/brand/` - brand tokens, validation, audit, recolor
- `tools/library_builder/` - normalizer, classifier, builder
- `tools/renderer/` - unified light/dark PNG renderer

## Commands

- Validate brand tokens: `python3 tools/brand/validate.py`
- Build master library: `python3 tools/library_builder/builder.py`
- Render scenes: `cd tools/renderer && node render_all.mjs "../../generators/Software Developers Roadmap to Excellence/generated"`
- Run tests: `python3 -m unittest tests.test_library_builder`
- Audit libs: `python3 tools/brand/audit_libs.py`
- Recolor libs: `python3 tools/brand/recolor_libs.py`
