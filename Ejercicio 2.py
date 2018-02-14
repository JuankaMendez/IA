# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 00:54:05 2018

@author: lox_j
"""

"""

PROGRAMA PARA CALCULAR LA DESCIACION ESTANDAR Y VARIANZA

"""

# ************************* Varianza y Desviación Estándar *************************

# -*- coding: utf-8 -*-

from math import pow, sqrt

listaDatos = list()
restar = list()
elevar = list()

def imprimir(texto, valor):
    print('\n{} {}'.format(texto, valor))

# ************************* Paso 1 y Paso 5 *************************
defsumatoria(datos):
        sumatoria = float(sum(datos))
        return sumatoria
# ************************* Paso 2 *************************
defmedia(datos):
    n = len(datos)
    mediana = sumatoria(datos) / n
    return round(mediana,2)
# ************************* Paso 3 *************************
defrestar_media_datos(datos):

    mediana = media(datos)
    imprimir ('Media: ', mediana)

    for i in datos:
        op = i - mediana
        restar.append(op)

# ************************* Paso 4 *************************
defelevar_cuadrado(datos):

    for i in datos:
        op = pow (i, 2)
        elevar.append(op)

# ************************* Paso 6 *************************

defraiz_datos():
    desviacion = sqrt(media(elevar))
    return round(desviacion,2)

# ************************* Inicio *************************
defmain():

    repetir = int(raw_input('Cuantos valores quieres ingresar? : '))

    for i in range(repetir):
            number = int(raw_input('Escribe el dato: '))
            listaDatos.append(number) # agregar el valor a la lista de datos

    suma = sumatoria(listaDatos)
    imprimir ('Sumatoria: ', suma)

    restar_media_datos(listaDatos)

    elevar_cuadrado(restar)

    mediana = media(elevar)
    imprimir ('Varianza: ', mediana)

    desviacion = raiz_datos()
    imprimir ('Desviación Estándar: ', desviacion)
    print ('\n')

if __name__ == '__main__': #Incio
    main()
