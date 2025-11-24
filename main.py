# main.py
from todo import TodoManager

def main():
    manager = TodoManager()
    manager.load_tasks()

    while True:
        print("\n" + "="*40)
        print("   SMART TODO LIST")
        print("="*40)
        print("1. Add Task    2. View Tasks   3. Complete Task")
        print("4. Delete Task 5. Edit Task    6. Save & Exit")
        choice = input("\nChoose an option (1-6): ").strip()

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            manager.complete_task()
        elif choice == "4":
            manager.delete_task()
        elif choice == "5":
            manager.edit_task()
        elif choice == "6":
            manager.save_tasks()
            print("Goodbye! Tasks saved.")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
