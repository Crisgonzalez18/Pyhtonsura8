from cgitb import html, text
from distutils import text_file
import pandas as pd

#CARGA LOS DATOS
dataFrame= pd.read_csv('./empleados.csv')
#print(dataFrame)

#CARGAR TODOS LOS DATOS
#print(dataFrame.to_string())

#CARGAR LOS PRIMEROS N REGISTROS DE UN BANCO DE DATOS
#print(dataFrame.head(20))

#CARGAR LOS ULTIMOS N REGISTROS DE UN BANCO DE DATOS
#print(dataFrame.tail(50))

#OBTENER INFORMACION DE LOS DATOS CARGADOS
#print(dataFrame.info())
#print(dataFrame.describe())

#ACCEDER A DATOS O REGISTROS ESPECIFICOS 
#print(dataFrame["nombres"].head())
#print(dataFrame["salario"].tail(20))

#ACCEDER A REGISTROS POR SU INDICE
#print(dataFrame.iloc[20:30]) rango
#print(dataFrame.loc[[10,20,30,40]]) serie o lista de registros

'''tabla=(dataFrame.loc[[1,5,10],['nombres']])

html= tabla.to_html()
text_file= open("index.html","w")
text_file.write(html)
text_file.close '''

#FILTROS CON CONDICIONES LOGICAS
#print(dataFrame[dataFrame['salario']>5500000].head(10))
print(dataFrame[(dataFrame['salario']>5500000)&(dataFrame['cargo']=="analista2")])