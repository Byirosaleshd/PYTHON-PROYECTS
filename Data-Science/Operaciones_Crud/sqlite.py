import sqlite3
from estudiantes import Estudiante
conn = sqlite3.connect('universidad.db')
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS estudiantes (
    matricula TEXT PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    promedio REAL)""")

#c.execute("INSERT INTO estudiantes VALUES('111','Roberto','Cruz',9.5)")
#conn.commit()

est_1 = Estudiante('222','Adriana','Cruz',9.5)
est_2 = Estudiante('333','Fabian','Romero',9.0)
est_3 = Estudiante('444','Alejandro','Cruz',7.5)
est_4 = Estudiante('555','Karen','Barrera',7.5)

#c.execute("INSERT INTO estudiantes VALUES(?,?,?,?)", 
#    (est_1.matricula, est_1.nombre, est_1.apellido, est_1.promedio))

#c.execute("INSERT INTO estudiantes VALUES(:matricula, :nombre, :apellido, :promedio)", {
#   'matricula': est_2.matricula, 'nombre': est_2.nombre, 'apellido': est_2.apellido,
#  'promedio': est_2.promedio})

#conn.commit()

#c.execute("SELECT * FROM estudiantes")
#estudiantes = c.fetchone()
#print(estudiantes)






conn.close()    