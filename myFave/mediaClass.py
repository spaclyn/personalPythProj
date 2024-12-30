"""
File name: mediaClass.py

Purpose: This file constructs, defines, and gets my media class to be used with my character file

Special Requirement for this file:
    a. Each class must have three or more properties, with at least two different types of properties
    (string, integer, floating point, Boolean, ...)
    b. One of the properties of a class is an object instance of another class.
    c. All properties are of significance to the object.
    d. Constructors and str methods are defined correctly. 
    e.Have an executable file to demonstrate the object creation and the use of at least one getter,
    one setter and one action method. Program runs and generates meaningful outputs.

First Create Date: November 11, 2024
Last Update Date: 11/12, 2024
Author: Atiyah Ellerbee
Version: 3.10

"""

class Media:            #Media Class created
    medName = "";
    medType = "";
    medCreate = "";

    #Constructors Code Block
    def __init__(self, mn, mt, mc):     #INIT definted
        self.medName = mn;
        self.medType = mt;
        self.medCreate = mc;
    
    def __str__(self):
        return " My Favorite Character is from: " + self.medName + ". " + "It is a(n) " + self.medType + ", created in/on " + self.medCreate;
        
    #SETTERS code block
    def setMedia(s, mn):
        s.medName = mn;

    def setType(s, mt):
        s.medType = mt;

    def setCreate(s, mc):
        s.medCreate = mc;

    #GETTERS code block
    def getMedName(s):
        return s.medName;

    def getMedType(s):
        return s.medType;

    def getMedCreate(s):
        return s.medCreate;