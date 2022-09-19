from importlib.resources import path
from posixpath import normpath
import random 
import os

def uno():
    col1 = []
    col2 = []
    col3 = []

    ingrese = int(input("Ingrese la cantidad de lineas: "))
    for i in range(ingrese):
        col1.append(random.randint(0,500))
        col2.append(random.randint(0,500))
        col3.append(random.randint(0,500))
    name = input("Ingrese el nombre del archivo: ")
    doc = open(name,'w')
    for j in range(ingrese):
        doc.write('{}, {}, {}\n'.format(col1[j],col2[j],col3[j]))
    doc.close()


def recorre():
    f = open(r'Registros.txt', 'r')
    for line in f:
        line = line.split(', ')
        print(line[0])
        print(line[1])
        print(line[2])

def obtenerRuta():
    #nombre = 'base.html'
    ruta = os.getcwd()
    returnruta

obtenerRuta()