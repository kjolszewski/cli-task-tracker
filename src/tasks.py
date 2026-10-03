# create task, find task, update task, delete task, complete task, search task and calculate statistics
# task contains "ID", task, priority, due date, status
from storage import load_tasks, save_tasks 
from display import show_tasks

def add_task(args):
    tasks = load_tasks()

    task = {
        "id": max([task["id"] for task in tasks], default=0) + 1,
        "title": args.title,
        "priority": args.priority,
        "due_date": args.due_date,
        "completed": False
    }

    for task in tasks:
        if task["title"] == args.title and task["due_date"] == args.due_date:
            print("A task of the same title and due date already exists")
            return 

    tasks.append(task)
    save_tasks(tasks)

    print("Task added")

def delete_task(args):
    tasks = load_tasks()

    for task in tasks:
        if task["title"] == args.title:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted")
            return 

    print("Task not found")

def list_tasks(args):
    tasks = load_tasks()

    if not tasks:
        print("No task found")
        return 

    for task in tasks:
        show_tasks(task)

def complete_task(args):
    tasks = load_tasks()

    for task in tasks:
        if task["title"] == args.title:
            task["completed"] = True
            print("Task marked as complete")
            return 

    print("Task not found")

def search_task(args):
    tasks = load_tasks()

    for task in tasks:
        if task["title"] == args.title:
            print(f"Task has been found. It has a completion status of {task["completed"]}, a due date of {task["due_date"]} and a priority of {task["priority"]}.")
        return 

    print("No task found") 

def display_tasks(args):
    print(f"Displaying tasks...")
