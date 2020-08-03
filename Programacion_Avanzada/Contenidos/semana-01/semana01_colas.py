#FIFO

from _collections import deque

#deque genera "double ended queue" o deque

cola=deque()
print(cola)
aux=[1,2,3]
cola_2=deque(aux)
print(cola_2)

cola=deque()
cola.append(1)
cola.append(2)
cola.append(3)

print(cola)
elemento=cola.popleft() #pop desde primer elemento
print(elemento)
elemento_2=cola_2.pop() #pop desde ultimo elemento
print(elemento_2)
print(aux[0],aux[-1])

d=deque([1,2,3,4,5])
d2=deque([1,2,3,4,5])
print(d,d2)
d.rotate(2) #cambia 2 primeros por 2 ultimos (en mismo orden en el que estan
print(d,d2)
d.popleft(),d2.popleft()
print(d,d2)