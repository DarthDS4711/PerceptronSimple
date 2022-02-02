import numpy as np


class PointBuilder:
    def __init__(self, fig, ax, plot, another, line, fig_test):
        self.fig = fig
        self.ax = ax
        self.plot = plot
        self.another = another
        self.fig_test = fig_test
        # conexión del evento para detección de clicks
        self.cid = fig.figure.canvas.mpl_connect('button_press_event', self)
        self.dataPlot = []
        self.dataPlot2 = []
        self.dataPlot3 = []
        self.class_data = -1 
        self.__line = line

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
            case 2:
                self.dataPlot3.append((event.xdata, event.ydata))
                self.fig_test.set_offsets(self.dataPlot3)
        # actualización de la figura
        self.fig.canvas.draw()


    def delete_data_test(self):
        self.dataPlot3.clear()
        self.fig.canvas.draw()

    def set_data_again(self):
        self.plot = self.ax.scatter([], [], color='red', marker='x')
        self.another = self.ax.scatter([], [], color='blue', marker='o')
        self.__line, = self.ax.plot(0, 0, 'b-')
        self.ax.set_xlim([-5, 5])
        self.ax.set_ylim([-5, 5])
        self.ax.set_title('Perceptron simple')

        self.plot.set_offsets(self.dataPlot)
        self.another.set_offsets(self.dataPlot2)
        
        self.fig.canvas.draw()


    def set_new_points(self, x1, x2, class_data):
        match class_data:
            case 0:
                self.dataPlot.append((x1, x2))
                self.plot.set_offsets(self.dataPlot)
            case 1:
                self.dataPlot2.append((x1, x2))
                self.another.set_offsets(self.dataPlot2)
        self.fig.canvas.draw()
    

    def update_line(self, weight1, weigth2, theta):
        line_points = np.linspace(-5, 5)
        self.__line.set_xdata(line_points)
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

'''
fig, ax = plt.subplots()
plot = ax.scatter([], [], color='red', marker='x')
another = ax.scatter([], [], color='blue', marker='o')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_title('Perceptron simple')
pointsBuilder = PointBuilder(fig, ax, plot, another)
'''
