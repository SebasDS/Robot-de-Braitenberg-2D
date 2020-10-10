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

# Eje y:#0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22   #Eje x:
mapa = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #0
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #1
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #2
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #3
		[1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1], #4
		[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], #5
		[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], #6
		[1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], #7
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #8
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #9
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #10
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #11
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1], #12
		[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1], #13
		[1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1], #14
		[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1], #15
		[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1], #16
		[1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1], #17
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1], #18
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #19
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #20
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #21
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1], #22
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #23
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #24
		[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], #25
		[1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #26
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #27
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #28
		[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], #29
		[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #30
		]



#Ubicacion inicial del Robot:

xInicial = 2
yInicial = 21
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
		"Pmf":0.75,
		"Pmi":0.125,
		"Pmd":0.125,
		"Pmr":0
	},
	1: {
		"Pmf":0.5,
		"Pmi":0.5,
		"Pmd":0,
		"Pmr":0
	},
	2: {
		"Pmf":0,
		"Pmi":0.4,
		"Pmd":0.4,
		"Pmr":0.2
	},
	3: {
		"Pmf":0,
		"Pmi":0.75,
		"Pmd":0,
		"Pmr":0.25
	},
	4: {
		"Pmf":0.5,
		"Pmi":0,
		"Pmd":0.5,
		"Pmr":0
	},
	5: {
		"Pmf":0.75,
		"Pmi":0,
		"Pmd":0,
		"Pmr":0.25
	},
	6: {
		"Pmf":0,
		"Pmi":0,
		"Pmd":0.75,
		"Pmr":0.25
	},
	7: {
		"Pmf":0,
		"Pmi":0,
		"Pmd":0,
		"Pmr":1
	}
}




# Iteraciones -----------------------------------------------------------------------------------------------------
def loop(posicion, direccion_actual):
	while posicion != [28, 21]:
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

	left = mapa[pos[0]+index.get("izquierda")[0]][pos[1]+index.get("izquierda")[1]]
	front = mapa[pos[0]+index.get("frente")[0]][pos[1]+index.get("frente")[1]]
	right = mapa[pos[0]+index.get("derecha")[0]][pos[1]+index.get("derecha")[1]]

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

	return [x,y], direccion
	
	
loop(posicion, direccion_actual)

time.sleep(10)
	
	
