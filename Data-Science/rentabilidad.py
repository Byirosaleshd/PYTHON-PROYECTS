import sqlite3
import pandas as pd
#no me importa el matplotlib hacia el codigo
#import matplotlib.pyplot as plt

#Obtiendo los 10 productos mas rentables
conn = sqlite3.connect("Northwind.db")
query = '''
    SELECT ProductName, SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    JOIN Products p ON p.Product.ID = od.ProductID
    GROUP BY od.ProductID
    ORDER BY Revenue DESC
    LIMIT 10
'''

#top_products = pd.read_sql_query(query,conn)

#top_products.plot(x="ProductName",y="Revenue",kind="bar",figsize=(10,5),legend=False)

#plt.title("10 Productos mas rentables")

#plt.xlab("Productos")
#plt.ylabel("Revenue")
#Plt.xticks(rotation=90)
#plt.show()

#Obteniendo los 10 empleados mas efectivos

#query2 = '''
#    SELECT FirstName || "" || LastName as Employee, COUNT(*)
#    FROM Orders o
#    JOIN Employees e
#    ON e.EmployeeID = o.EmployeeID
#    GROUP BY o.EmployeeID
#    ORDER BY Total DESC
#    LIMIT 10
#'''

#top_employees = pd.read_sql_query(query2,conn)

#top_products.plot(x="Employee",y="Total",kind="bar",figsize=(10,5),legend=False)

#plt.title("10 Empleados mas efectivos")

#plt.xlab("Empleados")
#plt.ylabel("Total vendido")
#Plt.xticks(rotation=45)
#plt.show()