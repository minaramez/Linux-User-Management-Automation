## **Linux User Management Automation**

### **Description**
This repository contains two Python scripts designed to automate user management on a **CentOS 8 Linux system**. The scripts handle:
- **Adding new users** from a CSV file (`add_user.py`).
- **Removing all users and groups** in a specific UID range (`remove_users.py`).

### **Features**
- **Bulk user creation** from `linux_users.csv`
- **Duplicate user handling** (e.g., `jsmith`, `jsmith1`, `jsmith2`)
- **Automatic group creation** if it doesn't exist
- **Assigns user home directories based on department**
- **Sets the correct default shell** (`csh` for "office" users, `bash` for others)
- **Ensures passwords expire** on first login
- **Handles missing and incorrect data gracefully**
- **Removes all dynamically created users and groups** with `remove_users.py`

---

## **Prerequisites**
- **CentOS 8** or similar Linux system
- Python 3 installed
- Root privileges to execute user management commands

---

## **Installation**
Clone this repository:
```bash
git clone https://github.com/yourusername/linux-user-management.git
cd linux-user-management
```

Ensure the scripts have execute permissions:
```bash
chmod +x add_user.py remove_users.py
```

---

## **Usage**

### **Adding Users**
Run the script to read from `linux_users.csv` and add users:
```bash
sudo python3 add_user.py
```

### **Removing Users**
Run this to remove all dynamically created users and their groups:
```bash
sudo python3 remove_users.py
```

---

## **CSV File Format**
The `linux_users.csv` file contains user details. The script automatically processes it **without modifications**.

| First Name | Last Name | Username | Password | Department | Group |
|------------|----------|----------|----------|------------|-------|
| John       | Doe      | jdoe     | password | IT         | office |
| Jane       | Smith    | jsmith   | password | HR         | hr     |

---

## **Example Output**
### **Adding Users**
```
Linux - Users Adding Automation
User data is typed as following:
Username:password | password type

Successfully added user: jdoe
Successfully added user: jsmith
```
### **Removing Users**
```
jdoe            Remove from system.
jsmith          Remove from system.
```

---

### License
This script is released under the **MIT License**, which allows modification, distribution, and use with minimal restrictions.