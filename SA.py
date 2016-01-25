import string
import random
import math
import operator
import copy

def calculaEnergia(solucion):

    energia = 0
    for i in range(len(solucion)-1):
        energia = energia + (math.fabs(solucion[i][0] - solucion[i+1][0]) + math.fabs(solucion[i][1] - solucion[i+1][1]))
    energia = energia + (math.fabs(solucion[0][0] - solucion[len(solucion)-1][0]) + math.fabs(solucion[0][1] - solucion[len(solucion)-1][1]))
        
    return energia

def swap(solucion):

    solucionS = solucion

    while(True):
        idRandom1 = random.randint(0,len(solucion)-1)
        idRandom2 = random.randint(0,len(solucion)-1)
        if(idRandom1 != idRandom2):
            break

    aux = solucionS[idRandom1]
    solucionS[idRandom1] = solucionS[idRandom2]
    solucionS[idRandom2] = aux
    
    return solucionS

def generaSolucionArbitraria(solucion):

    solucionA = solucion
    random.shuffle(solucionA)
    return solucionA

print 'Simulated Annealing'
print 'Problema del agente viajero'
print ''

while(1):

    solucion = []
    n = int(raw_input('Ingresa el numero de coordenadas >> '))

    for i in range(n):
        print i
        x = int(raw_input('Coordenada x del punto ' + str(i) + '>> '))
        y = int(raw_input('Coordenada y del punto ' + str(i) + '>> '))
        coordenadas = [x,y]
        solucion.append(coordenadas)
        print('')

    T = float(raw_input('Ingresa la temperatura inicial >> '))
    N = int(raw_input('Ingresa el numero de intentos >> '))
    K = int(raw_input('Ingresa la K >> '))
    Tf = float(raw_input('Ingresa la temperatura final >> '))

    print('Coordenadas: ' + str(solucion))
    print('')

    solucion = generaSolucionArbitraria(solucion)
    energia = calculaEnergia(solucion)

    solucionInicial = copy.deepcopy(solucion)
    energiaInicial = energia

    print('Solucion Arbitraria: ' + str(solucion))
    print('Energia: ' + str(energia))
    print('')

    while(T > Tf):
        i = 0
        while(i < N):
            solucionNueva = swap(solucion)
            energiaNueva = calculaEnergia(solucion)
            if(energiaNueva <= energia):
                energia = energiaNueva
                solucion = solucionNueva
            else:
                aleatorio = random.random()
                probabilidad = math.exp(-(energiaNueva-energia)/(K*T))
                if(aleatorio < probabilidad):
                    energia = energiaNueva
                    solucion = solucionNueva
            print('Solucion nueva: ' + str(solucion))
            print('Energia nueva: ' + str(energia))
            i += 1
        T = T * 0.95
    print('')
    print('Solucion inicial: ' + str(solucionInicial))
    print('Energia inicial: ' + str(energiaInicial))
    print('--------------------------------')
    #energia = calculaEnergia(solucion)
    print('Solucion final: ' + str(solucion))
    print('Energia final: ' + str(energia))
    print('')
    if(raw_input('Desea empezar de nuevo (S/N) >> ') == 'N'):
        break
    print('')


    

    
