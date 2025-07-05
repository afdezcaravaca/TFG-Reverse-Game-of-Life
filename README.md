# TFG-Reverse-Game-of-Life

Repositorio del Trabajo Fin de Grado "Predicción del Estado Inicial en el Juego de la Vida de Conway", por Ángel Fernández Caravaca. Aquí encontraremos:

**Autómata:** Scripts para la implementación del autómata celular del Game of Life.

**Contador:** Jupyter Notebook del contador de tableros iniciales asociados a un tablero final.

**Modelo V1:** Jupyter Notebooks para la implementación del modelo de referencia. El entrenamiento se realiza con respecto a los tableros iniciales, mientras que la evaluación se realiza con respecto a los tableros finales. Se usa como función de pérdidas la Binary Cross-Entropy.

**Modelo V1 GoL:** Jupyter Notebooks para la implementación del modelo de referencia. El entrenamiento y la evaluación se realizan con respecto a los tableros finales. Se usa como función de pérdidas la Binary Cross-Entropy. Solo se entrena un modelo por la dificultad para apren

**Modelo V2 GoL:** Jupyter Notebook para la mejora del modelo que contiene una capa extra mediante el uso de la Focal Binary Cross-Entropy. El entrenamiento y la evaluación se realizan con respecto a los tableros finales.

**Reverse GoL V1:** Jupyter Notebooks para propuesta de GoL inverso donde se implementa el modelo delta = 1 de referencia repetidas veces para realizar predicciones sobre las demás deltas.

**Reverse GoL V2:** Jupyter Notebooks para propuesta de GoL inverso donde se implementa el modelo delta = 1 que incorpora la capa del GoL para realizar predicciones sobre las demás deltas.

**Gráficas:** Scripts para la creación de gráficas mostradas en la memoria del TFG.

**NOTA:** es posible que para el correcto funcionamiento de los códigos sea necesaria la modificación de los paths o líneas similares.

Para los conjuntos de datos, por favor, referirse a la competición de Kaggle "Conway Reverse Game of Life": https://www.kaggle.com/competitions/conway-s-reverse-game-of-life
