# Contact Booklet — Python CLI Contact Manager

A **Python-based Contact Booklet** built as part of an **MCA (AI & ML) assignment**, designed to manage personal contacts through a **Command Line Interface (CLI)**.

The application demonstrates **file handling using CSV and JSON formats**, along with **error logging and full CRUD operations (Create, Read, Update, Delete)** for efficient contact management.

This project showcases practical Python concepts such as **data persistence, input validation, structured program design, and error tracking**.

---

# Project Overview

The **Contact Booklet** is a lightweight CLI application that allows users to create and manage their contact list directly from the terminal.

Users can:

* Add new contacts
* View all saved contacts
* Search contacts instantly
* Update existing contact details
* Delete contacts
* Import and export contact data
* Automatically sync records between **CSV and JSON files**
* Log errors with timestamps

The system ensures **data consistency and reliability** by maintaining multiple file formats and logging runtime issues.

---

# Problem Statement

Managing contacts manually or across different files can lead to **data inconsistencies and loss of information**.

This project solves that problem by providing a **centralized contact management system** that:

* Maintains structured records
* Automatically synchronizes multiple file formats
* Allows fast searching and editing
* Logs program errors for debugging

---

#  Solution Approach

The application is implemented using **Python and runs through a menu-driven CLI interface**.

Core implementation components include:

1. **CRUD Operations Module**

   * Handles contact creation, viewing, updating, and deletion.

2. **Data Persistence Layer**

   * Stores contacts in both **CSV and JSON files**.

3. **Synchronization Mechanism**

   * Automatically updates both storage formats whenever changes occur.

4. **Import/Export Module**

   * Supports importing contacts from external JSON files.

5. **Error Logging System**

   * Logs program errors with timestamps to help debugging.

---

#  Key Features

###  Add Contacts

Save contact details including:

* Name
* Phone number
* Email address

###  View All Contacts

Displays contacts in a **clean, formatted table layout** for better readability.

###  Search Contacts

Quickly locate contacts by entering a name.

###  Update Contacts

Modify existing contact details using the **contact's index number**.

###  Delete Contacts

Remove unwanted contacts safely from the contact list.

###  Auto Synchronization

Every change automatically updates:

* `contacts.csv`
* `contacts.json`

This ensures **data redundancy and reliability**.

###  Import / Export Support

Users can:

* Export contacts to JSON
* Import contacts from an external JSON file

###  Error Logging

All program errors are logged in:

```
error_log.txt
```

Each entry contains a **timestamp and error message**, making debugging easier.

---

#  Tech Stack

| Technology                       | Purpose                          |
| -------------------------------- | -------------------------------- |
| **Python 3**                     | Core programming language        |
| **CSV**                          | Structured contact data storage  |
| **JSON**                         | Data persistence and portability |
| **CLI (Command Line Interface)** | User interaction                 |
| **File Handling**                | Data synchronization and logging |

---

#  System Architecture

```
User Input (CLI)
        │
        ▼
 Contact Manager
 │      │      │
 ▼      ▼      ▼
CRUD   Search  Import/Export
        │
        ▼
Data Storage Layer
│                 │
▼                 ▼
contacts.csv   contacts.json
        │
        ▼
Error Logging (error_log.txt)
```

---

#  Project Structure

```
ContactBooklet
│
├── contact_booklet.py    # Main application file
├── contacts.csv          # CSV contact storage
├── contacts.json         # JSON contact storage
├── error_log.txt         # Error logging file
└── README.md             # Project documentation
```

*(File names may vary depending on implementation.)*

---

#  Example Usage

Example CLI interaction:

```
1. Add Contact
2. View Contacts
3. Search Contact
4. Update Contact
5. Delete Contact
6. Export to JSON
7. Import from JSON
8. Exit

Select an option: 1

Enter Name: Rahul Sharma
Enter Phone: 9876543210
Enter Email: rahul@email.com

Contact added successfully.
```

---

#  Example Contact Table Output

```
Index   Name           Phone        Email
------------------------------------------------
1       Rahul Sharma   9876543210   rahul@email.com
2       Priya Singh    9123456789   priya@email.com
```

---

#  Challenges & Learnings

### Multi-format Data Storage

Maintaining synchronization between **CSV and JSON formats** required careful file handling logic.

### CLI Usability

Designing a simple and intuitive command-line menu improved the overall user experience.

### Error Logging

Implementing structured logging helped track runtime issues effectively.

---

#  Future Improvements

Potential enhancements for this project include:

* Add **contact categories (Friends, Family, Work)**
* Implement **phone number validation**
* Add **search by phone or email**
* Integrate **SQLite database storage**
* Develop a **GUI version using Tkinter**
* Create a **web-based contact manager using Flask**

---

#  Author

**Vinayak Sharma**

GitHub
https://github.com/your-vsbeginner

LinkedIn
https://www.linkedin.com/in/vinayak-sharma-24a8aa384/

---
