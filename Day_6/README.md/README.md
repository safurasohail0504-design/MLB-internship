# Student Record Management System
This project is a simple Student Record Management System built using Python.
The purpose of this project was to practice file handling and working with JSON data.
The system allows users to:
- Add student records
- Search student records
- Update existing student information
- Delete student records
- Save all changes permanently in a JSON file
## What I Learned Today
Today I learned how to work with files in Python and how to store structured data using JSON.
### File Handling:
- Opening files using `open()`
- Reading data from files using `r` mode
- Writing data into files using `w` mode
- Using the `with` statement to automatically close files
- Handling missing files using exception handling
### JSON in Python:
- Understanding what JSON is and why it is used
- Converting Python dictionaries/lists into JSON format
- Saving Python data using `json.dump()`
- Reading JSON files using `json.load()`
- Loading JSON data back into Python objects
## How File Handling and JSON Work Together
File handling is used to create, read, and update the JSON file.
When the program starts, it checks if the JSON file already exists.
If the file exists, the program reads the stored student records using:
python
json.load()

Challenges Faced:
During implementation, I faced some challenges:
Understanding the difference between Python dictionaries/lists and JSON format.
Managing JSON file reading when the file did not exist.
This was solved using exception handling: 
try:
    with open("students.json","r")
except FileNotFoundError:
Updating and deleting records required searching through the list of dictionaries and modifying the correct student record.
Handling invalid inputs such as entering text instead of numbers.
This was solved using try-except blocks to prevent the program from crashing.
Technologies Used:
Python
JSON
File Handling
Conclusion:
This project helped me understand how real-world applications store and manage data permanently.
Using JSON with file handling allows Python programs to save information and retrieve it whenever needed.
