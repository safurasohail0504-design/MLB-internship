import json
with open("students.json","r")as file:
    student=json.load(file)
new_student={
    "name":"laiba",
    "depart":"AI",
    "session":2021,
    "age":20
}
student.append(new_student)
with open("students.json","w")as file:
    json.dump(student, file)