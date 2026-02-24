from datetime import datetime
import task_manager

def check_deadlines():
    today = datetime.today().strftime("%Y-%m-%d")
    for task in task_manager.tasks:
        if not task["done"] and task["deadline"] == today:
            print(f"⚠️ Reminder: Deadline tugas '{task['title']}' hari ini!")
