"""
Purpose:
   This file is the utilities file to Lab 5. In this file there will be a function with a for loop that parses a string for information.
   There should be 10 book titles with information that can be pulled when sucessfully ran in the excutable. It includes a way to search
   and calculate the files. It should also use the len(function)
   **~THIS IS THE UTILITY FILE~**

Problem description:
    "Create and Design a program that can be solved using while loops or for loops (or both) and string operations. The program will
    process a long string with a fixed structure, whose parts are separated using specific characters. The string will contain at least
    five objects of the same kind, and use a structure to describe the objects. The program will search through the string and perform at
    least two types of operations. One about string operations such as searching or encrypting, and another performing mathmatical computations
    such as finding the average total or largest value. Your prgram should simulate a real world scenario."

Special Requirement for this file only:
   The file must have a while or for loop and string operations. Has at least 5 objects of the same kind or 10 books. Contain a function that has
   two operations. Cannot use split(), rsplit(), splitlines(), built in functions. **~~ DIDN'T USE ANY USED MY OWN LOGIC USING THE SEPARATOR; DEFINING IT AS | AND ;~~** The file has to run.

First Create Date: September  27, 2024
Last Update Date: 10/1, 2024
Author: Atiyah Ellerbee
Version: 3.10
"""
# UTILITIES RELATED TO BOOK FUNCTIONS

# HEADER PRINT CODE BLOCK. Didn't want to deal with triple quotes or newlines so I just did it like this
def headerAtica():
    print("Hello World! This is a barebones Ray Bradbury Directory.");
    print("This directory will give you the function to search for 10 books.");
    print("Hint one has 451 in it. One of them is Clive Barker children's book");

# BOOK DEFINING. defines the books with ';' as a seperator for details of the sub-substring and | for the substrings
def takeBooks(bookString, separator=';'):
    fields = [];
    currBook = '';

    for char in bookString:
        if char == separator:                       # If separator found, add the current field
            fields.append(currBook.strip());
            currBook = '';                          #RESET HERE
        else:
            currBook += char;                       #BUILDS BOOK INFORMATION
    fields.append(currBook.strip());                #ADDS TO FIELDS
    return fields;

# EXTRACTING THE BOOKS DEFINED BEFORE. locates the whole substring with | defining where one information starts and stops
def extractBooks(bookDataStr, bookSeparator='|'):
    books = [];
    beginBook = 0;

    # For Loop that detects and trims the substrings!!!!
    for i in range(len(bookDataStr)):
        if bookDataStr[i] == bookSeparator or i == len(bookDataStr) - 1:                 #Learned how to use len dynamically through stackoverflow and w3 schools class recording
            if i == len(bookDataStr) - 1:                                                #Include the last character if no trailing '|'
                i += 1;
            books.append(bookDataStr[beginBook:i].strip());
            beginBook = i + 1;                                                          #Resets the whole thing at the start of the next book.
    return books;

#CALCULATE THE AVERAGE OF THE BOOKS. unfortunately not displayed outside of the loop. might be able to do that later
def avgPrice(books):
    totPrice = 0;
    countBooks = 0;

    for book in books:
        details = takeBooks(book, separator=';');

        #INSIDE OF MY FOR LOOP, THIS WILL CHECK THAT ALL FIELDS ARE THERE
        if len(details) == 6:
            i = 0;
            price = float(details[i+5]);
            totPrice += price;
            countBooks += 1;

    #Finds, Calculates, and determines the average of my books! Works Yippie!
    if countBooks > 0:
        return totPrice / countBooks;
    else:
        return None;  # In case there are no books to average

#SEARCH NEW? had to take out the details[1] etc
def bookByTitle(books, srchBook):                       #defines my BOOKS and how to search for them when using user input
    for book in books:
        details = takeBooks(book, separator=';')        #defines my takebooks easily as the details subvariable, which allows the book details to be indexed like this

        # If the title matches the search term, return the book details
        if srchBook.lower() == details[0].lower():      #.lower parses the strings in lowercase format and the search. might be better way to do this
            i = 0;
            return {
                'Title': details[0],
                'Author': details[i + 1],
                'Publisher': details[i + 2],
                'ISBN': details[i + 3],
                'LANGUAGE': details[i + 4],
                'Price': float(details[i + 5])
            }