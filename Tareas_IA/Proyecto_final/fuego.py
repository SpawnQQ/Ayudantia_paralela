import random

def llenar_hectarea(cantidad_combustible):
	hectarea=[None]* cantidad_combustible
	for i in range(cantidad_combustible):
		hectarea[i]="Disponible"
	return hectarea
def velocidad_prop(material_comb, potencial_viento,humedad_relativa):
	vel=material_comb*potencial_viento/humedad_relativa
	return vel

ii = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0] # probabilidad inicial incendio inicial	
prbav = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1] #probabilidad del avion inicial
ib = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0] # probabilidad inicial carro bomba
ica = [1, 1, 1, 1, 0, 0, 0, 0, 0, 0] # probabilidad camion agua
epi = [1, 0, 0] # probabilidad camion agua
#def propag_tmpo()

incendio_inicial = random.choice(ii)
estado_inicial = random.randint(1,50) #hectareas iniciales totales
combustible = random.randint (1,50 ) #hectareas disponibles

recurso = [None] * 6
recurso [0] = ["Grifo", 1, 20, 0, 1]
aux = random.randint (1,2)
recurso [1] = ["Extintor", 0.5, 1, 10, aux]
aux2 = random.choice(prbav)
recurso [2] = ["Avion", 10, 15, 20, aux2]
aux3 = random.choice(ib)
recurso [3] = ["Carro Bomba", 5, 50, 30, aux3]
aux4 = random.choice(ica)
recurso [4] = ["Camion con agua", 4, 60, 60, aux4]
aux5 = random.choice(epi)
recurso [5] = ["Espuma para incendios", 5, 30, 50, aux5]

tiempo=0

material_comb = random.randint(3,6)
potencial_viento = random.randint (2,5)
humedad_relativa = random.randint (1,4)

velocidad=random.randint(1,4)
# son 15 min para propagarse, la velocidad de 1 a 6 hectareas 


cantidad_combustible=5
hectarea=llenar_hectarea(cantidad_combustible)

vel = velocidad_prop(material_comb, potencial_viento, humedad_relativa)

print recurso

for i in range (combustible):
	if incendio_inicial==1:
		if estado_inicial>0:
			print "Hectareas danhadas", estado_inicial
			print "Incendio"
			for j in range(5):
				if recurso[j][-1]>0:
					print "Recurso", recurso[j][0]
					estado_inicial=estado_inicial-recurso[j][1]
					recurso[j][-1]=recurso[j][-1]-1
					tiempo=tiempo+recurso[j][2]
			
			tiempo=tiempo/15
			estado_inicial=velocidad*tiempo + estado_inicial
			tiempo=0		
			print estado_inicial
		else:
			print "Incendio amagado", estado_inicial			
	else:
		print "Fuera de peligro"			



#print vel
#print hectarea
#print recurso[0]
#print recurso