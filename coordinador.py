import datos 

ruta_estudiantes_aprobados="aprobados.json"
datos_estudiantes_aprobados= datos.cargar_datos(ruta_estudiantes_aprobados)

ruta_estudiantes_cursando="cursando.json"
datos_estudiantes_cursando= datos.cargar_datos(ruta_estudiantes_cursando)

ruta_de_rutas="rutas.json"
datos_de_rutas=datos.cargar_datos(ruta_de_rutas)

ruta_trainers="trainer.json"
datos_trainers=datos.cargar_datos(ruta_trainers)

def asignar_ruta(datos_estudiantes_aprobados, datos_estudiantes_cursando):
    print("Digite el documento del camper que desea modificar: ")
    doc = input()
    if doc in datos_estudiantes_aprobados["usuarios"]:
        usuario = datos_estudiantes_aprobados["usuarios"][doc]
        usuario["Proceso"] = "Cursando"
        usuario_sin_datos = usuario.copy()
        eliminar = ["Nombres", "Apellidos", "Direccion", "Acudiente", "Telefono fijo", "Contacto"]
        for i in eliminar:
            usuario_sin_datos.pop(i, None)
            usuario_sin_datos["Notas"] = {"Quizes y Trabajos": 0, "Prueba teorica":0, "Prueba practica(Proyecto)": 0,}
        print("Elija la ruta del camper: \n1.NodeJs \n2.Java \n3.NetCore\n")
        ruta = int(input())
        if ruta == 1:
            if len(datos_estudiantes_cursando.get("NodeJs")) < 32:
                datos_estudiantes_cursando["NodeJs"][doc] = usuario_sin_datos
            else:
                print("En la ruta NodeJs no caben más campers!")
        elif ruta == 2:
            if len(datos_estudiantes_cursando.get("Java")) < 32:
                datos_estudiantes_cursando["Java"][doc] = usuario_sin_datos
            else:
                print("En la ruta Java no caben más campers!")
        elif ruta == 3:
            if len(datos_estudiantes_cursando.get("NetCore")) < 32:
                datos_estudiantes_cursando["NetCore"][doc] = usuario_sin_datos
            else:
                print("En la ruta NetCore no caben más campers!")
            datos.guardar_datos(datos_estudiantes_cursando, ruta_estudiantes_cursando)
            datos.guardar_datos(datos_estudiantes_aprobados, ruta_estudiantes_aprobados)
            print("Estudiante aprobado movido exitosamente de aprobados a cursando.")
        else:
            print("El estudiante no está en proceso Cursando.")
    else:
        print("El documento no corresponde a ningún estudiante aprobado.")

def crear_rutas():
    name_ruta=input("Ingrese el nombre de la ruta: ")
    ruta={}

#def modificar_ruta():


def asignar_trainer(datos_trainers,datos_estudiantes_cursando):
    print("Digite el numero de documento del trainer ")
    doc=input()
    print("Digite el documento del camper")
    docu=input()
    if doc in datos_trainers and docu in datos_estudiantes_cursando:
        print("Elija la ruta del camper: \n1.NodeJs \n2.Java \n3.NetCore\n")
        ruta = int(input())
        if ruta==1:
            ola=datos_trainers["Trainers"][doc].get("Nombre")
            datos_estudiantes_cursando
        
    else:
        print("Trainer no existe!")
    


def crear_trainer(datos_trainers):
    bitbop={}
    print("Digite el numero de documento del trainer ")
    doc=input()
    if doc in datos_trainers:
        print("Trainer Existe!")
    else:
        bitbop["Nombre"]=input("Digite el nombre y apellido del trainer: ")
        bitbop["Edad"]=int(input("Digite la edad del trainer: "))
        datos_trainers["Trainers"][doc]=bitbop
        datos.guardar_datos(datos_trainers, ruta_trainers)
