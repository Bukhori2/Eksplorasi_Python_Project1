import hashlib

users = {}

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def register(username: str, password: str):
    if username in users:
        print("Username sudah ada!")
        return False
    users[username] = hash_password(password)
    print("Registrasi berhasil.")
    return True

def login():
    username = input("Username: ")
    password = input("Password: ")
    if username in users and users[username] == hash_password(password):
        print("Login berhasil.")
        return username
    else:
        print("Login gagal.")
        return None