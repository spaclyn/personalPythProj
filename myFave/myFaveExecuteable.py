"""
File name: AELab8Executeable.py
Purpose:
    this file is the source file that will import a pre-processed CSV file and
    write another file with the information in a 2-d array that should output a new
    column, header, and then put everything in the aforementioned CSV file

Problem description:
    "Think of a scenario when you will need to define at least two classes to implement. Define at least two
    classes that are related to each other, e.g. one class definition must use the object defined in another
    class, like the Address class and the Employee class used in the class demo. Define the class files, and
    create an executable file to demonstrate object-oriented programming."

Special Requirement for this file:
    a. Each class must have three or more properties, with at least two different types of properties
    (string, integer, floating point, Boolean, ...)
    b. One of the properties of a class is an object instance of another class.
    c. All properties are of significance to the object.
    d. Constructors and str methods are defined correctly. 
    e.Have an executable file to demonstrate the object creation and the use of at least one getter,
    one setter and one action method. Program runs and generates meaningful outputs.

First Create Date: November 11, 2024
Last Update Date: 11/19, 2024
Author: Atiyah Ellerbee
Version: 3.10

"""
from mediaClass import Media;
from characterClass import Character;
from villainClass import Villain;

#Create Media Object(s)
mediaOne = Media("Jujutsu Kaisen","AniManga","2020");
mediaTwo = Media("Jojo's Bizarre Adventure", "AniManga", "1995");
mediaThree = Media("Fantastic Four", "Film", "2023");

#Create A Villain Object
villain = Villain("Dr. Doom", 45, "Male", 75, mediaThree, 90, "Mr. Fantastic");

# Display the Villain details
print(villain);  # Calls the Villain's __str__, overriding the Character's __str__
print('\n');

#Changing Parent Property through a setter
villain.setName("Doctor Victor Von Doom");  # Using Character's setter method
print(villain);
print('\n');

# Increase evilness
villain.increase_evilness(10)
print('\n')

#Changing Villain child through Setter 
villain.set_evilness(200);  # Using Villain's setter method
print(f"Updated Evilness: {villain.evilness}");
print('\n');

#Create Character Object
charaOne = Character("Gojo Satoru", 28, "male", 50000, mediaOne); 
print(charaOne);
print('\n');

#Get Examples
charaOne.heatUP(100);
print(charaOne.getHotness());

print('\n');

print("Getting Character One's Name:");
print(charaOne.getName());

print('\n');

#Create ANOTHER Object
charaTwo = Character("", 30, "male", 100, mediaTwo);
charaTwo.setName("Jotaro Kujo");                #setter example
print(charaTwo)