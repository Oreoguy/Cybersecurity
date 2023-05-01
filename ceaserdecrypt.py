# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 10:20:50 2023

@author: Vansh
"""

def decrypt(string, shift):
    cipher=''
    for char in string:
        if char == '':
            cipher= cipher+char
        elif char.isupper():
            cipher= cipher + chr(((ord(char)-shift-65))% 25+65)
        else :
            cipher = cipher + chr(((ord(char)-shift - 97))% 25+97)
    return cipher

PT= input("Enter the string :")
Key=int(input("Enter the shift or key"))
print("Text",PT)
print ("Decrypted Text",decrypt(PT,Key))
