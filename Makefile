.PHONY: new render build validate test install-skill

new:
	python3 tools/new_course.py "$(NAME)"

render:
	python3 tools/render_course.py "$(SLUG)"

build:
	python3 tools/library_builder/builder.py

validate:
	python3 tools/brand/validate.py

test:
	python3 -m unittest tests.test_library_builder

install-skill:
	bash tools/install_skill.sh
