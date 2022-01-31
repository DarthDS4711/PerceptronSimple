import numpy as np


class Perceptron:
    def __init__(self):
        # pesos del perceptron
        self.__weigth1 = 0
        self.__weigth2 = 0
        # datos entrada
        self.__x1 = None
        self.__x2 = None
        # salida esperada
        self.__y = []
        # variable theta
        self.__theta = 0
        # variable de factor de aprendizaje
        self.__factor_learning = 0
        # variable de número de épocas máximo
        self.__epochs = 0
    

    def inicialize_weigths(self):
        self.__weigth1 = np.random.uniform(0, 3)
        self.__weigth2 = np.random.uniform(0, 3)
        print(f'Weigth 1: {self.__weigth1}')
        print(f'Weigth 2: {self.__weigth2}')