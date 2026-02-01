
import time
import json
import hashlib
import os

# Hashing logic
def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16).hex()

    password_salted = salt + password
    hashed_pass = hashlib.sha256(password_salted.encode('utf-8')).hexdigest()
    return hashed_pass, salt

# Data Management
def load_data():
    try:
        with open('password_db.json', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(db):
    try:
        with open('password_db.json', 'w') as file:
            json.dump(db, file, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")

# Core Features
def add_password(db):
    site = input("Enter site name: ").strip().lower()
    if not site:
        print("Site name cannot be empty.")
        return
        
    password = input(f"Enter password for {site}: ")
    hashed_password, salt = hash_password(password)

    db[site] = {"hash": hashed_password, "salt": salt}
    save_data(db)
    print(f"Password for '{site}' added successfully.")

def verify_password(db):
    site_to_find = input("Enter the site/service name: ").strip().lower()
    
    if site_to_find in db:
        saved_data = db[site_to_find]
        saved_hash = saved_data["hash"]
        saved_salt = saved_data["salt"]

        user_input = input(f"Enter password to verify for {site_to_find}: ")
        hashed_input, _ = hash_password(user_input, saved_salt)

        if hashed_input == saved_hash:
            print("Verification successful. Password is correct.")
        else:
            print("Verification failed. Incorrect password.")
    else:
        print(f"No entry found for '{site_to_find}'.")

# Main Execution
def main():
    db = load_data()
    while True:
        print("\n--- PASSWORD MANAGER ---")
        print("1. Add Password")
        print("2. Verify Password")
        print("3. Exit")
        
        try:
            choice = input("Select an option (1-3): ")
            if choice == '1':
                add_password(db)
            elif choice == '2':
                verify_password(db)
            elif choice == '3':
                print("Exiting... Goodbye!")
                time.sleep(1)
                break
            else:
                print("Invalid option. Please try again.")
        except KeyboardInterrupt:
            print("\nForce closing...")
            break

if __name__ == "__main__":
    main()
        






