import unittest
import tempfile
import os

from unittest.mock import patch
from task_tracker.task_service import load_tasks, save_tasks


class TestTaskTracker(unittest.TestCase):

    def test_save_and_load_tasks(self):
        tasks = [
            {
                "name": "Study Python",
                "completed": False
            }
        ]

        with tempfile.TemporaryDirectory() as folder:
            file_path = os.path.join(folder, "tasks.json")

            with patch("task_tracker.task_service.FILE_PATH", file_path):
                save_tasks(tasks)
                loaded_tasks = load_tasks()

                self.assertEqual(loaded_tasks, tasks)


if __name__ == "__main__":
    unittest.main()