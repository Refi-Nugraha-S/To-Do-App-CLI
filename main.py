# main.py
from text import text
from functions import load_data, save_data, add_task, delete_todo, complete_todo, show_task

text()

while True:
    start = input("Start? (y/n): ").lower()

    if start == "n":
        print("Bye!\n")
        break
        
    elif start == "y":
        try:
            print("\n=== MENU ===")
            print("1. Add task")
            print("2. Delete task")
            print("3. Complete task")
            print("4. Show all tasks")
            
            user_input = int(input("Choose (1-4): "))

            if user_input == 1:
                task = input("Enter task: ")
                add_task(task)
                print("\n")
                
            elif user_input == 2:
                show_task()
                id_task = int(input("Enter task ID to delete: "))
                delete_todo(id_task)
                print("\n")
                
            elif user_input == 3:
                show_task()
                task_id = int(input("Enter task ID to complete: "))
                complete_todo(task_id)
                print("\n")
                
            elif user_input == 4:
                show_task()
                print("\n")
                
            else:
                print("Invalid choice! Please choose 1-4\n")

        except ValueError:
            print("Error: Invalid input! Please enter a number.\n")
        except KeyboardInterrupt:
            print("\nError: Canceled by user!\n")
            break
        except Exception as e:
            print(f"Something wrong: {e}")
            print("Please report this error\n")

    else:
        print("Please choose (y/n)!\n")
