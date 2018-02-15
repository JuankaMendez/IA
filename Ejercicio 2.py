# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 00:54:05 2018

@author: lox_j
"""

"""

PROGRAMA PARA CALCULAR LA DESCIACION ESTANDAR Y VARIANZA

"""

from math import pow, sqrt

restar = list()
elevar = list()



def sumatoria(datos):
        sumatoria = float(sum(datos))
        return sumatoria

def media(datos):
    n = len(datos)
    mediana = sumatoria(datos) / n
    return round(mediana,2)


def restar_media_datos(datos):

    mediana = media(datos)

    for i in datos:
        op = i - mediana
        restar.append(op)

def elevar_cuadrado(datos):

    for i in datos:
        op = pow (i, 2)
        elevar.append(op)



def raiz_datos():
    desviacion = sqrt(media(elevar))
    return round(desviacion,2)

def main():
    #datos
    listaDatos = [13, 14, 15, 15, 15, 16, 17, 18, 20]

 
    restar_media_datos(listaDatos)

    elevar_cuadrado(restar)

    Varianza = media(elevar)
    print ("\n")
    print ('Varianza: ', Varianza, "\n")

    desviacion = raiz_datos()
    print ('Desviación Estándar: ', desviacion)
    print ("\n")

if __name__ == "__main__": #Incio
    main()
