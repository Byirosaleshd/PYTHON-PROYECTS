import csv

with open("datos.csv") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)