#!/usr/bin/env python3
"""Scaffold a new course generator from templates."""
import argparse
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
TEMPLATE = os.path.join(ROOT, "templates", "course")


def slugify(value):
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def main():
    parser = argparse.ArgumentParser(description="Scaffold a new Excalidraw course")
    parser.add_argument("name", help="Display name for the course")
    args = parser.parse_args()

    slug = slugify(args.name)
    if not slug:
        raise SystemExit("Course name must contain letters or numbers")

    course_dir = os.path.join(ROOT, "generators", slug)
    if os.path.exists(course_dir):
        raise SystemExit(f"Course already exists: {course_dir}")

    shutil.copytree(TEMPLATE, course_dir)
    generate_path = os.path.join(course_dir, "generator", "generate.py")
    with open(generate_path, encoding="utf-8") as f:
        content = f.read()
    content = content.replace("{{COURSE_NAME}}", args.name)
    with open(generate_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created course: {slug}")
    print(f"Directory: {course_dir}")
    print("Next steps:")
    print(f"  python3 generators/{slug}/generator/generate.py")
    print(f"  python3 tools/render_course.py {slug}")


if __name__ == "__main__":
    main()
