# 🎓 Student Data Organizer

A lightweight, interactive **Python-based Command Line Interface (CLI)** application designed to manage student records efficiently. It allows users to perform standard CRUD (Create, Read, Update, Delete) operations on student profiles.

---

## 🚀 Features

* ✨ **Add Students:** Register new student profiles with detailed metadata.
* 📋 **View Records:** Display all recorded student data in a structured, readable format.
* 🔄 **Update Profiles:** Modify specific fields (Name, Age, Grade) of existing students while maintaining unchanged values by default.
* ❌ **Delete Records:** Remove student profiles safely using their unique Student ID.
* 📚 **Course Catalog:** View a pre-defined list of all subjects offered by the institution.

---

## 🛠️ Built-in Python Data Structures Used

This project relies on core Python data structures to manage memory and handle inputs cleanly:

### 1. Dictionary (`dict`)
* **Main Database (`students_db = {}`):** Acts as the primary in-memory database. It maps unique `student_id` strings to their respective information.
* **Student Record:** A nested dictionary mapped to each ID, allowing quick, structured lookup for attributes like name, age, grade, and date of birth.

### 2. List (`list`)
* **Global Course Catalog (`subjects_offered`):** An ordered sequence of strings used to manage the set of available classes.
* **Student Subjects:** A dynamic list generated inside each student's profile via **List Comprehension** to store the subjects they are actively enrolled in.

---

## 📋 Data Structure Schema

Here is a visual map of how data is nested and stored inside the program:

```python
students_db = {
    "STUDENT_ID_101": {                   # Key: String (Unique ID) -> Value: Dictionary
        "name": "John Doe",               # String
        "age": "16",                      # String
        "grade": "10th",                  # String
        "dob": "2010-05-14",              # String (YYYY-MM-DD)
        "subjects": ["Math", "Science"]   # List of Strings
    }
}
```

---

## 💻 How To Run

### Prerequisites
Make sure you have **Python 3.10 or higher** installed on your system (required for `match-case` syntax syntax support).

### Execution Steps
1. **Save the script:** Save the Python code to a file named `main.py`.
2. **Open Terminal:** Navigate to the folder containing `main.py` using your command prompt or terminal.
3. **Run the script:** Execute the following command:
   ```bash
   python main.py
   ```

---

## 🕹️ Application Menu Interface

When you launch the script, you will interface with the following terminal options:

```text
Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit
Enter your choice: 
```
