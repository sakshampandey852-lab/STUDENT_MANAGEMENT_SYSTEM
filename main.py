import sqlite3

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))
    attendance = float(input("Enter attendance (%): "))

    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO students (name, roll_no, course, marks, attendance)
        VALUES (?, ?, ?, ?, ?)
        """, (name, roll_no, course, marks, attendance))

        conn.commit()
        print("\nStudent added successfully!")

    except sqlite3.IntegrityError:
        print("\nRoll number already exists!")

    conn.close()


def view_students():
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    print("\n----- Student Records -----")

    if not students:
        print("No student records found.")
    else:
        for student in students:
            print(
                "ID:", student[0],
                "| Name:", student[1],
                "| Roll No:", student[2],
                "| Course:", student[3],
                "| Marks:", student[4],
                "| Attendance:", student[5], "%"
            )

    conn.close()


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!") 