from database import create_tables
import models

def menu():
    print("\n1. Add Student\n2. Add Course\n3. Register Student to Course")
    print("4. List Students\n5. List Courses\n6. List Registrations\n0. Exit")

def main():
    create_tables()
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            models.add_student(input("Enter student name: "))
        elif choice == "2":
            models.add_course(input("Enter course name: "))
        elif choice == "3":
            sid = int(input("Enter student ID: "))
            cid = int(input("Enter course ID: "))
            models.register_student(sid, cid)
        elif choice == "4":
            models.list_students()
        elif choice == "5":
            models.list_courses()
        elif choice == "6":
            models.list_registrations()
        elif choice == "0":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
