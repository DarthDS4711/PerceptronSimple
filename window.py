from tkinter import Entry, Tk, Frame,Button,Label, ttk, messagebox
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from classes.Perceptron import Perceptron
from classes.PointBuilder import PointBuilder
from validators.validator import *


class Window:
    def __init__(self):
        self.__window = Tk()
        self.__window.geometry('850x620')
        self.__window.wm_title('Perceptron Simple')
        self.__window.minsize(width=850, height=620)
        self.__frame = Frame(self.__window,  bg='gray22',bd=3)
        self.__frame.grid(row=0, column=0, columnspan=4)
        fig, ax = plt.subplots()
        plot = ax.scatter([], [], color='red', marker='x')
        another = ax.scatter([], [], color='blue', marker='o')
        line, = ax.plot(0, 0, 'b-')
        ax.set_xlim([-5, 5])
        ax.set_ylim([-5, 5])
        ax.set_title('Perceptron simple')
        self.__pointsBuilder = PointBuilder(fig, ax, plot, another, line)
        self.__perceptron = Perceptron()
        # agregar el gráfico a la ventana 
        self.__canvas = FigureCanvasTkAgg(fig, master = self.__frame)  
        self.__canvas.get_tk_widget().grid(row=0, column=0, columnspan=4)

        # botones principales del programa
        self.__btn1 = Button(self.__window, text='Train', width = 15, bg='green',fg='white',
            command=self.train)
        self.__btn2 = Button(self.__window, text='Red Rose', width = 15, bg='red',fg='white',
            command=self.class_flower_rose)
        self.__btn3 = Button(self.__window, text='Blue Rose', width = 15, bg='blue',fg='white', 
            command=self.class_flower_rose)
        self.__btn4 = Button(self.__window, padx=5, pady=5, text='Inicialize weigths', 
            command=self.inicialize_random)
        self.__btn5 = Button(self.__window, width = 15, text='Test', 
            command=self.evaluate_points)
        self.__btn6 =Button(self.__window, text='Quit', bg='red', fg='white', 
            command=self.quit, width=15)
        # botones relacionados a los entrys
        self.__btn_epochs = Button(self.__window, text='Asign', 
            command=self.get_epochs, width = 15)
        self.__btn_learning_rate = Button(self.__window, text='Asign', 
            command=self.get_learning_rate, width = 15)
        
        # inicialización de entrys
        self.__entry_epochs = Entry(self.__window)
        self.__entry_learning_rate = Entry(self.__window)
        self.__entry1 = Entry(self.__window)
        self.__entry2 = Entry(self.__window)
        self.__entry3 = Entry(self.__window)

        # inicialización de labels (relacionados a los entrys)
        Label(self.__window, text='N° Epochs: ').grid(row=3, column=0)
        Label(self.__window, text='Learning Rate: ').grid(row=4, column=0)
        # inicialización de label relacionado a entrys de información
        Label(self.__window, text='Final Value theta: ').grid(row=3, column=3)
        Label(self.__window, text='Final number epochs: ').grid(row=4, column=3)
        Label(self.__window, text='Train: ').grid(row=5, column=3)

        # sección para inicializar los botones
        self.set_buttons()
        self.set_entrys()

        self.__window.mainloop()
    

    def set_entrys(self):
        # Entrys relacionados a ingresar información al programa
        self.__entry_epochs.grid(row=3, column=1)  
        self.__entry_learning_rate.grid(row=4, column=1)
        # entrys relacionados con desplegar información
        self.__entry1.grid(row=3, column=4)
        self.__entry2.grid(row=4, column=4)
        self.__entry3.grid(row=5, column=4)
        
    
    def set_buttons(self):
        # Botones principales del programa
        self.__btn1.grid(row=1, column=0)
        self.__btn2.grid(row=1, column=1)
        self.__btn3.grid(row=1, column=2)
        self.__btn4.grid(row=1, column=3)
        self.__btn5.grid(row=1, column=4)
        self.__btn6.grid(row=0, column=4)
        # botones relacionados a los entrys
        self.__btn_epochs.grid(row=3, column=2)
        self.__btn_learning_rate .grid(row=4, column=2)

        
    # boton para finalizar la execución de la aplicación
    def quit(self):
        self.__window.quit()
    

    # función para mostrar la información por pantalla
    def show_info(self):
        self.__entry1.insert(0, str(self.__perceptron.get_theta()))
        self.__entry2.insert(0, str(self.__perceptron.get_number_of_epochs()))
        if self.__perceptron.get_status_perceptron():
            self.__entry3.insert(0, "OK")
        else:
            self.__entry3.insert(0, "Error")
    
    def train(self):
        self.block_main_buttons()
        self.__perceptron.set_inputs_outpus(self.__pointsBuilder.get_data_class_one(), 
        self.__pointsBuilder.get_data_class_two())
        self.__perceptron.train(self.__pointsBuilder)
        self.show_info()

    # Cambio en el tipo de flor a mapear
    def class_flower_rose(self):	
        self.__pointsBuilder.change_class()

    def class_flower_white(self):
        self.__pointsBuilder.change_class()

    # inicialización de manera aleatoria de los pesos del perceptron
    def inicialize_random(self):
        self.__perceptron.inicialize_weigths()

    # evaluación de los puntos obtenidos posteriores al entrenamiento
    def evaluate_points():
        pass
    
    # función para obtener el learning rate
    def get_learning_rate(self):
        learning_rate = self.__entry_learning_rate.get()
        self.__entry_learning_rate.delete("0", "end")
        if not validate_float(learning_rate):
            messagebox.showinfo(message="Factor de aprendizaje incorrecto", title="Error")
        else:
            learning_rate = float(learning_rate)
            self.__perceptron.set_factor_learning(learning_rate)
            messagebox.showinfo(message="Factor de aprendizaje agregado correctamente", title="Éxito")
    

    # función relacionada a la obtención del número de epocas
    def get_epochs(self):
        n_epochs = self.__entry_epochs.get()
        self.__entry_epochs.delete("0", "end")
        if not validate_integer(n_epochs):
            messagebox.showinfo(message="Número de epocas incorrecto", title="Error")
        else:
            n_epochs = int(n_epochs)
            self.__perceptron.set_epochs(n_epochs)
            messagebox.showinfo(message="Número de epocas agregado correctamente", title="Éxito")

    def block_main_buttons(self):
        self.__btn1['state'] = tkinter.DISABLED
        self.__btn2['state'] = tkinter.DISABLED
        self.__btn3['state'] = tkinter.DISABLED
        self.__btn4['state'] = tkinter.DISABLED
