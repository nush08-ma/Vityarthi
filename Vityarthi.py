import sqlite3
#We are making a student database management system
#we are connecting database
def connect_db():
    """Here we are connecting a database"""
    conn = sqlite3.connect("student_data.db")
    cursor = conn.cursor()
    # Here the table is created
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
    """)
    conn.commit()
    conn.close()
# 2.We are adding the student
def add_student():
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Student Grade/Class: ")
    conn = sqlite3.connect("student_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, age, grade) VALUES(?,?,?)", (name, age, grade))
    conn.commit()
    conn.close()
    print(f"{name} added to database!")
# 3. Viewing of data (READ)
def view_students():
    conn = sqlite3.connect("student_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\nStudent Records")
    if not rows:
        print("No records found.")
    else:
        print(f"{'ID':<5} {'Name':<20} {'Age':<5} {'Grade':<10}")
        print("-" * 40)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<5} {row[3]:<10}")
    print("-" * 40)
    conn.close()
# 4. Deleting of a Student (Delete operation)
def delete_student():
    view_students() 
    student_id = input("\nEnter the ID of the student to delete: ")
    conn = sqlite3.connect("student_data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    if cursor.rowcount > 0:
        print(f" Student with ID {student_id} deleted.")
    else:
        print("Error- no ID is found.")
    conn.commit()
    conn.close()
# 5. Updating the details of a Student (Update operation)
def update_student():
    view_students()
    student_id = input("\nEnter ID to update: ")
    new_grade = input("Enter new Grade: ")
    conn = sqlite3.connect("student_data.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade = ? WHERE id = ?", (new_grade, student_id))
    conn.commit()
    conn.close()
    print("Record is updated")
# 6. Main Menu
def main():
    connect_db()
    while True:
        print("\nStudent Database Management System ")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student Grade")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        if choice=='1':
            add_student()
        elif choice=='2':
            view_students()
        elif choice=='3':
            update_student()
        elif choice=='4':
            delete_student()
        elif choice=='5':
            print("Program is exited")
            break
        else:
            print("Invalid choice, please try again.")
# Run the code
if __name__ == "__main__":
    main()
    
