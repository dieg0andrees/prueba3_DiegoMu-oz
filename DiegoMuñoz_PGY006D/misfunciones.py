import numpy
from colorama import Fore, Style
import random
import os
import msvcrt

#Funciones de diseño
def printVerde(texto):
    print(f"{Fore.GREEN}{texto}{Fore.RESET}")
def printError(texto):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")
def printTitulo(texto):
    print(f"""
    *********************
    {Fore.YELLOW}{texto}{Fore.RESET}
    *********************
    """)
def limpiarPantalla():
    print("<<Presione una tecla para continunar>>")
    msvcrt.getch()
    os.system("cls")


#Funciones Operacionales
colegio = numpy.empty([10,7],object)

def validarRut(rut):
    for i in range(10):
        if colegio[i,0] == rut:
            return i
    return -1



def registrar(rut,nombre,edad,genero,promedio,fecha_matricula,nombre_apoderado):
    if None in colegio:
        if validarRut(rut) < 0:
            if len(nombre)>=2 and len(nombre)<=30:
                if edad >=4:
                    for i in range(10):
                        if colegio[i,0] == None:
                            colegio[i,0] = rut
                            colegio[i,1] = nombre
                            colegio[i,2] = edad
                            colegio[i,3] = genero
                            colegio[i,4] = promedio
                            colegio[i,5] = fecha_matricula
                            colegio[i,6] = nombre_apoderado
                            printVerde("Alumno registrado!")
                            break
                else:
                    printError("El alumno debe ser mayor a 4 años")
            else:
                printError("El nombre debe contener entre 2 y 30 caracteres")
        else:
            printError("El alumno ya se encuentra registrado")
    else:
        printError("No hay más cupos para registrar alumnos")

def buscar(rut):
    posicion = validarRut(rut)
    if validarRut(rut) >= 0:
        print(f"""*DATOS ALUMNO*
        Rut              : {colegio[posicion,0]}
        Nombre           : {colegio[posicion,1]}
        Edad             : {colegio[posicion,2]}
        Genero           : {colegio[posicion,3]}
        Promedio de notas: {colegio[posicion,4]}
        Fecha Matricula  : {colegio[posicion,5]}
        Nombre Apoderado : {colegio[posicion,6]}
        """)
    else:
        printError("Alumno no encontrado")

anotaciones = []
anotaciones.append("Alumno conversa en clase")
anotaciones.append("Alumno llega tarde reiteradas veces")
anotaciones.append("Alumno le pega a compañero")
anotaciones.append("Alumno hizo todas las tareas ")
anotaciones.append("Alumno hace aseo en la sala")
anotaciones.append("Alumno le falta el respeto a profesor")
anotaciones.append("Alumno ocupa el celular en prueba")
anotaciones.append("Alumno rompe ventana")

def certificadoAnotaciones(rut):
    posicion = validarRut(rut)
    if validarRut(rut) >= 0:
        print(f"""
        Nombre: {colegio[posicion,1]}
        Rut: {colegio[posicion,0]}
        _____________________________
        1.- {anotaciones[random.randint(0,7)]}
        2.- {anotaciones[random.randint(0,7)]}
        3.- {anotaciones[random.randint(0,7)]}
        4.- {anotaciones[random.randint(0,7)]}
        """)
    else:
        printError("Alumno no registrado")
notas = []
notas.append(5.2)
notas.append(5.5)
notas.append(3.1)
notas.append(1.0)
notas.append(7.0)
notas.append(6.5)
notas.append(4.3)
notas.append(4.7)
notas.append(2.3)
notas.append(6.6)

def certificadoNotas(rut):
    posicion = validarRut(rut)
    if validarRut(rut) >= 0:
        print(f"""
        Nombre: {colegio[posicion,1]}
        Rut: {colegio[posicion,0]}
        __________________________
        Notas Matematica : {notas[random.randint(0,9)]}, {notas[random.randint(0,9)]}, {notas[random.randint(0,9)]}
        Notas Lenguaje   : {notas[random.randint(0,9)]}, {notas[random.randint(0,9)]}, {notas[random.randint(0,9)]}
        Notas Ingles     : {notas[random.randint(0,9)]}, {notas[random.randint(0,9)]}, {notas[random.randint(0,9)]}
        Notas Historia   : {notas[random.randint(0,9)]}, {notas[random.randint(0,9)]}, {notas[random.randint(0,9)]}
        PROMEDIO         : {sum(notas)/10}
        """)
    else:
        printError("Alumno no registrado")

curso = []
curso.append("Primero medio")
curso.append("Segundo medio")
curso.append("Tercero medio")
curso.append("Octavo Basico")
curso.append("Septimo Basico")
curso.append("Sexto Basico")
curso.append("Quinto Basico")
curso.append("Cuarto Basico")
curso.append("Tercero Basico")
curso.append("Segundo Basico")
curso.append("Primero Basico")

def certificadoAlumnoRegular(rut):
    posicion = validarRut(rut)
    if validarRut(rut) >= 0:
        print(f"""
        Se certifica que el alumno {colegio[posicion,1]} con rut {colegio[posicion,0]} que cursa
        {curso[random.randint(0,10)]} se encuentra matriculado en el colegio San Charlis.


        *Firma Director
        _______________ 
        """)
    else:
        printError("Alumno no registrado")