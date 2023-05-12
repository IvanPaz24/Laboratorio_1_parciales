import re
import datetime
import json

def split_de_raza(diccionario:dict, key:str)->dict:
    '''
    Brief: realiza un split de los strings de un diccionario 
    Parameters:
        diccionario:dict -> diccionario que se va a recorrer
        key:str -> clave del valor dentro del diccionario
    return: retorna el diccionario con su clave normalizado 
    '''
    if type(diccionario) == dict and type(key) == str:
        if diccionario[key] == "Shin-jin" or diccionario[key]== "Three-Eyed People":
            diccionario[key] = [diccionario[key]]
        else:
            diccionario[key] = re.split("-", diccionario[key])

    return diccionario[key]

def strip_clave(diccionario:dict, key:str)->dict:
    '''
    Brief: elimina los espacios que existen en los valores dentro de la lista 
    Parameters:
        diccionario:dict -> diccionario que se va a recorrer
        key:str -> clave del valor dentro del diccionario
    return: retorna el diccionario con su clave normalizado 
    '''
    if type(diccionario) == dict and type(key) == str:
        for i in range(len(diccionario[key])):
            diccionario[key][i] = diccionario[key][i].strip()
    
    return diccionario[key]

def parser_csv(path:str)->list:
    '''
    Brief: realiza un split de los strings de un diccionario 
    Parameters:
        diccionario:dict -> diccionario que se va a recorrer
        key:str -> clave del valor dentro del diccionario
    return: retorna el diccionario normalizado 
    '''
    if type(path) == str:
        flag = False
        lista = []
        with open(path, "r", encoding="utf-8") as archivo:
            for line in archivo:
                lectura = re.split(",|\n", line)
                personaje = {}
                personaje["id"] = lectura[0]
                personaje["nombre"] = lectura[1]
                personaje["raza"] = lectura[2]
                personaje["raza"] = split_de_raza(personaje, "raza")
                personaje["poder_de_pelea"] = lectura[3]
                personaje["poder_de_ataque"] = lectura[4]
                personaje["habilidades"] = lectura[5]
                personaje["habilidades"] = re.split("\|\$\%", personaje["habilidades"])
                personaje["habilidades"] = strip_clave(personaje,"habilidades")
                lista.append(personaje)
                flag = True
                
        if flag:
            print("Se extrajo los datos correctamente")
            return lista

def crear_archivo_json(path:str, lista:list)->bool:
    '''
    Brief: crea un archivo json 
    Parameters:
        path:str -> nombre del archivo
        lista:list -> lista de personajes
    return: retorna el diccionario normalizado 
    '''
    if type(path) == str and len(lista) > 0:
        with open(path, "w") as archivo:
            json.dump(lista, archivo, indent= 4)
        flag = True
    else:
        flag = False

    return flag

def crear_nombre_json(habilidad:str,raza:str)->str:
    '''
    Brief: crea el nombre para el archivo json segun la raza y habilidad
    Parameters:
        habilidad:str -> habilidad de los personajes
        raza:str -> raza de los personajes
    return: retorna el nombre del archivo
    '''
    if type(habilidad) == str and type(raza) == str:
        separador = "_"
        nombre_aux = habilidad.replace(" ", separador)
        nombre_archivo = separador.join([raza, nombre_aux]) +".json"

    return nombre_archivo



def guardar_json(lista:list, key_raza:str, key_habilidad:str)->str:
    '''
    Brief: se crea un archivo json de los personajes con su habilidad y raza
    Parameters:
        lista: list -> lista sobre la que voy a hacer la busqueda
        key_raza:str -> la key que que contiene "raza"
        key_habilidad:str -> la que key que contiene "habilidad"
    return: retorna el nombre del archivo
    '''
    if type(lista) == list and type(key_raza) == str and type(key_habilidad) == str and len(lista) > 0:
        lista_copia = lista.copy()
        lista_final = []
        raza_ingresada = ingreso_de_datos("Ingrese la raza: ", lista, key_raza)
        habilidad_ingresada = ingreso_de_datos("Ingrese la habilidad: ", lista, key_habilidad)
        for personaje in lista_copia:
            if validar_ingreso_datos(raza_ingresada, personaje[key_raza]):
                if validar_ingreso_datos(habilidad_ingresada, personaje[key_habilidad]):
                    personaje_aux = {}
                    personaje_aux["nombre"] = personaje['nombre']
                    personaje_aux['poder_de_ataque'] = personaje['poder_de_ataque']
                    personaje_aux["habilidades"] = personaje["habilidades"].copy()
                    personaje_aux["habilidades"].remove(habilidad_ingresada)
                    lista_final.append(personaje_aux)

        nombre_archivo = crear_nombre_json(habilidad_ingresada, raza_ingresada)

        if crear_archivo_json(nombre_archivo, lista_final):
            print("Se creo el archivo correctamente")
        else:
            print("Error")

        return nombre_archivo

def imprimir_json(lectura):
    '''
    Brief: imprime un archivo json con un formato 
    Parameters:
        lectura -> contiene los datos linea por linea del archivo
    '''
    for elemento in lectura:
        print(f"Nombre: {elemento['nombre']}|Poder de ataque: {elemento['poder_de_ataque']}\n"
            f"Habilidades: ",end = "")
        for habilidad in elemento["habilidades"]:
            print(f" {habilidad}",end= "")
        print("\n")

def leer_json(path:str):
    '''
    Brief: lee un archivo json y lo muestra 
    Parameters:
        path:str -> nombre del archivo
    '''
    with open(path, "r") as mi_archivo:
        lectura = json.load(mi_archivo)
        imprimir_json(lectura)

def crear_txt_batalla(path:str, ganador:dict, perdedor:dict, resultado:str, fecha:datetime.date)->bool:
    '''
    Brief: crea un archivo de texto  
    Parameters:
        path:str -> el nombre de archivo de texto
        ganador:dict -> el diccionario que contiene los datos del ganador
        perdedor:str -> el diccionario que contiene los datos del perdedor
        resultado:str -> el resultado de la batalla
        fecha:detetime.date -> la fecha actual que se realizo la batalla
    return: retorna True si se creo correctamente el archivo o False si hubo error
    '''
    if type(ganador) == dict and type(perdedor) == dict:
        if len(ganador) > 0 and len(perdedor) > 0:
            with open(path, "a") as archivo:
                if resultado != "Empate":
                    registro = "Ganador: {0} | Perdedor:{1} | Rersultado: {2}\n".format(ganador["nombre"], perdedor["nombre"], resultado)
                else:
                    registro = "{0} | {1} | Rersultado: {2}\n".format(ganador["nombre"], perdedor["nombre"], resultado)
                fecha = (f"Fecha: {fecha}\n")
                archivo.write(registro)
                archivo.write(fecha)
                flag = True
        else:
            flag = False

    return flag


def validar_ingreso_datos(dato:str, lista:list, key = None)->bool:
    '''
    Brief: busca y valida los datos existan en la lista segun su clave especifica
    o dentro de toda una lista
    Parameters:
        dato:str -> dato que verifico si existe
        lista: list -> lista sobre la que voy a hacer la busqueda
        key:str -> clave del valor dentro de la lista
    return: retorna True si el dato es correcto o False en caso de no serlo
    '''
    if type(lista) == list and type(dato) == str and len(lista) > 0:
        flag = False
        if key != None:
            for elemento in lista:
                if dato in elemento[key]:
                    flag = True
                    break
                else:
                    flag = False
        else:
            if dato in lista:
                flag = True

        return flag

def ingreso_de_datos(mensaje:str, lista:list, key:str):
    '''
    Brief: toma el dato que ingresa el usuario y si no es valido lo vuelve a pedir
    Parameters:
        mensaje:str -> mensaje que indica donde y que poner al usuario
        lista: list -> lista sobre la que voy a hacer la busqueda
        key:str -> clave del valor dentro de la lista
    return: retorna el dato ingresado
    '''
    if type(lista) == list and type(key) == str and len(lista) > 0 and type(mensaje) == str:
        elemento = input(mensaje)
        while True:
            if validar_ingreso_datos(elemento,lista, key) is False:
                print("Error")
                elemento = input(mensaje)
            else:
                break

        return elemento
