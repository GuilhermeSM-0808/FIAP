import os

## Simple version, remove and add one item at an time

tasks = []

def menu():
    os.system('cls')
    print("Tasks Menu:\n1. Add Task\n2. View Tasks\n3. Remove Task\n4. Leave")
    choice = input("Choose an option: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        leave()
    else:
        invalid_input()
    
def add_task():
    os.system('cls')
    new_task = input("Insert the task you would to add to the list: ")
    tasks.append(new_task)
    print("Task added!")
    
    return_menu()
    
def view_tasks():
    os.system('cls')
    print("Task list:")
    for n in range(len(tasks)):
        print(f"{n+1}. {tasks[n]}")
    
    return_menu()
    
def remove_task():
    os.system('cls')
    remove = input("Insert the task you would like to remove: ")
    if remove in tasks:
        tasks.remove(remove)
        print("Task removed!")
        return_menu()
    else:
        print("Task not found.")
        return_menu()
    
def leave():
    os.system('cls')
    print("Leaving app...")
    input("\nPress enter to continue.")
    os.system('cls')
    
def return_menu():
    input("\nPress enter to continue.")
    menu()
    
def invalid_input():
    os.system('cls')
    print("Error: Invalid input.")
    return_menu()

menu()