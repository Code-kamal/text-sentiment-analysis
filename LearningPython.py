# class LibraryItem:
#     def __init__(self, id, title):
#         self.id = id
#         self.title = title
#         self.available = True
#
#     def info(self):
#         print(self.id)
#         print(self.title)
#
#     def borrow(self):
#         self.available = False
#
#     def return_item(self):
#         self.available = True
#
# class Book(LibraryItem):
#     def __init__(self, id, title, author):
#         super().__init__(id, title)
#         self.author = author
#
#     def info(self):
#         print(self.id)
#         print(self.title)
#         print(self.author)
#
# class DVD(LibraryItem):
#     def __init__(self, id, title, duration):
#         super().__init__(id, title)
#         self.duration = duration
#
#     def info(self):
#         print(self.id)
#         print(self.title)
#         print(self.duration)
#
# class Magazine(LibraryItem):
#     def __init__(self, id, title, issue):
#         super().__init__(id, title)
#         self.issue = issue
#
#     def info(self):
#         print(self.id)
#         print(self.title)
#         print(self.issue)
#
# class Member:
#     def __init__(self, name):
#         self.name = name
#         self.borrowed_items = []
#
# class Library:
#
#     def __init__(self):
#         self.items = []
#         self.members = []
#     def add_item(self, item):
#         self.items.append(item)
#
#     def add_member(self, member):
#         self.members.append(member)
#
#     def borrowed_item(self, member, id):
#         for item in self.items:
#             if item.id == id and item.available:
#                 item.borrow()
#                 for mem in self.members:
#                     if mem.name == member:
#                         mem.borrowed_items.append(item)

# Project number FIVE

# class InvalidEmployeeError(Exception):
#     pass
#
# class Employee:
#     TAX_RATE = 0.10
#     def __init__(self, name):
#         self.name = name
#
#     def calculate_salary(self):
#         raise NotImplementedError("This method has to implemented by its subclass")
#
#     def get_net_salary(self):
#         gross = self.calculate_salary()*TAX_RATE
#         return self.calculate_salary() - gross
#
# class FullTimeEmployee(Employee):
#     def __init__(self, name, base_salary, bonus = 0):
#         super().__init__(name)
#         self.base_salary = base_salary
#         self.bonus = bonus
#
#     def calculate_salary(self):
#         return self.base_salary + self.bonus
#
# class PartialTimeEmployee(Employee):
#     def __init__(self, name, hourly_rate, hours_worked):
#         super().__init__(name)
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked
#
#     def calculate_salary(self):
#         return self.hourly_rate * self.hours_worked
#
# class Freelancer(Employee):
#     def __init__(self, name, project_fee):
#         super().__init__(name)
#         self.project_fee = project_fee
#
#     def calculate_salary(self):
#         return project_fee
#
# class CommissionEmployee(Employee):
#     def __init__(self, name,base_salary, commmission_rate, total_sales):
#         super().__init__(name)
#         self.commmission_rate = commmission_rate
#         self.total_sales = total_sales
#         self.base_salary = base_salary
#
#     def calculate_salary(self):
#         return self.base_salary + self.commmission_rate*self.total_sales
#
# class PayrollSystem(Employee):
#     def __init__(self, employees):
#         self.employees = []
#
#     def add_employee(self, employee):
#         if not isinstance(employee, Employee):
#             raise TypeError("employee must be an instance of Employee")
#         # You can also us this if type(employee) == Employee
#         # also use raise InvalidEmployeeError("کارمند نامعتبر است")
#         self.employees.append(employee)
#
#     def show_payroll(self):
#         for employee in self.employees:
#             print(f"{employee.name}'s payroll is {employee.calculate_salary()}, {employee.get_net_salary()}")
#
#     def total_cost(self):
#         return sum(employee.get_net_salary() for employee in self.employees)

# Project Six
# import json
# import datetime
# class Book:
#     def __init__(self, book_id: int, title: str, author: str, publication_date: str):
#
#         if not isinstance(book_id, int):
#             raise TypeError("book_id must be an integer")
#
#         if not isinstance(title, str):
#             raise TypeError("title must be a string")
#
#         if not isinstance(author, str):
#             raise TypeError("author must be a string")
#
#         if not isinstance(publication_date, str):
#             raise TypeError("publication_date must be a string")
#
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.publication_date = publication_date
#         self.is_available = True
#         self.borrowed_by = None
#
#     def __str__(self):
#         status = "Available" if self.is_available else "Not available"
#         return f"""ID: {self.book_id}
#                    Title: {self.title}
#                    Author: {self.author}
#                    Publication Date: {self.publication_date}
#                    Status: {status}"""
#
#     def change_status(self):
#         self.is_available = True if self.is_available == False else False
#
#     def to_dict(self) -> dict:
#         return {
#             "book_id": self.book_id,
#             "title": self.title,
#             "author": self.author,
#             "publication_date": self.publication_date,
#             "is_available": "Available" if self.is_available else "Not available"
#         }
#
#     def from_dict(cls, data: dict):
#         book = cls(data["book_id"], data["title"], data["author"], data["publication_date"])
#         book.is_available = True if data["is_available"] == "Available" else False
#         return book
#
# class Member:
#     def __init__(self, member_id: int, member_name: str, member_email: str):
#         if not isinstance(member_id, int):
#             raise TypeError("member_id must be an integer")
#         if not isinstance(member_name, str):
#             raise TypeError("member_name must be a string")
#         if not isinstance(member_email, str):
#             raise TypeError("member_email must be a string")
#
#         self.member_id = member_id
#         self.member_name = member_name
#         self.member_email = member_email
#         self.borrowed_books = []
#         self.borrowing_history = []
#
#     def __str__(self):
#         return f"""ID: {self.member_id}
#                    Name: {self.member_name}
#                    Email: {self.member_email}"""
#
#     def can_borrow(self, max_borrow:int = 3) -> bool:
#         return True if len(self.borrowed_books) < max_borrow else False
#
#     def borrow_book(self, book_id: int):
#         if not isinstance(book_id, int):
#             raise TypeError("book_id must be an integer")
#         if book_id not in self.borrowed_books:
#             self.borrowed_books.append(book_id)
#             now = datetime.datetime.now()
#             self.borrowing_history.append({now : book_id})
#
#     def return_book(self, book_id: int):
#         if not isinstance(book_id, int):
#             raise TypeError("book_id must be an integer")
#         if book_id in self.borrowed_books:
#             self.borrowed_books.remove(book_id)
#
#     def to_dict(self) -> dict:
#         return {
#             "member_id": self.member_id,
#             "member_name": self.member_name,
#             "member_email": self.member_email,
#             "borrowed_books": self.borrowed_books,
#             "borrowing_history": self.borrowing_history
#         }
#
#     def from_dict(cls, data: dict):
#         member = cls(data["member_id"], data["member_name"], data["member_email"])
#         member.borrowed_books = data["borrowed_books"]
#         member.borrowing_history = data["borrowing_history"]
#         return member
#
# class Transaction:
#     def __init__(self, transaction_id:int, book_id:int, member_id:int):
#         if not isinstance(transaction_id, int):
#             raise TypeError("transaction_id must be an integer")
#         if not isinstance(book_id, int):
#             raise TypeError("book_id must be an integer")
#         if not isinstance(member_id, int):
#             raise TypeError("member_id must be an integer")
#
#         self.transaction_id = transaction_id
#         self.book_id = book_id
#         self.member_id = member_id
#         self.borrow_date = datetime.datetime.today()
#         self.return_date = None
#         self.is_returned = False
#         self.fine_amount = 0.0
#
#     def return_book(self, days_late:int = 0, fine_per_day:int = 1000):
#         self.return_date = datetime.datetime.today()
#         self.is_returned = True
#
#         if days_late > 0:
#             self.fine_amount = fine_per_day*days_late
#
#     def to_dict(self) -> dict:
#         return {
#             "transaction_id": self.transaction_id,
#             "book_id": self.book_id,
#             "member_id": self.member_id,
#             "borrow_date": self.borrow_date,
#             "return_date": self.return_date,
#             "is_returned": "Returned" if self.is_returned else "Not returned",
#             "find_amount": self.fine_amount,
#         }
#
#     def __str__(self):
#         return f"""ID: {self.transaction_id}
#                    book ID: {self.book_id}
#                    member ID: {self.member_id}
#                    Borrowed Date: {self.borrow_date}
#                    Returned Date: {self.return_date}
#                    is_returned: {"Returned" if self.is_returned else "Not returned"}
#                    fine amount: {self.fine_amount}"""
#
#     def from_dict(cls, data: dict):
#         transaction = cls(data["transaction_id"], data["book_id"], data["member_id"])
#         transaction.is_returned = True if data["is_returned"] == "Returned" else False
#         transaction.fine_amount = data["fine_amount"]
#         transaction.return_date = data["return_date"]
#         transaction.borrow_date = data["borrow_date"]
#         return transaction
#
# class Library:
#     def __init__(self, name:str = "کتابخانه مرکزی"):
#         if not isinstance(name, str):
#             raise TypeError("name must be a string")
#
#         self.name = name
#         self.books = {} # {book id: Book}
#         self.transactions = {} # {transaction id: Transaction}
#         self.members = {} # {member id: Member}
#         self.next_book_id = 1
#         self.next_transaction_id = 1
#         self.next_member_id = 1
#
#     def add_book(self):
#         while True:
#             try:
#                 title = str(input("Please enter the book title: "))
#             except ValueError:
#                 print("Please enter a valid book title")
#
#         while True:
#             try:
#                 author = str(input("Please enter the author name: "))
#             except ValueError:
#                 print("Please enter a valid author name")
#
#         while True:
#             try:
#                 publication_date = str(input("Please enter the publication date: "))
#             except ValueError:
#                 print("Please enter a valid publication date")
#
#         self.books[next_book_id] = Book(next_book_id, title, author, publication_date)
#         self.next_book_id += 1
#         print("your book is now available!")
#
#     def add_member(self):
#         while True:
#             try:
#                 name = str(input("Please enter the member name: "))
#             except ValueError:
#                 print("Please enter a valid member name")
#
#         while True:
#             try:
#                 email = str(input("Please enter the member email: "))
#             except ValueError:
#                 print("Please enter a valid member email")
#
#         self.members[next_member_id] = Member(next_member_id, name, email)
#         self.next_member_id += 1
#         print("your member is now available!")
#
#     def find_book(self, search_term:str, search_by:str = "tile") -> list[Book]:
#         result = []
#         search_term = search_term.lower()
#         for book in self.books.values():
#             if search_by == "title" and search_term in book.title.lower():
#                 result.append(book)
#             elif search_by == "author" and search_term in book.author.lower():
#                 result.append(book)
#             elif search_by == "publication_date" and search_term in book.publication_date.lower():
#                 result.append(book)
#             else: print("Perhaps your search by is not true or your search term is not valid")
#
#         return result
#
#     def borrow_book(self, book_id:int, member_id:int):
#         if book_id in self.books.keys() and member_id in self.members.keys():
#             self.books[book_id].change_status()
#             self.books[book_id].borrowed_by = member_id
#             self.members[member_id].borrow_book(book_id)
#             self.transactions[next_transaction_id] = Transaction(next_transaction_id, book_id, member_id)
#             self.next_transaction_id += 1
#             print("book borrowed successfully!")
#
#         else: print("Your book id or member id is invalid")
#
#     def return_book(self, book_id:int, member_id:int):
#         if book_id not in self.books.keys():
#             return False
#
#         if member_id not in self.members.keys():
#             return False
#
#         if self.books[book_id].is_available or self.books[book_id].borrowed_by != member_id:
#             print("This book is not borrowed by this member")
#             return False
#
#
#
#         transaction_id = 0
#         for key, value in self.transactions.items():
#             if value.book_id == book_id and value.member_id == member_id:
#                 transaction_id = key
#                 break
#
#         self.books[book_id].change_status()
#         self.books[book_id].return_book(book_id)
#         self.members[member_id].return_book(book_id)
#         self.transactions[transaction_id].return_date = datetime.datetime.today()
#         days_late = self.transactions[transaction_id].return_date - self.transactions[transaction_id].borrow_date
#         if days_late > 0:
#             print(f"Your find is {self.transactions[transaction_id].return_book(days_late)}")
#
#         print(f"Your fine is {self.transactions[transaction_id].find_amount}")
#         print("book returned successfully!")


def fourSum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()
    if len(nums) < 4:
        return []
    result = []
    left1, left2 = 0, 1
    right1, right2 = len(nums) - 1, len(nums) - 2
    while left2 < right2:
        total = nums[left1] + nums[left2] + nums[right2] + nums[right1]
        if total == target:
            result.append([nums[left1], nums[left2], nums[right2], nums[right1]])
            if left2 - left1 >= 2:
                left1 += 1
            else:
                left2 += 1
        elif total < target:
            if left2 - left1 >= 2:
                left1 += 1
            else:
                left2 += 1
        else:
            if right1 - right2 >= 2:
                right1 -= 1
            else:
                right2 -= 1
    return result

print(fourSum([-5,-4,-3,-2,-1,0,1,2,3,4,5], 0))


























