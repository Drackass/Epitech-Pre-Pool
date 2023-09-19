# Basic functions

# Task 00
# def f(x):
#     return 2*x+1
# # print(f(5)) # 11: simple operation

# def g():
#     return 7
# # print(g(5)) # 7: return 7

# y = f(2) # get result of the f function with 2 in parameter
# print(y)
# y = f(5) + g() # do the sum of the 2 function f and g
# print(y) 

# # Task 01
# def bread():
#     print(" <////////// > ")
# def lettuce():
#     print(" ~~~~~~~~~~~~ ")
# def tomato():
#     print(" O O O O O O ")
# def ham():
#     print(" ============ ")

# bread()
# lettuce()
# tomato()
# ham()
# bread()

# Task 02
# def bread():
#     print(" <////////// > ")
# def lettuce():
#     print(" ~~~~~~~~~~~~ ")
# def tomato():
#     print(" O O O O O O ")
# def ham():
#     print(" ============ ")

# def bigMac():
#     bread()
#     lettuce()
#     tomato()
#     ham()
#     ham()
#     bread()
#     print("")

# for _ in range(42):
#     bigMac()

# Task 03
# def bread():
#     print(" <////////// > ")
# def lettuce():
#     print(" ~~~~~~~~~~~~ ")
# def tomato():
#     print(" O O O O O O ")
# def ham():
#     print(" ============ ")

# def bigMac(x):
#     for _ in range(max(0,x)):
#         bread()
#         lettuce()
#         tomato()
#         ham()
#         ham()
#         bread()
#         print("")


# bigMac(0)

# Task 04
# def bread():
#     print(" <////////// > ")
# def lettuce():
#     print(" ~~~~~~~~~~~~ ")
# def tomato():
#     print(" O O O O O O ")
# def ham():
#     print(" ============ ")

# def bigMac(x,veg=False):
#     for _ in range(max(0,x)):
#         if veg:
#             print("")
#             bread()
#             lettuce()
#             lettuce()
#             tomato()
#             tomato()
#             bread()
#         else:
#             print("")
#             bread()
#             lettuce()
#             tomato()
#             ham()
#             ham()
#             bread()


# bigMac(1,True)

# Challenge
# import time
# startingTime = time.time()

# def computePow(num,pow):
#     result = num
#     for _ in range(pow-1):
#         result*=num
#     return result

# print(pow(42,84))
# print(computePow(42,84))
# print(time.time()- startingTime)

# or

# def power(x, y):
#     if y == 0:
#         return 1

#     if y >= 1:
#         return x * power(x, y - 1)
    
# print(power(42,84))

# Task 01
# import re
# def palindrome(txt):
#     ispalindrome = True
#     txt = re.sub('[^a-zA-Z]+', '', txt)
#     txt.lower
#     for i in range(len(txt)):
#         if txt[i]!=txt[-1*(i+1)]:
#             ispalindrome = False
#     return ispalindrome

# print(palindrome("kayak"))

# Recursion
# Task 01
# import re

# def palindrome(txt):

#     ispalindrome = True
#     txt = re.sub('[^a-zA-Z]+', '', txt)
#     txt.lower

#     if txt == "":
#         return ispalindrome
    
#     if txt[0]==txt[-1]:
#         txt = txt[1:-1]
#         return palindrome(txt)
#     else:
#         ispalindrome = False
#     return ispalindrome
        
# print(palindrome("kayak"))

# Task 02

# non recursive
# import os

# def fileR(path = os.getcwd()):
#     splitPath = path.split("\\")
#     p = ""
#     for i in range(len(splitPath)):
#         p+= splitPath[i]+"\\"
#         print("--------------------------------")
#         print(os.listdir(p))
# fileR()

# Recursive test

# or with GPT

# import os

# def fileR(path):
#     print(f"------------- {path} -------------")
#     print(os.listdir(path))
#     if not path or path == os.path.abspath(os.path.sep):
#         return  # If the path is empty or the root directory, stop recursion
#     parent_path, _ = os.path.split(path)
#     fileR(parent_path)  # Recursively call fileR with the parent path

# fileR(os.getcwd())

# reverse GPT
# import os
# def ls(path):
#     print(f"Contenu de {path}:")
#     for item in os.listdir(path):
#         item_path = os.path.join(path, item)
#         if os.path.isfile(item_path):
#             print(f"Fichier : {item}")
#         elif os.path.isdir(item_path):
#             print(f"Dossier : {item}")
#             ls(item_path)
# ls(os.getcwd())

# import os

# def fileR(path):
#     if not path:
#         return
#     print(f"------------- {path} -------------")
#     print(os.listdir(path))
#     splitPath = path.split("\\")
#     splitPath = splitPath[:-1]
#     p= '\\'.join(splitPath)
#     fileR(p)
# fileR(os.getcwd())

# Higher-order function

# Task 00
# def funA(s,n):
#     CountLow=0
#     for letter in s:
#         if letter.islower():
#              CountLow+=1
#     print(True if CountLow>=n else False)

# funA("Hel",5)

# def funB(s,n):
#     CountUp=0
#     for letter in s:
#         if letter.isupper():
#              CountUp+=1
#     print(True if CountUp>=n else False)

# funB("HEl",1)

# def funC(s,n):
#     print(True if len(s)>=n else False)

# funC("HEl",5)

# import re
# def funD(s,n):
#     CountSpe=0
#     for letter in s:
#         if re.match("[^a-zA-Z0-9s]",letter):
#             CountSpe+=1
#     print(True if CountSpe>=n else False)

# funD("HEl//",5)

# import re
# def funD(s,n):
#     CountNum=0
#     for letter in s:
#         if re.match("[0-9]",letter):
#             CountNum+=1
#     print(True if CountNum>=n else False)

# funD("hello world12345",10)

# Task 01
import re
def lower(text):
    low=0
    for letter in text:
        if letter.islower():
             low+=1
    return low

def special(text):
    spe=0
    for letter in text:
        if re.match("[^a-zA-Z0-9s]",letter):
             spe+=1
    return spe


def check_password(func,n,s):
    txt = func(s)
    return True if txt>=n else False

print(check_password(lower,4,"mysecretpassword ") and check_password(special,2,"mysecretpassword "))

# Task 02
import re
def lower(text):
    low=0
    for letter in text:
        if letter.islower():
             low+=1
    return low

def special(text):
    spe=0
    for letter in text:
        if re.match("[^a-zA-Z0-9s]",letter):
             spe+=1
    return spe

def check_password(func,n=0,s=""):
    value = func(s)
    return True if value>=n else False

print(check_password(lower,4,"mysecretpassword"))

import re
def lower(text):
    low=0
    for letter in text:
        if letter.islower():
             low+=1
    return low

def special(text):
    spe=0
    for letter in text:
        if re.match("[^a-zA-Z0-9s]",letter):
             spe+=1
    return spe

def check_password(func,n=0,s=""):
    value = func(s)
    return True if value>=n else False

print(check_password(lower,4,"mysecretpassword"))
