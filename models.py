from database import get_connection

def add_student(name):
    with get_connection() as conn:
        conn.execute("INSERT INTO students (name) VALUES (?)", (name,))
        print("Student added successfully.")

def add_course(name):
    with get_connection() as conn:
        conn.execute("INSERT INTO courses (name) VALUES (?)", (name,))
        print("Course added successfully.")

def register_student(student_id, course_id):
    with get_connection() as conn:
        try:
            conn.execute("INSERT INTO registrations (student_id, course_id) VALUES (?, ?)", (student_id, course_id))
            print("Student registered to course.")
        except:
            print("Registration failed (maybe duplicate or invalid ID).")

def list_students():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM students").fetchall()
        print("Students:")
        for row in rows:
            print(row)

def list_courses():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM courses").fetchall()
        print("Courses:")
        for row in rows:
            print(row)

def list_registrations():
    with get_connection() as conn:
        rows = conn.execute("""
        SELECT s.name, c.name FROM registrations r
        JOIN students s ON s.id = r.student_id
        JOIN courses c ON c.id = r.course_id
        """).fetchall()
        print("Registrations:")
        for row in rows:
            print(f"{row[0]} -> {row[1]}")
