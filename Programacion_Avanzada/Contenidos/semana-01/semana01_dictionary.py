# se le asocia un valor a un key (mutables)
monedas={"Chile":"Peso","Peru":"Soles","Espana":"Euro","Holanda":"Euro","Brasil":"Real"}
print(monedas["Chile"])

print(monedas.get("Chile","No tiene moneda"))
print(monedas.get("Argentina","No tiene moneda")) #asocia un valor en caso de no encontrarse

monedas["Vaticano"]="Lira" #mutables
monedas[3.14]=("Peso","Dolar") #se agrega tipo distinto de dato
print(monedas)
del monedas[3.14]
print(monedas)

print(monedas.keys())
print(monedas.values())
print(monedas.items())

for m in monedas: #se recorren keys por defecto
    print(f'{m}')
for m,v in monedas.items(): #se tienen dos listas para keys y para values
    print(f'Se tiene que en {m} se utilizan {v}')

from string import ascii_lowercase as letras

#dict por comprension: a una ecuacion general se le aplica un iterable (rango)
numero_por_letra = {letras[i].upper():i+1 for i in range(len(letras))}
print(numero_por_letra)

numero_por_vocal={letras[i].upper():i+1 for i in range(len(letras)) if letras[i].upper() in "AEIOU"}
print(numero_por_vocal)

#defaultdicts: valor predeterminado para keys
from collections import defaultdict
msg='spercalifragilisticoespialidoso'
vocales=defaultdict(int)

for letra in msg:
    if letra not in "aeiou":
        continue
    vocales[letra]+=1
print(vocales)

from random import random

def function_default():
    return random

diccionario = defaultdict(function_default())
print(diccionario)
diccionario["A"]
print(diccionario)
diccionario["B"]
print(diccionario)

#HASH: asocia a cada key un valor. Notodo elemento puedo ser un key: ERROR

hello_1="Hello world"
hello_2="Hello world"
print(f'Hash de 1:{hash(hello_1)}')
print(f'Hash de 2:{hash(hello_2)}')
print(f'{hello_1==hello_2}')
print(f'{hello_2 is hello_1}')