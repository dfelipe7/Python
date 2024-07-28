import random

def opcionEscogida(opc):
    if(opc==2):
        print("Adios!!!")
    else:
        numeroIngresado=0
        numeroAleatorio=random.randint(1,10)
        while numeroIngresado!=numeroAleatorio:
            numeroIngresado=int(input("Ingresa un numero"))
            if numeroAleatorio<numeroIngresado:
                print("Bajale un poco")
            else:
                print("Subele un poco")   
        print("Lo adivinaste!!!")         
    
def menu():
    print("Adivina el numero")
    print("1.Iniciar")
    print("2.Salir")
    opc=int(input("Elija opcion"))
    return opc

opc=menu()   
while opc==1: 
    opcionEscogida(opc) 
    opc=menu()  
        

