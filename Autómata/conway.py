import pygame


class Conway:
    WIDTH = 20 # Ancho en celdas.
    HEIGHT = 20 # Alto en Celdas.
    LIVE = 1 # Valor para celda viva.
    DEAD = 0 # Valor para celda muerta.

    __world = [] # Espacio de juego. Es una lista de valores enteros donde cada valor se corresponde con el estado de una celda.
    __next = []  # Espacio de respaldo para guardar los datos de la generación siguiente.

    __born = [] # Lista de números enteros de celdas vecinas que hacen que una celda muerta pase a estar viva.
    __alive = [] # Lista de números de celdas vecinas vivas que hacen que una celda viva siga viva.

    __iterations = 0 # Número de generaciones que se han calculado.

    # Constructor: inicializa el espacio del autómata celular. Además almacena los valores de cada celda.

    def __init__(self, pattern: str = "23/3"):
        '''
        Constructor
        :param pattern: Patrón con función de transición clásica del Juego de Conway (23/3)
        '''
        self.reset()
        self.__alive = [int(v) for v in pattern.split("/")[0]]
        self.__born = [int(v) for v in pattern.split("/")[1]]

    @property
    def iterations(self) -> int:
        '''
        Número de generaciones que se han calculado.
        :return: Número de generaciones.
        '''
        return self.__iterations

    @property
    def livecells(self) -> int:
        '''
        Número de células vivas en la generación actual.
        :return: Número de células vivas.
        '''
        return self.__world.count(1)

    def reset(self):
        '''
        Inicializa el espacio de juego con todas las celdas muertas.
        '''
        self.__iterations = 0
        self.__world = [0] * (self.WIDTH * self.HEIGHT)
        self.__next = [0] * (self.WIDTH * self.HEIGHT)

    def read(self, x: int, y: int) -> int:
        '''
        Devuelve el valor de una celda dadas su coordenadas en el espacio con frontera reflectora.
        :param x: coordenada X en el espacio. (Anchura)
        :param y: coordenada Y en el espacio. (Altura)
        :return: valor de la celda (0) MUERTA - (1) VIVA
        '''

        if x >= self.WIDTH:
            x -= self.WIDTH # x = x - self.WIDTH
        elif x < 0:
            x += self.WIDTH  # x = x + self.WIDTH
        
        if y >= self.HEIGHT:
            y -= self.HEIGHT
        elif y < 0: 
            y += self.HEIGHT
        
        return self.__world[(y *self.WIDTH) + x]


    def write(self, x: int, y: int, value: int) -> None:
        '''
        Establece el valor de una celda dadas sus coordenadas en el espacio.
        :param x: coordenada X en el espacio. (Anchura)
        :param y: coordenada Y en el espacio. (Altura)
        :param value: valor de la celda (0) MUERTA - (1) VIVA
        :return:
    '''
        self.__world[(y *self.WIDTH) + x] = value

    def update(self) -> None:
        '''
        Actualiza el estado del autómata celular a la siguiente generación.
        :return:
        '''
        self.__iterations += 1 # Aumenta el número de generaciones.

        # Bucle de recorrido de todas las celdas del espacio.
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):

                near = [self.read(x - 1, y - 1),        # Obtención de los valores de las celdas vecinas.
                        self.read(x - 1, y), 
                        self.read(x - 1, y + 1),

                        self.read(x, y - 1),
                        self.read(x, y + 1),

                        self.read(x + 1, y - 1),
                        self.read(x + 1, y),
                        self.read(x + 1, y + 1)]
                
                alive_count = near.count(self.LIVE)  # Contamos el número de celdas vecinas vivas.

                current = self.read(x, y)  # Obtenemos el estado de la celda actual

                # Solo especificámos los cambios de estado, el resto es mantenerse igual.
                if current == self.LIVE:  # Si la celda actual está viva.
                    if alive_count not in self.__alive: # Si el número de celdas vecinas vivas no está en la lista de supervivencia.
                        current = self.DEAD # La celda muere.
                else: # Está muerta
                    if alive_count in self.__born: # Si el número de celdas vecinas vivas está en la lista de nacimiento.
                        current = self.LIVE # Se mantiene viva
                
                self.__next[(y * self.WIDTH) + x] = current # Actualizamos el estado de la celda en la siguiente generación.

        for i in range(self.WIDTH * self.HEIGHT):
            self.__world[i] = self.__next[i]  # Actualizamos el espacio de juego principal con la siguiente generación.


    def draw(self, context: pygame.Surface) -> None:
        '''
        Función de proyección del espacio con el estado de las celdas del autómata celular.
        :param context: contexto gráfico de la pantalla.
        :return:
        ''' 
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):

                current = self.read(x,y) # Obtenemos el estado de la celda.

                if current == self.LIVE: # Si está viva, la pintamos de blanco. # draw.rect: pintar rectángulo
                    pygame.draw.rect(surface= context, color= (255, 255, 255), rect= (x * 20, y * 20, 20, 20)) 
                
                else: # Si está muerta, tenemos un recuadro sin relleno con bordes grises. # draw.lines: pintar rlíneas
                    pygame.draw.lines(surface= context, color= (64,64,64), closed=True, points=((x*20,y*20),((x+1)*20, y * 20), ((x + 1) * 20, (y + 1)*20), (x*20,(y+1)*20)), width= 1)


    def save(self, filename:str) -> None:
        '''
        Para guardar el estado actual del autómata celular en un archivo.
        :return: Archivo de texto con una cadena de la forma [1,0,0,0,1,0,1,0]
        '''
        with open(filename, mode= "w", encoding = "utf-8") as fp:
            fp.write(str(self.__world))
        
    def load(self, filename:str) -> None:
        '''
        Para cargar un estado del autómata celular desde un archivo.
        :return:
        '''
        with open(filename, mode= "r", encoding = "utf-8") as fp:
            data = fp.read()[1:-1]    # [1:-1] para quitar los corchetes de la lista anterior.
            self.__world = [int(v) for v in data.split(",")]
