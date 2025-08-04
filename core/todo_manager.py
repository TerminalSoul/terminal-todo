import json
import os
from datetime import datetime


def get_user_todo_file(username):
    dir_path = "data"
    os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, f"todo_{username}")

    # If the file doesn't exist, create it with an empty list
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)  # Write empty JSON list

    return file_path


def load_todo(username):
    FILE_TODO = get_user_todo_file(username)
    with open(FILE_TODO, "r") as f:
        return json.load(f)


def save_todos(todos, username):
    FILE_TODO = get_user_todo_file(username)
    with open(FILE_TODO, "w") as f:
        json.dump(todos, f, indent=2)


def add_task(username, task):
    todo_file = load_todo(username)
    new_id = max([todo["id"] for todo in todo_file], default=0) + 1

    todo_file.append(
        {
            "id": new_id,
            "task": task,
            "done": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        }
    )
    save_todos(todo_file, username)
    print(f"✅ Added task #{new_id}: {task}")


def list_task(username):
    todo_file = load_todo(username)

    if not todo_file:
        print("📭 No tasks found.")
        return
    for todo in todo_file:
        status = "✅" if todo["done"] else "❌"
        print(f"{todo['id']}. {status} {todo['task']} (created: {todo['created_at']})")


def update_task(username, task_id, new_task):
    todo_file = load_todo(username)
    for todo in todo_file:
        if todo["id"] == task_id:
            todo["task"] = new_task
            save_todos(todo_file, username)
            print(f"✏️ Updated task #{task_id}")
            return
    print(f"⚠️ Task #{task_id} not found.")


def delete_task(username, task_id):
    todo_file = load_todo(username)
    new_todo = [todo for todo in todo_file if todo["id"] != task_id]

    if len(todo_file) == len(new_todo):
        print(f"⚠️ Task #{task_id} not found.")
    else:
        save_todos(new_todo, username)
        print(f"🗑️ Deleted task #{task_id}")


def complete_task(username, task_id):
    todo_file = load_todo(username)
    for todo in todo_file:
        if todo["id"] == task_id:
            if not todo["done"]:
                todo["done"] = True
                print(f"✅ Completed task #{task_id}")
            else:
                print("Task already completed")
    save_todos(todo_file, username)


def close_shell():
    exit(1)
