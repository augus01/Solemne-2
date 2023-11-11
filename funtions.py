import users

kilometrosGeneral = [0]
petroleoGeneral = [0]
inicioGeneral = [0]
terminoGeneral = [0]

def menuPrincipal ():
    tipoUsuario = input("Ingrese el tipo de usuario que esta usando este software (Supervisor o Operario) ").lower()
    if tipoUsuario == "supervisor":
        validarUsuarios(users.supervisor,tipoUsuario)
    elif tipoUsuario == "operario":
        validarUsuarios(users.operarios, tipoUsuario)
        menuPrincipal()
    else:
        print("No es un usuario valido")


def validarUsuarios(array,usuario):
    i = 0
    while i < 3:
        name = input("Ingresar numero de operario ")
        contra = input("ingresar contraseña ")
        for clave,data in array.items():
            if data["numOperario"] == name  and data["contrasena"] == contra:
                if usuario == "supervisor":
                    menuSupervisor()
                    i = 3
                    break                    
                solicitudInfo(clave, array)
                i = 3
                break
            else:  
                i += 1
                


def solicitudInfo(operario,tipoUsuario):
    numOrden = input("Ingresar numero de orden ")
    fecha = input("Ingresar fecha ")
    tipoUsuario[operario]["kilometros"] += int(input("Ingrese los kilometros recorridos "))
    kilometrosGeneral.append(tipoUsuario[operario]["kilometros"])

    tipoUsuario[operario]["petroleo"] += int(input("Ingrese el petroleo consumido "))
    petroleoGeneral.append(tipoUsuario[operario]["petroleo"])

    inicioRegistrado = 0
    inicioRegistrado += int(input("Ingresar hora de inicio "))
    tipoUsuario[operario]["inicio"].append(inicioRegistrado)
    inicioGeneral.append(inicioRegistrado)

    terminoRegistrado = 0
    terminoRegistrado += int(input("Ingresar hora de termino "))
    tipoUsuario[operario]["termino"].append(terminoRegistrado)
    terminoGeneral.append(terminoRegistrado)
    

def menuSupervisor():
    eleccion = input("ELegir que funcion desea emplear:\n [1] Ver Total Kilometraje registrado \n [2] Ver Total Petroleo Consumido \n [3] Ver promedio Hora de inicio \n [4] Ver promedio Hora termino \n [5] Ver informacion por operario \n [6] Volver al menu principal \n")
    if eleccion == "1":
        print(sum(kilometrosGeneral))
        menuSupervisor()
    elif eleccion == "2":
        print(sum(petroleoGeneral))
        menuSupervisor()
    elif eleccion == "3":
        print(sum(inicioGeneral)/(len(inicioGeneral)-1))
        menuSupervisor()
    elif eleccion == "4":
        print(sum(terminoGeneral)/(len(terminoGeneral)-1))
        menuSupervisor()
    elif eleccion == "5":
        operarioSolicitato = input("ingrese el numero de operario que desea revisar ")
        infoOperario(operarioSolicitato)
    elif eleccion == "6":
        menuPrincipal()

def infoOperario(operarioSolicitato):
    operario = operarioSolicitato
    for clave,data in users.operarios.items():
        if data["numOperario"] == operarioSolicitato:
                eleccionOperario = input("ELegir que funcion desea emplear en el operario:\n [1] Ver Total Kilometraje registrado \n [2] Ver Total Petroleo Consumido \n [3] Ver promedio Hora de inicio \n [4] Ver promedio Hora termino \n [5] Volver al menu principal")
                if eleccionOperario == "1":
                    print(data["kilometros"])
                    infoOperario(operario)
                elif eleccionOperario == "2":
                    print(data["petroleo"])
                    infoOperario(operario)
                elif eleccionOperario == "3":
                    print(sum(data["inicio"])/(len(data["inicio"])-1))
                    infoOperario(operario)
                elif eleccionOperario == "4":
                    print(sum(data["termino"])/(len(data["termino"])-1))
                    infoOperario(operario)
                elif eleccionOperario == "5":
                    menuPrincipal()