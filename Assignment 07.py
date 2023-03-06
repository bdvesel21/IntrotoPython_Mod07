# ------------------------------------------------- #
# Title: Pickling and Error Handling
# Description: An example of storing data in a binary file and genertaing custom errors
# ChangeLog: (Who, When, What)
# Brittany Vesel, 03/02/2023, Created Script
# ------------------------------------------------- #

# Pickling Data Example
# import pickle
#
# # Data -------------------------------------------- #
# FileName = 'Books.dat'
# lstBooks = []
#
# # Pickling -------------------------------------- #
# book_id = int(input("Enter an ID: "))
# book_title = str(input("Enter the title of a book: "))
# book_author = str(input("Enter the name of the author: "))
# lstbooks = [book_id, book_title, book_author]
# print(lstbooks)
# print()
#
# # Store the Pickled list
# objFile = open("books.dat", "wb")
# pickle.dump(lstbooks, objFile)
# objFile.close()
# print("List Pickled")
# print()
#
# #Retreive the Pickled List
# print("Unpickling List")
# objFile = open("books.dat", "rb")
# book1 = pickle.load(objFile)
# objFile.close()
# print(book1)
# print()

# Error Handling -------------------------------------- #
# try:
#     str(input("Enter your favorite number: "))
#     print(favorite_number)
#
# except NameError as e:
#     print("Variable 'favorite_number' not found")
#     print("Python exception explanation: ", e)

# Combining Pickling and Error Handling  -------------------------------------- #
import pickle

# Data -------------------------------------------- #
FileName = 'Books.dat'
lstBooks = []

# Pickling -------------------------------------- #
try:
    book_id = int(input("Enter an ID: "))
    book_title = str(input("Enter the title of a book: "))
    book_author = str(input("Enter the name of the author: "))
    lstbooks = [book_id, book_title, book_author]
    print(lstbooks)
    print()
except Exception as e:
    print("There was an error! Please check that you are using integers for IDs.")
    print("Python Exception Explanation: ", e)

# Store the Pickled list
try:
    objFile = open("books.dat", "ab")
    pickle.dump(lstbooks, objFile)
    objFile.close()
    print("List Pickled")
    print()
except Exception as e:
    print("Python Exception Explanation: ", e)

# #Retreive the Pickled List
try:
    print("Unpickling List")
    objFile = open("books.dat", "rb")
    book1 = pickle.load(objFile)
    objFile.close()
    print(book1)
    print()
except FileNotFoundError as e:
    print("The file must exist before reading it!")
    print("Python Exception Explanation: ", e)
except Exception as e:
    print("There was an error!")
    print("Python Exception Explanation: ", e)