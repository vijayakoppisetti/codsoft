# main.py
from todo_list import TodoList

def main():
    todo_list = TodoList()
    todo_list.load_tasks('tasks.txt')

    while True:
        print("\n===== To-Do List Application =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            tasks = todo_list.list_tasks()
            print("\n--- Tasks ---")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
        elif choice == '3':
            task_index = int(input("Enter task index to update: ")) - 1
            updated_task = input("Enter updated task: ")
            todo_list.update_task(task_index, updated_task)
        elif choice == '4':
            task_index = int(input("Enter task index to delete: ")) - 1
            todo_list.remove_task(task_index)
        elif choice == '5':
            todo_list.save_tasks('tasks.txt')
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
