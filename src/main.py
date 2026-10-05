# starts program, parses command, calls appropriate functionality and displays results
import requests, argparse
from datetime import datetime, date
from display import show_tasks
from storage import load_tasks, save_tasks
from tasks import add_task, delete_task, complete_task, search_task, list_tasks, task_statistics, sort_tasks

# validation
def valid_date(value):
    try:
        parsed = datetime.strptime(value, "%d/%m/%Y").date()
    except ValueError:
        raise argparse.ArgumentTypeError(
            "Date must be in DD/MM/YYYY format"
        )

    if parsed < date.today():
        raise argparse.ArgumentTypeError(
            "Date must be today or later"
        )

    return value
 
# main
def main():
    parser = argparse.ArgumentParser(description="CLI Task Tracker")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    add_parser.add_argument(
        "priority", 
        type=str.capitalize,
        choices=["Low", "Medium", "High"], 
        )
    add_parser.add_argument(
        "due_date",
        type=valid_date
        )
    add_parser.set_defaults(func=add_task)

    # list
    list_parser = subparsers.add_parser("list")
    list_parser.set_defaults(func=list_tasks)

    # complete
    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("id", help="mark a task as complete through its id", type=int)
    complete_parser.set_defaults(func=complete_task)

    # delete
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", help="delete a task through its id", type=int) 
    delete_parser.set_defaults(func=delete_task)

    # search
    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("title", help="search for a task by its title")
    search_parser.set_defaults(func=search_task)

    # statistics
    stats_parser = subparsers.add_parser("stats")
    stats_parser.set_defaults(func=task_statistics)

    # sort
    sort_parser = subparsers.add_parser("sort")
    sort_parser.set_defaults(func=sort_tasks)

    args = parser.parse_args()
    args.func(args)

# show_tasks(tasks)

if __name__ == "__main__":
    main()