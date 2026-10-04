from tabulate import tabulate 

def show_tasks(tasks):
    rows = [
        [
            task["id"],
            task["title"],
            task["priority"],
            task["due_date"],
            "Complete" if task["completed"] else "Incomplete"
        ]
        for task in tasks 
    ]

    print(tabulate(
        rows,
        headers = ["ID", "Task", "Priority", "Due Date", "Status"]
    ))

    