#tipo LIFO
#stack funciona como lista

stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop()
print(stack) #se elimina el ultimo en agregarse
tope=stack[-1] #peek permite ver ultimo elemento en agregarse, sin eliminarlo
print(tope)
 #ejemplos en direcciones url (boton de volver)

 class Texto()
     def __init__(self,original):
         self.pila=[]
         self.original=original

     def invertir_linea(self):
         print('Entrada:')
         for linea in self.original.split('\n'):
             print(linea)
             self.pila.append(linea)
         print()
         print('Salida:')
         while len(self.pila)>0:
             print(self.pila.pop())
