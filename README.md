# password-manager-py

A minimalist CLI application to manage and verify passwords using secure hashing techniques.

## 💡 Overview
This project is a practical implementation of password security fundamentals. Instead of storing passwords in plain text, this tool generates a unique **SHA-256 hash** for each entry, combined with a cryptographically secure **salt** to prevent Rainbow Table attacks.

## 🚀 Features
* **Secure Hashing:** Uses Python's `hashlib` for industry-standard SHA-256.
* **Unique Salting:** Implements `os.urandom` to ensure every hash is unique even if passwords are identical.
* **Local Storage:** Data is persisted in a structured `password_db.json` file.
* **User-Friendly CLI:** Simple menu-driven interface for adding and verifying credentials.

## 🛠️ Setup and Usage

1. **Clone the repository:**
   ```
   git clone [https://github.com/leumascripts/password-manager-py.git](https://github.com/leumascripts/password-manager-py.git)
   cd password-manager-py

   Run the script: python password-manager-py

2. ❗ **Important**:
*Runtime Issues (Windows) If, after attempting to add a password, the script exits with the error **PermissionError: [Errno 13] Permission denied**, this is a permissions issue with the operating system, not the code. **Solution**: Run the script via Command Prompt or PowerShell instead of double-clicking to grant write permissions to the JSON file.1. Open the project folder. 2. Type 'cmd' in the address bar and press Enter. 3. Run: python password_manager.py* 

## ⚠️ Security Disclaimer

This tool was developed for **educational purposes**. While it uses hashing, the database file is not encrypted. Do not use this for sensitive production credentials without implementing additional encryption (e.g., AES) for the storage file.

## 📝 License

Distributed under the MIT License. See LICENSE for more information.
