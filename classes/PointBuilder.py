class PointBuilder:
    def __init__(self, fig, ax, plot, another):
        self.fig = fig
        self.ax = ax
        self.plot = plot
        self.another = another
        # conexión del evento para detección de clicks
        self.cid = fig.figure.canvas.mpl_connect('button_press_event', self)
        self.dataPlot = []
        self.dataPlot2 = []
        self.class_data = 0

    def __call__(self, event):
        # si la figura no contiene un evento
        if event.inaxes!=self.ax.axes: 
            return
        # impresión de las pocisiones marcadas por el mouse
        print(f'Position X: {event.xdata}')
        print(f'Position Y: {event.ydata}')
        # si el contador es par se pone de un color diferente que si no lo es
        if self.class_data == 0:
            self.dataPlot.append((event.xdata, event.ydata))
            self.plot.set_offsets(self.dataPlot)
        else:
            self.dataPlot2.append((event.xdata, event.ydata))
            self.another.set_offsets(self.dataPlot2)
        # actualización de la figura
        self.fig.canvas.draw()

    def change_class(self):
        if self.class_data == 0:
            self.class_data = 1
        else:
            self.class_data = 0
'''
fig, ax = plt.subplots()
plot = ax.scatter([], [], color='red', marker='x')
another = ax.scatter([], [], color='blue', marker='o')
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_title('Perceptron simple')
pointsBuilder = PointBuilder(fig, ax, plot, another)
'''