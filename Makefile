.PHONY: new render test install-skill

new:
	python3 .opencode/skills/excalidraw-asset-pipeline/scripts/new_course.py "$(NAME)"

render:
	python3 .opencode/skills/excalidraw-asset-pipeline/scripts/render_course.py "$(SLUG)"

test:
	python3 -m unittest tests.test_scaffold

install-skill:
	bash .opencode/skills/excalidraw-asset-pipeline/scripts/install_skill.sh
