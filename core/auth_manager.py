import getpass
import json
import os

import bcrypt

USER_FILE = "user.json"


def load_user():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)


def save_user(user):
    with open(USER_FILE, "w") as f:
        json.dump(user, f, indent=2)


def login_or_register():
    users = load_user()
    username = input("Enter your username: ").strip()
    if username in users:
        for _ in range(3):
            password = getpass.getpass("Enter your password: ")
            if bcrypt.checkpw(password.encode(), users[username].encode()):
                print("🔓 Login successful.")
                return username
            print("❌ Incorrect password.")
        print("🚫 Too many failed attempts.")
        exit(1)
    else:
        password = getpass.getpass("Create your password: ")
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        users[username] = hashed.decode()
        save_user(users)
        print("✅ Registered successfully.")
        return username
