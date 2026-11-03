#!/usr/bin/env python3
"""Render a course's generated scenes to PNG."""
import argparse
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(HERE))))
RENDERER = os.path.join(ROOT, "tools", "renderer")


def main():
    parser = argparse.ArgumentParser(description="Render a course")
    parser.add_argument("slug", help="Course slug, e.g. software-developers-roadmap-to-excellence")
    parser.add_argument("--dark", action="store_true", help="Render dark mode")
    args = parser.parse_args()

    folder = os.path.join(ROOT, "generators", args.slug, "generated")
    if not os.path.isdir(folder):
        raise SystemExit(f"Generated folder not found: {folder}")

    cmd = ["node", "render_all.mjs", folder]
    env = os.environ.copy()
    if args.dark:
        env["DARK"] = "1"
    subprocess.run(cmd, cwd=RENDERER, env=env, check=True)


if __name__ == "__main__":
    main()
