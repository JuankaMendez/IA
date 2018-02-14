# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 00:41:25 2018

@author: lox_j
"""

"""

PROGRAMA PARA CALCULAR MODA, MEDIANA Y MEDIA

"""
# calcular de mediana
# calcular de la media aritmetica
# calcular la moda

print ("Datos a tratar: ")
data=[1525, 257, 378, 9543, 7854, 1527]

print (data)
dOrder=sorted(data)

n=len(dOrder)
middle=n/2

# codigo para calcular la mediana
if n%2==0:
	mediana=(dOrder[middle+1] + dOrder[middle+2]) / 2
else:
	mediana=dOrder[middle+1]*1

print ("Total datos"), n
print ("Mediana: "), mediana


# codigo para calcular la media aritmetica
print 'Mediana Aritmetica: ', round(sum(data)*1.0/n,2)

# codigo para calcular la moda
repetir = 0                                                                         
for i in data:                                                                              
    aparece = data.count(i)                                                             
    if aparece > repetir:                                                       
        repetir = aparece                                                       
                                                                                         
moda = []                                                                               
for i in data:                                                                              
    aparece = data.count(i)                                                             
    if aparece == repetir and i not in moda:                                   
        moda.append(i)                                                                  
                                                                                         
print "moda:", moda

