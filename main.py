from core.arg_parser import args_parser
from core.auth_manager import login_or_register
from core.todo_manager import (
    add_task,
    complete_task,
    delete_task,
    list_task,
    update_task,
)
from core.todo_shell import Todo_shell


def main():
    username = login_or_register()
    args = args_parser()
    if args.command:
        if args.command == "add":
            add_task(username, args.task)
        elif args.command == "list":
            list_task(username)
        elif args.command == "update":
            update_task(username, args.id, args.new_task)
        elif args.command == "done":
            complete_task(username, args.id)
        elif args.command == "del":
            delete_task(username, args.id)
    else:
        Todo_shell(username).cmdloop()


if __name__ == "__main__":
    main()
