# create task, find task, update task, delete task, complete task, search task and calculate statistics
# task contains "ID", task, priority, due date, status
from storage import load_tasks, save_tasks 
from display import show_tasks

def add_task(args):
    tasks = load_tasks()

    new_task = {
        "id": len(tasks) + 1,
        "title": args.title,
        "priority": args.priority,
        "due_date": args.due_date,
        "completed": False
    }

    for existing_task in tasks:
        if new_task["title"] == existing_task["title"] and new_task["due_date"] == existing_task["title"]:
            print("A task of the same title and due date already exists")
            return 

    tasks.append(new_task)
    save_tasks(tasks)

    print("Task added")

def delete_task(args):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == args.id:
            tasks.remove(task)
            save_tasks(tasks)
            print("Task deleted")
            return 

    print("Task not found")

def list_tasks(args):
    tasks = load_tasks()

    show_tasks(tasks)

def complete_task(args):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == args.id:
            task["completed"] = True
            save_tasks(tasks)
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
