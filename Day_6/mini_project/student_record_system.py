import json
try:
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = []
except json.JSONDecodeError:
    students = []
    print("JSON file error. Starting with empty records.")
print("\nADD STUDENT")
try:
    name = input("Enter name: ")
    rollno = int(input("Enter roll no: "))
    department = input("Enter department: ")
    session = input("Enter session: ")
    age = int(input("Enter age: "))
    student = {
        "name": name,
        "rollno": rollno,
        "department": department,
        "session": session,
        "age": age
    }
    students.append(student)
    with open("students.json", "w") as file:
        json.dump(students, file)
    print("Student added successfully")
except ValueError:
    print("Invalid input! Roll number and age must be numbers")
print("\nSEARCH STUDENT")
try:
    search_roll = int(input("Enter roll number to search: "))
    found = False
    for student in students:
        if student["rollno"] == search_roll:
            print("Student found:")
            print(student)
            found = True
            break
    if found == False:
        print("Student not found")
except ValueError:
    print("Invalid roll number")
print("\nUPDATE STUDENT")
try:
    update_roll = int(input("Enter roll number to update: "))
    found = False
    for student in students:
        if student["rollno"] == update_roll:
            print("Old record:")
            print(student)
            student["name"] = input("Enter new name: ")
            student["department"] = input("Enter new department: ")
            student["session"] = input("Enter new session: ")
            student["age"] = int(input("Enter new age: "))
            found = True
            break
    if found:
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)
        print("Student updated successfully")
    else:
        print("Student not found")
except ValueError:
    print("Invalid input")
print("\nDELETE STUDENT")
try:
    delete_roll = int(input("Enter roll number to delete: "))
    found = False
    for student in students:
        if student["rollno"] == delete_roll:
            students.remove(student)
            found = True
            break
    if found:
        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)
        print("Student deleted successfully")
    else:
        print("Student not found")
except ValueError:
    print("Invalid roll number")
print("\nFinal Student Records:")
for student in students:
    print(student)