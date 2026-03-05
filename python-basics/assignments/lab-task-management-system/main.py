# Import functions from task_manager.task_utils package

from task_manager import task_utils 

# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date as 'YYYY-MM-dd': ")
            task_utils.add_task(title, description, due_date)
        elif choice == "2":
            ids = [i+1 for i,task in enumerate(task_utils.tasks) if task["completed"] == False]
            idx = input(f"Enter the task id to mark as complete. Task IDs->{ids}: ")
            task_utils.mark_task_as_complete(idx)
        elif choice == "3":
            task_utils.view_pending_tasks()
        elif choice == "4":
            progress = task_utils.calculate_progress()
            print(progress)
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    main()
