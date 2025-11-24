# todo.py
import json
import os
from datetime import datetime

class TodoManager:
    def __init__(self, filename="data/tasks.json"):
        self.filename = filename
        self.tasks = []
        os.makedirs(os.path.dirname(filename), exist_ok=True) if filename.count("/") else None

    def add_task(self):
        title = input("Task title: ").strip()
        if not title:
            print("Title cannot be empty!")
            return

        priority = input("Priority (high/medium/low) [medium]: ").strip().lower() or "medium"
        if priority not in ["high", "medium", "low"]:
            priority = "medium"

        due = input("Due date (YYYY-MM-DD) or leave blank: ").strip()
        try:
            if due:
                datetime.strptime(due, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format! Using no due date.")
            due = None

        category = input("Category (work/personal/study/etc) [personal]: ").strip() or "personal"

        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "due_date": due,
            "category": category,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks yet! Add one.")
            return

        print("\nYour Tasks:")
        print("-" * 80)
        for t in self.tasks:
            status = "✓" if t["completed"] else " "
            due = f" | Due: {t['due_date']}" if t['due_date'] else ""
            print(f"[{status}] {t['id']}. {t['title']} | {t['priority'].upper()} | {t['category']}{due}")
        print("-" * 80)

    def complete_task(self):
        self.view_tasks()
        try:
            task_id = int(input("Enter task ID to mark complete: "))
            for t in self.tasks:
                if t["id"] == task_id:
                    t["completed"] = True
                    print(f"Task {task_id} marked as complete!")
                    return
            print("Task not found.")
        except:
            print("Invalid input.")

    def delete_task(self):
        self.view_tasks()
        try:
            task_id = int(input("Enter task ID to delete: "))
            self.tasks = [t for t in self.tasks if t["id"] != task_id]
            # Re-assign IDs
            for i, t in enumerate(self.tasks, 1):
                t["id"] = i
            print("Task deleted.")
        except:
            print("Invalid input.")

    def edit_task(self):
        self.view_tasks()
        try:
            task_id = int(input("Enter task ID to edit: "))
            task = next((t for t in self.tasks if t["id"] == task_id), None)
            if not task:
                print("Task not found.")
                return

            print(f"Editing: {task['title']}")
            title = input(f"New title [{task['title']}]: ").strip()
            if title:
                task['title'] = title

            priority = input(f"New priority (high/medium/low) [{task['priority']}]: ").strip()
            if priority in ["high", "medium", "low"]:
                task['priority'] = priority

            due = input(f"New due date (YYYY-MM-DD) [{task['due_date'] or 'none'}]: ").strip()
            if due:
                try:
                    datetime.strptime(due, "%Y-%m-%d")
                    task['due_date'] = due
                except:
                    print("Invalid date, keeping old.")
            elif due == "":
                task['due_date'] = None

            print("Task updated!")
        except:
            print("Invalid input.")

    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as f:
                    self.tasks = json.load(f)
            except:
                print("Could not load tasks. Starting fresh.")
