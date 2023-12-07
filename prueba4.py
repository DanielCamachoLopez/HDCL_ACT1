import pygame
import sys
from pygame import font, draw, mouse
from moviepy.editor import VideoFileClip
import numpy as np

#Botones de inicio
def botones(screen, boton, msg):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(screen, (252, 140, 3), boton, 0)
    else:
        draw.rect(screen, (166, 20, 7), boton, 0)
    texto = fuente.render(msg, True, WHITE)
    screen.blit(texto, (boton.x + (boton.width - texto.get_width()) / 2,
                         boton.y + (boton.height - texto.get_height()) / 2))

#Boton de pregunta 
def btnpregunta(screen,boton,msg):
    draw.rect(screen, (255, 0, 50), boton, 0)
    texto = fuente.render(msg, True, WHITE)
    screen.blit(texto, (boton.x + (boton.width - texto.get_width()) / 2,
                         boton.y + 2))
    
#Botones de respuestas (a hasta d)
def btnrespa(screen, boton, msg):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(screen, (252, 140, 3), boton, 0)
    else:
        draw.rect(screen, (166, 20, 7), boton, 0)
    texto = fuente.render(msg, True, WHITE)
    screen.blit(texto, (boton.x + 2,
                         boton.y + (boton.height - texto.get_height()) / 2))
    
def btnrespb(screen, boton, msg):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(screen, (252, 140, 3), boton, 0)
    else:
        draw.rect(screen, (166, 20, 7), boton, 0)
    texto = fuente.render(msg, True, WHITE)
    screen.blit(texto, (boton.x + 2,
                         boton.y + (boton.height - texto.get_height()) / 2))
def btnrespc(screen, boton, msg):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(screen, (252, 140, 3), boton, 0)
    else:
        draw.rect(screen, (166, 20, 7), boton, 0)
    texto = fuente.render(msg, True, WHITE)
    screen.blit(texto, (boton.x + 2,
                         boton.y + (boton.height - texto.get_height()) / 2))
    
def btnrespd(screen, boton, msg):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(screen, (252, 140, 3), boton, 0)
    else:
        draw.rect(screen, (166, 20, 7), boton, 0)
    texto = fuente.render(msg, True, WHITE)
    screen.blit(texto, (boton.x + 2,
                         boton.y + (boton.height - texto.get_height()) / 2))
                         

pygame.init()

#Definiendo colores
# Rojo, verde, azul
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (800, 500)


# Cargar el GIF con moviepy
gif_path = 'Imagenes/fondomenu2.gif'  # Reemplaza 'tu_archivo.gif' con la ruta de tu propio archivo GIF
clip = VideoFileClip(gif_path)

# Configuración de la pantalla
width, height = clip.size  # Obtener dimensiones del GIF
screen = pygame.display.set_mode((width, height))

# Obtener un numpy array de los frames del GIF
frames = [np.rot90(np.array(frame), 1) for frame in clip.iter_frames(fps=clip.fps)]

# Convertir los frames a objetos Surface de Pygame
surf_frames = [pygame.surfarray.make_surface(frame) for frame in frames]

# Configuración del bucle principal
clock = pygame.time.Clock()
frame_index = 0
background = pygame.image.load("Imagenes/fondomenu2.gif").convert()
imagenfondo = pygame.transform.scale(background, (800, 500))
fuente = font.SysFont("Russo One", 30)
iniciar = pygame.Rect(200, 300, 180, 60)
salir = pygame.Rect(400, 300, 180, 60)
pregunta = pygame.Rect(100, 20, 600, 100)
botona = pygame.Rect(0, 150, 200, 50)
botonb = pygame.Rect(600, 150, 200, 50)
botonc = pygame.Rect(0, 250, 200, 50)
botond = pygame.Rect(600, 250, 200, 50)

pygame.display.set_caption("Quiiz Kombat")

#Reproduccion de sonido
# Inicializar el mezclador de sonido
pygame.mixer.init()

# Cargar la canción
cancion = pygame.mixer.Sound('Audio/player.ogg')

# Reproducir la canción en bucle
cancion.play(-1)  # El argumento -1 indica que la canción se reproducirá en bucle

#sound = pygame.mixer.Sound("Audio/player.ogg")
#sound.play()
#sound.__repr__()
#screen = pygame.display.set_mode(size)


#VARIABLES IMPORTANTES
partida = 1
text = ""
text2 = ""
text3 = ""
text4 = ""
text5 = ""
mostrar_gif = 1
pantalla_negra = 0
historia_inicio = 0
geo_preg = 0
laboratorio = 0
bosque = 0
lab_preg = 0
escenario = 0
escenario2 = 0
gif_titulo = 1
g_over = 0
pregunta1 = 0
pregunta2 = 0
pregunta3 = 0
pregunta4 = 0
pregunta5 = 0
pregunta6 = 0
pregunta7 = 0
pregunta8 = 0
pregunta9 = 0
pregunta10 = 0
espada = 0
malo1 = 0
malo2 = 0
malo3 = 0
malo4 = 0
malo5 = 0
malo6 = 0
malo7 = 0
malo8 = 0
malo9 = 0
malo10 = 0
win1 = 0
msge = 0
msge = 2


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if iniciar.collidepoint(x, y):
                mostrar_gif = False
                pantalla_negra = True
                historia_inicio = True
                gif_titulo = False

            elif salir.collidepoint(x, y):
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Tecla Espacio
                historia_inicio = False
                escenario = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Tecla Enter
                laboratorio = True
                espada = True
                lab_preg = True
                pregunta1 = True
                pygame.time.delay(1000)

        if escenario2:
            laboratorio = False
            espada = False
            lab_preg = False
            malo5 = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Tecla Enter
                    geo_preg = True
                    pregunta6 = True
                    bosque = True
                    escenario2 = False
                    espada = True


    # Zona de dibujo
    # Dibujar el GIF
    if mostrar_gif:
        g_over = False
        scaled_frame = pygame.transform.scale(surf_frames[frame_index], (width, height))

        # Crear una nueva superficie combinando el fondo y el frame
        combined_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        combined_surface.blit(imagenfondo, (0, 0))
        combined_surface.blit(scaled_frame, (0, 0))

        # Dibujar los botones encima de la superficie combinada
        image = pygame.image.load("Imagenes/logojuego2.png")
        image = pygame.transform.scale(image, (320, 320))
        botones(combined_surface, iniciar, "Iniciar")
        botones(combined_surface, salir, "Salir")

        # Mostrar la superficie combinada en la pantalla
        screen.blit(combined_surface, (0, 0))
        screen.blit(image,(225, 0))
        pygame.display.flip()

        frame_index = (frame_index + 1) % len(surf_frames)

        clock.tick(clip.fps)
    
    #Pantalla en negro
    if pantalla_negra:
        screen.fill((0, 0, 0))

    #Tamaño de todas las letras
    font = pygame.font.Font(None, 28)

    # Renderizar y mostrar el texto
    text_surface = font.render(text, True, RED)
    screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 8 - text_surface.get_height() // 2))

    text_surface = font.render(text2, True, WHITE)
    screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 3 - text_surface.get_height() // 2))

    text_surface = font.render(text3, True, WHITE)
    screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 2 - text_surface.get_height() // 2))

    text_surface = font.render(text4, True, WHITE)
    screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 1.5 - text_surface.get_height() // 2))

    text_surface = font.render(text5, True, GREEN)
    screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 1.2 - text_surface.get_height() // 2))


    #Historia inicial
    if historia_inicio:
        text = "EL MUNDO ESTÁ EN PELIGRO"
        text2 = "Después de que una nave desconocida aterrizara en la tierra, el caos comienza."
        text3 = "Con todo el mundo en pánico y sin escape, es tu turno de defender nuestro hogar. "
        text4 = "Equipado con una espada, sales al rescate de nuestro planeta"
        text5 = "Presiona ESPACIO para continuar"

    if escenario:
        text = "Primer Kombate"
        text2 = "Escenario:  Laboratorio"
        text3 = ""
        text4 = ""
        text5 = "Presiona ENTER para komenzar"

    if laboratorio:
        image = pygame.image.load("Imagenes/laboratorio2.png") 
        screen.blit(image, (0, 0))
     
    if bosque:
        imagen = pygame.image.load("Imagenes/bosque4.png") 
        screen.blit(imagen, (0, 0))

    if malo1:
        malo = pygame.image.load("Imagenes/malo1.png") 
        screen.blit(malo, (170, 100))

    if malo2:
        malo = pygame.image.load("Imagenes/malo2.png") 
        screen.blit(malo, (170, 170))

    if malo3:
        malo = pygame.image.load("Imagenes/malo3.png") 
        screen.blit(malo, (200, 100))

    if malo4:
        malo = pygame.image.load("Imagenes/malo4.png") 
        screen.blit(malo, (170, 100))

    if malo5:
        malo = pygame.image.load("Imagenes/malo5.png") 
        screen.blit(malo, (170, 100))
    
    if malo6:
        malo = pygame.image.load("Imagenes/malo6.png") 
        screen.blit(malo, (150, 100))

    if malo7:
        malo = pygame.image.load("Imagenes/malo7.png") 
        screen.blit(malo, (170, 90))

    if malo8:
        malo = pygame.image.load("Imagenes/malo8.png") 
        screen.blit(malo, (170, 50))

    if malo9:
        malo = pygame.image.load("Imagenes/malo9.png") 
        screen.blit(malo, (190, 100))

    if malo10:
        malo = pygame.image.load("Imagenes/malo10.png") 
        screen.blit(malo, (190, 100))

    if espada:
        espada1 = pygame.image.load("Imagenes/espada1.png") 
        screen.blit(espada1, (230, 130))

    if win1:
        escenario = False
        escenario2 = False
        pantalla_negra = True
        if pantalla_negra:
            screen.fill((0, 0, 0))
        pregunta1 = False
        pregunta2 = False
        pregunta3 = False
        pregunta4 = False
        pregunta5 = False
        msge2 = True

        if msge2:
            text_surface = font.render(text, True, RED)
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 8 - text_surface.get_height() // 2))

            text_surface = font.render(text2, True, WHITE)
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 3 - text_surface.get_height() // 2))

            text_surface = font.render(text3, True, WHITE)
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 2 - text_surface.get_height() // 2))

            text_surface = font.render(text4, True, WHITE)
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 1.5 - text_surface.get_height() // 2))

            text_surface = font.render(text5, True, GREEN)
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 1.2 - text_surface.get_height() // 2))
            
            text = "FELICIDADES"
            text2 = "HAS GANADO EL JUEGO"
            text3 = "Los invasores han escapado... por ahora"
            text4 = ""
            text5 = "Presiona ENTER para volver al menú principal."

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Tecla Enter
                malo1 = False
                malo2 = False
                malo3 = False
                malo4 = False
                malo5 = False
                malo6 = False
                malo7 = False
                malo8 = False
                malo9 = False
                malo10 = False
                pregunta1 = False
                pregunta2 = False
                pregunta3 = False
                pregunta4 = False
                pregunta5 = False
                pregunta6 = False
                pregunta7 = False
                pregunta8 = False
                pregunta9 = False
                pregunta10 = False
                espada = False
                laboratorio = False
                bosque =  False
                escenario = False
                escenario2 = False
                mostrar_gif = True
                gif_titulo = True
                win1 = False
                msge2 = False
                text = ""
                text2 = ""
                text3 = ""
                text4 = ""
                text5 = ""
                pantalla_negra = False
                pygame.time.delay(1000)
    if g_over:
        pantalla_negra = True
        if pantalla_negra:
            screen.fill((0, 0, 0))
        pregunta1 = False
        pregunta2 = False
        pregunta3 = False
        pregunta4 = False
        pregunta5 = False
        pregunta6 = False
        pregunta7 = False
        pregunta8 = False
        pregunta9 = False
        pregunta10 = False
        win1 = False
        msge = True
        
        if msge:
            text = "GAME OVER"
            text2 = "Has sido derrotado"
            text3 = ""
            text4 = ""
            text5 = "Presiona ENTER para volver al menú principal."

            text_surface = font.render(text, True, RED)
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 8 - text_surface.get_height() // 2))

            text_surface = font.render(text2, True, WHITE)
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 3 - text_surface.get_height() // 2))

            text_surface = font.render(text3, True, WHITE)
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 2 - text_surface.get_height() // 2))

            text_surface = font.render(text4, True, WHITE)
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 1.5 - text_surface.get_height() // 2))

            text_surface = font.render(text5, True, GREEN)
            screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, height // 1.2 - text_surface.get_height() // 2))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Tecla Enter
                malo1 = False
                malo2 = False
                malo3 = False
                malo4 = False
                malo5 = False
                malo6 = False
                malo7 = False
                malo8 = False
                malo9 = False
                malo10 = False
                pregunta1 = False
                pregunta2 = False
                pregunta3 = False
                pregunta4 = False
                pregunta5 = False
                pregunta6 = False
                pregunta7 = False
                pregunta8 = False
                pregunta9 = False
                pregunta10 = False
                espada = False
                laboratorio = False
                bosque =  False
                escenario = False
                escenario2 = False
                mostrar_gif = True
                gif_titulo = True
                g_over = False
                msge = False
                text = ""
                text2 = ""
                text3 = ""
                text4 = ""
                text5 = ""
                pantalla_negra = False
                pygame.time.delay(1000)
    
    


    if lab_preg:   
        #Cargar preguntas cuando este el escenario del laboratorio  
        if pregunta1:
            malo1 = True
            btnpregunta(screen, pregunta, "1.-¿Qué es más grande un átomo o una célula?")
            btnrespa(screen, botona, "a) Àtomo")
            btnrespb(screen, botonb, "b) Cèlula")
            btnrespc(screen, botonc, "c) Protòn")
            btnrespd(screen, botond, "d) Son iguales")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if botonb.collidepoint(x, y):
                        pregunta1 = False
                        pregunta2 = True
                    elif botona.collidepoint(x,y) or botonc.collidepoint(x,y) or botond.collidepoint(x,y):
                        g_over = True

        if pregunta2:
            malo1 = False
            malo2 = True
            btnpregunta(screen, pregunta, "2.-¿Cuántos corazones tiene un pulpo?")
            btnrespa(screen, botona, "a) 3")
            btnrespb(screen, botonb, "b) 1")
            btnrespc(screen, botonc, "c) 8")
            btnrespd(screen, botond, "d) 2")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if botona.collidepoint(x, y):
                        pregunta1 = False
                        pregunta2 = False
                        pregunta3 = True

                    elif botonb.collidepoint(x,y) or botonc.collidepoint(x,y) or botond.collidepoint(x,y):
                        g_over = True
        
        if pregunta3:
            malo2 = False
            malo3 = True
            btnpregunta(screen, pregunta, "3.-¿Cuántos dientes tiene un humano adulto?")
            btnrespa(screen, botona, "a) 20")
            btnrespb(screen, botonb, "b) 35")
            btnrespc(screen, botonc, "c) 32")
            btnrespd(screen, botond, "d) Ninguna")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if botonc.collidepoint(x, y):
                        pregunta1 = False
                        pregunta2 = False
                        pregunta3 = False
                        pregunta4 = True
   
                    elif botona.collidepoint(x,y) or botonb.collidepoint(x,y) or botond.collidepoint(x,y):
                        g_over = True

        if pregunta4:
            malo3 = False
            malo4 = True
            btnpregunta(screen, pregunta, "4.-¿Cómo se llama el estudio de los hongos?") 
            btnrespa(screen, botona, "a) Micologìa")
            btnrespb(screen, botonb, "b) Hongologìa")
            btnrespc(screen, botonc, "c) Microbiologìa")
            btnrespd(screen, botond, "d) Zoologìa")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if botona.collidepoint(x, y):
                        pregunta1 = False
                        pregunta2 = False
                        pregunta3 = False
                        pregunta4 = False
                        pregunta5 = True
                    elif botonb.collidepoint(x,y) or botonc.collidepoint(x,y) or botond.collidepoint(x,y):
                        g_over = True

        if pregunta5:
            malo4 = False
            malo5 = True
            btnpregunta(screen, pregunta, "5.-¿Cuántos elementos hay en la Tabla Periódica?") 
            btnrespa(screen, botona, "a) 118")
            btnrespb(screen, botonb, "b) 98")
            btnrespc(screen, botonc, "c) 124")
            btnrespd(screen, botond, "d) 110")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if botona.collidepoint(x, y):
                        pantalla_negra = True
                        malo5 = False
                        laboratorio = False
                        espada = False
                        laboratorio = False
                        escenario2 = True

                    elif botonb.collidepoint(x,y) or botonc.collidepoint(x,y) or botond.collidepoint(x,y):
                        g_over = True
        

    if escenario2:
        pygame.time.delay(250)
        text = "Segundo Kombate"
        text2 = "Escenario:  Bosque en llamas"
        text3 = ""
        text4 = ""
        text5 = "Presiona ENTER para komenzar"

    if geo_preg:
        if pregunta6:
            malo6 = True
            btnpregunta(screen, pregunta, "1.-¿Cuál es el país más pequeño del mundo?")
            btnrespa(screen, botona, "a) Turquía")
            btnrespb(screen, botonb, "b) El Vaticano")
            btnrespc(screen, botonc, "c) San Marino")
            btnrespd(screen, botond, "d) Isla de Pascua")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if botonb.collidepoint(x, y):
                        pregunta6 = False
                        pregunta7 = True
                    elif botona.collidepoint(x,y) or botonc.collidepoint(x,y) or botond.collidepoint(x,y):
                        g_over = True
        
        if pregunta7:
            malo6 = False
            malo7 = True
            btnpregunta(screen, pregunta, "2.-¿Qué país es el más grande del mundo?")
            btnrespa(screen, botona, "a) Rusia")
            btnrespb(screen, botonb, "b) China")
            btnrespc(screen, botonc, "c) Estados Unidos")
            btnrespd(screen, botond, "d) Canadá")
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if botona.collidepoint(x, y):
                        pregunta6 = False
                        pregunta7 = False
                        pregunta8 = True
                    elif botonb.collidepoint(x,y) or botonc.collidepoint(x,y) or botond.collidepoint(x,y):
                        g_over = True
        
        if pregunta8:
            malo7 = False
            malo8 = True
            btnpregunta(screen, pregunta, "3.-¿Cuál es la capital de Suecia?")
            btnrespa(screen, botona, "a) Estocolmo")
            btnrespb(screen, botonb, "b) Dublín")
            btnrespc(screen, botonc, "c) Washington")
            btnrespd(screen, botond, "d) Oslo")
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if botona.collidepoint(x, y):
                        pregunta6 = False
                        pregunta7 = False
                        pregunta8 = False
                        pregunta9 = True
                    elif botonb.collidepoint(x,y) or botonc.collidepoint(x,y) or botond.collidepoint(x,y):
                        g_over = True
        

        if pregunta9:
            malo8 = False
            malo9 = True
            btnpregunta(screen, pregunta, "4.-¿Cuántos países son parte de las Naciones Unidas?") 
            btnrespa(screen, botona, "a) 174")
            btnrespb(screen, botonb, "b) 202")
            btnrespc(screen, botonc, "c) 185")
            btnrespd(screen, botond, "d) 193")
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if botond.collidepoint(x, y):
                        pregunta6 = False
                        pregunta7 = False
                        pregunta8 = False
                        pregunta9 = False
                        pregunta10 = True
                    elif botona.collidepoint(x,y) or botonb.collidepoint(x,y) or botonc.collidepoint(x,y):
                        g_over = True
        
        
        if pregunta10:
            malo9 = False
            malo10 = True
            btnpregunta(screen, pregunta, "5.-¿En qué país están las ruinas de Petra?") 
            btnrespa(screen, botona, "a) Egipto")
            btnrespb(screen, botonb, "b) Irán")
            btnrespc(screen, botonc, "c) Jordania")
            btnrespd(screen, botond, "d) Israel")
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = event.pos
                    if botonc.collidepoint(x, y):
                        lab_preg = False
                        geo_preg = False
                        win1 = True
                    elif botona.collidepoint(x,y) or botonb.collidepoint(x,y) or botond.collidepoint(x,y):
                        g_over = True
        
    


    # Actualizar la pantalla
    pygame.display.flip()