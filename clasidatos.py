# -*- coding: utf-8 -*-
"""
Created on Sun Apr 1 15:23:50 2018

@author: lox_j
"""

# Ejercicios de julia en pyhton 
"""
rabaja con la persona junto a tí y grafiquen las cuatro características 
en cuatro figuras distintas. Determinen cuales son las dos características 
que mejor sirven para diferenciar las tres especies de flores.
"""


scatter(0.1*randn(50,1),caracteristicas[1:50,1])
scatter(1+0.1*randn(50,1),caracteristicas[51:100,1])
scatter(2+0.1*randn(50,1),caracteristicas[101:150,1])
ylabel("Longitud del Pétalos (cm)")
xlabel("Ancho de los petalos")

# graficamos la anchura del pétalo
figure(2)

# graficamos la longitud del sépalo
figure(3)

# graficamos la anchura del sépalo
figure(4)