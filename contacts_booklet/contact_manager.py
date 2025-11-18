"""
Contact Book Manager
Student: Vinayak Sharma
Date: 2025-11-15
"""

import csv
import json
import os
from datetime import datetime

# Files
CSV_FILE = "contacts.csv"
JSON_FILE = "contacts.json" 
ERROR_LOG = "error_log.txt"

def log_error(op, err):
    """Task 6: Log errors with timestamp"""
    try:
        with open(ERROR_LOG, "a") as f:
            f.write(f"[{datetime.now()}] {op}: {err}\n")
    except:
        pass

def load_contacts():
    """Load contacts from CSV file"""
    contacts = []
    try:
        # Check if file exists and is not empty
        if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
            # Create empty CSV file with headers if missing or empty
            with open(CSV_FILE, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["name", "phone", "email"])
                writer.writeheader()
            return []

        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get('name'):  # Only add if name exists
                    contacts.append(row)
                    
    except Exception as e:
        log_error("load_contacts", e)
        # If error occurs, return empty list to prevent crash
        return []
        
    return contacts

def save_contacts(contacts):
    """Save contacts to CSV file and auto-sync to JSON"""
    try:
        # Save to CSV
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "phone", "email"])
            writer.writeheader()
            writer.writerows(contacts)
            
        # Auto-sync: Save to JSON as well
        with open(JSON_FILE, "w") as f:
            json.dump(contacts, f, indent=2)
            
        return True
    except Exception as e:
        log_error("save_contacts", e)
        return False

def show_contacts(contacts, title="CONTACTS"):
    """Task 3: Show contacts in table"""
    if not contacts:
        print("\nNo contacts found.")
        return
    
    print(f"\n{title}")
    print("-" * 50)
    print(f"{'No.':<5} {'Name':<20} {'Phone':<15} {'Email'}")
    print("-" * 50)
    for i, c in enumerate(contacts, 1):
        print(f"{i:<5} {c['name']:<20} {c['phone']:<15} {c['email']}")
    print(f"Total: {len(contacts)}")

def add_contact():
    """Task 2: Add new contact"""
    print("\nAdd Contact")
    name = input("Name: ").strip().title()
    
    if not name:
        print("Name cannot be empty!")
        return
        
    phone = input("Phone: ").strip()
    email = input("Email: ").strip().lower()
    
    contacts = load_contacts()
    
    # Check duplicate
    for c in contacts:
        if c['name'].lower() == name.lower():
            print("Contact already exists!")
            return
    
    contacts.append({"name": name, "phone": phone, "email": email})
    
    if save_contacts(contacts):
        print("Contact saved!")
    else:
        print("Error saving contact!")

def search_contact():
    """Task 4: Search contacts"""
    print("\nSearch Contact")
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts to search.")
        return
    
    name = input("Search name: ").strip().lower()
    found = [c for c in contacts if name in c['name'].lower()]
    
    show_contacts(found, "SEARCH RESULTS")

def update_contact():
    """Task 4: Update contact (Name, Phone, Email)"""
    print("\nUpdate Contact")
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts to update.")
        return
        
    show_contacts(contacts)
    
    try:
        num_str = input("Contact number: ")
        if not num_str.isdigit():
            print("Please enter a valid number.")
            return

        num = int(num_str)
        if 1 <= num <= len(contacts):
            c = contacts[num-1]
            print(f"Updating: {c['name']}")
            
            # Allow updating Name, Phone, and Email
            new_name = input(f"New name ({c['name']}): ").strip().title()
            new_phone = input(f"New phone ({c['phone']}): ").strip()
            new_email = input(f"New email ({c['email']}): ").strip().lower()
            
            if new_name:
                c['name'] = new_name
            if new_phone: 
                c['phone'] = new_phone
            if new_email: 
                c['email'] = new_email
            
            if save_contacts(contacts):
                print("Contact updated!")
        else:
            print("Invalid contact number!")
    except ValueError:
        print("Please enter a valid number!")

def delete_contact():
    """Task 4: Delete contact"""
    print("\nDelete Contact")
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts to delete.")
        return
        
    show_contacts(contacts)
    
    try:
        num_str = input("Contact number: ")
        if not num_str.isdigit():
            print("Please enter a valid number.")
            return

        num = int(num_str)
        if 1 <= num <= len(contacts):
            c = contacts[num-1]
            confirm = input(f"Delete {c['name']}? (y/n): ").lower()
            
            if confirm == 'y':
                contacts.pop(num-1)
                if save_contacts(contacts):
                    print("Contact deleted!")
            else:
                print("Deletion cancelled.")
        else:
            print("Invalid contact number!")
    except ValueError:
        print("Please enter a valid number!")

def export_json():
    """Task 5: Export to JSON"""
    print("\nExport to JSON")
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts to export.")
        return
    
    try:
        with open(JSON_FILE, "w") as f:
            json.dump(contacts, f, indent=2)
        print(f"Exported {len(contacts)} contacts to {JSON_FILE}!")
    except Exception as e:
        log_error("export_json", e)
        print("Export failed!")

def import_json():
    """Task 5: Import from JSON and save to CSV"""
    print("\nImport from JSON")
    try:
        with open(JSON_FILE, "r") as f:
            imported_contacts = json.load(f)
        
        if not imported_contacts:
            print("JSON file is empty.")
            return

        print(f"Found {len(imported_contacts)} contacts in JSON.")
        show_contacts(imported_contacts, "PREVIEW IMPORT")
        
        confirm = input("Do you want to merge these into your main contacts? (y/n): ").lower()
        if confirm == 'y':
            current_contacts = load_contacts()
            
            # Merge logic: Avoid duplicates by name
            existing_names = {c['name'].lower() for c in current_contacts}
            added_count = 0
            
            for c in imported_contacts:
                if c['name'].lower() not in existing_names:
                    current_contacts.append(c)
                    existing_names.add(c['name'].lower())
                    added_count += 1
            
            if save_contacts(current_contacts):
                print(f"Successfully imported {added_count} new contacts!")
            else:
                print("Error saving imported contacts.")
        else:
            print("Import cancelled.")

    except FileNotFoundError:
        print("No JSON file found! Export contacts first.")
    except Exception as e:
        log_error("import_json", e)
        print("Error importing JSON!")

def main():
    """Task 1: Main program"""
    print("CONTACT BOOK MANAGER")
    print("====================")
    
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact") 
        print("5. Delete Contact")
        print("6. Export JSON")
        print("7. Import JSON")
        print("8. Exit")
        
        choice = input("\nChoose (1-8): ").strip()
        
        if choice == "1": 
            add_contact()
        elif choice == "2": 
            show_contacts(load_contacts())
        elif choice == "3": 
            search_contact()
        elif choice == "4": 
            update_contact()
        elif choice == "5": 
            delete_contact()
        elif choice == "6": 
            export_json()
        elif choice == "7": 
            import_json()
        elif choice == "8": 
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1-8.")

if __name__ == "__main__":

    main()
