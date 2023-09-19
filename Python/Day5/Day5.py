# Lists creation and browsing

# Task 01
# list = [1,2,3,4,5]
# print(list[0])

# Task 02
# list = [1,2,3,4,5]
# print(list[-1])

# Task 03
# list = [1,2,3,4,5]
# list.append(6)
# print(list[-1])

# Task 04
# list = [1,2,3,4,5]
# print(list)

# Task 05
# list = [1,2,3,4,5]
# list.remove(5)
# print(list)

# Task 06
# list = [1,2,3,4,5]
# list.insert(0,0)
# print(list)

# Task 07
# list = [1,2,3,4,5]
# print(list[1]-list[2]-list[3]-list[4])

# task 08
# ma_liste = [1, 2, 3]
# ma_liste.reverse()
# print(ma_liste)

# Task 09
# list_1 = [9, 5, 7, 2, 5, 3, 8, 14, 6, 11]
 
# for i in range(0, len(list_1), 2) :
#     print(list_1[i])

# Task 10
# list = [9, 5, 7, 2, 5, 3, 8, 14, 6, 11]
# for i in range(10):
#     list.append(i)
# print(list)

# Task 11
# my_first_list = [4,5,6]
# my_second_list = [1,2,3]
# my_first_list.extend(my_second_list)
# print(my_first_list) #[4, 5, 6, 1, 2, 3] Join 2 lists

# my_first_list=[7,8,9]
# my_second_list=[4,5,6]
# my_first_list = [* my_first_list,* my_second_list]
# print(my_first_list) # [7, 8, 9, 4, 5, 6] Join 2 lists, like the last script

# Operations on lists
# Task 01
# list =[i for i in range(1,11)]

# endValue = list[0]
# for value in list:
#     endValue*=value
# print(endValue)

# Task 02
# print([x + 10 for x in [3, 2, 6, 7, 1, 4]])
# for each value of the list, set in a new list the sum of this value + 10

# Task 03
# print(list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4])))
# map function provide to act on each value of a list, lambda is a anonym function who do the product of a value by the same value*
# so we have a new list with each value of the last list multiply by themselves

# Task 04
# list = [42,12,3,58,64,2,763,51]
# print(min(list))
# print(max(list))

# Task 05
# list = [42,12,3,58,64,2,763,51]
# for e in list:
#     if e<7:
#         print(e)

# Task 06
# list = [42,12,3,58,64,2,763,51]
# list.sort(reverse=True)
# print(list)

# Task 07
# print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])
# initial list [42, 3, 4, 18, 3, 10]
# act on each value of the list with the for value=x
# condition: if x%2==0 return a new value for the new list with x//2 euclidan dividing
# condition: else return a new value for the new list with x * 2 

# Task 08
# print(list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10])))
# return a new list with each value of the last one and keep only with the anonym function only the value strictly superior to 10

# Task 09
# print([*enumerate([42, 3, 4, 18, 3, 10])])
# create a new list bye adding for each value his index in a 'tuple'

# Task 10
# first_name = [ " Jackie " , " Bruce " , " Arnold " , " Sylvester " ] # first name
# last_name = [ " Stallone " , " Schwarzenegger " , " Willis " , " Chan " ] # last name
# magic = [* zip(first_name,last_name[:: -1]) ] # create a new list and zip in a tuple each value of the first name with the reversed version of the last name list, like a matrix
# print ( magic [0]) # show the first tuple
# print ( magic [3]) #show the third tuple
# print ( magic [1][0]) # show value in the matrix at (1,0)
# print ( magic [0][1]) # show value in the matrix at (0,1)
# print ( magic [2]) # show the second tuple

# Task 11
# import random,time
# startingTime = time.time()
# theList = [random.randint(0,10) for _ in range(1000000)]
# theList.sort()
# print(theList)
# print(time.time()- startingTime) # 1.3s

# theList = [random.randint(0,9) for _ in range(1000000)]
# theList.sort()
# theList

# Dictionaries

# Task 01
# student = {"jean":2000,"seb":2001}

# Task 02
# student = {
#     "name":"jean",
#     "academic_year":2003,
#     "unit":[{
#         "name":"Web Development",
#         "credits":42,
#         "grade":"A"
#     },
#     {
#         "name":"Network and System Administratio",
#         "credits":21,
#         "grade":"B"
#     },
#     {
#         "name":"java",
#         "credits":69,
#         "grade":"C"
#     }]
#     }

# print(student)

# Task 03
# grade_weight_mapping = {
#     "A":4,
#     "B":3,
#     "C":2,
#     "D":1,
#     "E":0
# }

# student = {
#     "name":"jean",
#     "academic_year":2003,
#     "unit":[
#     {
#         "name":"Web Development",
#         "credits":10,
#         "grade":"A"
#     },
#     {
#         "name":"Network and System Administratio",
#         "credits":10,
#         "grade":"B"
#     },
#     {
#         "name":"java",
#         "credits":10,
#         "grade":"C"
#     }],
#     "total_credits":0,
#     "GPA":"X"
#     }

# totalcredits = sum(student["unit"][i]["credits"] for i in range(len(student["unit"])))

# ListGPA = []
# for i in range(len(student["unit"])):
#     letterGrade = student["unit"][i]["grade"]
#     valueGrade = grade_weight_mapping[letterGrade]
#     valueGPA = student["unit"][i]["credits"]*valueGrade
#     ListGPA.append(valueGPA)
# GPA = sum(ListGPA)/totalcredits

# student["GPA"] = list(grade_weight_mapping.keys())[list(grade_weight_mapping.values()).index(GPA)]
# student["total_credits"] = totalcredits
# print(student)

# Task 04

# grade_weight_mapping = {
#     "A":4,
#     "B":3,
#     "C":2,
#     "D":1,
#     "E":0
# }

# student = [{
#     "name":"jean",
#     "academic_year":2003,
#     "unit":[
#     {
#         "name":"Web Development",
#         "credits":10,
#         "grade":"A"
#     },
#     {
#         "name":"Network and System Administratio",
#         "credits":10,
#         "grade":"A"
#     },
#     {
#         "name":"java",
#         "credits":10,
#         "grade":"A"
#     }],
#     "total_credits":0,
#     "GPA":"X"
#     },
#     {
#     "name":"seb",
#     "academic_year":2003,
#     "unit":[
#     {
#         "name":"Web Development",
#         "credits":10,
#         "grade":"B"
#     },
#     {
#         "name":"Network and System Administratio",
#         "credits":10,
#         "grade":"B"
#     },
#     {
#         "name":"java",
#         "credits":10,
#         "grade":"B"
#     }],
#     "total_credits":0,
#     "GPA":"X"
#     },
#     {
#     "name":"leny",
#     "academic_year":2003,
#     "unit":[
#     {
#         "name":"Web Development",
#         "credits":10,
#         "grade":"C"
#     },
#     {
#         "name":"Network and System Administratio",
#         "credits":10,
#         "grade":"C"
#     },
#     {
#         "name":"java",
#         "credits":10,
#         "grade":"C"
#     }],
#     "total_credits":0,
#     "GPA":"X"
#     }]

# # student.sort(key=lambda x: x["name"])




# for stud in range(len(student)):
#     totalcredits = sum(student[stud]["unit"][i]["credits"] for i in range(len(student[stud]["unit"])))

#     ListGPA = []
#     for i in range(len(student[stud]["unit"])):
#         letterGrade = student[stud]["unit"][i]["grade"]
#         valueGrade = grade_weight_mapping[letterGrade]
#         valueGPA = student[stud]["unit"][i]["credits"]*valueGrade
#         ListGPA.append(valueGPA)
#     GPA = sum(ListGPA)/totalcredits

#     student[stud]["GPA"] = list(grade_weight_mapping.keys())[list(grade_weight_mapping.values()).index(GPA)]
#     student[stud]["total_credits"] = totalcredits

# student.sort(key=lambda x: x["GPA"])
# # student.sort(key=lambda x: x["GPA"],reverse=True)
# print(student)

# Task 01
# list = ["leny","jean","marc","oliver"]

# theName = "leny"
# if list.count(theName)==0:
#     print("get lost!")
# else:
#     print("welcom in")

# Task 02
# import random
# list = [random.randint(1,3) for _ in range(10)]
# newList = []
# for value in list:
#     if newList.count(value)==0:
#         newList.append(value)
# print(newList)

# Task 03
# meetings = [
#     {
#         "day":"monday",
#         "time":"3:30 PM",
#         "lname":"leny",
#         "fname":"leny"
#     },
#     {
#         "day":"sunday",
#         "time":"3:30 PM",
#         "lname":"leny",
#         "fname":"leny"
#     },
#     {
#         "day":"monday",
#         "time":"3:30 PM",
#         "lname":"seb",
#         "fname":"seb"
#     },
#     {
#         "day":"Wednesday",
#         "time":"3:30 PM",
#         "lname":"leny",
#         "fname":"leny"
#     },
#     {
#         "day":"monday",
#         "time":"3:30 PM",
#         "lname":"jean",
#         "fname":"jean"
#     },
#     {
#         "day":"friday",
#         "time":"3:30 PM",
#         "lname":"seb",
#         "fname":"seb"
#     }
# ]
# max(0,100)
# print(meetings)

# def theMeetings(name):
#     theMeet = []
#     for i in range(len(meetings)):
#         if meetings[i]["lname"] == name:
#             theMeet.append(meetings[i])
#     return theMeet
# print(theMeetings("leny"))
