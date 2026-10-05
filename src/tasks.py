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

def task_statistics(args):
    tasks = load_tasks()

    if not tasks:
        print("No tasks available")
        return 

    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    incomplete_tasks = total_tasks - completed_tasks

    completion_rate = (completed_tasks / total_tasks) * 100

    priority_count = {}

    for task in tasks:
        priority = task["priority"]

        if priority in priority_count:
            priority_count[priority] += 1
        else:
            priority_count[priority] = 1

    print("Task Statistics")
    print("----------------")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed: {completed_tasks}")
    print(f"Incomplete: {incomplete_tasks}")
    print(f"Completion rate: {completion_rate:.1f}%")

    print("\nTasks by priority:")
    for priority, amount in priority_count.items():
        print(f"{priority}: {amount}")



def sort_tasks(args):
    tasks = load_tasks()

    tasks.sort(key=lambda task: task["due_date"])
