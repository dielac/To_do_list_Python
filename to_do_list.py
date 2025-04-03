task = []  # this code equals an empty list so I can start my project



# Function to display the menu options 
def display_menu():

    print("\n=== To-Do List Menu ===")  # this code adds a simple header to make it pop out more than the others 
    print("1. Add Task")  
    print("2. View Tasks")  
    print("3. Delete Task")  
    print("4. Quit")  




# Function to add a task to the list 
def add_task():

    global task  # task is a global list 
    new_task = input("Enter a task: ")  # Getting user input for the new task/ also input is a user interaction one of the requierements 
    
    if new_task.strip():  
        task.append(new_task)  # adding task to the list
        print(f"Task '{new_task}' added successfully.") 
   
    else:
        print("Task cannot be empty. Please try again.")  




# Function to view all the tasks in the list
def view_task():
    
    if len(task) == 0:  # Checking if the list is empty
        print("No tasks available so add some to get started!")
    
    else:
        print("\n=== Your To-Do List ===")  # trying to keep the 'to do list' the same and pop out more then the rest 
        for i, t in enumerate(task, start=1):  # loops though task with numbering
            print(f"{i}. {t}")  # this code shows the tasks with a number 




# Function to delete a task from the list
def delete_task():
    view_task()  # this code shows the task first so you can see what youre deleting 
    try:
        task_number = int(input("Enter the task number to delete: "))  

        if 1 <= task_number <= len(task):  # this code checks if the code is valid
            removed_task = task.pop(task_number - 1)  #this removes the task by number
            print(f"Task '{removed_task}' deleted successfully.") 

        else:

            print("Invalid task number. Please choose a valid one.") 
    except ValueError:
        print("Oops! Please enter a valid number.")  # 

    except Exception as e:
        print(f"Something went wrong: {str(e)}")  # this catches any unexpected errors




# Main function - where everything starts
def main():

    print("Welcome to your personal To-Do List ! Get started now!")  # start of the page 
    while True:  # infinate loop that keeps the app running 

        display_menu()  # shows the menu each time 
        choice = input("What do you want to do? ")  

        if choice == "1":  
            add_task()
        elif choice == "2": 
            view_task()
        elif choice == "3":  
            delete_task()
        elif choice == "4":  
            print("Goodbye! Have a great day!")
            break  # this last code breaks the loop to exit 
        else:
            print("Invalid choice. Please pick a number from 1 to 4.")  # this code handles invalid choices

main()  # this starts the whole program 
