tasks = []

while True:
    print("\n===== TASK TRACKER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task_name = input("Enter your task: ")
        task = {"name": task_name, "completed": False}
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(i, ".", task["name"], "-", status)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to complete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task["name"])

            try:
                number = int(input("Enter task number to complete: "))
                if 1 <= number <= len(tasks):
                    tasks[number - 1]["completed"] = True
                    print("Task marked as completed!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, ".", task["name"])

            try:
                number = int(input("Enter task number to delete: "))
                if 1 <= number <= len(tasks):
                    deleted_task = tasks.pop(number - 1)
                    print("Deleted task:", deleted_task["name"])
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a number.")

    elif choice == "5":
        print("Thank you for using Task Tracker!")
        break

    else:
        print("Invalid option")