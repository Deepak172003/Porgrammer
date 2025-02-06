import json
from colorama import init, Fore, Style

init(autoreset=True)

def load_tasks(filename="to-do-list"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task, tasks):
    tasks.append(task)
    save_tasks(tasks)
    print(Fore.GREEN + f'Task "{task}" added successfully!')

def remove_task(index, tasks):
    try:
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(Fore.RED + f'Task "{removed_task}" removed successfully!')
    except IndexError:
        print(Fore.RED + "Invalid task number.")

def show_tasks(tasks):
    if not tasks:
        print(Fore.YELLOW + "No tasks available.")
    else:
        print(Fore.CYAN + "\nYour To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(Fore.CYAN + f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print(Fore.BLUE + "\nTo-Do List Menu:")
        print(Fore.BLUE + "1. Show tasks")
        print(Fore.BLUE + "2. Add task")
        print(Fore.BLUE + "3. Remove task")
        print(Fore.BLUE + "4. Exit")
        
        choice = input(Fore.BLUE + "Enter your choice: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            task = input(Fore.BLUE + "Enter task: ")
            add_task(task, tasks)
        elif choice == "3":
            show_tasks(tasks)
            try:
                index = int(input(Fore.BLUE + "Enter task number to remove: ")) - 1
                remove_task(index, tasks)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number.")
        elif choice == "4":
            print(Fore.GREEN + "Exiting... Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()