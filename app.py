import sqlite3

# --- 1. SETUP THE DATABASE ---
# This creates the database file automatically
connection = sqlite3.connect("project.db")
cursor = connection.cursor()

# Create a simple table for "Projects"
cursor.execute("CREATE TABLE IF NOT EXISTS projects (id INTEGER PRIMARY KEY, name TEXT)")
connection.commit()

# --- 2. SIMPLE FUNCTIONS ---
def add_project(name):
    cursor.execute("INSERT INTO projects (name) VALUES (?)", (name,))
    connection.commit()
    print(f"Project '{name}' saved!")

def show_projects():
    cursor.execute("SELECT * FROM projects")
    results = cursor.fetchall()
    print("\n--- MY SAVED PROJECTS ---")
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]}")

# --- 3. THE MENU ---
print("Welcome to your Fresh Start!")
user_input = input("Enter a project name to save it: ")
add_project(user_input)
show_projects()

# Clean up
connection.close()