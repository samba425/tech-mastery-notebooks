"""
Demo Project 4: Todo List Application with JSON
Part 1: Python Fundamentals - Hour 6
Difficulty: ⭐⭐⭐ Advanced

Features:
- Add tasks with priority levels
- Mark tasks as complete
- Delete tasks
- Filter by status/priority
- Save/load from JSON file
- Persistent storage
"""

import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Load todos from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def save_todos(self):
        """Save todos to JSON file"""
        with open(self.filename, 'w') as f:
            json.dump(self.todos, f, indent=2)
    
    def add_todo(self, task, priority="medium"):
        """Add a new todo"""
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "priority": priority,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✅ Added: {task}")
    
    def list_todos(self, show_all=True):
        """List all todos"""
        if not self.todos:
            print("No todos yet!")
            return
        
        print("\n" + "="*60)
        print(f"{'ID':<5} {'Task':<30} {'Priority':<10} {'Status':<10}")
        print("="*60)
        
        for todo in self.todos:
            if not show_all and todo['completed']:
                continue
            
            status = "✓ Done" if todo['completed'] else "○ Pending"
            print(f"{todo['id']:<5} {todo['task']:<30} {todo['priority']:<10} {status:<10}")
        
        print("="*60 + "\n")
    
    def complete_todo(self, todo_id):
        """Mark todo as completed"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                todo['completed'] = True
                self.save_todos()
                print(f"✅ Completed: {todo['task']}")
                return
        print(f"❌ Todo {todo_id} not found!")
    
    def delete_todo(self, todo_id):
        """Delete a todo"""
        for i, todo in enumerate(self.todos):
            if todo['id'] == todo_id:
                deleted_task = self.todos.pop(i)
                # Re-number remaining todos
                for j, t in enumerate(self.todos):
                    t['id'] = j + 1
                self.save_todos()
                print(f"🗑️ Deleted: {deleted_task['task']}")
                return
        print(f"❌ Todo {todo_id} not found!")
    
    def search_todos(self, keyword):
        """Search todos by keyword"""
        results = [t for t in self.todos if keyword.lower() in t['task'].lower()]
        
        if not results:
            print(f"No todos found with '{keyword}'")
            return
        
        print(f"\n🔍 Search results for '{keyword}':")
        for todo in results:
            status = "✓" if todo['completed'] else "○"
            print(f"  {status} [{todo['id']}] {todo['task']}")
    
    def get_stats(self):
        """Show todo statistics"""
        total = len(self.todos)
        completed = sum(1 for t in self.todos if t['completed'])
        pending = total - completed
        
        print("\n📊 Todo Statistics:")
        print(f"  Total: {total}")
        print(f"  Completed: {completed}")
        print(f"  Pending: {pending}")
        
        if total > 0:
            completion_rate = (completed / total) * 100
            print(f"  Completion Rate: {completion_rate:.1f}%")

def show_menu():
    """Display menu"""
    print("\n" + "="*40)
    print("        TODO LIST APPLICATION")
    print("="*40)
    print("1. Add Todo")
    print("2. List All Todos")
    print("3. List Pending Todos")
    print("4. Complete Todo")
    print("5. Delete Todo")
    print("6. Search Todos")
    print("7. Show Statistics")
    print("0. Exit")
    print("="*40)

def main():
    """Main program"""
    app = TodoApp()
    
    while True:
        show_menu()
        choice = input("Enter choice (0-7): ")
        
        if choice == '0':
            print("Goodbye! Stay productive! 🚀")
            break
        
        elif choice == '1':
            task = input("Enter task: ")
            priority = input("Priority (high/medium/low) [medium]: ").lower() or "medium"
            if priority not in ['high', 'medium', 'low']:
                priority = 'medium'
            app.add_todo(task, priority)
        
        elif choice == '2':
            app.list_todos(show_all=True)
        
        elif choice == '3':
            app.list_todos(show_all=False)
        
        elif choice == '4':
            app.list_todos(show_all=False)
            try:
                todo_id = int(input("Enter todo ID to complete: "))
                app.complete_todo(todo_id)
            except ValueError:
                print("❌ Invalid ID!")
        
        elif choice == '5':
            app.list_todos()
            try:
                todo_id = int(input("Enter todo ID to delete: "))
                app.delete_todo(todo_id)
            except ValueError:
                print("❌ Invalid ID!")
        
        elif choice == '6':
            keyword = input("Enter search keyword: ")
            app.search_todos(keyword)
        
        elif choice == '7':
            app.get_stats()
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()


