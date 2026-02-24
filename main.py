import user_auth, task_manager, database, ui, notifications

def main():
    database.init_db()

    user = user_auth.login()
    if not user:
        print("Login gagal.")
        return

    ui.run(user)

if __name__ == "__main__":
    main()
