import numpy as np
from numpy import random

Vector = np.array([1, 2, 3])
Matriz = np.array([[1, 2],[3, 4]])
Seleccion = Matriz[0, 1]
Tamaño = Matriz.shape
MatrizCambio = np.array([[10, 20],[30, 40]])
MatrizCambio = MatrizCambio.reshape(1,4)
VectorDesordenado = np.array([5, 2, 8, 1, 4, 9])
VectorOrdenado = np.sort(VectorDesordenado)
Random = random.randint(10)
NuevoRandom = random.rand()
VectorAleatorio = random.randint(10, size=(15))
MatrizAleatoria = random.rand(5, 5)


print(Vector)
print(Matriz)
print(Seleccion)
print(Tamaño)
print(MatrizCambio)
print(VectorOrdenado)
print(Random)
print(NuevoRandom)
print(VectorAleatorio)
print(MatrizAleatoria)