# Conditions

# Task 00
# print(42>12)
# True

# print(12=12)
# error

# print(12==12)
# True

# print("hello"=="world")
# False

# print(218>=118)
# True

# print("a".upper() == "A")
# True

# print(1*2*3*4<=9)
# False

# print("z" in "azerty")
# True

# Task 01
# value:int = int(input("num: "))
# if value==42:
#     print("correct answer")

# Task 02
# value:int = int(input("num: "))
# if value%2==0:
#     print("even")
# else:
#     print("odd")

# Task 03
# value:str = str(input("str: "))
# match value:
#     case "open sesame":
#         print("access granted")
#     case "will you open, your goddamn !¤*@":
#         print("access fucking granted")
#     case _:
#         print("permission denied")

# Task 04
# value:int = int(input("num: "))
# if value==42 or value <= 21 or value%2==0 or (value/2)<21 or (value%2!=0 and value >=45):
#     print("OK")
# else:
#     print("You got wrong my poor friend!")

# Task 05
# a = 42
# b = 41
# if a == b:
#     print(" A and B are the sames ")
# if b <= a:
#     print(" B is equal or lower as A ")
# if b != a:
#     print(" B his different from A ")

# Loops

# Task 00
# for i in range(1,101):
#     print(i)

# Task 01
# mot:str = str(input("str: "))
# for letter in mot:
#     print(letter*2, end="")

# Task 02
# for i in range(1,10001):
#     if i%7==0:
#         print(i)

# Task 03
# for i in range(-30,30):
#     noFB = True
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#         noFB = False
#     else:
#         if i%3==0:
#             print("Fizz")
#             noFB = False
#         if i%5==0:
#             print("Buzz")
#             noFB = False
#         if noFB:
#             print(i)

# Task 04
# i = 99
# while i>=0:
#     print(f"{i} bouteilles d'un âge approprié sur le mur")
#     i-=1

# Task 05
# def prog(n):
#     for i in range(2,n//2+1):
#         value = i
#         line = ""
#         while value<n:
#             line = f"{value} {line}"
#             value+=i
#         print(line)
# prog(14)

# Challenge
# num:int = int(input("num: "))
# txt:str = str(input("str: "))

# matches = ["a","e","i","o","u","y"]

# if num == 0:
#     exit()
# elif any([x in txt for x in matches]):
#     print(num)
# elif num >= 42:
#     print(num)
# else:
#     print(txt)

# Encryption

# Task 01
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(txt,key):
#     txtLow = str.lower(txt)
#     txtEnd = ""
#     for letter in txtLow:
#         if letter!= " ":
#             txtEnd += alphabet[(alphabet.index(letter)+key)%26]
#         else:
#             txtEnd+=" "
#     return txtEnd

# def decrypt(txt,key):
#     txtLow = str.lower(txt)
#     txtEnd = ""
#     for letter in txtLow:
#         if letter!= " ":
#             txtEnd += alphabet[(alphabet.index(letter)-key)%26]
#         else:
#             txtEnd+=" "
#     return txtEnd

# print(encrypt("Hello World",4))
# print(decrypt("lipps asvph",4))

# task 02
# # import numpy
# import numpy as np

# # set the alphabet and initialize the first row of the Vigenère matrix
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# tab = np.array([alphabet])

# # generate the Vigenère matrix
# for r in range(1,26): 
#     col = []
#     for c in range(26):
#         col.append(alphabet[(r+c)%26])
#     tab = np.r_[tab,[col]]

# # function to encrypt

# # j adore ecouter la radio toute la journee=> DECRYPTED
# # m usiqu emusiqu em usiqu emusi qu emusiqu => KEY MUSIQUE
# # v uvwhy ioimbul pm lslyi xaolm bu naojvuy => ENCRYPTED

# def encrypt(txt,key):

#     # set txt in lowercase
#     lowTxt = txt.lower()

#     # init final value
#     encryption = ""

#     # get the length of the key
#     lenKey = len(key)

#     i=0
#     for letter in lowTxt: # browse all letters
#         if letter!=" ":
#             encryption += tab[alphabet.index(letter)][alphabet.index(key[i%lenKey])] # find the value in the Vigenère matrix with the row and the column
#             i+=1
#         else:
#             encryption+=" "

#     return encryption # return the encryption

# # function to decrypt

# # v uvwhy ioimbul pm lslyi xaolm bu naojvuy => ENCRYPTED
# # m usiqu emusiqu em usiqu emusi qu emusiqu => KEY MUSIQUE
# # j adore ecouter la radio toute la journee => DECRYPTED

# def decrypt(txt,key):

#     # set txt in lowercase
#     lowTxt = txt.lower()

#     # init final value
#     decryption = ""

#     # get the length of the key
#     lenKey = len(key)
    
#     i=0
#     for letter in lowTxt: # browse all letters
#         if letter!=" ":
#             KeyLetter = key[i%lenKey]
#             KeyLetterPos = alphabet.index(KeyLetter)
#             listAtKeyLetter = tab[KeyLetterPos]
#             indexOfColumn = int(np.where(listAtKeyLetter==letter)[0])
#             decryption += alphabet[indexOfColumn] # find the value in the Vigenère matrix with the row and the value
            
#             # Or decryption += alphabet[int(np.where(tab[alphabet.index(key[i%lenKey])]==letter)[0])]
#             i+=1
#         else:
#             decryption+=" "
#     return decryption # return the decryption

# # commands:
# while True:
#     cmd = input("CMD: ")
#     match cmd:
#         case "/enc":
#             txt = input("text to encrypt: ")
#             key = input("key to use: ")
#             print(encrypt(txt,key))
#         case "/dec":
#             txt = input("text to decrypt: ")
#             key = input("key to use: ")
#             print(decrypt(txt,key))
#         case "/quit":
#             exit()
#         case "/help":
#             print("/enc => encrypt\n/dec => decrypt\n/quit => quit terminal\n/help => show all commands")
#         case _:
#             print("unknow command")

string = "Hello world."
def cryptage(key):
    count = 0
    crypter = []
    for i in string:
        if i != " ":
            x = ord(i) + key
            y = chr(x)
            count += 1

            crypter.append(y)
    print(''.join(crypter))
cryptage(2)