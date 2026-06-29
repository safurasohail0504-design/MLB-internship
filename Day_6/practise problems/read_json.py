import json
with open("students.json","r")as file:
    read=json.load(file)
print(read)