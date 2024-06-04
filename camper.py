import datos

ruta_estudiantes_registrados="registrados.json"
datos_estudiantes_registrados=datos.cargar_datos(ruta_estudiantes_registrados)

ruta_estudiantes_aprobados="aprobados.json"
datos_estudiantes_aprobados= datos.cargar_datos(ruta_estudiantes_aprobados)

ruta_estudiantes_cursando="cursando.json"
datos_estudiantes_cursando= datos.cargar_datos(ruta_estudiantes_cursando)

def registrar_camper(datos):
    global doc
    dixi = {}
    print("Para registrarse debe: ")
    doc = input("Digite su numero de documento: ")
    if doc in datos["usuarios"]:
        print("Ya estas registrado como camper!")
    elif doc not in datos["usuarios"]:
        dixi["Nombres"] = input("Escriba sus Nombres: ")
        dixi["Apellidos"] = input("Escriba sus Apellidos: ")
        dixi["Direccion"] = input("Escriba su direccion: ")
        dixi["Acudiente"] = input("Escriba el nombre y apellido de su acudiente: ")
        dixi["Contacto"] = input("Escriba su numero de contacto: ")
        dixi["Telefono fijo"] = input("Escriba su telefono fijo: ")
        dixi["Proceso"] = "Inscrito"
        dixi["Riesgo"] = False
        datos["usuarios"][doc] = dixi
        print("Has sido registrado para presentar la prueba de admision")
      
def modificar_camper (datos):
    global doc
    print("Digite el documento del camper que desea modificar: ")
    doc= input()
    if doc in datos["usuarios"]:
        print ("El camper saco en las pruebas de admision: ", datos["usuarios"][doc].get("Resultado prueba"))
        proceso = input("Ingrese el proceso en el que se encuentra el camper: ")
        datos["usuarios"][doc]["Proceso"] = proceso
    else:
        print("El documento no corresponde a ningun camper")


def aprobar_camper(datos_estudiantes_registrados, datos_estudiantes_aprobados):
    if doc in datos_estudiantes_registrados["usuarios"]:
        roxane=datos_estudiantes_registrados["usuarios"][doc]
        if roxane["Proceso"]=="Aprobado":
            datos.guardar_datos(datos_estudiantes_registrados, ruta_estudiantes_registrados)
            datos_estudiantes_aprobados["usuarios"][doc] = roxane
            datos_estudiantes_registrados["usuarios"].pop(doc, None)
            datos.guardar_datos(datos_estudiantes_registrados, ruta_estudiantes_aprobados)
            datos.guardar_datos(datos_estudiantes_registrados, ruta_estudiantes_registrados)  
            print("Estudiante aprobado movido exitosamente de registrados a aprobados.")

def ver_notas():
    print("Digite su documento: ")
    doc=input()
    print ("¿En que ruta esta?\n1.NodeJs\n2.Java\n3.NetCore")
    opc=int(input())
    if opc==1:
        notas = datos_estudiantes_cursando["NodeJs"][doc].get("Notas")
        print("A continuacion se le muestran sus notas: ")
        for clave, valor in notas.items():
            print (clave, valor )
    elif opc==2:
        notas = datos_estudiantes_cursando["Java"][doc].get("Notas")
        print("A continuacion se le muestran sus notas: ")
        for clave, valor in notas.items():
            print (clave, valor )
    elif opc==3:
        notas = datos_estudiantes_cursando["NetCore"][doc].get("Notas")
        print("A continuacion se le muestran sus notas: ")
        for clave, valor in notas.items():
            print (clave, valor )
    else:
        print("Valor no encontrado!")

    
def ver_horario():
    print("Digite su documento: ")
    doc=input()
    datos_estudiantes_cursando

