import os
import pandas as pd
import matplotlib.pyplot as plt

WIDTH = 0.2

class Precio:
  def __init__(self, cuarto=None, entero=None, medio=None, octavo=None):
    self.cuarto = cuarto
    self.entero = entero
    self.medio = medio
    self.octavo = octavo

  def __str__(self):
    return f"Precio:\n\tcuarto: {self.cuarto}\n\tentero: {self.entero}\n\tmedio: {self.medio}\n\toctavo: {self.octavo}"


class Tabla:
  def __init__(self):
    self.precio = Precio()
    self.tabla = []

  def __repr__(self):
    ret = ""
    ret += str(self.precio)
    ret += '\n'
    ret += str(self.tabla)
    return ret


tabla_actual = Tabla()
tablas = [tabla_actual]
#Aquí se debe poner el archivo que se está abriendo
with open("Sens_Inv_hold_cuarto_+0.0875.txt", "r") as file:
  salio_precio = True
  for i, line in enumerate(file.readlines()):
    line = line.strip()
    if not line or i == 0:
      # ignorar lineas vacias la primera
      continue

    # Aquí se debe poner la variable que se sensibilizó
    if line.startswith("hold [*] :="):
      salio_precio = True
      tabla_actual = Tabla()
      tablas.append(tabla_actual)
      continue
    if salio_precio and line.startswith(";"):
      salio_precio = False
      continue

    if salio_precio:
      precio = line.split()[1]
      if line.startswith('Cuarto'):
        tabla_actual.precio.cuarto = float(precio)
      elif line.startswith('Entero'):
        tabla_actual.precio.entero = float(precio)
      elif line.startswith('Medio'):
        tabla_actual.precio.medio = float(precio)
      elif line.startswith('Octavo'):
        tabla_actual.precio.octavo = float(precio)

    # Aquí se debe poner la variable que es el output (generalmente producción o inventario)
    else:
      if line.startswith("TInv [*,*] (tr)"):
        continue
      elif line.startswith(";"):
        continue
      elif line.startswith(":"):
        continue
      else:
        tabla_actual.tabla.append([float(val) for val in line.split()])


# pasar tablas a pandas
for tabla in tablas:
  tabla.tabla = pd.DataFrame(tabla.tabla, columns=['index', 'cuarto', 'entero', 'medio', 'octavo'])

# guardar imagenes
#Las imágenes se guardan en una carpeta llamada "figures", si esta ya existe, la sobreescribe
os.makedirs('figures', exist_ok=True)
for i in range(len(tablas)):
    print(f'guardando la imagen {i}')
    tabla = tablas[i]
    titulo = f"Hold: Cuarto: {round(tabla.precio.cuarto,4)}; Entero: {round(tabla.precio.entero,2)}; Medio: {round(tabla.precio.medio,2)}; Octavo: {round(tabla.precio.octavo,2)}"
    plt.title(titulo)
    plt.xlabel("Días")
    plt.ylabel("Inventario (un)")
    plt.bar(1+tabla.tabla.index-(WIDTH*3/2), tabla.tabla.entero, color='blue', width=WIDTH, align='center')
    plt.bar(1+tabla.tabla.index-(WIDTH*1/2), tabla.tabla.medio, color='red', width=WIDTH, align='center')
    plt.bar(1+tabla.tabla.index+(WIDTH*1/2), tabla.tabla.cuarto, color='green', width=WIDTH, align='center')
    plt.bar(1+tabla.tabla.index+(WIDTH*3/2), tabla.tabla.octavo, color='black', width=WIDTH, align='center')
    plt.gca().legend(("Entero", "Medio", "Cuarto", "Octavo"))
    plt.savefig(f'figures/fig_{i}.png')
    plt.clf()

