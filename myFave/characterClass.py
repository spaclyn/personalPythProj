"""
File name: characterClass.py

Purpose: This file constructs, defines, and gets my character class to be used with my executable for lab 8

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

class Character:                        #Character Class Defintion
    charaName = "";
    age = "";
    gender = "";
    hotness = "";

    #Definition Code Block
    def __init__(char, n, a, g, h, m):         #INIT definition
        char.charaName = n;
        char.age = a;
        char.gender = g;
        char.hotness = h;
        char.mediaType = m;

    def __str__(char):
        return (
        f"My Favorite Character is: {char.charaName}. "
        f"They are {char.gender} and {char.age} years old. "
        f"I personally find them this hot: {char.hotness}%. "
        f"{char.mediaType}"
        );

    #SETTERS code block
    def setName(c, n):
        c.charaName = n;

    def setAge(c, a):
        c.age = a;

    def setGender(c, g):
        c.gender = g;

    def setHotness(c, h):
        c.hotness = h;

    #GETTERS code block
    def getName(c):
        return c.charaName;

    def getAge(c):
        return c.age;

    def getGender(c):
        return c.gender;

    def getHotness(c):
        return c.hotness;

    #MISC DEFINTIONS BLOCK

    def getMedia(self):
        return "My Favorite Character is from: " + self.medName + ". " + "It is a(n) " + self.medType + ", created in/on" + self.medCreate;

    def heatUP(c, level):
        c.hotness = c.hotness + level;
        print("Hotness level updated: ");