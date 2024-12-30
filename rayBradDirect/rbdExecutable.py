"""
Purpose:
   This file is the utilities file to Lab 5. In this file there will be a function with a for loop that parses a string for information.
   There should be 10 book titles with information that can be pulled when sucessfully ran in the excutable. **~THIS IS THE EXECUTABLE FILE~**

Problem description:
    "Create and Design a program that can be solved using while loops or for loops (or both) and string operations. The program will
    process a long string with a fixed structure, whose parts are separated using specific characters. The string will contain at least
    five objects of the same kind, and use a structure to describe the objects. The program will search through the string and perform at
    least two types of operations. One about string operations such as searching or encrypting, and another performing mathmatical computations
    such as finding the average total or largest value. Your prgram should simulate a real world scenario."

Special Requirement for this file only:
   The file must have a while or for loop and string operations. Has at least 5 objects of the same kind. Contain a function that has
   two operations. The file has to run.

First Create Date: September  27, 2024
Last Update Date: 10/1, 2024
Author: Atiyah Ellerbee
Version: 3.10
"""
#IMPORTED rbdUtilities.PY

import rbdUtilities;

#BOOK DATA STRING DEFINITED
#ALL BOOKS ARE RAY BRADBURY BOOKS WITH A FEW OTHERS FOR FILLER
bookData = """
A Medicine For Melancholy; Ray Bradbury; Avon; 9780380730863; English; 9.82|
Abarat; Clive Barker; HarperCollins; 9780062094106; English; 7.99|
Absolute Midnight; Clive Barker; Harper; 9780007100485; English; 15.74|
Dandelion Wine; Ray Bradbury; Bantam Books; 97805553277537; English; 8.49|
Fahrenheit 451; Ray Bradbury; Simon & Schuster; 9781451673319; English; 17.00|
I Sing the Body Electric!; Ray Bradbury; William Morrow Paperbacks; 9780380789620; English; 13.59|
The Golden Apples of the Sun; Ray Bradbury; William Morrow Paperbacks; 9780380730391; English; 12.79|
The Illustrated Man; Ray Bradbury; Simon & Schuster; 9781451678165; English; 9.99|
The Lord Of The Rings; J.R.R. Tolkien; William Morrow Paperbacks; 9780544003415; English; 18.47|
The Martian Chronicles; Ray Bradbury; Simon & Schuster; 9781451678192; English; 6.99|
The Silmarillion; J.R.R. Tolkien; Del Rey; 9780345325815; English; 8.09|
Something Wicked This Way Comes; Ray Bradbury; Simon & Schuster; 9780671679600; English; 10.79|
""";                                                            #Using Triple Quotes here to allow for multi line formatting of my string data.

# DEFINING BOOKS AS MY EXTRACTBOOKS FUNCTION FROM ULTILITIES
books = AElab5utilities.extractBooks(bookData);

#the header for the information part of the file.
AElab5utilities.headerAtica();


#SEARCH THROUGH AND PRINT. CODE BLOCKS;
print("\n");
srchBook = input("Please Enter A Book Title: ");
book = AElab5utilities.bookByTitle(books, srchBook);

if book:                                                         #Prints my books in the correct format
    print("\n(!) Book Found:");                                  # not the {book['something']} it is defined once the loop is called in the utilities file
    print(f"Title: {book['Title']}");                            #calls my Title Index here
    print(f"Author: {book['Author']}");                          #calls my Author Index Here
    print(f"Publisher: {book['Publisher']}");                    #calls my Publisher Index here
    print(f"ISBN: {book['ISBN']}");                              #calls my ISBN Index here
    print(f"Language: {book['LANGUAGE']}");                      #calls my Language Index here
    print(f"Price: ${book['Price']:.2f}");                       #calls my Price Index Here
else:
    print(f"\nSorry dude, Book titled '{srchBook}' not found. Try again.");     #jokey here

# Defining my avgprice function in this file as the Utilities avgPrice; should return the average of all the books
avgPrices = AElab5utilities.avgPrice(books);

if avgPrices:
    print(f"\nAverage Price of all books: ${avgPrices:.2f}");    #W3Schools String Formating, fixed number w/ 2 decimals.
else:
    print("math is not real, there are no books to average.");                                    #if there is no average, because the string is empty then print this.
