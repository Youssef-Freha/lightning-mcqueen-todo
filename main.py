import os

FILENAME = "tasks.txt"

def load_tasks():
    """تحميل المهام من ملف txt عند تشغيل البرنامج"""
    tasks = []
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(" | ")
                    if len(parts) == 2:
                        title, status = parts
                        tasks.append({"title": title, "completed": status == "True"})
        except Exception as e:
            print(f"\n⚠️ Error loading file: {e}")
    return tasks

def save_tasks(tasks):
    """حفظ المهام في ملف txt فور حدوث أي تغيير"""
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            for task in tasks:
                file.write(f"{task['title']} | {task['completed']}\n")
    except Exception as e:
        print(f"\n⚠️ Error saving tasks: {e}")

def add_task(tasks):
    task_title = input("\nEnter the task description: ").strip()
    if task_title:
        task = {"title": task_title, "completed": False}
        tasks.append(task)
        save_tasks(tasks)
        print(f"\n✨ Got it! Added '{task_title}' to Lightning's list.")
    else:
        print("\n⚠️ Task description cannot be empty!")

def view_tasks(tasks):
    if not tasks:
        print("\n🏁 Your to-do list is empty! No tasks right now.")
        return
    
    print("\n📋 LIGHTNING MCQUEEN'S TO-DO LIST:")
    print("-" * 40)
    for index, task in enumerate(tasks, start=1):
        status = "✅ [Done]" if task["completed"] else "⏳ [Pending]"
        print(f"{index}. {task['title']} ---> {status}")
    print("-" * 40)

def mark_task_done(tasks):
    if not tasks:
        print("\n🏁 No tasks available to mark as done.")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task you finished: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print(f"\n🏆 Ka-chow! Checked off '{tasks[task_num - 1]['title']}'!")
        else:
            print("\n⚠️ Invalid task number.")
    except ValueError:
        print("\n⚠️ Please enter a valid number.")

def remove_task(tasks):
    if not tasks:
        print("\n🏁 No tasks available to remove.")
        return
    
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the number of the task to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"\n🗑️ Removed '{removed['title']}' from your list.")
        else:
            print("\n⚠️ Invalid task number.")
    except ValueError:
        print("\n⚠️ Please enter a valid number.")

def show_menu():
    print("\n" + "="*35)
    print("⚡ LIGHTNING MCQUEEN'S TO-DO LIST ⚡")
    print("="*35)
    print("1. Add a task")
    print("2. View my to-do list")
    print("3. Mark a task as done")
    print("4. Remove a task")
    print("5. Quit")
    print("="*35)

def main():
    # تحميل المهام المخزنة في tasks.txt إن وجدت
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("What's the move, champ? ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("\nCatch ya at the finish line! 🏎️💨")
            break
        else:
            print("\nInvalid choice! Please choose a number from 1 to 5.")

if __name__ == "__main__":
    main()