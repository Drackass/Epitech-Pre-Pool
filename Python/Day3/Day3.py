# String

# Task 00
# variable = "hello world"
# print(variable)

# Task 01
# text = "Python"
# first_char = text[0]  # 'P'
# second_char = text[4]  # 'y'
# print(first_char)
# print(second_char)

# Task 02
# text = "Python"
# print(text[-1])

# Task 03
# print("abcdefghijklmnopqrstuvw"[4:9])

# String Methods

# Task 00
# text = "Python"
# print(text.lower())

# Task 01
# print("tutatotatutato".replace("tu","ta"))

# Task 02
# # set a string variable
# string = " hello world "
# #  search occurence and return the index
# position = string . find ( " a " )

# # print the index
# print ( position )

# result: -1 because he doesnt find a occurence

# Task 03
# p = "abcdefghij" 
# # [:: -2] jhfdb chaque deuxième caractère de la chaîne en commençant par la fin. 
# # [:5] jhfdb les 5 premiers caractères de la chaîne
# # [:: -1] bdfhj renverse la chaîne
# # [3:] les caractères à partir de l'index 3 
# print (p[::-2][:5][::-1][3:])

# Task 04
# print("abcdefghij"[7::2])

# Task 05
# for _ in range(10):
#     print("hello world")

# Task 06
# print(["Hello World" for _ in range(10)])

# Task 07
# s1 = " Hello "
# s2 = 42
# concat = s1 + str(s2)
# print ( concat )

# Task 08
# string1 = "42"
# string2 = " is "
# string3 = "the answer"
# concat = string1 + string2 + string3
# print ( f"The string {concat} characters ) ." )

# Challenge
# t = "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN".lower()
# text = t+t[:: -1]
# Catnb = text.count("cat")
# Gardennb = text.count("garden")
# Mice = text.count("mice")
# print(f"Cat = {Catnb} Garden = {Gardennb} Mice = {Mice}")

# User input

# Task 00
# name = input("Name : ")
# print(f"Hello {name}")

# Task 01
# name = input("Name : ")
# print(f"Hello {name.capitalize()}")

# Task 02
# num1 = int(input("num 1 : "))
# num2 = int(input("num 2 : "))
# print(f"The sum of the two provided numbers is {num1+num2}")

# Task 03
# Value = int(input("value :"))
# print(type(Value))

# Task 04

# import re

# text = "This is a test. Is it possible to fly? Good things come to those who never give up."

# sentences = re.split(r'[.?]', text)

# FirstWords = []
# for sentence  in sentences:
#     sentence = sentence.strip()
#     words=[]
#     words = sentence.split(" ")
#     FirstWords.append(words[0])

# result = ""
# for FirstWord in FirstWords:
#     result += FirstWord+" "
# print(result)