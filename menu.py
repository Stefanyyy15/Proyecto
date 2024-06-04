def pedir_opc():
    opc=0
    try:
        opc= int(input())
        return opc
    except Exception:
        print("Valor invalido!")
        return 0

def menu_principal ():
    print("""                                  CAMPUSLANDS                         
                          Bienvenido a la plataforma!
                      1.Registrarse  2.Ingresar  3.Pruebas""")

def main_menu():
    print("Seleccione el perfil al que desea ingresar: ")
    print("1.Camper\n2.Trainer\n3.Coordinador")

def menu_camper():
    print("BIENVENIDO CAMPER")
    print("¿Que desea hacer?")
    print("1.Ver notas\n2.Ver horario")

def menu_trainer():
    print("BIENVENIDO TRAINER")
    print("¿Que desea hacer?")
    print("1.Ver horario\n2.Modificar notas")

def menu_coordinador():
    print("BIENVENIDO COORDINADOR")
    print("¿Que desea hacer?")
    print("1.Modificar proceso camper \n2.Asignar rutas\n3.Crear rutas\n4.Modificar rutas\n6.Modificar riesgo camper\n7.Reportes")    

def pruebas_admision(datos):
    doc=input("Digite su documento: ")
    if  doc in datos["usuarios"]:
        print("¿Cuanto sacaste en la prueba teorica?")
        prueba_t=int(input())
        print("¿Cuanto sacaste en la prueba practica?")
        prueba_p=int(input())
        resultado=prueba_t + prueba_p / 2
        datos["usuarios"][doc]["Resultado prueba"] = resultado
        if resultado>=60:
            print("FELICIDADES\nEstas oficialmente inscrito en el programa")
        elif resultado<60:
            print("No pasaste las pruebas de admision\nSuerte para la proxima!")
    else: 
        print("Documento no esta asociado a ningun camper inscrito!")


