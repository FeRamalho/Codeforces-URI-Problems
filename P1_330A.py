#################
## Cakeminator ##
#################

def main():
	r,c = input().split(" ")
	cake = []
	eat = 0
	eliminate = []

	for i in range(int(r)):
		row = input()
		row = list(row)
		cake.append(row)

	for i in range(int(r)):
		evilstrwbr = 0
		for j in range(int(c)):
			if(cake[i][j] == 'S'):
				evilstrwbr += 1
		if(evilstrwbr == 0):
			eliminate.append(i)
	
	#eliminating rows
	while(len(eliminate) != 0):
		indice = eliminate.pop()
		del(cake[indice])
		eat = eat + int(c)
	if not cake:
		print(eat)
	else:
		for i in range(len(cake[0])):
			evilstrwbr = 0
			for j in range(len(cake)):
				if(cake[j][i] == 'S'):
					evilstrwbr += 1
			if(evilstrwbr == 0):
				eliminate.append(i) #collums

		#eliminating collumns
		while(len(eliminate) != 0):
			indice = eliminate.pop()
			for i in range(len(cake)):
				del(cake[i][indice])
			eat = eat + len(cake)

		print(eat)



if __name__ == "__main__":
	main()