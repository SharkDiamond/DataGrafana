import mysql.connector



Trabajadores=["Jose Rondon","Moises Rondon","Luis Vela","Daniel Mogollon","Ander Uribe","Alejandra Giraldo","Jim Lozano","Gabriel Arispe","Juan Andres","Sergio Sanchez","Greider Trejo","Luigi Panella"]



x=range(len(Trabajadores))

#ELIMINAR 59 REGISTROS
for i in x:

 mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    port="3306",
    password="",
    database="test3cx"
    )

 mycursor=mydb.cursor(buffered=True)

 sql="delete FROM Trabajadores where Fecha='2021-08-14' and Trabajador='"+Trabajadores[i]+"'  limit 59;"

 mycursor.execute(sql)

 mycursor.close()

 mydb.commit()

 mydb.close()
