#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# Escrito por Sebastian Vahos
 
# ---------------------------
# Importacion de los modulos
# ---------------------------
 
import random
import pygame
from pygame.locals import *
import sys
import os
import time
<<<<<<< HEAD
=======

 
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
 
# -----------
# Constantes
# -----------
<<<<<<< HEAD

=======
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
 
PantX = 740
PantY = 710
ImgDir = "images"


<<<<<<< HEAD

#TamImg = 100
#Margen = 10
#InicioX = 100
#InicioY = 100

=======
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
DARKGRAY = (60, 60, 60)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)
<<<<<<< HEAD
=======
BLACK = (0, 0, 0)
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d

NumeroImagenes = 18


def cargar_imagen(numDog):
    # Encontramos la ruta completa de la imagen
    nombreImg = "dog"+str(numDog)+".jpg"
    ruta = os.path.join(ImgDir, nombreImg)
    try:
        image = pygame.image.load(ruta)
    except:
        print "Error, no se puede cargar la imagen: ", ruta
        sys.exit(1)
    image = pygame.transform.scale(image,(TamImg,TamImg))
    image = image.convert()
    return image
 
<<<<<<< HEAD
def cargar_menu():
=======
def cargar_menu(cargarAnimacion = False):
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
    op2x2=pygame.image.load("images/2x2.jpg")
    op4x4=pygame.image.load("images/4x4.jpg")
    op6x6=pygame.image.load("images/6x6.jpg")
     
    op2x2 = pygame.transform.scale(op2x2,(200,75))
    op4x4 = pygame.transform.scale(op4x4,(200,75))
    op6x6 = pygame.transform.scale(op6x6,(200,75))
    
    op2x2 = op2x2.convert()
    op4x4 = op4x4.convert()
    op6x6 = op6x6.convert()
    
    rec2=op2x2.get_rect()
    rec4=op4x4.get_rect()
    rec6=op6x6.get_rect()
    
    x=370
    y=250

    #** Animacion
<<<<<<< HEAD
#    clock = pygame.time.Clock()
#    tick=200
#    for i in range(600):
#        clock.tick(tick)
#        screen.fill((255, 255, 255))
#        screen.blit(op2x2, (i, y))
#        pygame.display.update()
#    for i in range(600):
#        clock.tick(tick)
#        screen.fill((255, 255, 255))
#        screen.blit(op4x4, (i, y+100))
#        pygame.display.update()
#    for i in range(600):
#        clock.tick(tick)
#        screen.fill((255, 255, 255))
#        screen.blit(op6x6, (i, y+200))
#        pygame.display.update()
=======
    if(cargarAnimacion):
        clock = pygame.time.Clock()
        tick=200
        for i in range(600):
            clock.tick(tick)
            screen.fill((255, 255, 255))
            screen.blit(op2x2, (i, y))
            pygame.display.update()
        for i in range(600):
            screen.blit(op2x2, rec2)
            clock.tick(tick)
            screen.fill((255, 255, 255))
            screen.blit(op4x4, (i, y+100))
            pygame.display.update()
        for i in range(600):
            screen.blit(op4x4, rec4)
            clock.tick(tick)
            screen.fill((255, 255, 255))
            screen.blit(op6x6, (i, y+200))
            pygame.display.update()
        cargarAnimacion=False
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
        
    
    screen.fill((255, 255, 255))
    
    
    rec2.centerx = x
    rec2.centery = y
    rec4.centerx = x
    rec4.centery = y+100
    rec6.centerx = x
    rec6.centery = y+200
    
    screen.blit(op2x2, rec2)
    screen.blit(op4x4, rec4)
    screen.blit(op6x6, rec6)
    
<<<<<<< HEAD
    return ((rec2,(2,250,10,230,230)),(rec4,(4,150,10,130,130)),(rec6,(6,100,10,90,90)))
=======
    # Se retorna un objeto pygame.Rec para el manejo de coordenas junto con toda la configuracion
    # requerida en cada tipo de juego dentro de una tupla.
    #  Num      --> Indica la modalidad del juego. (Ej: Num=2 indica un cuadro de 2x2).
    #  TamImg   --> Indica que tamaños en pixeles llevaran cada imagen del juego (Ej: TamImg=200 indica imagenes de 200x200 pixeles).
    #  Margen   --> Indica la separacion en pixeles entre las imagenes.
    #  InicioX  --> Indica la coordenada X de la parte superior izquierda de la pantalla donde se empiezan a pintar los recuadros.
    #  InicioY  --> Indica la coordenada Y de la parte superior izquierda de la pantalla donde se empiezan a pintar los recuadros.
    #  Intentos --> Indica cuantos pares de imagenes puede el jugador destapar en cada modalidad antes de que pierda.
    #  Tupla = (Num,TamImg,Margen,InicioX,InicioY,Intentos).
    return ((rec2,(2,250,10,230,230,2)),(rec4,(4,150,10,130,130,8)),(rec6,(6,100,10,90,90,18)))
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
    
class Imagen(pygame.sprite.Sprite):
    
    def __init__(self,x,y,dogNum,index):
        pygame.sprite.Sprite.__init__(self)
        self.dogNum = dogNum
        self.image = cargar_imagen(dogNum)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.index = index
        self.isOculta = True
        self.ocultar()
        self.noSelect = True
    
    def pintar(self):
        screen.blit(self.image, self.rect)
    
    def resaltar(self):
        pygame.draw.rect(screen, BLUE, self.rect, 3)
        pygame.display.update()
    
    def ocultar(self):
        pygame.draw.rect(screen, GREEN, self.rect)
    
    def mostrar(self):
        if self.isOculta:
            self.ocultar()
        else:
            self.pintar()
    
    def desOcultar(self):
        self.isOculta = False
    
    def desOcultar2(self):
        self.pintar()
        pygame.display.update()
        self.isOculta = False
        time.sleep(0.5)
    
    def ocultarAnterior(self):
        self.noSelect = True
        self.isOculta = True
        
<<<<<<< HEAD

        
        
#    def mostrar(self):
#    if self.oculta:
=======
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
        
def inicializar_tablero(tam):
    # tam=2 , 4 , 6
    numImagenes = tam**2/2
    
    allImgs = range(1,NumeroImagenes+1)
    random.shuffle(allImgs)
    
    #se seleccionan solo las primeras imagenes ya sea 2,8,18  (4/2 16/2 36/2)
    images = allImgs[:numImagenes]
    #luego se sacan las parejas 
    images = images*2
    #Por ultimo vuelve y se realiza un random
    random.shuffle(images)
    
    index = 0
    x=InicioX
    y=InicioY
    
    tablero=[]
    for i in range(tam):
        fila = []
        for j in range(tam):
            oImg = Imagen(x,y,images[index],index)
            fila.append(oImg)
            x+=TamImg+Margen
            index+=1
        tablero.append(fila)    
        y+=TamImg+Margen
        x=InicioX
    return tablero

<<<<<<< HEAD
=======
# Resalta las opcion del menu principal (2x2 4x4 6x6)
def isOverOptions(x,y,opciones):
    for op in opciones:
        if op[0].collidepoint(x,y):
            pygame.draw.rect(screen, BLUE, op[0], 3)
            pygame.display.update()
            break;

# Resalta los recuadros del juego
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
def isOverBox(x, y):
    for i in range(Num):
        for j in range(Num):
            oImg = Tablero[i][j]
            if oImg.rect.collidepoint(x, y):
                oImg.resaltar()
                break

def getImagenClick(x,y):
    for i in range(Num):
        for j in range(Num):
            oImg = Tablero[i][j]
            if oImg.rect.collidepoint(x, y):
                if oImg.noSelect:
                    oImg.noSelect = False
                    return oImg
                else:
                    return None
    return None

<<<<<<< HEAD
def pintar_tablero():
=======
def pintar_tablero(numIntentos):
    screen.fill(WHITE)
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
    for i in range(Num):
        for j in range(Num):
            oImg = Tablero[i][j]
            oImg.mostrar()
<<<<<<< HEAD
=======
    informacionJuego(numIntentos)
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d

def hayGanador():
    for i in range(Num):
        for j in range(Num):
            oImg = Tablero[i][j]
            if oImg.isOculta:
                return False
    return True
<<<<<<< HEAD
=======

def informacionJuego(numIntentos):
    text = "Concentrese: %d X %d        Intentos: %3d " % (Num,Num, numIntentos)
    mensaje = font.render(text, 1,DARKGRAY)
    screen.blit(mensaje, (15, 5))

   
def splitIntoGroupsOf(groupSize, theList):
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i+groupSize])
    return result   
   
def vistaRapida():
    pintar_tablero(Intentos)
    coordenadaImages = []
    for x in range(Num):
        for y in range(Num):
            coordenadaImages.append( (x, y) )
    random.shuffle(coordenadaImages)
    contWait = 1
    for dirImg in coordenadaImages:
        x=dirImg[0]
        y=dirImg[1]
        oImg = Tablero[x][y]
        oImg.pintar()
        if contWait == Num:
            pygame.display.update()
            time.sleep(0.7)
            pintar_tablero(Intentos)
            pygame.display.update()
            contWait=1
        else:
            contWait+=1
            
    
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
 
def main():
    pygame.init()
    # Num = 2,4,6
<<<<<<< HEAD
    global Num,TamImg,Margen,InicioX,InicioY,Tablero
=======
    global Num,TamImg,Margen,InicioX,InicioY,Tablero,Intentos
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
    # creamos la ventana y le indicamos un titulo:
    global screen
    screen = pygame.display.set_mode((PantX, PantY))
    pygame.display.set_caption("Concentrese!")
    screen.fill((255, 255, 255))
<<<<<<< HEAD
 
   
    # se muestran lo cambios en pantalla
#    Num = 2
#    TamImg = 250
#    Margen = 10
#    InicioX = 230
#    InicioY = 230
    
#    Num = 4
#    TamImg = 150
#    Margen = 10
#    InicioX = 130
#    InicioY = 130
##    
#    Num = 6
#    TamImg = 100
#    Margen = 10
#    InicioX = 90
#    InicioY = 90
    
    
 
#    Tablero=inicializar_tablero(Num)
#    pygame.display.flip()
    
    
    # el bucle principal del juego
    #MENU
    opciones=cargar_menu()
=======
    
    #Se define el tipo de letra
    global font
    font = pygame.font.Font(None, 20)
    
    #MENU
    opciones=cargar_menu(True)
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
    Menu=True
    
    mousex = 0
    mousey = 0
    firstClick = True
    img_click1 = None
<<<<<<< HEAD
=======
    #Bucle principal del juego
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
    while True:
        clicked = False
        
        #Eventos Mouse
        #inicializar_tablero(Num)
        
        if Menu:
<<<<<<< HEAD
#            cargar_menu()
            pygame.display.flip()
=======
            pygame.display.flip()
            cargar_menu()
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
<<<<<<< HEAD
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    clicked = True
            if clicked:
                for rec in opciones:
                    if rec[0].collidepoint(mousex, mousey):
                        Num,TamImg,Margen,InicioX,InicioY = rec[1]
                        Menu=False
                        Tablero=inicializar_tablero(Num)
                        screen.fill((255, 255, 255))
=======
                if event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    clicked = True
            isOverOptions(mousex,mousey,opciones)
            if clicked:
                for rec in opciones:
                    if rec[0].collidepoint(mousex, mousey):
                        screen.fill(WHITE)
                        #Se inicializan la variables principales del juego y el tablero de juego
                        Num,TamImg,Margen,InicioX,InicioY,Intentos = rec[1]
                        Tablero=inicializar_tablero(Num)
                        vistaRapida()
                        Menu=False
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
                        break
                    
                print("Tablero")
        else:
<<<<<<< HEAD
            pintar_tablero()
=======
            pintar_tablero(Intentos)
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEMOTION:
                    mousex, mousey = event.pos
                if event.type == MOUSEBUTTONUP:
                    mousex, mousey = event.pos
                    clicked = True

            isOverBox(mousex,mousey)
            if clicked:
                img=getImagenClick(mousex,mousey)
                if img is not None:
                    if firstClick:
                        img_click1 = img
                        img_click1.desOcultar()
                        firstClick = False
                        print "Desocultar"
                    else:
                        img.desOcultar2()
                        if img_click1.dogNum == img.dogNum:
                            print("iguales")
                        else:
                            print("diferentes")
<<<<<<< HEAD
=======
                            #Se decrementa el numero de intentos
                            Intentos-=1
                            print("Intentos",Intentos)
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
                            img_click1.ocultarAnterior()
                            img.ocultarAnterior()
                        firstClick = True
            if hayGanador():
<<<<<<< HEAD
                text = "GANASTE!!!"
                fuente = pygame.font.Font(None, 30)
                mensaje = fuente.render(text, 1, (255, 255, 255))
                screen.fill((30, 145, 255))
                screen.blit(mensaje, (100, 350))
                pygame.display.flip()
                time.sleep(3)
                screen.fill((255, 255, 255))
                opciones=cargar_menu()
                Menu=True
                print("GANASTE!!")
            
=======
                text = "GANASTE..."
                fuente = pygame.font.Font(None, 30)
                mensaje = fuente.render(text, 1, WHITE)
                screen.fill((30, 145, 255))
                screen.blit(mensaje, (300, 350))
                pygame.display.flip()
                time.sleep(2)
                screen.fill(WHITE)
                opciones=cargar_menu()
                Menu=True
                print(text)
            elif(Intentos == 0):
                text = "PERDISTE..."
                fuente = pygame.font.Font(None, 30)
                mensaje = fuente.render(text, 1, BLACK)
                screen.fill(ORANGE)
                screen.blit(mensaje, (300, 350))
                pygame.display.flip()
                time.sleep(2)
                screen.fill(WHITE)
                opciones=cargar_menu()
                Menu=True
                print(text)
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
            
 
if __name__ == "__main__":
    main()
<<<<<<< HEAD
    
=======
    
>>>>>>> c34cc2353447233334a23d7f604c57840c668e5d
