class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following book in our library :{self.name}")
        for book in self.booklist:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender-Book Database has been updated, You can Take the book now ")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBook(self, book):
        self.booklist.append(book)
        print("Book has been added to the book list")

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == "__main__":
    vikram = Library([
        'python', 'Rich Daddy poor Daddy',
        'Harry Potter',
        'C++ Basics',
        'Algorith by vikram'
    ], "vikram singh")
    while(True):
        print(
            f"Welcome to the {vikram.name} Library . Enter your choice to continue")
        print("1. Dispaly Books")
        print("2. lend a book")
        print("3. add a book")
        print("4. return a book")
        user_choice = input("Enter Your Choive ")
        if user_choice not in ['1', '2', '3', '4', 'exit', 'q']:
            print("Please Enter your valide number")
            continue
        elif user_choice in ['exit', 'q']:
            exit()
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            vikram.displayBooks()
        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend : ")
            user = input("Enter your name")
            vikram.lendBook(user, book)
        elif user_choice == 3:
            book = input("Enter the name of the book you wan tto add")
            vikram.addBook(book)
        elif user_choice == 4:
            book = input("Enter the name of the book you wan tto retrunt")
            vikram.returnBook(book)
        else:
            print("Not a Valid option")
        print("press q to quit and c to continue")
        user_choice2 = ""
        while(user_choice2 != "c" and user_choice2 != "q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                continue
