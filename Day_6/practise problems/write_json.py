import json
students=[
    {"name":"safura","depart":"cs", "session":2024, "age":21
     },
    {"name":"eman","depart":"se", "session":2023, "age":22
     }
]
with open("students.json","w")as file:
    json.dump(students,file)