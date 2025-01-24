import os

# List to store tasks
tasks = []

# Function to show the main menu
def show_menu():
    print("\nTo-Do List Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task as complete")
    print("5. Exit")

# Function to get the user choice
def get_choice():
    choice = input("Choose an option (1-5): ")
    return choice

def add_task():
    task = input("Enter the task description: ")
    tasks.append(task)  # Add the task to the list
    print(f"Task added: {task}")

def view_tasks():
    if tasks:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, 1):  # Starts numbering from 1
            print(f"{idx}. {task}")
    else:
        print("No tasks to display.")

def delete_task():
    view_tasks()  # Show the tasks before deleting
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)  # Remove the task
            print(f"Task '{removed_task}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_complete():
    view_tasks()  # Show the tasks before marking
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] += " (Completed)"
            print(f"Task {task_num} marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")



# Main function to control the program flow
def main():
    global tasks
    tasks = load_tasks()

    while True:
        show_menu()
        choice = get_choice()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_complete()
        elif choice == "5":
            save_tasks()
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose between 1 and 5.")
        
if __name__ == "__main__":
    main()  # Run the main function
