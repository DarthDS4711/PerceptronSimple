from tkinter import Entry, Tk, Frame,Button,Label, ttk
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from classes.Perceptron import Perceptron
from classes.PointBuilder import PointBuilder
# Perceptron
perceptron = Perceptron()

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

def inicialize_random():
    perceptron.inicialize_weigths()

def evaluate_points():
    pass

# inicialización de la ventana tkinker
window = Tk()
window.geometry('850x620')
window.wm_title('Perceptron Simple')
window.minsize(width=850, height=620)

# inicialización de los gráficos en nuestra ventana
frame = Frame(window,  bg='gray22',bd=3)
frame.grid(row=0, column=0, columnspan=4)

# agregar el gráfico a la ventana 
canvas = FigureCanvasTkAgg(fig, master = frame)  
canvas.get_tk_widget().grid(row=0, column=0, columnspan=4)

# Botones principales del programa
Button(window, text='Train', width = 15, bg='green',fg='white',
    command=train).grid(row=1, column=0)

Button(window, text='Blue Rose', width = 15, bg='blue',fg='white',
    command=class_flower_rose).grid(row=1, column=1)

Button(window, text='Yellow Rose', width = 15, bg='orange',fg='white', 
    command=class_flower_rose).grid(row=1, column=2)

Button(window, padx=5, pady=5, text='Inicialize weigths', 
    command=inicialize_random).grid(row=1, column=3)

Button(window, width = 15, text='Test', 
    command=evaluate_points).grid(row=1, column=4)

# Labels, Entradas y botones relacionados a la obtención del número de epocas
Label(window, text='N° Epochs: ').grid(row=3, column=0)
entry_epochs = Entry(window)
entry_epochs.grid(row=3, column=1)

# funciones relacionadas a la obtención y validación del número de epocas
def get_epochs():
    n_epochs = entry_epochs.get()
    print(f'{n_epochs}')
    entry_epochs.delete("0", "end")
# Boton relacionado a obtener el número de epocas
Button(window, text='Asign', command=get_epochs, width = 15).grid(row=3, column=2)

# Labels, Entradas y botones relacionados a la obtención del factor de aprendizaje
Label(window, text='Learning Rate: ').grid(row=4, column=0)
entry_learning_rate = Entry(window)
entry_learning_rate.grid(row=4, column=1)

# funciones relacionadas a obtener y validar el factor de aprendizaje
def get_learning_rate():
    learning_rate = entry_learning_rate.get()
    print(f'{learning_rate}')
    entry_learning_rate.delete("0", "end")
# Boton relacionado a obtener el valor del factor de aprendizaje
Button(window, text='Asign', command=get_learning_rate, width = 15).grid(row=4, column=2)

# labels y Entrys (desabilitados) relacionados al estado final del programa
Label(window, text='Final learning Rate: ').grid(row=3, column=3)
Label(window, text='Final number epochs: ').grid(row=4, column=3)
Label(window, text='Train: ').grid(row=5, column=3)
Entry(window, state=tkinter.DISABLED).grid(row=3, column=4)
Entry(window, state=tkinter.DISABLED).grid(row=4, column=4)
Entry(window, state=tkinter.DISABLED).grid(row=5, column=4)

window.mainloop()