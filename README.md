# to-do-list
That’s a great project idea! A console-based To-Do List Manager in Python will help you practice basic concepts like lists, functions, loops, and file handling. Let’s break it down step by step. I’ll guide you through each phase and explain the syntax along the way.

### Step 1: Plan the Features
Before we start coding, let's first think about the features you want for your To-Do List Manager. Here are some basic ones:
1. Add a task
2. View all tasks
3. Delete a task
4. Mark a task as complete
5. Save tasks to a file (so they persist between sessions)
6. Load tasks from a file on start

### Step 2: Set Up the Project Structure
Create a new folder on your computer to hold your project. Inside that folder, create a file called `todo_manager.py`.

### Step 3: Basic Structure of the Program
Let’s start by laying out the basic structure of our program. We’ll begin with creating a simple menu and a place to hold our tasks.

```python
# todo_manager.py

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

# Main function to control the program flow
def main():
    while True:
        show_menu()  # Display the menu
        choice = get_choice()  # Get user input

        if choice == "1":
            print("Adding task...")
        elif choice == "2":
            print("Viewing tasks...")
        elif choice == "3":
            print("Deleting task...")
        elif choice == "4":
            print("Marking task as complete...")
        elif choice == "5":
            print("Exiting the program...")
            break  # Exit the loop and terminate the program
        else:
            print("Invalid choice. Please choose between 1 and 5.")
        
if __name__ == "__main__":
    main()  # Run the main function
```

### Explanation:
- **`tasks = []`**: We start with an empty list to hold our tasks.
- **`show_menu()`**: This function prints out the menu options to the user.
- **`get_choice()`**: This function asks for the user’s input, capturing which option they want to choose.
- **`main()`**: This is the main loop of the program. It keeps displaying the menu and processing the user's choice until they choose to exit the program.

### Step 4: Adding a Task
Next, we’ll implement the functionality to add a task to our list.

1. We will ask the user for a task description.
2. Add the task to the `tasks` list.

```python
def add_task():
    task = input("Enter the task description: ")
    tasks.append(task)  # Add the task to the list
    print(f"Task added: {task}")
```

- **`input()`**: This function asks the user to type something. It returns the value as a string.
- **`append()`**: This method adds an item to the end of the list. In this case, it adds the task to the `tasks` list.

Now, modify the main loop to call the `add_task()` function when the user selects option 1:

```python
elif choice == "1":
    add_task()
```

### Step 5: Viewing Tasks
To display the tasks, we will iterate over the `tasks` list and print each task.

```python
def view_tasks():
    if tasks:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, 1):  # Starts numbering from 1
            print(f"{idx}. {task}")
    else:
        print("No tasks to display.")
```

- **`enumerate()`**: This function returns both the index (starting from 1 in this case) and the value of each item in the list.

Add the call to `view_tasks()` in the main loop for option 2:

```python
elif choice == "2":
    view_tasks()
```

### Step 6: Deleting a Task
Now, let’s add functionality to delete a task. We’ll ask the user for the task number they want to delete, and then remove it from the list.

```python
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
```

- **`pop()`**: This method removes and returns an item at the given index. We subtract 1 from `task_num` because lists are zero-indexed.
- **`try-except` block**: This is used to catch errors like if the user doesn’t enter a valid number.

Add the call to `delete_task()` in the main loop for option 3:

```python
elif choice == "3":
    delete_task()
```

### Step 7: Marking a Task as Complete
To mark a task as complete, we will append "(Completed)" to the task description.

```python
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
```

- We simply append the string `"(Completed)"` to the task description.

Add the call to `mark_task_complete()` in the main loop for option 4:

```python
elif choice == "4":
    mark_task_complete()
```

### Step 8: Saving and Loading Tasks to/from a File
We want our tasks to be saved even after the program closes. Let’s save them to a file when the program exits, and load them back when the program starts.

```python
import os

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")
```

- **`os.path.exists()`**: Checks if the file `tasks.txt` exists.
- **`open()`**: Used to open a file. `"r"` means reading, and `"w"` means writing.
- **`readlines()`**: Reads all the lines from the file.
- **`strip()`**: Removes any leading/trailing whitespace or newline characters.

Call `load_tasks()` at the start of the program to load tasks from the file, and call `save_tasks()` before exiting:

```python
def main():
    global tasks
    tasks = load_tasks()  # Load tasks from file at the beginning

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
            save_tasks()  # Save tasks before exiting
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please choose between 1 and 5.")
```

### Final Program Structure
Here’s how the full code will look:

```python
import os

tasks = []

def show_menu():
    print("\nTo-Do List Manager")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Mark task as complete")
    print("5. Exit")

def get_choice():
    choice = input("Choose an option (1-5): ")
    return choice

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = input("Enter the task description: ")
    tasks.append(task)
    print(f"Task added: {task}")

def view_tasks():
    if tasks:
        print("\nYour tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks to display.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' has been deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_complete():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] += " (Completed)"
            print(f"Task {task_num} marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

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
    main()
```

### Final Thoughts
Now you have a fully functional To-Do List Manager in Python! You can:
- Add tasks
- View tasks
- Delete tasks
- Mark tasks as complete
- Save and load tasks from a file

You can improve it further by adding features like sorting tasks, prioritizing tasks, or adding deadlines. 

Is there anything you’d like to add or change?
