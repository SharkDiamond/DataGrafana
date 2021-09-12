import mysql.connector


Trabajadores=["Jose Rondon","Moises Rondon","Luis Vela","Daniel Mogollon","Ander Uribe","Alejandra Giraldo","Jim Lozano","Gabriel Arispe","Juan Andres","Sergio Sanchez","Greider Trejo","Luigi Panella","Iliandris Oviedo","Milagros Garrido","Hemily Rodriguez","Jose Vergara","Andreina Ortegano","Allix Taborda","Rebeca Belisario","Marili Morales","Janna Vizcaya","Isimar Castillo","Lourdes Calderon","Jessenia Tirado","Cynthia Soto","Silvia Bonilla","Rossini Linares","Iriana Bejarano","Nataly Torres","Hector Castillo","Mariana Gallardo","Deimar Garrido"]

Extensiones=["Ext.1547","Ext.1514","Ext.1545","Ext.1558","Ext.1588","Ext.1578","Ext.1592","Ext.1519","Ext.1548","Ext.1542","Ext.1543","Ext.1544","Ext.1596","Ext.1553","Ext.1579","Ext.1590","Ext.1576","Ext.1577","Ext.1555","Ext.1567","Ext.1554","Ext.1539","Ext.1501","Ext.1518","Ext.1523","Ext.1594","Ext.1583","Ext.1550","Ext.1598","Ext.1551","Ext.1574","Ext.1536"]



x=range(len(Trabajadores))

for n in x:

 mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    port="3306",
    password="",
    database="test3cx"
    )

 mycursor=mydb.cursor(buffered=True)
 
 sql="select InsertarCantidadesTrabajadores('"+Extensiones[n]+"','"+Trabajadores[n]+"');"
 
 mycursor.execute(sql)
 
 mycursor.close()
 
 mydb.commit()

 mydb.close()

#ELIMINAR 59 REGISTROS
#for i in x:

# mydb = mysql.connector.connect(
#    host="localhost",
#    user="test",
#    port="3306",
#    password="",
#    database="test3cx"
#    )

# mycursor=mydb.cursor(buffered=True)

# sql="delete FROM Trabajadores where Fecha=SUBSTRING(now(), 1,10) and Trabajador=+Trabajadores[i]+  limit 59;"

# mycursor.execute(sql)

# mycursor.close()

# mydb.commit()

# mydb.close()
