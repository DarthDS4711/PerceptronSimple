from tkinter import Tk, Frame,Button,Label, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from classes.PointBuilder import PointBuilder

# Bloque de código relacionado a cargar la gráfica
fig, ax = plt.subplots()
plot = ax.scatter([], [], color='yellow', marker='x')
another = ax.scatter([], [], color='blue', marker='o')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_title('Perceptron simple')
pointsBuilder = PointBuilder(fig, ax, plot, another)
plt.title("Muestreo de los datos",color='white',size=16)

# Bloque de funciones relacionadas con los botones 
def train():
    pass

# metodos que cambian de clase los datos
def class_flower_rose():	
	pointsBuilder.change_class()

def class_flower_white():
    pointsBuilder.change_class()

# inicialización de la ventana tkinker
window = Tk()
window.geometry('642x535')
window.wm_title('Perceptron Simple')
window.minsize(width=642, height=535)

# inicialización de los gráficos en nuestra ventana
frame = Frame(window,  bg='gray22',bd=3)
frame.pack(expand=1, fill='both')

# agregar el gráfico a la ventana 
canvas = FigureCanvasTkAgg(fig, master = frame)  
canvas.get_tk_widget().pack(padx=5, pady=5 , expand=1, fill='both') 

# Botones principales del programa
Button(frame, text='Entrenamiento', width = 15, bg='green',fg='white',
    command=train).pack(pady =5,side='left',expand=1)
Button(frame, text='Rosa azul', width = 15, bg='blue',fg='white',
    command=class_flower_rose).pack(pady =5,side='left',expand=1)
Button(frame, text='Rosa Amarilla', width = 15, bg='orange',fg='white', 
    command=class_flower_rose).pack(pady =5,side='left',expand=1)

window.mainloop()