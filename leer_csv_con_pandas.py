import pandas as pd


#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("datos.csv")
df2 = pd.read_csv("datos.csv")

#obteniendo los datos de la columna nombre
nombres = df["nombre"]

print(df)

cadena = "0123456789"
print(cadena[2:4])

#ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("edad")

print(df_orden_ascendente)

#ordenando de forma descendente

df_orden_descendente= df.sort_values("edad",ascending=False)

print(df_orden_descendente)

#concatenando los 2 dataframes
df_concantenado = pd.concat([df,df2])

print(df_concantenado)

#accediendo a la primeras 3 filas con head()
primer_fila = df.head(3)

print(primer_fila)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

print(ultimas_filas)

#accediendo a la cantidad de filas y columnas con shape

filas_totales,columnas_totales = df.shape

print(filas_totales,columnas_totales)

#obteniendo data estadistica del dataframe:
df_info = df.describe()

print(df_info)

#accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

print(elemento_especifico_loc)

#accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2,2]

print(elemento_especifico_iloc)

#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]

print(apellidos)

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

print(fila_3)

#accediendo a la fila 3 con iloc
fila_3_1 = df.iloc[2,:]

print(fila_3_1)

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]!=30,:]

print(mayor_que_30)  