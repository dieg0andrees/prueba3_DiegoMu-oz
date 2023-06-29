import misfunciones as mf

while True:
    try:
        mf.limpiarPantalla()
        print("""
        ****Bienvenido****
        1) Registrar Alumno
        2) Buscar alumno
        3) Imprimir certificado
        0) Salir 
        """)
        opcion = int(input("Seleccione -->"))
        if opcion == 0:
            mf.printVerde("Adios")
            break
        elif opcion == 1:
            mf.printTitulo("REGISTRAR")
            rut = int(input("Ingrese rut sin puntos ni guión -->"))
            nombre = input("Ingrese nombre completo -->").capitalize()
            edad = int(input("Ingrese edad -->"))
            genero = input("Ingrese genero -->")
            promedio = float(input("Ingrese promedio -->"))
            fecha_matricula = input("Ingrese fecha matricula (dd/mm/aa) -->")
            nombre_apoderado = input("Ingrese nombre de apoderado -->").capitalize()
            mf.registrar(rut,nombre,edad,genero,promedio,fecha_matricula,nombre_apoderado)

        elif opcion == 2:
            mf.printTitulo("BUSCAR")
            rut = int(input("Ingrese rut sin puntos ni guión -->"))
            mf.buscar(rut)
        elif opcion == 3:
            while True:
                print("""
        1) Certificado de anotaciones
        2) Certificado de notas
        3) Certificado de alumno regular
        0) Salir
                """)
                opcion2 = int(input("Seleccione -->"))
                if opcion2 == 0:
                    break
                elif opcion2 == 1:
                    mf.printTitulo("CERTIFICADO DE ANOTACIONES")
                    rut = int(input("Ingrese rut sin puntos ni guión -->"))
                    mf.certificadoAnotaciones(rut)
                    break

                elif opcion2 == 2:
                    mf.printTitulo("CERTIFICADO DE NOTAS")
                    rut = int(input("Ingrese rut sin puntos ni guión -->"))
                    mf.certificadoNotas(rut)
                    break
            
                elif opcion2 == 3:
                    mf.printTitulo("CERTIFICADO DE ALUMNO REGULAR")
                    rut = int(input("Ingrese rut sin puntos ni guión -->"))
                    mf.certificadoAlumnoRegular(rut)
                    break
                else:
                    mf.printError("Opcion Invalida")
        else:
            mf.printError("Opcion Invalida")
    except:
        mf.printError("ERROR")
