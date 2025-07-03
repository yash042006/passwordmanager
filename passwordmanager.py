import json
import os
import secrets
import string
from getpass import getpass

DATA_FILE = "data.json"
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# ---------- Core Functionalities ----------

def add_password():
    site = input("Enter site name: ").lower()
    username = input("Enter username/email: ")
    choice = input("Do you want to generate a password? (y/n): ").lower()
    if choice == 'y':
        password = generate_password()
        print(f"Generated Password: {password}")
    else:
        password = getpass("Enter password (input hidden): ")

    data = load_data()
    data[site] = {"username": username, "password": password}
    save_data(data)
    print("✅ Credentials saved successfully.")

def view_password():
    site = input("Enter site name to retrieve: ").lower()
    data = load_data()
    if site in data:
        print(f"🔐 Username: {data[site]['username']}")
        print(f"🔑 Password: {data[site]['password']}")
    else:
        print("❌ No credentials found for this site.")

def update_password():
    site = input("Enter site name to update: ").lower()
    data = load_data()
    if site in data:
        username = input("Enter new username/email (leave blank to keep old): ")
        password = getpass("Enter new password (leave blank to keep old): ")

        if username:
            data[site]['username'] = username
        if password:
            data[site]['password'] = password

        save_data(data)
        print("✅ Credentials updated.")
    else:
        print("❌ No entry found for this site.")

def delete_password():
    site = input("Enter site name to delete: ").lower()
    data = load_data()
    if site in data:
        confirm = input(f"Are you sure you want to delete credentials for '{site}'? (y/n): ")
        if confirm.lower() == 'y':
            del data[site]
            save_data(data)
            print("🗑️ Credentials deleted.")
    else:
        print("❌ No credentials found for this site.")

# ---------- Main Menu ----------

def main():
    while True:
        print("\n🔐 Password Manager Menu")
        print("1. Add New Password")
        print("2. View Password")
        print("3. Update Password")
        print("4. Delete Password")
        print("5. Generate Random Password")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == '1':
            add_password()
        elif choice == '2':
            view_password()
        elif choice == '3':
            update_password()
        elif choice == '4':
            delete_password()
        elif choice == '5':
            print(f"Generated Password: {generate_password()}")
        elif choice == '6':
            print("👋 Exiting Password Manager. Stay secure!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

