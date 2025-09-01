# Day 30: Final Project - Simple Task Manager CLI
# -----------------------------------------------

# A simple command-line interface (CLI) application to manage tasks.
# Features: Add task, View tasks, Remove task, Save to file, Load from file.

import json
import os
import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    task = {
        "title": title,
        "description": description,
        "created_at": created_at,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    print("\n--- Tasks ---")
    if not tasks:
        print("No tasks found.")
    for index, task in enumerate(tasks):
        status = "[x]" if task["completed"] else "[ ]"
        print(f"{index + 1}. {status} {task['title']} - {task['created_at']}")
        print(f"   Desc: {task['description']}")
    print("-------------\n")

def complete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed['title']}' removed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # For automation purposes, we will not run the main loop if this script is imported or run non-interactively.
    # But we will print a message saying how to run it.
    print("To run the Task Manager, execute this file in your terminal and interact with the menu.")
    print("Example: python Day_30_Final_Project.py")
    
    # Uncomment the line below to run the app interactively
    # main()

# Reviewed on 2025-09-01
