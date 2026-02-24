import task_manager, notifications

def run(user):
    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Tandai Selesai")
        print("4. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            title = input("Judul tugas: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            task_manager.add_task(title, deadline)
        elif choice == "2":
            task_manager.list_tasks()
        elif choice == "3":
            index = int(input("Index tugas: ")) - 1
            task_manager.mark_done(index)
        elif choice == "4":
            print("Keluar aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")

        notifications.check_deadlines()
