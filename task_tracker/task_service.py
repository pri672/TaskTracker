import json
import os

FILE_PATH = "data/tasks.json"


def load_tasks():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(FILE_PATH, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    task_name = input("Enter your task: ")

    task = {
        "name": task_name,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(i, ".", task["name"], "-", status)


def complete_task(tasks):
    if not tasks:
        print("No tasks to complete.")
        return

    for i, task in enumerate(tasks, start=1):
        print(i, ".", task["name"])

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return

    for i, task in enumerate(tasks, start=1):
        print(i, ".", task["name"])

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            deleted_task = tasks.pop(number - 1)
            save_tasks(tasks)
            print("Deleted task:", deleted_task["name"])
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")