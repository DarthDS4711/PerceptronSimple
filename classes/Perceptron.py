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