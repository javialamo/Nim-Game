# EL JUEGO DE NIM v 1.3
# Javier del Álamo -=- 02/18/2013


import random
import time

def displayIntro():
    print()
    print()
    print('= EL JUEGO DE NIM =')
    time.sleep(1.5)
    print('Nim es un juego para dos jugadores.')
    time.sleep(1.5)
    print('Se juega por turnos. En cada partida ')
    time.sleep(1.5)
    print('habra un numero aleatorio de filas ')
    time.sleep(1.5)
    print('con un numero aleatorio de fichas.')
    time.sleep(1.5)
    print('En cada turno, un jugador puede coger ')
    time.sleep(1.5)
    print('cuantas fichas quiera de una unica fila.')
    time.sleep(1.5)
    print('Gana el jugador que retira la ultima ficha.')
    time.sleep(1.5)
    print('¡A divertirse!')
    print()



def pintaTablero(tablero):
    print()
    for i in range(len(tablero)-1):
        fichas='O' * tablero[i]
        print(str(i+1) +'.'+ chr(27) + "[1;31m" + ' ||' + chr(27) + "[0;32m" + fichas + chr(27)+"[0m")
#        print(str(tablero[i]))
    print()

displayIntro()

Player=[None]*2

for i in range(2):
    time.sleep(2)
    print('Hola jugador '+str(i+1))
    time.sleep(1)
    print('Por favor, introduce tu nombre.')
    print()
    Player[i]=input()
    print()
    time.sleep(1)
    print('Bienvenid@ '+ Player[i])
    print()

time.sleep(1)
print('Este es vuestro tablero')
time.sleep(1)

columns=random.randint(3,6)
tablero=[None]*columns

for i in range(columns):
    tablero[i]=random.randint(1,15)

juego = 1
turno = 1

while juego == 1:
    if turno == 1:
        pintaTablero(tablero)
        time.sleep(1)
        print('Es tu turno '+Player[0])
        time.sleep(1)
        fila=0
        while int(fila)<1 or int(fila)>(columns-1) or tablero[int(fila)-1]==0:
            print('¿De que fila querras recoger fichas?')
            fila=input()
            fila=int(float(fila)/1.0)
        numero=0
        while int(numero)<1 or int(numero)>tablero[int(fila)-1]:
            print('¿Cuantas fichas?')
            numero=input()
            numero=int(float(numero)/1.0)
        tablero[int(fila)-1] = tablero[int(fila)-1]-int(numero)
        tabla=tablero[:]
        x=tabla.pop()
        if sum(tabla) == 0:
            print('¡Has ganado '+Player[0]+'!')
            juego = 0
        else:
            turno = 0
    else:
        pintaTablero(tablero)
        time.sleep(1)
        print('Es tu turno '+Player[1])
        time.sleep(1)

        fila=0
        while int(fila)<1 or int(fila)>(columns-1) or tablero[int(fila)-1]==0:
            print('¿De que fila querras recoger fichas?')
            fila=input()
            fila=int(float(fila)/1.0)
        numero=0
        while int(numero)<1 or int(numero)>tablero[int(fila)-1]:
            print('¿Cuantas fichas?')
            numero=input()
            numero=int(float(numero)/1.0)
        tablero[int(fila)-1] = tablero[int(fila)-1]-int(numero)
        tabla=tablero[:]
        x=tabla.pop()
        if sum(tabla) == 0:
            print('¡Has ganado '+Player[1]+'!')
            juego = 0
        else:
            turno = 1
