import json
class libraryItem:
    def __init__(self,title,id,status):
        self.title=title
        self.id=id
        self.status=status
    def display(self):
        print("item-info:")
        print(self.title)
        print(self.id)
        print(self.status)
class book(libraryItem):
    def __init__(self, title, author, id, status):
        super().__init__(title, id, status)
        self.author = author
    def display(self):
        super().display()
        print(self.author)
class library:
    def __init__(self):
        self.book=[] 
    def add_book(self):
        new_title = input("enter title:")
        new_author = input("enter author:")
        new_id = input("enter id:")
        new_status = input("enter status:")
        new_book=book(new_title,new_author,new_id,new_status)
        self.book.append(new_book)
    def view_book(self):
        if len(self.book) == 0:
            print("no books in library")
        for b in self.book:
            b.display()
    def search_book(self):
        is_found=False
        search_title=input("enter title to search:")
        for b in self.book:
            if(search_title==b.title):
                is_found=True
                b.display()
                break
        if(is_found==False):
            print("book not found")
    def borrow_book(self):
        borrow_title=input("enter title to borrow:")
        is_found=False
        for b in self.book:
            if(borrow_title==b.title):
                is_found=True
                if(b.status=="borrowed"):
                    print("book not available")
                else:
                    b.status="borrowed"
                    print("book borrowed")
                break
        if(is_found==False):
            print("book not found")
    def return_book(self):
        return_title=input("enter title to return:")
        is_found=False
        for b in self.book:
            if(return_title==b.title):
                is_found=True
                if(b.status=="available"):
                    print("never borrowed")
                else:
                    b.status="available"
                break
        if(is_found==False):
            print("book not found")
    def load_from_json(self):
        try:
            with open("book.json", "r")as file:
                data=json.load(file)
            for d in data:
                new_book=book(d["title"], d["author"], d["id"], d["status"])
                self.book.append(new_book)
        except FileNotFoundError:
            self.book=[]
    def save_to_json(self):
        book_list=[]
        for b in self.book:
            d={
                "title":b.title,
                "author":b.author,
                "id":b.id,
                "status":b.status
            }
            book_list.append(d)
        with open("book.json","w")as file:
            json.dump(book_list,file)

l1=library()
l1.load_from_json()
num_books=int(input("no of books to add:"))
for i in range(num_books):
    l1.add_book()
l1.save_to_json()
l1.borrow_book()
l1.save_to_json()
l1.return_book()
l1.save_to_json()
l1.view_book()
l1.search_book()
