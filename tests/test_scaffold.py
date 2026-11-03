import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "zz-scaffold-test-course"


class ScaffoldTests(unittest.TestCase):
    def tearDown(self):
        course_dir = os.path.join(ROOT, "generators", SLUG)
        if os.path.exists(course_dir):
            import shutil
            shutil.rmtree(course_dir)

    def test_new_course_creates_expected_files(self):
        subprocess.run(
            [sys.executable, ".opencode/skills/excalidraw-asset-pipeline/scripts/new_course.py", "ZZ Scaffold Test Course"],
            cwd=ROOT,
            check=True,
        )
        # The slug is deterministic for this name.
        course_dir = os.path.join(ROOT, "generators", "zz-scaffold-test-course")
        self.assertTrue(os.path.isdir(course_dir))
        self.assertTrue(os.path.isfile(os.path.join(course_dir, "generator", "generate.py")))
        self.assertTrue(os.path.isdir(os.path.join(course_dir, "generated")))


if __name__ == "__main__":
    unittest.main()
