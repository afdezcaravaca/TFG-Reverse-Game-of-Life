import sys, pygame
import tkinter as tk
from tkinter import filedialog, messagebox
import os

root = tk.Tk()
root.withdraw() # Oculta la ventana principal (root) de Tkinter para mostrar los cuadros de dialogo de carga y guardado de archivo.

from conway import Conway # Importamos la clase Conway del módulo conway.

# Definición de las constantes:

    # Ancho y alto de la ventana en pixeles.
size = width, height = 400, 564  

    # Colores de la pantalla. Formato RGB:
black = (0,0,0) 
white = (255,255,255)
gray = (92,92,92)


def mouse_click(world: Conway, mouse_x: int, mouse_y: int) -> None:
    '''
    Función de captura de la pulsación del raton sobre área de proyección del espacio del autómata celular.
    :param world: instancia de la clase Conway.
    :param mouse_x: coordenada X en píxeles del cursor del ratón al hacer click.
    :param mouse_y: coordenada Y en píxeles del cursor del ratón al hacer click.
    :return:
    '''

    x = int(mouse_x /20) # Conversión de coordenada X en píxeles a coordenada X en el espacio.
    y = int(mouse_y /20) # Conversión de coordenada Y en píxeles a coordenada Y en el espacio.

    if world.read(x, y) == world.LIVE: # Si la celda está viva.
        world.write(x, y, world.DEAD) # Muere
    else: # Está muerta
        world.write(x, y, world.LIVE) # Nace

def guardar_tablero_como_imagen(screen: pygame.Surface) -> None:
    '''
    Guarda solo el área del tablero (400x400 px) como imagen PNG.
    '''
    file_path_png = filedialog.asksaveasfilename(defaultextension=".png", filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
    if file_path_png:
        tablero_surface = screen.subsurface(pygame.Rect(0, 0, 400, 400))  # Solo el tablero
        pygame.image.save(tablero_surface, file_path_png)



def main():
    # Instancias:
    pygame.init()
    pygame.font.init()
    world = Conway()

    # Cargar imágenes PNG para icónos de control.
    os.chdir(os.path.join(os.getcwd(), "Imágenes"))
    
    # Creación de la ventana:
    screen = pygame.display.set_mode(size) # Creación de la ventana.
    pygame.display.set_caption('Juego de la Vida Conway') # Título de la ventana.
   

    
    start = pygame.image.load('start.png') # Cargar imagen de inicio.
    startrect = start.get_rect() # Obtener el rectángulo de la imagen de inicio.
    startrect = startrect.move(24,410) # Lo movemos a los píxeles 404,500.	

    stop = pygame.image.load('stop.png') 
    stoprect = stop.get_rect() 
    stoprect = stoprect.move(98,410) 

    clear = pygame.image.load('clear.png') 
    clearrect = clear.get_rect() 
    clearrect = clearrect.move(172,410) 

    save = pygame.image.load("guardar.png") 
    saverect = save.get_rect()
    saverect = saverect.move(246,410)

    cargar = pygame.image.load("cargar.png")
    cargarrect = cargar.get_rect()
    cargarrect = cargarrect.move(320,410)

    
    # Fuente de texto:
    myfont = pygame.font.SysFont('Lucida Console', 20)

    # Estado del AC -> Parado
    running = False

    # Bucle principal:
    while 1:
        # Captura de eventos:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Evento de cierre de ventana.
                print("Saliendo...")
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN: # Evento de pulsación d ratón.
                x, y = pygame.mouse.get_pos() # Coordenadas del ratón.

                if y <= 400: 
                    mouse_click(world, x, y)  # Pulsación sobre celda.
                else:
                    if startrect.collidepoint(x, y):  # Pulsación sobre icono de Start.
                        running = True
                        

                    if stoprect.collidepoint(x, y):  # Pulsación sobre icono de Stop.
                        running = False

                    if clearrect.collidepoint(x, y): # Pulsación icono Limpiar.
                        world.reset()

                    if cargarrect.collidepoint(x, y): # Pulsación icono Cargar.
                        file_path_string = filedialog.askopenfilename(filetypes=(("Conway GoL files", "*.cgl"), ("All files", "*.*"))) # Diálogo de carga de archivo.
                        if file_path_string != '':
                            world.load(file_path_string) # Cargar archivo.

                    if saverect.collidepoint(x, y):  # Pulsación de icono Guardar.
                        file_path_string = filedialog.asksaveasfilename(
                        defaultextension=".cgl",
                        filetypes=(
                                ("Conway GoL files", "*.cgl"),
                                ("PNG image", "*.png"),
                                ("All files", "*.*")
                            )
                        )
                        if file_path_string:
                            if file_path_string.endswith(".cgl"):
                                world.save(file_path_string)
                            elif file_path_string.endswith(".png"):
                                guardar_tablero_como_imagen(screen)



        # Actualización del AC:
        i = 1
        if running:
             pygame.time.delay(500)    
             world.update()


        # Refresco de pantalla:
        screen.fill(black)
        world.draw(screen) # Repintado celdas del AC.
        screen.blit(start, startrect) # Repintado de los iconos
        screen.blit(stop, stoprect)
        screen.blit(clear, clearrect)
        screen.blit(save, saverect)
        screen.blit(cargar, cargarrect)

        # Actualización del texto.
        text0 = "Estado:" + ("Running" if running else "Paused") # Texto del estado del AC.
        textsurface = myfont.render(text0, True, white) # Texto del estado del AC.
        screen.blit(textsurface, (20,480)) # Posición del texto.

        text1 = "Generación: " + str(world.iterations) # Texto con el número de generaciones.
        screen.blit(myfont.render(text1, True, white), (20,500)) # Texto con el número de generaciones.

        text2 = "Células vivas: " + str(world.livecells) # Texto con el número de células vivas.
        screen.blit(myfont.render(text2, True, white), (20,520)) # Texto con el número de células vivas.

        pygame.display.flip() # Refresco de la pantalla.
    
if __name__ == '__main__':
    main() 




    
