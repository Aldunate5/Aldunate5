import pandas as pd
import csv
from itertools import zip_longest

import matplotlib.pyplot as plt
data = pd.read_csv('base.txt',sep='\t',header=None)
x1=data[0].tolist()
x1=[element*100 for element in x1]
y1=data[1].tolist()



data2=pd.read_csv('data.txt',sep='\t',header=None)
x2=data2[0].tolist()
x2=[element*100 for element in x2]
y2=data2[1].tolist()



plt.plot(x1,y1,label='Ingenieria')
plt.plot(x2,y2,label='Real')

plt.axis([0,10,0,1000]) #genera largo de ejes
plt.title('Curvas Niquel Inconel 718') #se genera titulo y se hace un label
plt.xlabel("Deformacion (%)");plt.ylabel("Tension (MPa)") #se generan ejes y se hace un label
plt.legend(loc="center left",bbox_to_anchor=(1,0.5)) #se genera un key de manera de identificar cada simulacion segun color
plt.tight_layout() #se ajusta legend al ancho de la pantalla
plt.show()

'''
d = [x, y]
export_data = zip_longest(*d, fillvalue = '')
with open('base.csv', 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("List1", "List2"))
      wr.writerows(export_data)
myfile.close()
'''