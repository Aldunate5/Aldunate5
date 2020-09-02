#import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#todas las listas que se ocupan para almacenar datos
prod_entero = list()
prod_medio = list()
prod_cuarto = list()
prod_octavo = list()
inv_entero = list()
inv_medio = list()
inv_cuarto = list()
inv_octavo = list()
#la lista variable es el eje x que se graficará, lo dejé siemopre en entero, para que no se saliera del rango
variable = list()
funcionobj = list()

def Average(lst):
    return sum(lst) / len(lst)

#Creación de la clase de inventario
class Tinv:
  def __init__(self, cuarto=None, entero=None, medio=None, octavo=None):
    self.cuarto = cuarto
    self.entero = entero
    self.medio = medio
    self.octavo = octavo

#Este alfa depende de la variable que se está cambiando, puede ser beta, hold, etc.
  def __str__(self):
    return f"Alfa:\n\tcuarto: {self.cuarto}\n\tentero: {self.entero}\n\tmedio: {self.medio}\n\toctavo: {self.octavo}"

#La clase tabla es la que permite almacenar la información que se obtiene del txt.
#El nombre precio es la variable que se está cambiando, la primera vez lo hice con el precio y por eso quedó el nombre.
class Tabla_inv:
  def __init__(self):
    self.precio = Tinv()
    self.tabla_inv = []

  def __repr__(self):
    ret = ""
    ret += str(self.precio)
    ret += '\n'
    ret += str(self.tabla_inv)
    return ret

#Se repite lo mismo que antes, pero para la producción
class Prod:
  def __init__(self, cuarto=None, entero=None, medio=None, octavo=None):
    self.cuarto = cuarto
    self.entero = entero
    self.medio = medio
    self.octavo = octavo

  def __str__(self):
    return f"Alfa:\n\tcuarto: {self.cuarto}\n\tentero: {self.entero}\n\tmedio: {self.medio}\n\toctavo: {self.octavo}"


class Tabla_prod:
  def __init__(self):
    self.precio = Prod()
    self.tabla_prod = []

  def __repr__(self):
    ret = ""
    ret += str(self.precio)
    ret += '\n'
    ret += str(self.tabla_prod)
    return ret

#conjunto de tablas de la clase Tabla_inv o Tabla_prod
tablas_i = []
tablas_p = []

modo_lectura = 0    # modo lectura indica si estamos leyendo hold, inventario o produccion (0, 1, 2, 3, respectivamente)
contador_punto_coma = 0
with open("Sens_Final_por_ap.txt", "r") as file:
  for i, line in enumerate(file.readlines()):
    line = line.strip()

    if not line:
      # ignorar lineas vacias
      continue

    if line.startswith("FO"):
        salio_precio = False
        num = line.split()[2]
        funcionobj.append([float(num)])
        continue

    if line.startswith(';'):    # linea vacia
      contador_punto_coma += 1
      continue

    modo_lectura = (contador_punto_coma % 3)

    if line.startswith("hold"):
      # si sale hold crear nuevas tablas de prod e inventario
      salio_precio = True
      tabla_actual_i = Tabla_inv()
      tabla_actual_p = Tabla_prod()
      tablas_i.append(tabla_actual_i)
      tablas_p.append(tabla_actual_p)
      continue

    if line.startswith(':'):
      # ignorar lineas que parten con :
      continue

    if line[0].isnumeric():
      # si primer caracter es numerico--> dato de tabla
      if modo_lectura == 1:
        tabla_actual_i.tabla_inv.append([float(val) for val in line.split()])
      elif modo_lectura == 2:
        tabla_actual_p.tabla_prod.append([float(val) for val in line.split()])
      else:
        import pdb; pdb.set_trace()
    else:
      precio = line.split()[1]
      if line.startswith('Cuarto'):
        tabla_actual_i.precio.cuarto = float(precio)
        tabla_actual_p.precio.cuarto = float(precio)
      elif line.startswith('Entero'):
        tabla_actual_i.precio.entero = float(precio)
        tabla_actual_p.precio.entero = float(precio)
      elif line.startswith('Medio'):
        tabla_actual_i.precio.medio = float(precio)
        tabla_actual_p.precio.medio = float(precio)
      elif line.startswith('Octavo'):
        tabla_actual_i.precio.octavo = float(precio)
        tabla_actual_p.precio.octavo = float(precio)

# pasar tablas a pandas
for tabla in tablas_i:
  tabla.tabla_inv = pd.DataFrame(tabla.tabla_inv, columns=['index', 'cuarto', 'entero', 'medio', 'octavo'])
for tabla in tablas_p:
  tabla.tabla_prod = pd.DataFrame(tabla.tabla_prod, columns=['index', 'cuarto', 'entero', 'medio', 'octavo'])

#Aquí se calculan los promedios
medios_i = []
for tabla_i in tablas_i:
    medios = tabla_i.tabla_inv.mean()
    medios_i.append(medios)
medias_inv = list(zip(*medios_i))     # ['index', 'cuarto', 'entero', 'medio', 'octavo']

medios_p = []
for tabla_p in tablas_p:
    medios = tabla_p.tabla_prod.mean()
    medios_p.append(medios)
medias_prod = list(zip(*medios_p))

#Esto permite crear el eje y a la misma escala para los dos gráficos
ylim = max(max(medias_prod[1]), max(medias_prod[2]), max(medias_prod[3]), max(medias_prod[4]), max(medias_inv[1]), max(medias_inv[2]), max(medias_inv[3]), max(medias_inv[4]))
ylim = ylim*1.03

#Tuve que hacer esto para crear la variable que se está sensibilizando. Son los mismos números que en el AMPL.
array = np.arange(0, 0.8, 0.0016)
for i in array:
  variable.append(i)
variable.append(0.8016)
print(len(variable))

#Finalmente, graficar
plt.clf()
grid = plt.GridSpec(1, 3)
ax1 = plt.subplot(grid[0,0])
ax1.plot(variable, medias_inv[2], color = "blue") #Entero
ax1.plot(variable, medias_inv[3], color = "red") #Medio
ax1.plot(variable, medias_inv[1], color = "green") #Cuarto
ax1.plot(variable, medias_inv[4], color = "black") #Octavo
ax1.set_title("Promedio Inventario Mensual")
ax1.set_ylim([0, ylim])
ax1.set_ylabel("Unidades")
plt.gca().legend(("Entero", "Medio", "Cuarto", "Octavo"))
ax2 = plt.subplot(grid[0,1])
ax2.plot(variable, medias_prod[2], color = "blue")
ax2.plot(variable, medias_prod[3], color = "red")
ax2.plot(variable, medias_prod[1], color = "green")
ax2.plot(variable, medias_prod[4], color = "black")
ax2.set_title("Promedio Producción Mensual")
ax2.set_ylim([0, ylim])
ax2.set_xlabel("Porcentaje Aprendizaje (por_ap)")
ax3 = plt.subplot(grid[0,2])
ax3.plot(variable, funcionobj, color = "blue", )
ax3.set_title("Función Objetivo vs Porcentaje Aprendizaje (por_ap)")
ax3.set_ylabel("Valor FO")
ax3.yaxis.set_label_position("right")
ax3.yaxis.tick_right()
plt.show()
