import datetime
import random
from lecturas_escrituras import *

def dbz_normalizar_datos(lista:list)->list:
    '''
    Brief: castea los valores string a numericos
    Parameters: lista: list -> lista sobre la que voy a catear los datos
    '''

    flag = False
    if len(lista) > 0:
        for personaje in lista:
            if type(personaje["id"]) != int:
                personaje["id"] = int(personaje["id"])
                flag = True 
            if type(personaje["poder_de_pelea"]) != int:
                personaje["poder_de_pelea"] = int(personaje["poder_de_pelea"])
                flag = True
            if type(personaje["poder_de_ataque"] != int):
                personaje["poder_de_ataque"] = int(personaje["poder_de_ataque"])
                flag = True
    else: 
        print("Lista vacia")
    
    if flag:
        print("Datos normalizados")
        return lista
    else:
        return None

def determinar_contar_raza(lista:list,key:str)->dict:
    '''
    Brief: crea un un diccionario que cuenta la cantidad de razas  
    Parameters:
        lista: list -> lista sobre la que voy a hacer la busqueda
        key:str -> clave del valor dentro de la lista
    return: retorna el diccionario con la cantidad de razas
    '''
    if type(lista) == list and type(key) == str and len(lista) > 0:
        raza_cantidad = {}

        for personaje in lista:
            for elemento in personaje[key]:
                raza = elemento
                if raza in raza_cantidad:
                    raza_cantidad[raza] += 1
                else:
                    raza_cantidad[raza] = 1

        return raza_cantidad

def mostrar_lista(lista:list, key = None):
    '''
    Brief: puede mostrar la lista de elementos segun su key o simplemente mostrar su contenido
    Parameters:
        lista: list -> lista sobre la que voy a recorrer
        key = None -> clave del valor dentro de la lista
    '''
    if type(lista) == list and len(lista) > 0:
        if key == None:
            for elemento in lista:
                print(f"{elemento}")
        else:
            for dato in lista:
                    print(f"{key}: {dato[key]}")

def mostrar_diccionario(diccionario:dict)->None:
    '''
    Brief: crea un set de la lista dentro de lista de diccionarios  
    Parameters:
        diccionario:dict -> el diccionario que voy a reccorrer
    '''
    if type(diccionario) == dict:
        for key in diccionario:
            print(f"{key}: {diccionario[key]}")

def agrupar_mostrar_raza(lista:list,key:str)->dict:
    if type(lista) == list and type(key) == str and len(lista) > 0:
        '''
        Brief: recorre la lista agrupando y mostrando los personajes (segundo la raza en este caso) 
        Parameters:
        lista: list -> lista sobre la que voy a hacer la busqueda
        key:str -> clave del valor dentro de la lista
        '''
        personaje_set = crear_set(lista, key)
        
        for rasgo in personaje_set:
                print(f"\n{rasgo}: ", end= "\n")
                for personaje in lista:
                    if rasgo in personaje[key]:
                            print(f"{personaje['nombre']}|{personaje['poder_de_ataque']}")

def crear_set(lista:list, key:str)->set:
    '''
    Brief: crea un set de la lista dentro de lista de diccionarios  
    Parameters:
        lista: list -> lista sobre la que voy a hacer la busqueda
        key:str -> clave del valor dentro de la lista
    return: retorna el set
    '''
    if type(lista) == list and type(key) == str and len(lista) > 0:
        mi_set = set()
        for personaje in lista:
            for i in range(len(personaje[key])):
                mi_set.add(personaje[key][i])
        return mi_set

def dividir(dividendo:float, divisor:int)->float:
    '''
    Brief:divide los datos que pase por parametro
    Parameters:
        dividendo:float -> representa el numero el cual divido
        divisor:int -> reprenta el numero por el cual voy a dividir
    return: retora el resultado de la division
    '''
    if divisor == 0:
        resultado = 0
    else:
        resultado = dividendo / divisor

    return resultado


def calcular_promedio(acumulador:int, contador:int):
    '''
    Brief: calcula el promedio deseado que representa el valor de las keys
    Parameters:
        lista: list -> lista sobre la que voy a hacer la busqueda
        key:str -> clave del valor dentro de la lista
    return: retorna el resultado del promedio
    '''

    if acumulador > 0:
        promedio = dividir(acumulador, contador)
        return promedio
    else:
        print("Error")

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

def listar_habilidad(lista:list, key:str):
    '''
    Brief: recorre y mustra las las habilidades con sus personajes  
    Parameters:
        lista: list -> lista sobre la que voy a hacer la busqueda
        key:str -> clave del valor dentro de la lista
    '''
    if type(lista) == list and type(key) == str and len(lista) > 0:
        elemento = ingreso_de_datos("Ingrese la habilidad: ", lista, key)
        for personaje in lista:
            if validar_ingreso_datos(elemento, personaje[key]):
                acumulador = personaje["poder_de_pelea"] + personaje["poder_de_ataque"]
                promedio = calcular_promedio(acumulador, 2)
                print(f"{personaje['nombre']}", end= "")
                for raza in personaje["raza"]:
                    print(f"|{raza}", end= "")
                print(f"|Promedio:{promedio:.2f}")

def devolver_diccionario(buscado:str, lista:list, key:str)->dict:
    '''
    Brief: busca un personaje especifico dentro de la lista y lo devuelve 
    Parameters:
        buscado:str -> el personaje que estoy buscando
        lista: list -> lista sobre la que voy a hacer la busqueda
        key:str -> clave del valor dentro de la lista
    return: retorna el diccionario entero del personaje
    '''
    if type(buscado) == str and type(lista) == list and type(key) == str:
        if len(lista) > 0:
            for personaje in lista:
                if buscado == personaje[key]:
                    return personaje

def batalla_dbz(lista:list, key:str):
    '''
    Brief: se realiza una batalla y se determina el ganador y perdedor
    Parameters:
        lista: list -> lista sobre la que voy a hacer la busqueda
        key:str -> clave del valor dentro de la lista
    '''
    if type(lista) == list and type(key) == str and len(lista) > 0:
        aleatorio = random.choice(lista)
        fecha_actual = datetime.date.today()
        elegido = ingreso_de_datos("Elija un personaje: ", lista, key)
        elegido_diccionario = devolver_diccionario(elegido, lista, key)
        if elegido_diccionario["poder_de_ataque"] > aleatorio["poder_de_ataque"]:
            ganador = elegido_diccionario
            perdedor = aleatorio
            resultado = "Gano el usuario"
        elif elegido_diccionario["poder_de_ataque"] < aleatorio["poder_de_ataque"]:
            ganador = aleatorio
            perdedor = elegido_diccionario
            resultado = "Gano la maquina"
        else:
            ganador = aleatorio
            perdedor = elegido_diccionario
            resultado = "Empate"

        if crear_txt_batalla("Batalla.txt", ganador, perdedor, resultado, fecha_actual):
            print("Se cargo correctamente el archivo")
        else:
            print("Error")

def mostrar_menu():
    '''
    Brief:muestra el menu principal con sus opciones
    '''
    menu = ["\n1.Traer datos desde archivo", "2.Listar cantidad por raza", "3.Listar personajes por raza", "4.Listar personajes por habilidad", 
    "5.Jugar batalla", "6.Guardar Json", "7.Leer Json", "8.Salir"]
    for opcion in menu:
        print(opcion)

def validar_entero(numero:str):
    '''
    Brief: valida que el dato ingresado sea un numero en string y lo castea a entero
    Parameters: 
    numero:str -> string que se valida y se castea 
    return: retorna el numero casteado
    '''
    if numero.isnumeric():
        return True
    else:
        return False

def dbz_menu_principal():
    '''
    Brief: funcion donde se contiene la logica del menu y se lo muestra
    Parameters:....
    return:...
    '''
    mostrar_menu()
    respuesta = input("Ingrese una opcion: ")
    if validar_entero(respuesta):
        return int(respuesta)
    else:
        return -1

def dbz_app(path:str):
    '''
    Brief: continene toda la logica del programa con las demas funciones agrupadas
    Parameters:
        lista: list -> lista sobre la que voy a hacer la busqueda
    '''
    flag = False
    flag_json = False
    while True:
        respuesta = dbz_menu_principal()

        if respuesta != -1:
            if respuesta < 1 or respuesta > 7:
                print("Error")
            else:
                match respuesta:
                    case 1: 
                        lista_personajes = parser_csv(path)
                        lista_normalizada = dbz_normalizar_datos(lista_personajes)
                        flag = True
                    case 2:
                        if flag:
                            raza_cantidad = determinar_contar_raza(lista_normalizada,"raza")
                            mostrar_diccionario(raza_cantidad)
                        else:
                            print("No se cargo el archivo")
                    case 3:
                        if flag:
                            agrupar_mostrar_raza(lista_normalizada,"raza")
                        else:
                            print("No se cargo el archivo")
                    case 4:
                        if flag:
                            habilidad_set = crear_set(lista_normalizada, "habilidades")
                            mostrar_lista(list(habilidad_set))
                            listar_habilidad(lista_normalizada,"habilidades")
                        else:
                            print("No se cargo el archivo")
                    case 5:
                        if flag:
                            mostrar_lista(lista_normalizada, "nombre")
                            batalla_dbz(lista_normalizada, "nombre")
                        else:
                            print("No se cargo el archivo")
                    case 6:
                        if flag:
                            nombre_json = guardar_json(lista_normalizada, "raza", "habilidades")
                            flag_json = True
                        else:
                            print("No se cargo el archivo")
                    case 7:
                        if flag_json:
                            leer_json(nombre_json)
                        else:
                            print("No se cargo el archivo")
                    case 8:
                        break
