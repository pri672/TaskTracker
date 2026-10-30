Task Tracker

Project Description

Task Tracker is a simple Python project used to manage daily tasks.

Users can add tasks, view tasks, mark tasks as completed, and delete tasks.

Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Save tasks in a JSON file

Technologies Used

* Python
* JSON
* Visual Studio Code
* Git and GitHub

Project Structure

TaskTracker/
│
├── main.py
├── README.md
├── .gitignore
│
├── task_tracker/
│   ├── __init__.py
│   └── task_service.py
│
├── data/
│   └── tasks.json
│
└── tests/
    └── test_task_tracker.py

Setup Instructions

1. Install Python on your computer.
2. Download or clone this project from GitHub.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

python3 main.py

How to Use

1. Run the program.
2. Select an option from the menu.
3. Enter a task name to add a new task.
4. View your tasks.
5. Select a task number to mark it as completed.
6. Select a task number to delete it.
7. Select Exit to close the program.

Example

===== TASK TRACKER =====
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

Testing

Run the following command to test the project:

python3 -m unittest discover -s tests -v

Author

Prity