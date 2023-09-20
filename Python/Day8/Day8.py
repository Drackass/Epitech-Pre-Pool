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

# from tkinter import *
# from PIL import Image, ImageTk

# root = Tk()

# def display():
#     value = my_entry.get()
#     print(value.upper())

# root.title('Tkinter - Test')

# # label
# label = Label(root, text="Tkinter - Test", background="#fff")
# label.pack()

# # input
# my_entry = Entry(root, background='#efefef', border="0")
# my_entry.pack()

# # button
# btn = Button(root, text="display", command=display, background='#121212', foreground="#fff", border="0")
# btn.pack(side=TOP, padx=50, pady=10)

# # canva
# canvas = Canvas(root)
# canvas.pack()
# img = ImageTk.PhotoImage(Image.open("C:\\Users\\lenys\\Desktop\\Works\\DEV\\Epitech\\Pre-Pool\\Python\\Day8\\flowers.jpg"))
# canvas.create_image(0, 0, anchor=NW, image=img)  # Specify both x and y coordinates

# # drawCanva
# drawCanva=Canvas(root, width=400, height=400, highlightthickness=1, highlightbackground="black")
# drawCanva.pack()

# # body
# drawCanva.create_line(200,250,200,100, fill="green", width=2)

# def create_circle(x, y, r, canvas): #center coordinates, radius
#     x0 = x - r
#     y0 = y - r
#     x1 = x + r
#     y1 = y + r
#     return canvas.create_oval(x0, y0, x1, y1,fill="green")

# create_circle(200,75, 25, drawCanva)

# def animate():
#     global left_arm_coords, right_arm_coords, left_leg_coords, right_leg_coords
#     # Mettez à jour les coordonnées des lignes pour simuler l'animation
#     left_arm_coords[0] -= 1  # Déplace le bras gauche vers la gauche
#     left_arm_coords[2] -= 1
#     right_arm_coords[0] += 1  # Déplace le bras droit vers la droite
#     right_arm_coords[2] += 1

#     left_leg_coords[0] -= 1  # Déplace la jambe gauche vers la gauche
#     left_leg_coords[2] -= 1
#     right_leg_coords[0] += 1  # Déplace la jambe droite vers la droite
#     right_leg_coords[2] += 1

#     # Mettez à jour les coordonnées des lignes sur le canevas
#     drawCanva.coords(left_arm, left_arm_coords)
#     drawCanva.coords(right_arm, right_arm_coords)
#     drawCanva.coords(left_leg, left_leg_coords)
#     drawCanva.coords(right_leg, right_leg_coords)

#     # Planifiez la prochaine mise à jour de l'animation après 100 ms
#     root.after(100, animate)

# # Définissez les coordonnées de départ des lignes
# left_arm_coords = [150, 150, 200, 125]
# right_arm_coords = [250, 150, 200, 125]
# left_leg_coords = [150, 275, 200, 250]
# right_leg_coords = [250, 275, 200, 250]

# # Créez les lignes sur le canevas
# left_arm = drawCanva.create_line(left_arm_coords, fill="red", width=2)
# right_arm = drawCanva.create_line(right_arm_coords, fill="blue", width=2)
# left_leg = drawCanva.create_line(left_leg_coords, fill="purple", width=2)
# right_leg = drawCanva.create_line(right_leg_coords, fill="orange", width=2)

# # Commencez l'animation en appelant la fonction animate()
# animate()

# root.mainloop()

# Challenge
# How to generate a sphere in 3D Numpy array : https://stackoverflow.com/questions/46626267/how-to-generate-a-sphere-in-3d-numpy-array

# import raster_geometry as rg
# import numpy as np


# arr = rg.sphere(3, 1)
# print(arr.astype(np.int_))
# # [[[0 0 0]
# #   [0 1 0]
# #   [0 0 0]]
# #  [[0 1 0]
# #   [1 1 1]
# #   [0 1 0]]
# #  [[0 0 0]
# #   [0 1 0]
# #   [0 0 0]]]



# def sphere(shape, radius, position):
#     """Generate an n-dimensional spherical mask."""
#     # assume shape and position have the same length and contain ints
#     # the units are pixels / voxels (px for short)
#     # radius is a int or float in px
#     assert len(position) == len(shape)
#     n = len(shape)
#     semisizes = (radius,) * len(shape)

#     # genereate the grid for the support points
#     # centered at the position indicated by position
#     grid = [slice(-x0, dim - x0) for x0, dim in zip(position, shape)]
#     position = np.ogrid[grid]
#     # calculate the distance of all points from `position` center
#     # scaled by the radius
#     arr = np.zeros(shape, dtype=float)
#     for x_i, semisize in zip(position, semisizes):
#         # this can be generalized for exponent != 2
#         # in which case `(x_i / semisize)`
#         # would become `np.abs(x_i / semisize)`
#         arr += (x_i / semisize) ** 2

#     # the inner part of the sphere will have distance below or equal to 1
#     return arr <= 1.0

# # this will save a sphere in a boolean array
# # the shape of the containing array is: (256, 256, 256)
# # the position of the center is: (127, 127, 127)
# # if you want is 0 and 1 just use .astype(int)
# # for plotting it is likely that you want that
# arr = sphere((256, 256, 256), 10, (127, 127, 127))

# # just for fun you can check that the volume is matching what expected
# # (the two numbers do not match exactly because of the discretization error)

# print(np.sum(arr))
# # 4169
# print(4 / 3 * np.pi * 10 ** 3)
# # 4188.790204786391

# arr = sphere((256, 256, 256), 10, (127, 127, 127))


# # plot in 3D
# import matplotlib.pyplot as plt
# from skimage import measure

# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1, projection='3d')

# verts, faces, normals, values = measure.marching_cubes(arr, 0.5)
# ax.plot_trisurf(
#     verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap='Spectral',
#     antialiased=False, linewidth=0.0)
# plt.show()

# My Solution in 2D
# from tkinter import *
# from PIL import Image, ImageTk

# root = Tk()

# root.title('Tkinter - Test')

# # drawCanva
# drawCanva=Canvas(root, width=1000, height=1000, highlightthickness=1, highlightbackground="black")
# drawCanva.pack()

# def create_circle(x, y, r, canvas,color): #center coordinates, radius
#     x0 = x - r
#     y0 = y - r
#     x1 = x + r
#     y1 = y + r
#     return canvas.create_oval(x0, y0, x1, y1,fill=color)

# spherePos = 600
# rad = 250

# x = spherePos
# y = spherePos
# drawCanva.create_oval(spherePos-250, spherePos-150, spherePos+150, spherePos+200,fill=('#aaaaaa'),outline="#aaaaaa")
# i=0
# while rad > 0:
#     i+=1
#     create_circle(x,y, rad, drawCanva, '#777')
#     x += .05
#     y -= .05
#     rad -= 5*(i/10000)
# root.mainloop()

# Packaging

# Task 00
from tkinter import *

root = Tk()

drawCanva=Canvas(root, width=600, height=500, highlightthickness=1, highlightbackground="black")
drawCanva.pack()

root.mainloop()