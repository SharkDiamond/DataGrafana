
import mysql.connector



crea6=["insert into cantidadPorDia (fecha,cantidad) select SUBSTRING(now(), 1,10) as Fecha,(select count(*) from calls where Date(dateCall)=SUBSTRING(SUBDATE(now(),INTERVAL 5 HOUR), 1,10) and not NumberEnter like 'Ext.%' and not length(callTransfer)=1)+(select count(*) from calls where  not NumberEnter like 'Ext.%' and Date(dateCall)=SUBSTRING(SUBDATE(now(),INTERVAL 5 HOUR), 1,10) and length(callTransfer)=1)+(select count(*) from calls where  NumberEnter like 'Ext.%' and Date(dateCall)=SUBSTRING(SUBDATE(now(),INTERVAL 5 HOUR), 1,10) and NOT length(callTransfer)=1) as Cantidad","insert into LLamadasAtendidasDepartamentos values ('Atencion Al Cliente',SUBSTRING(now(), 1,10),CantidadLLamadasEntrantesAtc())","select InsertarCantidadLLamadasDepartamento('Tier 1','Tier1')","select InsertarCantidadLLamadasDepartamento('Tier 2','Ext.8012')","select InsertarCantidadLLamadasDepartamento('BILLING','BILLING')"]


test="select InsertarCantidadLLamadas()"

x=range(len(crea6))

for n in x:

 mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    port="3306",
    password="",
    database="test3cx"
    )

 mycursor=mydb.cursor(buffered=True)


 mycursor.execute(crea6[n])

 mycursor.close()

 mydb.commit()

 mydb.close()
