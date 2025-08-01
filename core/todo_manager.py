import json
import os
from datetime import datetime

FILE_TODO = "../todo.json"


def load_todo():
    if not os.path.exists(FILE_TODO):
        return []
    with open(FILE_TODO, "r") as f:
        return json.load(f)


def save_todos(todos):
    with open(FILE_TODO, "w") as f:
        json.dump(todos, f, indent=2)


def add_task(task):
    todo_file = load_todo()
    new_id = max([todo["id"] for todo in todo_file], default=0) + 1

    todo_file.append(
        {
            "id": new_id,
            "task": task,
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
    )
    save_todos(todo_file)
    print(f"✅ Added task #{new_id}: {task}")


def list_task():
    todo_file = load_todo()

    if not todo_file:
        print("📭 No tasks found.")
        return
    for todo in todo_file:
        status = "✅" if todo["done"] else "❌"
        print(f"{todo['id']}. {status} {todo['task']} (created: {todo['created_at']})")


def update_task(task_id, new_task):
    todo_file = load_todo()
    for todo in todo_file:
        if todo["id"] == task_id:
            todo["task"] = new_task
            save_todos(todo_file)
            print(f"✏️ Updated task #{task_id}")
            return
    print(f"⚠️ Task #{task_id} not found.")


def delete_task(task_id):
    todo_file = load_todo()
    new_todo = [todo for todo in todo_file if todo["id"] != task_id]

    if len(todo_file) == len(new_todo):
        print(f"⚠️ Task #{task_id} not found.")
    else:
        save_todos(new_todo)
        print(f"🗑️ Deleted task #{task_id}")


def complete_task(task_id):
    todo_file = load_todo()
    for todo in todo_file:
        if todo["id"] == task_id:
            if not todo["done"]:
                todo["done"] = True
                print(f"✅ Completed task #{task_id}")
            else:
                print("Task already completed")
    save_todos(todo_file)
