from modules import user_auth, task_manager, database, ui, notifications

def main():
    # Inisialisasi database
    database.init_db()

    # Login/Register
    user = user_auth.login()
    if not user:
        print("Login gagal.")
        return

    # Jalankan UI
    ui.run(user)

if __name__ == "__main__":
    main()
