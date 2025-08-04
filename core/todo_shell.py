import cmd

from core.todo_manager import (
    add_task,
    close_shell,
    complete_task,
    delete_task,
    list_task,
    update_task,
)


class Todo_shell(cmd.Cmd):
    intro = (
        "📋 Welcome to Terminal.todo!\n"
        "Type 'help' to see available commands.\n"
        "Use commands like: add, list, done, del, update, bye"
    )
    prompt = "terminal_todo> "

    def __init__(self, username):
        super().__init__()
        self.username = username

    def do_add(self, arg):
        """
        add <task>

        ➕ Add a new task.
        Example:
            add Buy groceries
        """
        add_task(self.username, arg)

    def do_done(self, arg):
        """
        done <id>

        ✅ Mark a task as completed.
        Example:
            done 2
        """
        if not arg.isdigit():
            print("❗ Please provide a valid task ID.")
            return
        task_id = int(arg)
        complete_task(self.username, task_id)

    def do_update(self, arg):
        """
        update <id> <new_task>

        ✏️ Update an existing task with a new description.
        Example:
            update 3 Walk the dog at night
        """
        parts = arg.split(maxsplit=1)
        if not len(parts) == 2 or not parts[0].isdigit():
            print("❗ Usage: update <id> <new_task>")
            return
        task_id = int(parts[0])
        new_task = parts[1]
        update_task(self.username, task_id, new_task)

    def do_del(self, arg):
        """
        del <id>

        🗑️ Delete a task by its ID.
        Example:
            del 1
        """
        if not arg.isdigit():
            print("❗ Please provide a valid task ID.")
            return
        task_id = int(arg)
        delete_task(self.username, task_id)

    def do_list(self, arg):
        """
        list

        📋 Show all tasks with their status (done or not).
        Example:
            list
        """
        list_task(self.username)

    def do_bye(self, arg):
        """
        bye

        👋 Exit the Terminal.todo shell.
        Example:
            bye
        """
        print("Thank you for using Terminal.todo. Goodbye! 👋")
        close_shell()
