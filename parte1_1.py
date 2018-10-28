# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:19:00 2018

@author: azaa0
"""

from pylab import *
import numpy as np
import scipy.io
import matplotlib.pyplot as plt
iris = scipy.io.loadmat('iris.mat')

caracteristicas = iris['meas']
especies = iris['species']
print("==============================PARTE 1.1===================================")
plot(0.1*randn(50,1),caracteristicas[0:50,0],'bo')
plot(1+0.1*randn(50,1),caracteristicas[50:100,0],'ro')
plot(2+0.1*randn(50,1),caracteristicas[100:151,0],'go')
ylabel("Longitud del Pétalo (cm)")
show()
plot(0.1*randn(50,1),caracteristicas[0:50,1],'bo')
plot(1+0.1*randn(50,1),caracteristicas[50:100,1],'ro')
plot(2+0.1*randn(50,1),caracteristicas[100:151,1],'go')
ylabel("Anchura del Pétalo (cm)")
show()
plot(0.1*randn(50,1),caracteristicas[0:50,2],'bo')
plot(1+0.1*randn(50,1),caracteristicas[50:100,2],'ro')
plot(2+0.1*randn(50,1),caracteristicas[100:151,2],'go')
ylabel("Longitud del Sépalo (cm)")
show()
plot(0.1*randn(50,1),caracteristicas[0:50,3],'bo')
plot(1+0.1*randn(50,1),caracteristicas[50:100,3],'ro')
plot(2+0.1*randn(50,1),caracteristicas[100:151,3],'go')
ylabel("Anchura del Sépalo (cm)")
show()
plot(caracteristicas[1:50,0],caracteristicas[1:50,1],'bo')
plot(caracteristicas[51:100,0],caracteristicas[51:100,1],'ro')
plot(caracteristicas[101:150,0],caracteristicas[101:150,1],'go')
xlabel("Longitud del Pétalo (cm)")
ylabel("Anchura del Pétalo (cm)")
show()
print("==============================PARTE 1.2===================================")
# graficamos las dos características que más sirven para diferenciar las especies de flores.
scatter(caracteristicas[0:50,1],caracteristicas[0:50,2], color="b")
scatter(caracteristicas[50:100,1],caracteristicas[50:100,2], color="r")
scatter(caracteristicas[100:151,1],caracteristicas[100:151,2], color="g")
xlabel("Longitud del Pétalo (cm)")
ylabel("Anchura del Pétalo (cm)")
# generamos una variable con las dos características que nos interesan
x = [caracteristicas[0:151,1], caracteristicas[0:151,2]]

# obtenemos las características globales promedio
x_prom = mean(x,1)

# extraemos las caracteristicas globales promedio de nuestros datos
#x = x - x_prom*np.ones(150,2)
print(x)
# graficamos nuevamente
plot(x[0:50,0],x[0:50,1], color="b")
plot(x[50:100,0],x[50:100,1], color="r")
plot(x[100:151,0],x[100:151,1], color="g")
xlabel("Longitud del Pétalo (cm)")
ylabel("Anchura del Pétalo (cm)")
grid("on")
show()
# graficamos los datos nuevamente
scatter(x[0:50,1],x[0:50,2],alpha=0.25, color="b")
scatter(x[50:100,1],x[50:100,2],alpha=0.25, color="r")
scatter(x[100:151,1],x[100:151,2],alpha=0.25, color="g")
xlabel("Longitud del Pétalo (cm)")
ylabel("Anchura del Pétalo (cm)")
grid("on")

# obtenemos los vectores con las características promedio para cada una de las clases de flores
prom_1 = mean(x[0:50,0:151],1)
prom_2 = mean(x[50:100,0:151],1)
prom_3 = mean(x[100:151,0:151],1)

# graficamos los vectores
quiver(prom_1[1,1],prom_1[1,2],angles="xy", scale_units="xy", scale=1, color="b")
quiver(prom_2[1,1],prom_2[1,2],angles="xy", scale_units="xy", scale=1, color="r")
quiver(prom_3[1,1],prom_3[1,2],angles="xy", scale_units="xy", scale=1, color="g")
# escogemos aleatoriamente una ilera en los datos
ilera_al = rand(151,0)

# extraemos los datos de esta ilera en una variable nueva
x_muestra = x[ilera_al,0:151]

# calculamos el producto interno de esta muestra con cada uno de los vectores promedio
prod_1 = x_muestra*prom_1
prod_2 = x_muestra*prom_2
prod_3 = x_muestra*prom_3

# imprimimos los resultados
print("el producto interno del vector muestra con de los vectores promedio correspondientes a las especies de plantas son: \n")
print("\n setosa ", prod_1)
print("\n versicolor ", prod_2)
print("\n virginica ", prod_3)
print("\n\ny la especie correcta del vector muestra es: \n")
print("\n ", especies[ilera_al])