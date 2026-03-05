
# Import validation functions
from task_manager import validation 

# Define tasks list
tasks = []

def add_task(title, description, due_date):
    try:
        validation.validate_task_title(title)
        validation.validate_task_description(description)
        dd = validation.validate_due_date(due_date)
    except ValueError as e:
        print(e) 
        return
    task = {"title": title, "description": description, "due_date": dd, "completed": False}
    tasks.append(task)
    print("Task added successfully!")
    
def mark_task_as_complete(index, tasks=tasks):
    try:
        idx = int(index)
    except ValueError:
        print("Invalid task ID.")
        return
    idx-=1 
    if idx >= len(tasks):
        print("No task at that index exists")
        return
    
    tasks[idx]["completed"] = True 
    print(f"Task marked as complete!")
    
def view_pending_tasks(tasks=tasks):
    pending_tasks = [task for task in tasks if task["completed"] == False]
    msg = "Pending Tasks:\n"
    for task in pending_tasks:
        msg += f"{task['title']} - {task['description']} - {task['due_date']}.\n"
    print(msg)
    

def calculate_progress(tasks=tasks):
    done = len([task for task in tasks if task["completed"] == True]) 
    total = len(tasks)
    progress = (done / total) * 100
    return progress 