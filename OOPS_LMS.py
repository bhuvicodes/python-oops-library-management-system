import datetime

class LMS:
    """
    This class is used to keep records of the books library.
    It has total four module : "Display Books", "Issue Books", "Return Books", "Order Books"
    """

    def __init__(self, list_of_books, library_name):
        self.list_of_books = "List_of_books.txt"
        self.library_name = library_name
        self.books_dict = {}
        id = 101

        with open(self.list_of_books) as bk:
            content = bk.readlines()
        
        for line in content:
            self.books_dict.update({
                str(id):{"Books_title":line.replace("\n", ""), 
                "Lender_name":"", "Issue_data":"", "Status":"Available"}
                })
            id += 1
             
    # Displays all the books
    def display_books(self):
        print("--------------------List Of Books--------------------")
        print("Books ID", "\t", "Title")
        print("-----------------------------------------------------")
        
        for key, value in self.books_dict.items():
            print(key, "\t\t", value.get("Books_title"), "- [", value.get("Status"), "]")

    # Issues a book to a person
    def issue_books(self):
        book_id = input("Enter the Book ID: ")
        current_date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        if book_id in self.books_dict.keys() and not self.books_dict[book_id]["Status"] == "Available":
            print(f"This book is already issued to {self.books_dict[book_id]['Lender_name']} on {self.books_dict[book_id]['Issue_date']}")
        
        elif book_id in self.books_dict.keys() and self.books_dict[book_id]["Status"] == "Available":
            your_name = input("Enter your name: ")
            self.books_dict[book_id]["Lender_name"] = your_name
            self.books_dict[book_id]["Issue_date"] = current_date
            self.books_dict[book_id]["Status"] = "Already Issued"
            print("Book issued successfully!!!")

        else:
            print("Book not found :((")
            return self.issue_books()

    # Adds a book in the library
    def add_books(self):
        new_book = input("Enter the title: ")
        if new_book == "":
            return self.add_books()

        elif len(new_book) > 25:
            print("Book's title length is too long! Title's length must be less than 25 characters")
            return self.add_books()

        else:
            with open(self.list_of_books, "a") as bk:
                bk.writelines(f"{new_book}\n")
                self.books_dict.update({str(int(max(self.books_dict)) + 1):{"Books_title":new_book, "Lender_name":"",
                "Issued_date":"", "Status":"Available"}})

                print(f"{new_book} has been added successfully!!!")
                return self.display_books

    # Returns the book back to the library
    def return_books(self):
        book_id = input("Enter the Book ID: ")
        if book_id in self.books_dict.keys() and self.books_dict[book_id]["Status"] == "Available":
            print(f"This book is already available in the library. Please check your book ID!")
            return self.return_books()
        
        elif book_id in self.books_dict.keys() and not self.books_dict[book_id]["Status"] == "Available":
            self.books_dict[book_id]["Lender_name"] = ""
            self.books_dict[book_id]["Issue_date"] = ""
            self.books_dict[book_id]["Status"] = "Available"
            print("Successfullty returned!!!")

        else:
            print("Book ID not found!!! Please check you book ID")
            return self.return_books()