import time
import os
import random as rnd


def borrar ():
            if os.name == "posix":
                        os.system ("clear")
            elif os.name == "ce" or os.name == "nt" or os.name == "dos":
                        os.system ("cls")

# Muro = 1, Espacio = 0, Robot = X;
# mapa = [] #Pendiente por definir

# Eje y:#0  1  2  3  4  5  6  7  8  9 10 11 12 13 14  #Eje x:
mapa = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #0
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #1
	[1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #2
	[1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1], #3
	[1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1], #4
	[1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1], #5
	[1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1], #6
	[1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1], #7
	[1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1], #8
	[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1], #9
	[1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1], #10
	[1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1], #11
	[1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1], #12
	[1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1], #13
	[1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1], #14
	[1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1], #15
	[1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1], #16
	[1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1], #17
	[1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1], #18
	[1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1], #19
	[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #20
	]

#Ubicacion inicial del Robot:

xInicial = 2
yInicial = 12
posicion = [xInicial, yInicial]

#Orientacion inicial del Robot:

direcciones=["arriba", "derecha", "abajo", "izquierda"]
direccion_actual=0;

# Declaracion inicial de detectores

sense_index = {}
sense_left, sense_front, sense_right = 0, 0, 0

# Probabilidades de desplazamiento

Probabilidades_movimiento = {
	0: {
		"Pmf":0.2,
		"Pmi":0.2,
		"Pmd":0.55,
		"Pmr":0.05
	},
	1: {
		"Pmf":0.45,
		"Pmi":0.45,
		"Pmd":0.05,
		"Pmr":0.05
	},
	2: {
		"Pmf":0.05,
		"Pmi":0.2,
		"Pmd":0.65,
		"Pmr":0.1
	},
	3: {
		"Pmf":0.05,
		"Pmi":0.65,
		"Pmd":0.05,
		"Pmr":0.25
	},
	4: {
		"Pmf":0.25,
		"Pmi":0.05,
		"Pmd":0.65,
		"Pmr":0.05
	},
	5: {
		"Pmf":0.8,
		"Pmi":0.05,
		"Pmd":0.05,
		"Pmr":0.1
	},
	6: {
		"Pmf":0.05,
		"Pmi":0.05,
		"Pmd":0.8,
		"Pmr":0.1
	},
	7: {
		"Pmf":0.05,
		"Pmi":0.05,
		"Pmd":0.05,
		"Pmr":0.85
	}
}

# Iteraciones -----------------------------------------------------------------------------------------------------
def loop(posicion, direccion_actual):
	while posicion != [19, 12]:
		borrar()
		pintar_tablero(mapa, posicion, direcciones[direccion_actual])
		sense_index = actualizar_sense(direcciones[direccion_actual])
		sense_left, sense_front, sense_right = detectar_entorno(posicion, sense_index)
		movimiento_posibles = binaryToDecimalForChoose(sense_left, sense_front, sense_right, Probabilidades_movimiento)
		posicion, direccion_actual = mover_robot(movimiento_posibles, posicion, sense_index, direccion_actual)

		time.sleep(0.2)
	borrar()
	pintar_tablero(mapa, posicion, direcciones[direccion_actual])
	print('¡¡Prueba Completada!!')
#-----------------------------------------------------------------------------------------------------

#Dibuja el mapa en la consola
def pintar_tablero(mp, pos, direccion):
	n = len(mp)
	m = len(mp[0])
	print()
	for j in range (m):
	        for i in range (n):
	        	if (i==pos[0]) and (j==pos[1]):
	        	    if direccion=="arriba":
	        	        print ("^", end="")
	        	    elif direccion=="derecha":
	        	        print (">", end="")
	        	    elif direccion=="abajo":
	        	        print ("V", end="")
	        	    elif direccion=="izquierda":
	        	        print ("<", end="")
	        	    else:
	        	        print("?", end="")
	        	elif mp[i][j]==1:
	        	    print ("█", end="")
	        	else:
	        	    print (" ", end="")
	        print()

#Redefine las coordenadas relativas para el frente, atras y los lados del robot
def actualizar_sense(direccion):
	orientacion = {}
	if direccion == "arriba":
		orientacion = {
			"izquierda": [-1,0],
			"frente": [0,-1],
			"derecha": [1,0],
			"atras": [0,1]
		}
	elif direccion == "derecha":
		orientacion = {
			"izquierda": [0,-1],
			"frente": [1,0],
			"derecha": [0,1],
			"atras": [-1,0]
		}
	elif direccion == "abajo":
		orientacion = {
			"izquierda": [1,0],
			"frente": [0,1],
			"derecha": [-1,0],
			"atras": [0,-1]
		}
	elif direccion == "izquierda":
		orientacion = {
			"izquierda": [0,1],
			"frente": [-1,0],
			"derecha": [0,-1],
			"atras": [1,0]
		}
	else:
		print('Error en la Orientacion')

	return orientacion

#Lectura y deteccion del entorno del robot
def detectar_entorno(pos, index):
	n=len(mapa)
	m=len(mapa[0])

	left = mapa[(pos[0]+index.get("izquierda")[0])%n][(pos[1]+index.get("izquierda")[1])%m]
	front = mapa[(pos[0]+index.get("frente")[0])%n][(pos[1]+index.get("frente")[1])%m]
	right = mapa[(pos[0]+index.get("derecha")[0])%n][(pos[1]+index.get("derecha")[1])%m]

	return left, front, right

#Conversion de Binarios sensados en el mapa left+front+right para escoger probabilidades
def binaryToDecimalForChoose(l, f, r, tabla_Pm):

	if (l+f+r) == 0: #Correccion para el caso 000
		decimal = 0 
	else:
		decimal = pow(l*2, 2)+pow(f*2, 1)+pow(r*2, 0)

	return tabla_Pm.get(decimal)

# Traslacion y rotacion del robot en la matriz
def mover_robot(P, pos, index, way):
	direccion = 0;
	move=rnd.random()

	n=len(mapa)
	m=len(mapa[0])

	Pmf = P.get("Pmf")
	Pmi = P.get("Pmi")
	Pmd = P.get("Pmd")
	Pmr = P.get("Pmr")

	idx_i = index.get("izquierda")
	idx_f = index.get("frente")
	idx_d = index.get("derecha")
	idx_a = index.get("atras")

	if move<=Pmr:
		x = pos[0]+idx_a[0]
		y = pos[1]+idx_a[1]
		direccion = (way+2)%4
	elif (move<=(Pmr+Pmd)) and (move>Pmr):
		x = pos[0]+idx_d[0]
		y = pos[1]+idx_d[1]
		direccion = (way+1)%4
	elif (move<=(Pmr+Pmd+Pmi)) and (move>(Pmr+Pmd)):
		x = pos[0]+idx_i[0]
		y = pos[1]+idx_i[1]
		direccion = (way+3)%4
	elif (move<=(Pmr+Pmd+Pmi+Pmf)) and (move>(Pmr+Pmd+Pmi)):
		x = pos[0]+idx_f[0]
		y = pos[1]+idx_f[1]
		direccion = way
	else:
		print('Algo salio mal moviendo el robot')

	return [x%n,y%m], direccion	
	
loop(posicion, direccion_actual)

time.sleep(10)
