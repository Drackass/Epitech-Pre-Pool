# ============================ Variables ============================


# # --------------------------- Task 01 ---------------------------
# # Fonction pour calculer la somme des séquences de nombres
# def compute_sequence_sum(n):
#     sequence_sum = 0
#     current_number = 0
#     for i in range(n):
#         current_number = current_number * 10 + 1
#         sequence_sum += current_number
#     return sequence_sum

# # Calcul de la somme des séquences
# sequence_sum = compute_sequence_sum(9)  # Pour 111111111

# # Calcul des puissances
# powers = [sequence_sum ** i for i in range(2, 8)]

# # Affichage des résultats
# for i, power in enumerate(powers, start=2):
#     print(f"Sequence Sum ^ {i} = {power}")



# --------------------------- Task 02 ---------------------------
# print(17**1024)





# ============================ Modulo ============================


# --------------------------- Task 01 ---------------------------
# def euclidean(a,b):
#     print(a/b)
#     print(a//b)
#     print(a%b)

# euclidean(42,4)



# --------------------------- Task 02 ---------------------------
# list = [10, 12, 17, 19, 53, 513]
# nbEven = 0
# nbOdd = 0
# i = 0
# while (i < len(list)):
#     if (list[i] % 2 == 0):
#         nbEven += 1
#     else:
#         nbOdd += 1
#     i += 1 
# print(f"there is {nbEven} even number & {nbOdd} odd number")

# or

# number = 42
# if (number%2==0):
#     print("even")
# else:
#     print("odd")



# # --------------------------- Task 03 ---------------------------
# digit = 44490320097 # 123434565
# curent = 0
# list = [int(i) for i in str(digit)]
# for i in range(len(list)):
#     curent += list[i]
# print(curent)




# --------------------------- Task 04 ---------------------------
# digit = 424242.8412 #12.24
# curent = 0
# list = [int(i) for i in str(digit).replace(".","")]
# for i in range(len(list)):
#     print(list[i], end=" ")




# --------------------------- Task 05 ---------------------------
# import math

# number= 424242.8412 #12.24
# print(number - math.floor(number))





# ============================ Archimedes constant and more ============================



# --------------------------- Task 01 ---------------------------
# # Calculation of PI using Leibniz formula
# import math

# # Function to calcultae PI using Leibniz
# def leibniz(n):
#     t_sum = 0
#     for i in range(n):
#         term = (-1) ** i /(2*i+1)
#         t_sum = t_sum + term
    
#     return t_sum * 4

# # Reading number of terms to be considered in Leibniz formula
# terms = int(1000000)

# # Function call
# pi = leibniz(terms)

# # # keep decimal only
# # pi = pi - math.floor(pi)

# # # nb of decimal
# # nbDecimal = 6
# # pi = round(pi,6)

# # # Convertir la partie décimale de pi en une liste d'entiers
# # decimal_part = str(pi)[2:]  # Obtenir la partie décimale sous forme de chaîne de caractères
# # decimal_digits = [int(digit) for digit in decimal_part]

# # # Afficher les chiffres de la partie décimale
# # for digit in decimal_digits:
# #     print(digit, end=" ")

# # or

# print(f"{pi:.6f}")




# --------------------------- Task 02 ---------------------------
# skip




# --------------------------- Task 03 ---------------------------
import math
from fractions import Fraction
numerator = 98
denominator = 42
print(f"1{numerator} / {denominator} = {numerator/denominator}")
for i in range(2,9):
    while ((numerator%i==0)and(denominator%i==0)):
        numerator /= i
        denominator /= i
print(f"{numerator} / {denominator} = {numerator/denominator}")