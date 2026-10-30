from task_tracker.task_service import (
    load_tasks,
    add_task,
    view_tasks,
    complete_task,
    delete_task
)


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TASK TRACKER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            delete_task(tasks)

        elif choice == "5":
            print("Thank you for using Task Tracker!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()