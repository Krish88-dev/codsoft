todo_list = []  

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("Task added successfully.")

def view_tasks():
    if not todo_list:
        print("Your task list is empty.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to update: "))
        if 1 <= task_no <= len(todo_list):
            new_task = input("Enter updated task: ")
            todo_list[task_no - 1] = new_task
            print("Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        if 1 <= task_no <= len(todo_list):
            del todo_list[task_no - 1]
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        update_task()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Exiting... Have a great day!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
