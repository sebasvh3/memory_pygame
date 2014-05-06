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
 
# -----------
# Constantes
# -----------

 
PantX = 740
PantY = 710
ImgDir = "images"



#TamImg = 100
#Margen = 10
#InicioX = 100
#InicioY = 100

DARKGRAY = (60, 60, 60)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

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
 
def cargar_menu():
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
    
    return ((rec2,(2,250,10,230,230)),(rec4,(4,150,10,130,130)),(rec6,(6,100,10,90,90)))
    
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
        

        
        
#    def mostrar(self):
#    if self.oculta:
        
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

def pintar_tablero():
    for i in range(Num):
        for j in range(Num):
            oImg = Tablero[i][j]
            oImg.mostrar()

def hayGanador():
    for i in range(Num):
        for j in range(Num):
            oImg = Tablero[i][j]
            if oImg.isOculta:
                return False
    return True
 
def main():
    pygame.init()
    # Num = 2,4,6
    global Num,TamImg,Margen,InicioX,InicioY,Tablero
    # creamos la ventana y le indicamos un titulo:
    global screen
    screen = pygame.display.set_mode((PantX, PantY))
    pygame.display.set_caption("Concentrese!")
    screen.fill((255, 255, 255))
 
   
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
    Menu=True
    
    mousex = 0
    mousey = 0
    firstClick = True
    img_click1 = None
    while True:
        clicked = False
        
        #Eventos Mouse
        #inicializar_tablero(Num)
        
        if Menu:
#            cargar_menu()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
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
                        break
                    
                print("Tablero")
        else:
            pintar_tablero()
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
                            img_click1.ocultarAnterior()
                            img.ocultarAnterior()
                        firstClick = True
            if hayGanador():
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
            
            
 
if __name__ == "__main__":
    main()
    