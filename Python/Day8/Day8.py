# matplotlib and numpy

# | Matplotlib :
# python -m pip install -U matplotlib
# | Tkinter :
# pip install tk

# from matplotlib import pyplot as plt
# x_values = [1,2,3,4]
# y_values = [5,4,6,2]
# plt.plot(x_values, y_values)
# plt.show()

# Task 01
# import numpy as np
# x_values = np.linspace(0,10, 100) # Return evenly spaced numbers over a specified interval.
# print(x_values)

# Task 02
# import matplotlib.pyplot as plt
# # X axis values:
# x = [0,1,2,3]
# # Y axis values:
# y = [12,32,42,52]
# plt.grid()
# # Create scatter plot:
# plt.scatter(x, y,color="red")
# plt.show()

# Task 03
# import matplotlib.pyplot as plt

# def displayGraph(x,y):
#     plt.grid()
#     plt.scatter(x, y,color="red")
#     plt.plot(x,y,color="red")
#     plt.show()

# displayGraph([0,1,2,3],[12,32,42,52])

# Task 04
# import numpy as np
# from matplotlib import pyplot as plt
# import math

# def f(x):
#     return x**2+x*3+2

# def plot_fct(func, min, max):
#     plt.grid()
#     x = np.linspace(min, max, 1000)  # Utilisez un échantillon de 1000 points pour un tracé plus lisse
#     y = np.vectorize(func)(x)  # Appliquez la fonction à l'ensemble des valeurs de x
#     plt.plot(x, y, color='red')
#     plt.show()

# plot_fct(math.sin, 0, 50)
# plot_fct(f, -100 , 200)
# plot_fct(lambda x :x **2,-10,10)
# plot_fct(lambda x : 1/x , -100 , 100)

# By the way, can you explain what is lambda x: x**2 and lambda x: 1/x?
# is a lambda function who return a simple operation

# Tkinter

# Task 01
# from tkinter import * 
# fenetre = Tk()
# label = Label(fenetre, text="Hello World")
# label.pack()
# fenetre.mainloop()

# Task 02
# https://python.doctor/page-tkinter-interface-graphique-python-tutoriel

from tkinter import *
 
root = Tk()
 
def display():
    value = my_entry.get()
    print(value.upper())

root.title('Tkinter  - Test')
root.configure(bg="#fff")
# root.geometry('250x300')

# label
label = Label(root, text="Tkinter  - Test",background="#fff")
label.pack()

# input
my_entry = Entry(root,background='#efefef',border="0")
my_entry.pack()
 
#  button
btn=Button(root, text="display", command=display, background='#121212' ,foreground="#fff",border="0")
btn.pack(side=TOP, padx=50, pady=10)
 
# canva

# Add image file
bg = PhotoImage(file = "\Python\Day8\bg.jpg")
canvas = Canvas(root, width=150, height=120, background='yellow')
ligne1 = canvas.create_line(75, 0, 75, 120)
ligne2 = canvas.create_line(0, 60, 150, 60)
txt = canvas.create_text(75, 60, text="Cible", font="Arial 16 italic", fill="blue")
canvas.pack()
canvas.create_image(0,0,Image=bg)

root.mainloop()

