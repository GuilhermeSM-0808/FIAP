import os

## Complete version, able to add multiple tasks in a row

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
    try:
        amount = int(input("Insert the amount of tasks you would like to add: "))
        if amount == 1:
            new_task = input("Insert the name of the task you would to add to the list: ")
            tasks.append(new_task)
            print("Task added!")
            return return_menu()
        elif amount > 1:
            for i in range(amount):
                new_task = input(f"Insert the name of task N°{i+1}: ")
                tasks.append(new_task)
                print("Task added.")
            print("All Tasks added.")
            return return_menu()
        else:
            print("Invalid input. Insert a number equal or greater than 1.")
            input("Press enter to try again.")
            return add_task()
    except ValueError:
        print("Invalid input. Insert numbers only.")    
        return_menu()
    
def view_tasks():
    os.system('cls')
    if tasks:
        print("Task list:")
        for n in range(len(tasks)):
            print(f"{n+1}. {tasks[n]}")
    else:
        print("The list is empty...")
    
    return_menu()
    
def remove_task():
    os.system('cls')
    if tasks:
        try:
            amount = int(input("Insert the amount of tasks you would like to add: "))
            if amount >= len(tasks):
                tasks.clear()
                print("All tasks removed.")
                return return_menu()
            elif amount == 1:
                remove = input("Insert the task you would like to remove: ")
                if remove in tasks:
                    tasks.remove(remove)
                    print("Task removed!")
                    return return_menu()
                else:
                    print("Task not found.")
                    return return_menu()
            elif amount > 1:
                for i in range(amount):
                    remove = input(f"Insert the name of task N°{i+1} you would like to remove: ")
                    if remove in tasks:
                        tasks.remove(remove)
                        print("Task removed!")
                    else:
                        print("Task not found.")
                print("All tasks found were removed.")
                return return_menu()
            else:
                print("Invalid input. Insert a number equal or greater than 1.")
                input("Press enter to try again.")
                return remove_task()
        except ValueError:
            print("Invalid input. Insert numbers only.")    
            return return_menu()
    else:
        print("The list is empty, no tasks to remove.")
        return return_menu()
    
        
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