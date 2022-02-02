import time
import numpy as np

class Perceptron:
    def __init__(self):
        # pesos del perceptron
        self.__weigth0 = 0
        self.__weigth1 = 0
        self.__weigth2 = 0
        # datos entrada
        self.__x1 = []
        self.__x2 = []
        # salida esperada
        self.__y = []
        # variable theta
        self.__theta = 0
        # variable de factor de aprendizaje
        self.__factor_learning = 0
        # variable de número de épocas máximo
        self.__epochs = 0
        # variable bias
        self.__bias = -1
        # variable de estado del perceptron
        self.__done_learn = False
        # variable de numero de épocas requeridas
        self.__number_of_epochs = 0


    def get_epochs(self):
        return self.__epochs

    def get_factor_learning(self):
        return self.__factor_learning
    

    def get_number_of_epochs(self):
        return self.__number_of_epochs


    def get_status_perceptron(self):
        return self.__done_learn

    # función que nos devuelve el valor de la net, evaluado por la función de activación
    def __return_value_of_z(self, index):
        z = (self.__x1[index] * self.__weigth1) + \
            (self.__x2[index] * self.__weigth2) +  (self.__weigth0 * self.__bias)
        if z >= 0:
            return 1
        else:
            return 0

    # función que nos devuelve el valor de clase predecida para un nuevo elemento
    def __return_value_of_z_out_of_train(self, x1, x2):
        z = (x1 * self.__weigth1) + (x2 * self.__weigth2) + (self.__weigth0 * self.__bias)
        if z >= 0:
            return 1
        else:
            return 0

    # función de predicción de los nuevos datos
    def predict_data(self, pointBuilder):
        data = pointBuilder.dataPlot3
        pointBuilder.ax.cla()
        pointBuilder.set_data_again()
        pointBuilder.update_line(self.__weigth1, self.__weigth2, self.__weigth0) 
        for value in data:
            x1 = value[0]
            x2 = value[1]
            class_predicted = self.__return_value_of_z_out_of_train(x1, x2)
            pointBuilder.set_new_points(x1, x2, class_predicted)
            time.sleep(1)
        pointBuilder.update_line(self.__weigth1, self.__weigth2, self.__weigth0) 
        pointBuilder.dataPlot3 = []     
            
    def get_weigth1(self):
        return self.__weigth1
    
    def get_weigth2(self):
        return self.__weigth2
    

    def get_theta(self):
        return self.__weigth0


    # ajuste de los pesos conforme al indice donde se encontró el error 
    def __adjust_weigths(self, error, index):
        self.__weigth1 = self.__weigth1 + (self.__x1[index] * error * self.__factor_learning)
        self.__weigth2 = self.__weigth2 + (self.__x2[index] * error * self.__factor_learning)
        self.__weigth0 = self.__weigth0 + (self.__bias * error * self.__factor_learning)


    # función principal de entrenamiento
    def train(self, pointBuilder):
        done = False
        n_epochs = 0
        while (not done and n_epochs < self.__epochs):
            done = True
            for index in range(0, len(self.__y)):
                z = self.__return_value_of_z(index)
                if z != self.__y[index]:
                    done = False
                    # calcular el error
                    error = (self.__y[index] - z)
                    # ajuste del valor de thetha
                    self.__adjust_weigths(error, index)
                    n_epochs += 1
                    pointBuilder.update_line(self.__weigth1, self.__weigth2, self.__weigth0)
                    time.sleep(1)
        if n_epochs < self.__epochs:
            self.__done_learn = True
        self.__number_of_epochs = n_epochs
        pointBuilder.update_line(self.__weigth1, self.__weigth2, self.__weigth0)
        print(f'Weigth 1: {self.__weigth1}')
        print(f'Weigth 2: {self.__weigth2}')
        print(f'Theta: {self.__weigth0}')
        print(f'N epochs: {n_epochs}')



    def set_epochs(self, epochs):
        self.__epochs = epochs
    
    def set_factor_learning(self, factor_learning):
        self.__factor_learning = factor_learning

    
    def set_inputs_outpus(self, xdata, xdata1):
        for data in xdata:
            self.__x1.append(data[0])
            self.__x2.append(data[1])
            self.__y.append(0)
        for data in xdata1:
            self.__x1.append(data[0])
            self.__x2.append(data[1])
            self.__y.append(1)
        
    

    def inicialize_weigths(self):
        self.__weigth0 = np.random.uniform(0, 1)
        self.__weigth1 = np.random.uniform(0, 1)
        self.__weigth2 = np.random.uniform(0, 1)
