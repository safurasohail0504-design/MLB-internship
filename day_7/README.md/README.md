Library Management System - OOP Project

What Object Oriented Programming Is

Object Oriented Programming, or OOP, is a way of organizing code around real world things called objects, instead of just writing one long sequence of instructions. Each object is created from a class, which acts like a blueprint describing what data the object holds and what actions it can perform. For example, in this project, a book is represented as an object that holds information like title, author, id, and status, and also knows how to display its own details.

OOP makes programs easier to manage and extend because related data and behavior are grouped together inside a class, rather than being scattered across many separate variables and functions. It also allows code reuse through a concept called inheritance, where one class can build on top of another instead of repeating the same code again.

Where Inheritance Was Used In My Project

In this project, I created a parent class called LibraryItem, which holds attributes that are common to anything stored in a library, such as title, id, and status, along with a display method to print this information.

The book class inherits from LibraryItem. Since every book also needs an author, which is not something every library item would necessarily have, I added that as an extra attribute specific to the book class. Inside the book class, I used super dot init to call the parent class constructor first, so the shared attributes get set up properly, and then I added the author attribute on top of that.

I also used method overriding in the book class. The display method in book calls the parent class display method first using super dot display, and then prints the additional author information. This way, the book class reuses the parent's logic instead of repeating it, while still adding its own extra detail.

Challenges Faced And How I Solved Them

One challenge I faced early on was mixing up the difference between a parameter name and an attribute stored using self. I once tried to access an attribute using the original parameter name instead of self dot name, which caused an attribute error. Once I understood that only self dot variables are actually stored on the object permanently, this became much clearer.

Another challenge was with my loop logic inside the search and borrow methods. At first, I placed my not found message inside the else block of the loop, which caused it to print multiple times whenever a non matching item was checked. I fixed this by moving the found check outside the loop, using a flag variable that only gets evaluated once the entire loop has finished running.

I also initially nested an if statement incorrectly inside the borrow method, which caused the program to wrongly update the status of unrelated books instead of only the one the user searched for. Fixing the indentation so that the status update only happened inside the matching condition solved this issue.

Working with JSON also took some adjustment. I learned that when saving data, I cannot directly save custom objects like book objects into a JSON file. Instead, I had to convert each object into a plain dictionary first, save the list of dictionaries, and then when loading the data back, manually recreate book objects from those dictionaries. I also added exception handling for the case where the JSON file does not exist yet, so the program does not crash the very first time it runs.

Overall, this project helped me understand how classes, inheritance, and JSON persistence work together to build a small but functional real world style application.
