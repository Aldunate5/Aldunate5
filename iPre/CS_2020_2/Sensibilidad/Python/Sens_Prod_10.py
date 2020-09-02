import os
import pandas as pd
import matplotlib.pyplot as plt

WIDTH = 0.2

class Apren:
  def __init__(self, p1=None, p10=None, p2=None, p3=None, p4=None, p5=None, p6=None, p7=None, p8=None, p9=None):
    self.p1 = p1
    self.p10 = p10
    self.p2 = p2
    self.p3 = p3
    self.p4 = p4
    self.p5 = p5
    self.p6 = p6
    self.p7 = p7
    self.p8 = p8
    self.p9 = p9
    self.p10 = p10

  def __str__(self):
    return f"Apren:\n\tp1: {self.p1}\n\tp10: {self.p10}\n\tp2: {self.p2}\n\tp3: {self.p3}\n\tp4: {self.p4}\n\tp5: {self.p5}\n\tp6: {self.p6}\n\tp7: {self.p7}\n\t8: {self.p8}\n\tp9: {self.p9}"


class Tabla:
  def __init__(self):
    self.apren = Apren()
    self.tabla = []

  def __repr__(self):
    ret = ""
    ret += str(self.apren)
    ret += '\n'
    ret += str(self.tabla)
    return ret


tabla_actual = Tabla()
tablas = [tabla_actual]
#Aquí se debe poner el archivo que se está abriendo
with open("Sens_apren.txt", "r") as file:
  salio_apren = True
  for i, line in enumerate(file.readlines()):
    line = line.strip()
    if not line or i == 0:
      # ignorar lineas vacias la primera
      continue

#Aquí se debe poner la variable que se sensibilizó
    if line.startswith("apren"):
      salio_apren = True
      tabla_actual = Tabla()
      tablas.append(tabla_actual)
      continue
    if salio_apren and line.startswith(";"):
      salio_apren = False
      continue

    if salio_apren:
      apren = line.split()[1]
      if line.startswith('p10'):
        tabla_actual.apren.p10 = float(apren)
      elif line.startswith('p1'):
        tabla_actual.apren.p1 = float(apren)
      elif line.startswith('p2'):
        tabla_actual.apren.p2 = float(apren)
      elif line.startswith('p3'):
        tabla_actual.apren.p3 = float(apren)
      elif line.startswith('p4'):
        tabla_actual.apren.p4 = float(apren)
      elif line.startswith('p5'):
        tabla_actual.apren.p5 = float(apren)
      elif line.startswith('p6'):
        tabla_actual.apren.p6 = float(apren)
      elif line.startswith('p7'):
        tabla_actual.apren.p7 = float(apren)
      elif line.startswith('p8'):
        tabla_actual.apren.p8 = float(apren)
      elif line.startswith('p9'):
        tabla_actual.apren.p9 = float(apren)

#Aquí se debe poner la variable que es el output (generalmente producción o inventario)
    else:
      if line.startswith("P [*,*] (tr)"):
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
    if tabla.apren.p1 == tabla.apren.p2 and tabla.apren.p1 == tabla.apren.p3 and tabla.apren.p1 == tabla.apren.p4 and tabla.apren.p1 == tabla.apren.p5 and tabla.apren.p1 == tabla.apren.p6 and tabla.apren.p1 == tabla.apren.p7 and tabla.apren.p1 == tabla.apren.p8 and tabla.apren.p1 == tabla.apren.p9 and tabla.apren.p1 == tabla.apren.p10:
      titulo = f"Aprendizaje: p_i: {tabla.apren.p1}"
    else:
      titulo = f"Aprendizaje: p1: {tabla.apren.p1}; p2: {tabla.apren.p2}; p3: {tabla.apren.p3};\np4: {tabla.apren.p4}; p5: {tabla.apren.p5}; p6: {tabla.apren.p6}; p7: {tabla.apren.p7};\np8: {tabla.apren.p8}; p9: {tabla.apren.p9}; p10: {tabla.apren.p10}"
    plt.title(titulo)
    plt.bar(1+tabla.tabla.index-(WIDTH*3/2), tabla.tabla.entero, color='blue', width=WIDTH, align='center')
    plt.bar(1+tabla.tabla.index-(WIDTH*1/2), tabla.tabla.medio, color='red', width=WIDTH, align='center')
    plt.bar(1+tabla.tabla.index+(WIDTH*1/2), tabla.tabla.cuarto, color='green', width=WIDTH, align='center')
    plt.bar(1+tabla.tabla.index+(WIDTH*3/2), tabla.tabla.octavo, color='brown', width=WIDTH, align='center')
    plt.gca().legend(("Entero", "Medio", "Cuarto", "Octavo"))
    plt.savefig(f'figures/fig_{i}.png')
    plt.clf()

