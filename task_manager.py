tasks = []

def add_task(title: str, deadline: str):
    task = {"title": title, "deadline": deadline, "done": False}
    tasks.append(task)
    print("Tugas ditambahkan.")

def list_tasks():
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else "✗"
        print(f"{i}. {task['title']} - {task['deadline']} [{status}]")

def mark_done(index: int):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        print("Tugas selesai.")
    else:
        print("Index tidak valid.")
