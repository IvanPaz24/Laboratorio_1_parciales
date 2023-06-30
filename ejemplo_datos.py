import sqlite3

id = 3 
sueldo = 100

with sqlite3.connect("path") as conexion:
    try:
        #create table
        # sentencia = '''
        #             create table Empleados
        #             (
        #                 id integer primary key autoincrement,
        #                 nombre text,
        #                 apellido text,
        #                 sueldo real
        #             )
        #             '''
        # sentencia = '''
        # alter table Empleados
        # add direccion text
        # '''
        ### insertar contenido
        # nombre = "Martin"
        # apellido = "Gomez"
        # sueldo = 30247
        # direccion = "Av siempreviva 123"
        # sentencia = '''
        # insert into Empleados(nombre, apellido, sueldo, direccion) values(?,?,?,?)
        # '''
        # # conexion.execute(sentencia)
        # conexion.execute(sentencia,(nombre,apellido,sueldo,direccion))
        # print("Tabl creada con exito")
        # sentencia = 'insert into Empleados(sueldo, apellido, nombre,direccion) values(2500000,"ruiz","ana","cochabamba 333")'
        # conexion.execute(sentencia)
        # conexion.commit()
        # sentencia = 'sentencia * from Empleados order by sueldo desc limit 3'
        # cursor = conexion.execute(sentencia)

        # for fila in cursor:
        #     print(fila)
        # sentencia = 'update Empleados set sueldo = 500 where id = ?' 
        # cursor = conexion.execute(sentencia, (sueldo, id))#aunque sea uno solo tengo que poner coma
        sentencia = 'delete Empleados where sueldo < 1000' #siempre usar el where sino borra todo
        cursor = conexion.execute(sentencia)

        print("Dato insertado con exito")
    except:
        print("Error")

######################################
'''
Insert into tabla([lista_campos]) values(lista_valore)

Selec nombre , apellido /o suma(sueldos)/ *(todos los datos)
FROM Empleados
/opcional /WHERE sueldo > 500 
order by asc(ascendente)|desc(desendente)
limit 2 (los dos primeros)

####Update
'update Tabla set campo = valor [where condicion]'

####Delete
DELETE FROM tabla WHERE condicion

'''    
