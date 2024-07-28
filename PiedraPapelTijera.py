import random
import os
def partida():
    numPartidas=int(input("Ingrese numero de partidad a jugar"))
    contador=0
    puntosMaquina=0
    puntosHumano=0
    while(numPartidas!=contador):
        print("1.Piedra")
        print("2.Papel")
        print("3.Tijera")
        turnoHumano=int(input("Elije que quieres tirar"))
        turnoMaquina=random.randint(1,3)
        if(turnoHumano==1):
            turnoH="Piedra"
        elif(turnoHumano==2):
            turnoH="Papel"  
        else:
            turnoH="Tijera"      
            
        if(turnoMaquina==1):
            turnoM="Piedra"
        elif(turnoMaquina==2):
            turnoM="Papel"  
        else:
            turnoM="Tijera"      
                
        print("*************************")
        print("Lanzamientos")
        print("Humano:",turnoH," Maquina:",turnoM)
        
        if(turnoHumano==1):
            if(turnoMaquina==1):
                print("Empate")
            elif(turnoMaquina==2):
                print("Gana maquina")
                puntosMaquina+=1
            else:
                print("Gana humano")
                puntosHumano+=1
        elif(turnoHumano==2):
                if(turnoMaquina==1):
                    print("Gana humano")
                    puntosHumano+=1
                elif(turnoMaquina==2):
                    print("Empate")
                else:
                    print("Gana Maquina") 
                    puntosMaquina+=1

        else:
            if(turnoHumano==3):
                if(turnoMaquina==1):
                    puntosMaquina+=1
                    print("Gana maquina")
                elif(turnoMaquina==2):
                    print("Gana Humano")
                    puntosHumano+=1
                else:
                    print("Empate")  
                    
      
        print("Puntajes")      
        print("Maquina",puntosMaquina)   
        print("Humano",puntosHumano)                           
        print("*************************")                              
        print("")
        contador+=1    

def menu():
    print("Piedra, papel o tijera")
    print("1.Jugar")
    print("2.salir")
    opc=int(input("Ingrese opcion"))
    return opc
    
opc=0
while(opc!=2):
    opc=menu()
    if(opc==1):
        partida()
    elif (opc==2):
        print("Adios!!!")
    else:
        print("Opcion incorrecta")    
        