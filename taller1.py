# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 11:49:25 2020

@author: Nestor Ribero
"""

import cv2


class colorImage:  # se crea la clase colorImage

    def __init__(self, path_file):  # se define el constructor
        self.image = cv2.imread(path_file, 1)  # se carga la imagen (via OpenCV) y se almacena en self

    def displayProperties(self):  # metodo para mostrar tamaño de la imagen
        print("La dimensión de la imagen son", self.image.shape[0], "x", self.image.shape[
            1])  # se utiliza la funcion shape que es una lista donde se encuentra en la primera posicion el alto y en la segunda el ancho

    def makeGray(self):  # metodo para mostrar la imagen en escala de grises

        Gray_Img = cv2.cvtColor(self.image,
                                cv2.COLOR_BGR2GRAY)  # se utiliza la funcion cv2.cvtColor() cuyos parámetros son la imagen y el espacio de color que se quiere usar, en nuestro caso se quiere pasar de BGR a Gray por lo que se utiliza cv2.COLOR_BGR2GRAY
        cv2.imshow('Gray Image', Gray_Img)

    def colorizeRGB(self, canal_de_color):  # metodo para mostrar imagen colorizada con un respectivo canal de color

        Gray_Img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        if canal_de_color == 'blue':  # condicional que verifica si el canal de color deseado es azul
            b = self.image.copy()  # se copia la imagen original en la variable b
            b[:, :, 0] = Gray_Img  # se colocan las componentes verdes en cero
            b[:, :, 1] = 0  # se colocan las componentes verdes en cero
            b[:, :, 2] = 0  # se colocan las componentes rojas en cero
            cv2.imshow('Blue image', b)  # se muestra la imagen

        if canal_de_color == 'green':  # condicional que verifica si el canal de color deseado es verde
            g = self.image.copy()  # se copia la imagen original en la variable g
            g[:, :, 0] = 0  # se colocan las componentes azules en cero
            g[:, :, 1] = Gray_Img  # se colocan las componentes verdes en cero
            g[:, :, 2] = 0  # se colocan las componentes rojas en cero
            cv2.imshow('Green image', g)  # se muestra la imagen

        if canal_de_color == 'red':  # condicional que verifica si el canal de color deseado es rojo
            r = self.image.copy()  # se copia la imagen original en la variable r
            r[:, :, 0] = 0  # se colocan las componentes azules en cero
            r[:, :, 1] = 0  # se colocan las componentes verdes en cero
            r[:, :, 2] = Gray_Img  # se colocan las componentes verdes en cero
            cv2.imshow('Red image', r)  # se muestra la imagen

    def makeHue(self):  # metodo para mostrar imagen en tonos
        HSV_Image = cv2.cvtColor(self.image,
                                 cv2.COLOR_BGR2HSV)  # se guarda en HSV_Image la imagen original en el espacio de color HSV, por lo que se utiliza la funcion cv2.cvtColor() cuyos parámetros son la imagen y el espacio de color que se quiere usar
        HSV_Image[:, :, 1] = 255  # se coloca la componentes S en 255
        HSV_Image[:, :, 2] = 255  # se coloca la componente V en 255
        HSV_Image = cv2.cvtColor(HSV_Image, cv2.COLOR_HSV2BGR)  # se transforma el espacio de color de HSV a BGR
        cv2.imshow('Imagen en tonos', HSV_Image)  # se muestra la imagen


if __name__ == '__main__':
    ruta_imagen = input(
        'Ingrese la ruta de la imagen: ')  # se pide al usuario que ingrese la ruta completa de la imagen
    try:  # Intenta realizar el proceso a partir de una ruta especifica
        imagen = colorImage(ruta_imagen)  # se hace un llamado a la clase y se ingresa como parámetro la ruta
        imagen.displayProperties()  # se muestran las propiedades de la imagen
        imagen.makeGray()  # se muestra la imagen en escala de grises
        imagen.colorizeRGB('red')  # se muestra la imagen colorizada en rojo
        imagen.makeHue()  # se muestra la imagen en tonos
        cv2.waitKey(
            0)  # espera a que el usuario presione cualquier tecla (desplega todas las imagenes solicitadas)
        cv2.destroyAllWindows()
        cv2.waitKey(1)
    except:  # En caso de error se asume que la ruta especificada no es correcta
        print("La ruta no es correcta")
