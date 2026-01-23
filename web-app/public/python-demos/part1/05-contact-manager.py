"""
Demo Project 5: Contact Management System
Part 1: Python Fundamentals - Hour 7
Difficulty: ⭐⭐⭐ Advanced

Features:
- Add contacts (name, phone, email, address)
- Search contacts by name
- Update contact information
- Delete contacts
- List all contacts
- Save to JSON file
"""

import json
import os
from datetime import datetime

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()
    
    def load_contacts(self):
        """Load contacts from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_contacts(self):
        """Save contacts to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=2)
    
    def add_contact(self, name, phone, email="", address=""):
        """Add a new contact"""
        contact = {
            "id": len(self.contacts) + 1,
            "name": name,
            "phone": phone,
            "email": email,
            "address": address,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f"✅ Contact added: {name}")
    
    def list_contacts(self):
        """List all contacts"""
        if not self.contacts:
            print("No contacts found!")
            return
        
        print("\n" + "="*80)
        print(f"{'ID':<5} {'Name':<20} {'Phone':<15} {'Email':<25} {'Address':<15}")
        print("="*80)
        
        for contact in self.contacts:
            print(f"{contact['id']:<5} {contact['name']:<20} {contact['phone']:<15} "
                  f"{contact['email']:<25} {contact['address']:<15}")
        
        print("="*80 + "\n")
    
    def search_contact(self, keyword):
        """Search contacts by name"""
        results = [c for c in self.contacts if keyword.lower() in c['name'].lower()]
        
        if not results:
            print(f"No contacts found with '{keyword}'")
            return
        
        print(f"\n🔍 Search results for '{keyword}':")
        for contact in results:
            print(f"\n  ID: {contact['id']}")
            print(f"  Name: {contact['name']}")
            print(f"  Phone: {contact['phone']}")
            print(f"  Email: {contact['email']}")
            print(f"  Address: {contact['address']}")
    
    def update_contact(self, contact_id, field, new_value):
        """Update a contact field"""
        for contact in self.contacts:
            if contact['id'] == contact_id:
                if field in contact:
                    old_value = contact[field]
                    contact[field] = new_value
                    self.save_contacts()
                    print(f"✅ Updated {field}: {old_value} → {new_value}")
                    return
                else:
                    print(f"❌ Invalid field: {field}")
                    return
        print(f"❌ Contact {contact_id} not found!")
    
    def delete_contact(self, contact_id):
        """Delete a contact"""
        for i, contact in enumerate(self.contacts):
            if contact['id'] == contact_id:
                deleted_name = self.contacts.pop(i)['name']
                # Re-number remaining contacts
                for j, c in enumerate(self.contacts):
                    c['id'] = j + 1
                self.save_contacts()
                print(f"🗑️ Deleted contact: {deleted_name}")
                return
        print(f"❌ Contact {contact_id} not found!")

def show_menu():
    """Display menu"""
    print("\n" + "="*40)
    print("     CONTACT MANAGEMENT SYSTEM")
    print("="*40)
    print("1. Add Contact")
    print("2. List All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("0. Exit")
    print("="*40)

def main():
    """Main program"""
    manager = ContactManager()
    
    while True:
        show_menu()
        choice = input("Enter choice (0-5): ")
        
        if choice == '0':
            print("Goodbye! 👋")
            break
        
        elif choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email (optional): ")
            address = input("Enter address (optional): ")
            manager.add_contact(name, phone, email, address)
        
        elif choice == '2':
            manager.list_contacts()
        
        elif choice == '3':
            keyword = input("Enter name to search: ")
            manager.search_contact(keyword)
        
        elif choice == '4':
            manager.list_contacts()
            try:
                contact_id = int(input("Enter contact ID to update: "))
                print("\nFields: name, phone, email, address")
                field = input("Enter field to update: ").lower()
                new_value = input(f"Enter new {field}: ")
                manager.update_contact(contact_id, field, new_value)
            except ValueError:
                print("❌ Invalid ID!")
        
        elif choice == '5':
            manager.list_contacts()
            try:
                contact_id = int(input("Enter contact ID to delete: "))
                manager.delete_contact(contact_id)
            except ValueError:
                print("❌ Invalid ID!")
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()


