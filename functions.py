import json
import os

task_file = "task.json"

def load_data():
    if not os.path.exists(task_file):
        return []
    with open(task_file, "r") as file:
        return json.load(file)

def save_data(data):
    with open(task_file, "w") as file:
        json.dump(data, file, indent=4)

def add_task(task):
    data = load_data()
    if data:
        new_id = max(todo["id"] for todo in data) + 1
    else:
        new_id = 1
    data.append({
        "id": new_id,
        "task": task,
        "done": False
    })
    save_data(data)
    print("Task added!")

def delete_todo(todo_id):
    data = load_data()
    data = [todo for todo in data if todo["id"] != todo_id]
    save_data(data)
    print("Todo deleted!")

def complete_todo(todo_id):
    data = load_data()
    for todo in data:
        if todo["id"] == todo_id:
            todo["done"] = True
    save_data(data)
    print("Todo done!")

def show_task():
    data = load_data()
    for todo in data:
        status = "Done" if todo["done"] else "Not yet"
        print(f"{todo['id']}. {todo['task']} [{status}]")

if __name__ == "__main__":

    while True:
        print("\n=== TODO LIST MANAGER ===")
        print("1. Show all tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Choose option (1-5): ")
        
        if choice == "1":
            show_task()
        elif choice == "2":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "3":
            todo_id = int(input("Enter task ID to complete: "))
            complete_todo(todo_id)
        elif choice == "4":
            todo_id = int(input("Enter task ID to delete: "))
            delete_todo(todo_id)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
