######## modularizacion #######
import ejemplo
#from ejemplo import mi_variable, MiClase, saludar

print(ejemplo.__name__) #utiliza nombre del modulo original; si es original es __main__
ejemplo.mi_variable
ejemplo.saludar()
instancia=ejemplo.MiClase("42")
print(instancia.argumento)

#mi_variable
#saludar()
#instancia=MiClase("23")
#print(instancia.argumento)

