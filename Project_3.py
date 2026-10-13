students_db = {}
subjects_offered = ["Math", "Science", "English", "History", "Art"]

def print_menu():
    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

print("Welcome to the Student Data Organizer!")

while True:
    print_menu()
    choice = input("Enter your choice: ").strip()

    
    match choice:
        case "1":
            print("\nEnter student details:")
            student_id = input("Student ID: ").strip()
            name = input("Name: ").strip()
            age = input("Age: ").strip()
            grade = input("Grade: ").strip()
            dob = input("Date of Birth (YYYY-MM-DD): ").strip()
            subs = input("Subjects (comma-separated): ").strip()
            
            students_db[student_id] = {
                "name": name,
                "age": age,
                "grade": grade,
                "dob": dob,
                "subjects": [s.strip() for s in subs.split(",")]
            }
            print("\nStudent added successfully!")

        case "2":
            print("\n--- Display All Students ---")
            if not students_db:
                print("No students recorded yet.")
            for s_id, data in students_db.items():
                subs_str = ", ".join(data["subjects"])
                print(f"Student ID: {s_id} | Name: {data['name']} | Age: {data['age']} | "
                      f"Grade: {data['grade']} | Subjects: {subs_str}")

        case "3":
            s_id = input("\nEnter Student ID to update: ").strip()
            if s_id in students_db:
                print("Enter new details (leave blank to keep current value):")
                name = input(f"Name [{students_db[s_id]['name']}]: ") or students_db[s_id]['name']
                age = input(f"Age [{students_db[s_id]['age']}]: ") or students_db[s_id]['age']
                grade = input(f"Grade [{students_db[s_id]['grade']}]: ") or students_db[s_id]['grade']
                
                students_db[s_id].update({"name": name, "age": age, "grade": grade})
                print("Student information updated successfully!")
            else:
                print("Student ID not found.")

        case "4":
            s_id = input("\nEnter Student ID to delete: ").strip()
            if students_db.pop(s_id, None):
                print("Student deleted successfully!")
            else:
                print("Student ID not found.")

        case "5":
            print("\n--- Subjects Offered ---")
            print(", ".join(subjects_offered))

        case "6":
            print("\nExiting Student Data Organizer. Goodbye!")
            break

        case _:
            print("\nInvalid selection. Please choose a number between 1 and 6.")
