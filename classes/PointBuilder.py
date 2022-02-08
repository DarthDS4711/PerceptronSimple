import numpy as np


class PointBuilder:
    def __init__(self, fig, ax, plot, another, line, fig_test):
        self.fig = fig
        self.ax = ax
        self.plot = plot
        self.another = another
        self.fig_test = fig_test
        # conexión del evento para detección de clicks
        self.cid = self.fig.figure.canvas.mpl_connect('button_press_event', self)
        self.dataPlot = []
        self.dataPlot2 = []
        self.class_data = -1 
        self.__line = line

    # función que nos actualizará el estado del evento de clicks
    def update_state_event(self, state):
        if state:
            self.fig.figure.canvas.mpl_connect('button_press_event', self)
        else:
            self.fig.canvas.mpl_disconnect(self.cid)

    def __call__(self, event):
        # si la figura no contiene un evento
        if event.inaxes!=self.ax.axes: 
            return
        # impresión de las pocisiones marcadas por el mouse
        print(f'Position X: {event.xdata}')
        print(f'Position Y: {event.ydata}')
        # si el contador es par se pone de un color diferente que si no lo es
        match self.class_data:
            case 0:
                self.dataPlot.append((event.xdata, event.ydata))
                self.plot.set_offsets(self.dataPlot)
            case 1:
                self.dataPlot2.append((event.xdata, event.ydata))
                self.another.set_offsets(self.dataPlot2)
        # actualización de la figura
        self.fig.canvas.draw()



    # asignar de nueva cuenta, los datos iniciales (valores de entrenamiento) del gráfico
    def set_data_again(self):
        self.plot = self.ax.scatter([], [], color='red', marker='x')
        self.another = self.ax.scatter([], [], color='blue', marker='o')
        self.__line, = self.ax.plot(0, 0, 'b-')
        self.fig_test = self.ax.scatter([], [], color='black', marker='8')
        self.ax.set_xlim([-5, 5])
        self.ax.set_ylim([-5, 5])
        self.ax.set_title('Perceptron simple')
        
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    # función que nos actualiza los datos que fueron evaluados, para su ubicación en una clase
    def set_new_points(self, x1, x2, class_data):
        match class_data:
            case 0:
                self.dataPlot.append((x1, x2))
                self.plot.set_offsets(self.dataPlot)
            case 1:
                self.dataPlot2.append((x1, x2))
                self.another.set_offsets(self.dataPlot2)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
    

    # función que nos actualiza la línea de la frontera de decisión
    def update_line(self, weight1, weigth2, theta):
        line_points = np.linspace(-5, 5)
        self.__line.set_xdata(line_points)
        # ecuación de la recta tipo y = mx +b 
        weights_data = (-weight1 * line_points + theta) / weigth2
        self.__line.set_ydata(weights_data)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def change_class(self, class_data):
        self.class_data = class_data
        print(self.class_data)
    

    def get_data_class_one(self):
        return self.dataPlot
    

    def get_data_class_two(self):
        return self.dataPlot2
