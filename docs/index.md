**Assignment 07 – Files and Exceptions** 

**Introduction**
 
This week in Foundations of Programming: Python we focused on using the incorporated pickling function in Python, writing and reading to binary files, and creating custom exception messages. The homework was also more involved this week as we had to research our own explanations online for how certain aspects of the program work.
 
**Pickling**

Pickling is a processing module included in the Python language that packs data into a simple binary file of 0s and 1s. This helps store large data sets or databases in a smaller format and can be packed and unpacked on many different machine types and systems. The first step of our assignment was to find a webpage we liked that we thought explained the process well. I chose https://www.tutorialspoint.com/python-pickling because not only did it use simple examples to help understand the concepts, it included potential errors for the process in case I ran into them creating my own program. In this way, it helped me prepare better for the assignment and what errors I could see when I moved on the exception handling part of the assignment. 

_Figure 1: Pickle Display Code_
~~~
Pickling Data Example
import pickle

# Data
FileName = 'Books.dat'
lstBooks = []

# Pickling
book_id = int(input("Enter an ID: "))
book_title = str(input("Enter the title of a book: "))
book_author = str(input("Enter the name of the author: "))
lstbooks = [book_id, book_title, book_author]
print(lstbooks)
print()

# Store the Pickled list
objFile = open("books.dat", "wb")
pickle.dump(lstbooks, objFile)
objFile.close()
print("List Pickled")
print()

#Retreive the Pickled List
print("Unpickling List")
objFile = open("books.dat", "rb")
book1 = pickle.load(objFile)
objFile.close()
print(book1)
print()
~~~
After watching the lectures and reading the course book, I decided to try to build my own pickling code using a list based on books, shown in Figure 1 above. First, I imported the pickle module at the top of the program. I then asked the user for an ID number, a book title and an author name, then stored that data as a list in memory. This was code we have been using for many weeks now, but it was fun to configure it for my own interest. Next in the code came the file writing via the pickling method. I opened the file using “wb” for binary write, dumped the list inside the file, then closed the list before displaying a message to the user. Once that was completed, I wrote the program to continue by displaying a message to the user that it would unpickle the list. I opened the file using the binary read feature, assigned the created line to the book1 variable, and then closed the file. I then displayed the book1 list values to the user to finish off the pickle display method. The output of the pickle display is shown in Figure 2.

_Figure 2: Pickle Display Output_

![image](https://user-images.githubusercontent.com/94942326/223216837-5484f457-8626-44b2-a513-23c34f86ac19.png)

**Exception Handling**

Handling exceptions is when the programmer tries to predict what potential problems could result from the code or user input and try to either negate them or explain as the program runs for the user. The second part of this week’s assignment started with researching exception handling in Python and creating custom error messages. For exception handling, I actually liked the Python documentation (https://docs.python.org/3/tutorial/errors.html ), as it not only gave explanations and examples of potential errors, it also linked to a complete list of errors you could see and read about. 

_Figure 3: Exception Handling Code_
~~~
Error Handling
try:
    str(input("Enter your favorite number: "))
    print(favorite_number)

except NameError as e:
    print("Variable 'favorite_number' not found")
    print("Python error explanation: ", e)
~~~

After watching the lectures and reading the book, I picked the NameError exception from the list in the textbook to display in the exception handling part of my code. I initially wrote code asking for the user to input their favorite number but didn’t assign it to a variable. When I asked the program to print that number to the user again, it returned an exception. Figure 3 shows the code I initially wrote, and Figure 4 is the output in Pycharm. 

_Figure 4: Output in Pycharm_

![image](https://user-images.githubusercontent.com/94942326/223216874-15bfe810-d03c-4af6-9896-f2cd39298916.png)

**Combining Pickling and Error Handling**

The final assignment was to combine the two into one program. I cut my code into pieces and tried to implement a potential exception on each part. To display a different exception that was also in the text book, I chose to create an exception handling block for if the user input a non-integer character for the ID. I chose to display my own customer error, and then add a second line to include the Python Exception Explanation, shown in Figure 5.

_Figure 5: Initial User Input Exception Handling_
~~~
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
~~~

Next, I copied the code to save the list into a pickled binary file. I added the try and except block around that code to display if there was an error saving the file. I don’t know if there are potential errors with this but thought it would be best to include it anyway. This code is shown in Figure 6. 

_Figure 6: Pickling the List with Exception Handling_
~~~
try:
    objFile = open("books.dat", "ab")
    pickle.dump(lstbooks, objFile)
    objFile.close()
    print("List Pickled")
    print()
except Exception as e:
    print("Python Exception Explanation: ", e)
~~~

The last part of the program was to create exeception handling around the reading of the pickled binary file. This was displayed in Randall Root’s notes, so I did use his code as a reference to create my own exception handling here. I added a FileNotFoundError exception to display text to the user, as well as a general exception error in case something else went wrong. Figure 7 shows the code for error handling while retrieving a pickled list, while Figures 8 and 9 show the code running without exceptions in Pycharm and the Command Prompt. 

_Figure 7: Retrieving a Pickled List with Exception Handling_
~~~
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
~~~

_Figure 8: Output in Pycharm_
 ![image](https://user-images.githubusercontent.com/94942326/223216910-8aa06970-edb8-429c-8e8a-fdbb42131a3d.png)

_Figure 9: Output in Command Prompt_
![image](https://user-images.githubusercontent.com/94942326/223216931-88c03c7c-f086-4cb5-bae8-2f11b3238d30.png) 

Conclusion

This week’s assignment was slightly more difficult because we had to start the code on our own and assimilate knowledge from not only the textbook and lectures, but what we could research online about the topics. I didn’t have many wrong turns in the code this week not working, because I was modifying code examples from Randall Root’s notes and the internet. If anything, my most common mistake is forgetting to put the print strings in quotations and forgetting colons after certain commands like try or else. Luckily, Python is very good at explaining what I missed on those occasions. As I obtain more experience writing Python, I hope those little errors go away and I move on to trying to debug bigger issues with my syntax. 
