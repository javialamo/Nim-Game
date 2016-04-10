# NIM GAME v 1.3
# Javier del Álamo -=- 02/18/2013


import random
import time

def displayIntro():
    print()
    print()
    print('= NIM GAME =')
    time.sleep(1.5)
    print('Nim is a game for two players.')
    time.sleep(1.5)
    print('Played by turns, in each game ')
    time.sleep(1.5)
    print('will be a random rows number ')
    time.sleep(1.5)
    print('with a random tokens number.')
    time.sleep(1.5)
    print('In each turn, a player can pick ')
    time.sleep(1.5)
    print('any number of tokens from a single row.')
    time.sleep(1.5)
    print('The player who pick the last token is the winner.')
    time.sleep(1.5)
    print('Lets play!')
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
    print('Hi player '+str(i+1))
    time.sleep(1)
    print('Please, tell me your name.')
    print()
    Player[i]=input()
    print()
    time.sleep(1)
    print('Welcome '+ Player[i])
    print()

time.sleep(1)
print('This is your board')
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
        print('It's your turn '+Player[0])
        time.sleep(1)
        fila=0
        while int(fila)<1 or int(fila)>(columns-1) or tablero[int(fila)-1]==0:
            print('From what row do you wanna pick the tokens?')
            fila=input()
            fila=int(float(fila)/1.0)
        numero=0
        while int(numero)<1 or int(numero)>tablero[int(fila)-1]:
            print('How many tokens?')
            numero=input()
            numero=int(float(numero)/1.0)
        tablero[int(fila)-1] = tablero[int(fila)-1]-int(numero)
        tabla=tablero[:]
        x=tabla.pop()
        if sum(tabla) == 0:
            print('¡You win '+Player[0]+'!')
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
            print('From what row do you wanna pick the tokens?')
            fila=input()
            fila=int(float(fila)/1.0)
        numero=0
        while int(numero)<1 or int(numero)>tablero[int(fila)-1]:
            print('How many tokens?')
            numero=input()
            numero=int(float(numero)/1.0)
        tablero[int(fila)-1] = tablero[int(fila)-1]-int(numero)
        tabla=tablero[:]
        x=tabla.pop()
        if sum(tabla) == 0:
            print('You win '+Player[1]+'!')
            juego = 0
        else:
            turno = 1
