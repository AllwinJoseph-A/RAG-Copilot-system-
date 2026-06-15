import sqlite3
from datetime import date

def initialize_database():
    # Connect to SQLite (it will automatically create a file called 'workforce.db')
    connection = sqlite3.connect("workforce.db")
    cursor = connection.cursor()

    print("Creating tables...")
    # 1. Create the Employees table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            employee_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            designation TEXT NOT NULL,
            department TEXT NOT NULL,
            manager_id TEXT,
            salary REAL NOT NULL,
            joining_date TEXT NOT NULL,
            location TEXT NOT NULL,
            skills TEXT NOT NULL, -- Stored as a comma-separated string for simplicity
            experience_years INTEGER NOT NULL,
            role TEXT NOT NULL
        )
    """)

    print("Seeding sample employee profiles...")
    # 2. Define clear seed data (Notice Rahul Sharma is included here)
    sample_employees = [
        ("EMP001", "Rahul Sharma", "Senior Software Engineer", "Engineering", "EMP002", 95000.00, "2024-01-15", "Delhi", "Python,Generative AI,SQL", 5, "Employee"),
        ("EMP002", "Sarah Jenkins", "VP of Engineering", "Engineering", "CEO001", 160000.00, "2022-03-10", "Mumbai", "System Design,Leadership,Cloud", 12, "Department_Manager"),
        ("CEO001", "Alok Kumar", "Chief Executive Officer", "Executive", None, 320000.00, "2020-01-01", "Mumbai", "Strategy,Governance,Finance", 20, "CEO"),
        ("EMP003", "Priya Patel", "HR Specialist", "Human Resources", "CEO001", 70000.00, "2025-05-20", "Bangalore", "Recruiting,Onboarding", 3, "HR_Manager")
    ]

    # 3. Safely insert data if it doesn't already exist
    for emp in sample_employees:
        cursor.execute("""
            INSERT OR IGNORE INTO employees 
            (employee_id, name, designation, department, manager_id, salary, joining_date, location, skills, experience_years, role)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, emp)

    connection.commit()
    connection.close()
    print("Database built and loaded with records successfully!")

if __name__ == "__main__":
    initialize_database()