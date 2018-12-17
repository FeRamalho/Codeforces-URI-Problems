###########################
## A Blend of Springtime ##
###########################


def main():
	flowers = input()
	aux = 0;

	for i in range(len(flowers)-2):
		if(flowers[i] == 'A' and flowers[i+1] == 'B' and flowers[i+2] == 'C'):
			print('Yes')
			aux = 1
			break
		elif(flowers[i] == 'A' and flowers[i+1] == 'C' and flowers[i+2] == 'B'):
			print('Yes')
			aux = 1
			break
		elif(flowers[i] == 'B' and flowers[i+1] == 'A' and flowers[i+2] == 'C'):
			print('Yes')
			aux = 1
			break
		elif(flowers[i] == 'B' and flowers[i+1] == 'C' and flowers[i+2] == 'A'):
			print('Yes')
			aux = 1
			break
		elif(flowers[i] == 'C' and flowers[i+1] == 'A' and flowers[i+2] == 'B'):
			print('Yes')
			aux = 1
			break
		elif(flowers[i] == 'C' and flowers[i+1] == 'B' and flowers[i+2] == 'A'):
			print('Yes')
			aux = 1
			break
	if(aux == 0):
		print('No')


if __name__ == "__main__":
	main()
