"""
agente.py

criar aqui as funções que respondem às perguntas
e quaisquer outras que achem necessário criar

colocar aqui os nomes e número de aluno:
45500, Manuel Garcia
46033, Diogo Pires

"""

import time
import math
import networkx as nx;
import numpy as np;
from scipy.optimize import curve_fit, fsolve
import matplotlib.pyplot as plt


stack = []
lstHomens = [['operário_Paulo'],['visitante_Ricardo'],['operário_Adérito'],
			 ['operário_Rui'],['operário_Miguel'],['visitante_Joaquim'],
			 ['supervisor_Carlos']]
			 
def decimalParaMinutosSegundo(numero):
	segundos , minutos = math.modf(numero)
	segundos *= 60
	return "",minutos,"minutos ",segundos,"segundos"



#Exercicio 3
zona_empacotamento = ['zona_empacotamento']

G = nx.Graph()


G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(1,5)
G.add_edge(2,6)
G.add_edge(2,7)
G.add_edge(3,4)
G.add_edge(3,12)
G.add_edge(3,13)
G.add_edge(3,14)
G.add_edge(4,8)
G.add_edge(4,9)
G.add_edge(4,10)
G.add_edge(4,11)

#Exercicio1
nomes_masculinos = ['Miguel', 'João', 'Manuel', 'António', 'Francisco', 'Pedro', 'Paulo', 'André', 'Luís', 'Carlos',
    'José', 'Rui', 'Fernando', 'Jorge', 'Bruno', 'Ricardo', 'Nuno', 'Tiago', 'Daniel', 'David',
    'Sérgio', 'Vasco', 'Gonçalo', 'Ruben', 'Diogo', 'Filipe', 'Rafael', 'Duarte', 'Mário', 'Eduardo',
    'Hélder', 'Gabriel', 'Victor', 'Abel', 'Marcelo', 'Bernardo', 'Artur', 'Leonel', 'Álvaro', 'Armando',
    'Afonso', 'Xavier', 'Tomás', 'Simão', 'Henrique', 'Adriano', 'Renato', 'Elias', 'Agostinho', 'Lucas',
    'Renato', 'Óscar', 'Nelson', 'Adérito', 'Hugo', 'Gilberto', 'Baltazar', 'Bernardo', 'Caetano', 'Dinis', 'Fábio',
    'Humberto', 'Igor', 'Jacinto', 'Lino', 'Milton', 'Natanael', 'Octávio', 'Prudêncio', 'Quirino', 'Rolando',
    'Salvador', 'Teodoro', 'Urbano', 'Valdemar', 'Xavier', 'Zacarias', 'Bento',
    'Cristiano', 'Dário', 'Fausto', 'Gil', 'Horácio', 'Ícaro', 'Joaquim', 'Kevin', 'Leandro',
    'Marco', 'Norberto', 'Óscar', 'Quim', 'Rogério', 'Sandro', 'Telmo', 'Virgílio', 'Guilherme']

#Exercicio2

lista_obj = []

areas = {}

areas_a_adicionar = [{"nome" : "Zona 1", "coordenadas_x_y": [29 ,136, 164, 381]},
{"nome" : "Zona 2", "coordenadas_x_y": [135, 486, 164, 186]},
{"nome" : "Zona 3", "coordenadas_x_y": [29, 635, 379, 436]},
{"nome" : "Zona 4", "coordenadas_x_y": [529, 636, 184, 436]},
{"nome" : "Zona 5", "coordenadas_x_y": [29, 136, 29, 165]},
{"nome" : "Zona 6", "coordenadas_x_y": [179, 286, 29, 165]},
{"nome" : "Zona 7", "coordenadas_x_y": [329, 486, 29, 165]},
{"nome" : "Zona 8", "coordenadas_x_y": [529, 771, 29, 185]},
{"nome" : "Zona 9", "coordenadas_x_y": [635, 771, 229, 286]},
{"nome" : "Zona 10", "coordenadas_x_y": [635, 771, 329, 386]},
{"nome" : "Zona 11_1", "coordenadas_x_y": [529, 771, 435, 571]},
{"nome" : "Zona 11_2", "coordenadas_x_y": [635, 771, 429, 436]},
{"nome" : "Zona 12", "coordenadas_x_y": [329, 486, 435, 571]},
{"nome" : "Zona 13", "coordenadas_x_y": [179, 286, 435, 571]},
{"nome" : "Zona 14", "coordenadas_x_y": [29, 136, 435, 571]},
{"nome" : "Zona 15", "coordenadas_x_y": [135, 486, 229, 336]}] 


for area in areas_a_adicionar:
	nome_area = area["nome"]
	coordenadas_area = area["coordenadas_x_y"]
	areas[nome_area] = coordenadas_area
	
areas_tmp = [{"nome" : "Zona 1", "zona_correspondente" : "corredor"},
{"nome" : "Zona 2", "zona_correspondente" : "corredor"},
{"nome" : "Zona 3", "zona_correspondente" : "corredor"},
{"nome" : "Zona 4", "zona_correspondente" : "corredor"},
{"nome" : "Zona 10", "zona_correspondente" : "zona_inicial"}

]

areas_predefinidas = {}


for area in areas_tmp:
	nome_area = area["nome"]
	area_pre = area["zona_correspondente"]
	areas_predefinidas[nome_area] = area_pre
	
x_global = 0
y_global = 0


lista_pessoas = []


class Zona:
	def __init__(self,xesquerda,xdireita,ycima,ybaixo,numero_da_zona):
		self.xesquerda = xesquerda
		self.ycima = ycima
		self.xdireita = xdireita
		self.ybaixo = ybaixo
		self.numero_da_zona = numero_da_zona
		
	def esta_na_zona(self, lista):
		
		if lista[0] >= self.xesquerda and lista[0] <= self.xdireita and lista[1] >= self.ycima and lista[1] <= self.ybaixo:
			return self.numero_da_zona
	
zona_empacotamento_area= None	


zona0 = Zona(136,510,186,344,0)
zona1 = Zona(30,135,165,345,1)
zona2 = Zona(136,485,165,185,2)
zona3 = Zona(30,510,346,435,3)
zona4 = Zona(511,635,185,440,4)
zona5 = Zona(30,135,30,164,5)
zona6 = Zona(180,285,30,164,6)
zona7 = Zona(330,485,30,164,7)
zona8 = Zona(530,770,30,184,8)
zona9 = Zona(636,770,230,285,9)
zona10 = Zona(635,770,330,385,10)
zona11a = Zona(530,635,441,570,11)
zona11b = Zona(636,770,430,570,11)
zona12 = Zona(330,485,436,570,12)
zona13 = Zona(180,285,436,570,13)
zona14 = Zona(30,135,436,570,14)

pos_atual = []

#Exercicio 4

zona_laboratorio = ['zona_laboratório']
coordenadasLab = None


def distancia_entre_pontos( pontoA, pontoB):
	x1, y1 = pontoA
	x2, y2 = pontoB
	return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))

PassCent = nx.Graph()

c0 = (305, 285)
p0_1 = (135, 285)
c1 = (80,255)
p1_2 = (135, 170)
p1_3 = (80, 345)
p1_5 = (80,165)
c2 = (310, 175)
p2_6 = (230, 165)
p2_7 = (405, 165)
c3 = (270, 390)
p3_4 = (510, 340)
p3_12 = (405, 435)
p3_13 = (230, 435)
p3_14 = (80, 435)
c4 = (570, 310)
p4_8 = (570, 185)
p4_9 = (635, 255)
p4_10 = (635, 355)
p4_11 = (580, 440)
c5 = (80, 95)
c6 = (230, 95)
c7 = (405, 95)
c8 = (650, 105)
c9 = (700, 255)
c10 = (700, 355)
c11 = (650, 505)
c12 = (405, 500)
c13 = (230, 500)
c14 = (80, 500)


PassCent.add_edge(c0,p0_1,weight =distancia_entre_pontos(c0,p0_1))
PassCent.add_edge(c1,p0_1,weight =distancia_entre_pontos(c1,p0_1))
PassCent.add_edge(c1,p1_2,weight =distancia_entre_pontos(c1,p1_2))
PassCent.add_edge(c1,p1_3,weight =distancia_entre_pontos(c1,p1_3))
PassCent.add_edge(c1,p1_5,weight =distancia_entre_pontos(c1,p1_5))
PassCent.add_edge(c2,p1_2,weight =distancia_entre_pontos(c2,p1_2))
PassCent.add_edge(c2,p2_6,weight =distancia_entre_pontos(c2,p2_6))
PassCent.add_edge(c2,p2_7,weight =distancia_entre_pontos(c2,p2_7))
PassCent.add_edge(c3,p1_3,weight =distancia_entre_pontos(c3,p1_3))
PassCent.add_edge(c3,p3_4,weight =distancia_entre_pontos(c3,p3_4))
PassCent.add_edge(c3,p3_12,weight =distancia_entre_pontos(c3,p3_12))
PassCent.add_edge(c3,p3_13,weight =distancia_entre_pontos(c3,p3_13))
PassCent.add_edge(c3,p3_14,weight =distancia_entre_pontos(c3,p3_14))
PassCent.add_edge(c4,p3_4,weight =distancia_entre_pontos(c3,p3_4))
PassCent.add_edge(c4,p4_8,weight =distancia_entre_pontos(c4,p4_8))
PassCent.add_edge(c4,p4_9,weight =distancia_entre_pontos(c4,p4_9))
PassCent.add_edge(c4,p4_10,weight =distancia_entre_pontos(c4,p4_10))
PassCent.add_edge(c4,p4_11,weight =distancia_entre_pontos(c4,p4_11))
PassCent.add_edge(c5,p1_5,weight =distancia_entre_pontos(c5,p1_5))
PassCent.add_edge(c6,p2_6,weight =distancia_entre_pontos(c6,p2_6))
PassCent.add_edge(c7,p2_7,weight =distancia_entre_pontos(c7,p2_7))
PassCent.add_edge(c8,p4_8,weight =distancia_entre_pontos(c8,p4_8))
PassCent.add_edge(c9,p4_9,weight =distancia_entre_pontos(c9,p4_9))
PassCent.add_edge(c10,p4_10,weight =distancia_entre_pontos(c10,p4_10))
PassCent.add_edge(c11,p4_11,weight =distancia_entre_pontos(c11,p4_11))
PassCent.add_edge(c12,p3_12,weight =distancia_entre_pontos(c12,p3_12))
PassCent.add_edge(c13,p3_13,weight =distancia_entre_pontos(c13,p3_13))
PassCent.add_edge(c14,p3_14,weight =distancia_entre_pontos(c14,p3_14))
PassCent.add_edge(p3_14,p1_3,weight =distancia_entre_pontos(p3_14, p1_3))
PassCent.add_edge(p1_5,p1_2,weight= distancia_entre_pontos(p1_5,p1_2))
PassCent.add_edge(p4_11,p3_4,weight= distancia_entre_pontos(p4_11,p3_4))
PassCent.add_edge(p4_8,p4_9,weight= distancia_entre_pontos(p4_8,p4_9))
PassCent.add_edge(p4_10,p4_11,weight = distancia_entre_pontos(p4_10,p4_11))


zona_laboratorio_area = None

#Exercicio 5

zona_escritorio = ['zona_escritório']
coordenadasEsc = None

velocidade_mts_p_seg = 225

xi = None
yi = None
start_timeS = None


#Exercicio 6 

time_atual = None
array_teste = np.arange(100)
vd = [0.0]
vida = None
vi = [0.0] 
bateria_atual = None
start_time = None
time_anterior = None
bateria_anterior = 100.0
estimated = None

def tent_5(x, a, b, c, d):
	return  np.log(a) - b * x + c * np.log(d * x + 1)
	#return  np.log(a) - b * x





def work(posicao, bateria, objetos):
    # esta função é invocada em cada ciclo de clock
    # e pode servir para armazenar informação recolhida pelo agente
    # recebe:
    # posicao = a posição atual do agente, uma lista [X,Y]
    # bateria = valor de energia na bateria, um número inteiro >= 0
    # objetos = o nome do(s) objeto(s) próximos do agente, uma string
    
    #pergunta 1 - adiciona os objetos pelos quais o robo passa à lista lista_obj
	if len(objetos) != 0:
		for obj in objetos:
			if len(lista_obj) == 0:
				lista_obj.append(obj)
			elif obj != lista_obj[-1]:
				lista_obj.append(obj)
    
    #pergunta 2 - faz corresponder no dicionario areas_predefinidas os objetos que sejam zonas ou armazens a um numero de zona numérico através da sua posiçao no mundo
	for obj in objetos:
		if "zona" in obj or "armazém" in obj:
			x, y = posicao
			for chave, valor in areas.items():
				x1, x2, y1, y2 = valor
				if (x > x1 and x < x2) and (y > y1 and y < y2):
					if chave == "Zona 11_1" or chave == "Zona 11_2":
						areas_predefinidas["Zona 11_1"] = obj
						areas_predefinidas["Zona 11_2"] = obj
					else:
						areas_predefinidas[chave] = obj
	
	#guarda a posição atual do robo nas variáveis globais x_gloval e y_global
	global x_global
	global y_global
	x_global, y_global = posicao
    
    #pergunta 7 - adiciona todas as pessoas que encontra independentemente da sua função, e adiciona-as à çista lista_pessoas caso ainda não existam na lista
	for obj in objetos:
		if("operário" in obj or "visitante" in obj or "supervisor" in obj) and obj not in lista_pessoas:
			lista_pessoas.append(obj)
		
    
    
    
    
    
	global vida
	global pos_atual
	global zona_empacotamento_area
	global coordenadasLab
	global coordenadasEsc
	global empty_array
	global array_certo
	global bateria_atual
	global bateria_posterior
	global start_time
	global time_anterior
	global time_atual
	global xi
	global yi
	global start_timeS
	global vd
	global vi
	global vdA
	global vdI
	global estimated
	global bateria_anterior
	
	vida = int(bateria)
	#global lista_tempo_dez_por_cento
	#global vida
	pos_atual = posicao
	vida = bateria
	
	if objetos != None:
		stack.append(objetos)
		if objetos == zona_empacotamento:
			if zona0.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona0.esta_na_zona(pos_atual)
			if zona1.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona1.esta_na_zona(pos_atual)
			if zona2.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona2.esta_na_zona(pos_atual)
			if zona3.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona3.esta_na_zona(pos_atual)
			if zona4.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona4.esta_na_zona(pos_atual)
			if zona5.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona5.esta_na_zona(pos_atual)
			if zona6.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona6.esta_na_zona(pos_atual)
			if zona7.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona7.esta_na_zona(pos_atual)
			if zona8.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona8.esta_na_zona(pos_atual)
			if zona9.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona9.esta_na_zona(pos_atual)
			if zona10.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona10.esta_na_zona(pos_atual)
			if zona11a.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona11a.esta_na_zona(pos_atual)
			if zona11b.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona11b.esta_na_zona(pos_atual)
			if zona12.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona12.esta_na_zona(pos_atual)
			if zona13.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona13.esta_na_zona(pos_atual)
			if zona14.esta_na_zona(pos_atual) is not None:
				zona_empacotamento_area = zona14.esta_na_zona(pos_atual)
		if objetos == zona_laboratorio:
			if zona0.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c0
			if zona5.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c5
			if zona6.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c6
			if zona7.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c7
			if zona8.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c8
			if zona9.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c9
			if zona10.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c10
			if zona11a.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c11
			if zona11b.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c11
			if zona12.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c12
			if zona13.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c13
			if zona14.esta_na_zona(pos_atual) is not None:
				coordenadasLab = c14
				
		if objetos == zona_escritorio:
			if zona0.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c0
			if zona5.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c5
			if zona6.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c6
			if zona7.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c7
			if zona8.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c8
			if zona9.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c9
			if zona10.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c10
			if zona11a.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c11
			if zona11b.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c11
			if zona12.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c12
			if zona13.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c13
			if zona14.esta_na_zona(pos_atual) is not None:
				coordenadasEsc = c14
		
	if bateria_atual is None:
		bateria_atual	= float(bateria)
	else:
		bateria_anterior = float(bateria_atual)
		bateria_atual = float(bateria)
	
	if time_atual is None:
		time_atual = time.time() 
		start_time = float(time_atual)
	else:
		time_anterior = float(time_atual)
		time_atual = time.time()
	if bateria_atual < bateria_anterior:
		elapsed_time = time_atual - time_anterior
		vd.append(elapsed_time + vd[-1])
		vi.append(vi[-1] + bateria_anterior - bateria_atual)
		
			
			
			 
		
		
	
	
	
	
	#print(posicao)
	
	
	#Para achar a velocidade maxima
	start_timeS = time.time() if  start_timeS == None else start_timeS
		
		
	
	current_timeS= time.time()
	elapsed_timeS = current_timeS - start_timeS
	if elapsed_timeS < 0.1:
		xi = posicao[0]
		yi = posicao[1]
	if elapsed_timeS >= 1:
		#print("Speed = ", math.sqrt(math.pow(posicao[0] - xi, 2) + math.pow(posicao[1] - yi,2) ))
		start_timeS = time.time()
	
	
	
	
	
	
	
    # podem achar o tempo atual usando, p.ex.
    # time.time()
    

def resp1():
	count = 0
	nome = ''
	for i in range(len(lista_obj)-1,-1,-1):
		for elemento in nomes_masculinos:
			if elemento in lista_obj[i] and lista_obj[i] != lista_obj[i-1]:
				if count == 1:
					nome = lista_obj[i]
				count = count + 1
	
	print(nome)
	
    

def resp2():
	global x_global
	global y_global
	
	zona_atual = ''
	for chave, valor in areas.items():
		x1,x2,y1,y2 = valor
		if(x_global > x1 and x_global < x2) and (y_global > y1 and y_global < y2):
			zona_atual = chave
		
	if zona_atual in areas_predefinidas:
		for chave, valor in areas_predefinidas.items():
			if chave == zona_atual:
				if "corredor" in valor or "armazém" in valor:
					print(f"Estou no {valor}")
				elif "zona" in valor:
					print(f"Estou na {valor}")
	else:
		print("Não sei onde estou!!")
						
	
	
	
	
	
def resp3():	
	partida = None
	global pos_atual
	global zona_empacotamento_area
	if zona_empacotamento_area is None:
		print('Ainda não aí passámos')
		return None
	if zona0.esta_na_zona(pos_atual) is not None:
		partida = zona0.esta_na_zona(pos_atual)
	if zona1.esta_na_zona(pos_atual) is not None:
		partida = zona1.esta_na_zona(pos_atual)
	if zona2.esta_na_zona(pos_atual) is not None:
		partida = zona2.esta_na_zona(pos_atual)
	if zona3.esta_na_zona(pos_atual) is not None:
		partida = zona3.esta_na_zona(pos_atual)
	if zona4.esta_na_zona(pos_atual) is not None:
		partida = zona4.esta_na_zona(pos_atual)
	if zona5.esta_na_zona(pos_atual) is not None:
		partida = zona5.esta_na_zona(pos_atual)
	if zona6.esta_na_zona(pos_atual) is not None:
		partida = zona6.esta_na_zona(pos_atual)
	if zona7.esta_na_zona(pos_atual) is not None:
		partida = zona7.esta_na_zona(pos_atual)
	if zona8.esta_na_zona(pos_atual) is not None:
		partida = zona8.esta_na_zona(pos_atual)
	if zona9.esta_na_zona(pos_atual) is not None:
		partida = zona9.esta_na_zona(pos_atual)
	if zona10.esta_na_zona(pos_atual) is not None:
		partida = zona10.esta_na_zona(pos_atual)
	if zona11a.esta_na_zona(pos_atual) is not None:
		partida = zona11a.esta_na_zona(pos_atual)
	if zona11b.esta_na_zona(pos_atual) is not None:
		partida = zona11b.esta_na_zona(pos_atual)
	if zona12.esta_na_zona(pos_atual) is not None:
		partida = zona12.esta_na_zona(pos_atual)
	if zona13.esta_na_zona(pos_atual) is not None:
		partida = zona13.esta_na_zona(pos_atual)
	if zona14.esta_na_zona(pos_atual) is not None:
		partida = zona14.esta_na_zona(pos_atual)
	
	start_node = partida
	lista = list(nx.bfs_edges(G, source = start_node))
	caminho = []
	
	destino = zona_empacotamento_area
	ultimo = None
	atual = destino
	iterator = 0
	while (atual != partida):
		nodo1, nodo2 = lista[iterator]
		if (nodo1 == atual or nodo2 == atual) and \
		(nodo1 not in caminho or nodo2 not in caminho) and \
		ultimo != lista[iterator] :
			if atual not in caminho:
				caminho.append(atual)
				ultimo= lista[iterator]
				iterator = -1
			if nodo1 == atual and nodo2 not in caminho:
				atual = nodo2
			else:
				if nodo1 not in caminho:
					atual = nodo1
					
		iterator+=1
		
		
	caminho.append(atual)
	caminho.reverse()
	
	print(caminho)
    

def resp4():
	partida = None
	global pos_atual
	global zona_laboratorio
	global coordenadasLab
	if coordenadasLab is None:
		print('Ainda não aí passámos!')
		return None
	if zona0.esta_na_zona(pos_atual) is not None:
		partida = c0
	if zona1.esta_na_zona(pos_atual) is not None:
		partida = c1
	if zona2.esta_na_zona(pos_atual) is not None:
		partida = c2
	if zona3.esta_na_zona(pos_atual) is not None:
		partida = c3
	if zona4.esta_na_zona(pos_atual) is not None:
		partida = c4
	if zona5.esta_na_zona(pos_atual) is not None:
		partida = c5
	if zona6.esta_na_zona(pos_atual) is not None:
		partida = c6
	if zona7.esta_na_zona(pos_atual) is not None:
		partida = c7
	if zona8.esta_na_zona(pos_atual) is not None:
		partida = c8
	if zona9.esta_na_zona(pos_atual) is not None:
		partida = c9
	if zona10.esta_na_zona(pos_atual) is not None:
		partida = c10
	if zona11a.esta_na_zona(pos_atual) is not None:
		partida = c11
	if zona11b.esta_na_zona(pos_atual) is not None:
		partida = c11
	if zona12.esta_na_zona(pos_atual) is not None:
		partida = c12
	if zona13.esta_na_zona(pos_atual) is not None:
		partida = c13
	if zona14.esta_na_zona(pos_atual) is not None:
		partida = c14
	
	start_node = partida
	lista = list(nx.bfs_edges(PassCent, source = start_node))
	caminho = []
	
	destino = coordenadasLab
	ultimo = None
	atual = destino
	iterator = 0
	while (atual != partida):
		nodo1, nodo2 = lista[iterator]
		if (nodo1 == atual or nodo2 == atual) and \
		(nodo1 not in caminho or nodo2 not in caminho) and \
		ultimo != lista[iterator] :
			if atual not in caminho:
				caminho.append(atual)
				ultimo= lista[iterator]
				iterator = -1
			if nodo1 == atual and nodo2 not in caminho:
				atual = nodo2
			else:
				if nodo1 not in caminho:
					atual = nodo1
					
		iterator+=1
		
		
	caminho.append(atual)
	caminho.reverse()
	
	distancia = 0
	for i in range( len(caminho)- 1 ):
		for node in PassCent.edges(data = True) :
			node1, node2, atributos = node
			if(caminho[i] == node1 and caminho[i+1] == node2) or \
			(caminho[i] == node2 and caminho[i +1] == node1) :
				weight = atributos.get("weight", 0)
				distancia += weight
				break
	print(distancia)
	print(caminho)

def resp5():
	partida = None
	global pos_atual
	global zona_escritorio
	global coordenadasEsc
	
	if coordenadasEsc is None:
		print('Ainda não aí passámos!')
		return None
	if zona0.esta_na_zona(pos_atual) is not None:
		partida = c0
	if zona1.esta_na_zona(pos_atual) is not None:
		partida = c1
	if zona2.esta_na_zona(pos_atual) is not None:
		partida = c2
	if zona3.esta_na_zona(pos_atual) is not None:
		partida = c3
	if zona4.esta_na_zona(pos_atual) is not None:
		partida = c4
	if zona5.esta_na_zona(pos_atual) is not None:
		partida = c5
	if zona6.esta_na_zona(pos_atual) is not None:
		partida = c6
	if zona7.esta_na_zona(pos_atual) is not None:
		partida = c7
	if zona8.esta_na_zona(pos_atual) is not None:
		partida = c8
	if zona9.esta_na_zona(pos_atual) is not None:
		partida = c9
	if zona10.esta_na_zona(pos_atual) is not None:
		partida = c10
	if zona11a.esta_na_zona(pos_atual) is not None:
		partida = c11
	if zona11b.esta_na_zona(pos_atual) is not None:
		partida = c11
	if zona12.esta_na_zona(pos_atual) is not None:
		partida = c12
	if zona13.esta_na_zona(pos_atual) is not None:
		partida = c13
	if zona14.esta_na_zona(pos_atual) is not None:
		partida = c14
	
	start_node = partida
	lista = list(nx.bfs_edges(PassCent, source = start_node))
	caminho = []
	
	destino = coordenadasEsc
	ultimo = None
	atual = destino
	iterator = 0
	while (atual != partida):
		nodo1, nodo2 = lista[iterator]
		if (nodo1 == atual or nodo2 == atual) and \
		(nodo1 not in caminho or nodo2 not in caminho) and \
		ultimo != lista[iterator] :
			if atual not in caminho:
				caminho.append(atual)
				ultimo= lista[iterator]
				iterator = -1
			if nodo1 == atual and nodo2 not in caminho:
				atual = nodo2
			else:
				if nodo1 not in caminho:
					atual = nodo1
					
		iterator+=1
		
		
	caminho.append(atual)
	caminho.reverse()
	
	distancia = 0
	for i in range( len(caminho)  -1 ):
		for node in PassCent.edges(data = True) :
			node1, node2, atributos = node
			if(caminho[i] == node1 and caminho[i+1] == node2) or \
			(caminho[i] == node2 and caminho[i +1] == node1) :
				weight = atributos.get("weight", 0)
				distancia += weight
				break
	print((distancia/velocidade_mts_p_seg),'segundos')

	
def resp6():

	
	
	global vida
	global estimated
	print(len(vd)== len(vi))
	x = np.array(vd) 
	y = np.array(vi)
	param, cov = curve_fit(tent_5, np.array(vd), np.array(vi),maxfev=1_000_000)
	a, b, c, d = param
	y_fit = tent_5(x,a,b,c,d)
	plt.scatter(vd,vi,label="original_data", color= "orange")
	plt.plot(x,y_fit,label="fit",color="black")
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.legend()
	plt.savefig("test1.png")
	
	root = fsolve(lambda x : np.log(a) - b * x + c* np.log(d * x + 1) -100  ,100)#return  np.log(a) - b * x
	estimated = root[0] - (time_atual)
	out_phrase = f"Faltam cerca de {round(root[0]- (time_atual - start_time), 1)} segundos" if vida != 0 else "Bateria acabou"
	print(out_phrase)

def resp7():
	prob_inicial = 1/3
	n_total_pessoas = 0
	n_supervisores = 0
	
	if len(lista_pessoas) == 0:
		print("A probabilidade de a proxima pessoa ser um supervisor é de {:.2f}".format(prob_inicial))
		return
	else:
		for pessoa in lista_pessoas:
			n_total_pessoas += 1
			if "supervisor" in pessoa:
				n_supervisores += 1
	
	prob_supervisor = n_supervisores /n_total_pessoas
	print("A probabilidade de a próxima pessoa ser um supervisor é de {:.2f}".format(prob_supervisor))

def resp8():
	n_zonas = 15
	n_operarios = 0
	n_maquinas = 0
	n_supervisor = 0
	n_total_pessoas = 0
    
	for elemento in lista_obj:
		if "máquina" in elemento:
			n_maquinas += 1
			
	for elemento in lista_pessoas:
		n_total_pessoas += 1 
		if "operário" in elemento:
			n_operarios += 1
		elif "supervisor" in elemento:
			n_supervisor += 1
			
	prob_maquina = n_maquinas / n_zonas
	prob_operario = n_operarios / n_total_pessoas
	prob_neg_supervisor =  1 -(n_supervisor / n_total_pessoas)
	
	prob_cima = prob_maquina * prob_operario * prob_neg_supervisor
	prob_baixo = prob_maquina * prob_neg_supervisor
	
	prob_final = prob_cima / prob_baixo
	
	print("{:.3f}".format(prob_final))
