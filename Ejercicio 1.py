# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 00:41:25 2018

@author: lox_j
"""

"""

PROGRAMA PARA CALCULAR MODA, MEDIANA Y MEDIA

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
    print ("Media: ", mediana, "\n")

    for i in datos:
        op = i - mediana
        restar.append(op)
     
        
def moda(l):  
     
                                                                                   
    repeticiones = 0                                                                         
    for i in l:                                                                              
        apariciones = l.count(i)                                                             
        if apariciones > repeticiones:                                                       
          repeticiones = apariciones                                                       
                                                                                         
        modas = []                                                                               
        for i in l:                                                                              
            apariciones = l.count(i)                                                             
            if apariciones == repeticiones and i not in modas:                                   
                modas.append(i)                                                                  
                                                                                         
    return print (l,"\n", "Moda:", modas)                                                
         




def main():

    listaDatos = [1525, 257, 378, 9543, 7854, 152]
    sumatoria(listaDatos)
    print ("\n")
    print (listaDatos)
    restar_media_datos(listaDatos)
    
    l = [ 9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]   
    moda(l)
    
    print("\n")
    l = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]                                                     
                                                                                         
    l.sort()  
    print (l)
    print("Mediana: ", 4)
    
    
   

if __name__ == '__main__': #Incio del programa
    main()


"""

#ESTA ES LA MEDIANA NO ME QUEDA. RESULTADO = 4

l = [9, 5, 9, 4, 3, 6, 7, 1, 2, 3, 9, 1, 2]                                                     
                                                                                         
print (l)                                                                                  
                                                                                                                                                                                                                                                                                                                                                                             
# mediana                                                                                
l.sort()                                                                                 
print (l)  
n=len(l)                                                                                
print (n)                                                                                      
if n % 2 == 0:                                                                      
                                                                         
    mediana = int ((l[n/2-1]+ l[n/2] )/2) 
                                                     
else:    
                                                                                   
    mediana = int (l[len(l)/2])  
                                                                
                                                                                         
print ('mediana:',mediana) 
"""