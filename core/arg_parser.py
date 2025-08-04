import argparse


def args_parser():
    parser = argparse.ArgumentParser(description="simple CLI-based todo app")
    subparsers = parser.add_subparsers(dest="command")

    # Add task
    add_parser = subparsers.add_parser("add", help="add a new todo")
    add_parser.add_argument("task", type=str, help="description of task")

    # List tasks
    subparsers.add_parser("list", help="list all the tasks")

    # Delete task
    delete_parser = subparsers.add_parser("del", help="delete a task")
    delete_parser.add_argument("id", type=int, help="task ID to delete")

    # Update task
    update_parser = subparsers.add_parser("update", help="update a task")
    update_parser.add_argument("id", type=int, help="task ID to update")
    update_parser.add_argument("new_task", type=str, help="new task description")

    # Mark task as done
    complete_parser = subparsers.add_parser("done", help="mark a task as done")
    complete_parser.add_argument("id", type=int, help="task ID to mark as done")

    return parser.parse_args()
