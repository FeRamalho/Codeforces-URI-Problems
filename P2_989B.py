##########################
## A Tide of Riverscape ##
##########################

def main():
	n,p = input().split(" ")
	s = input()
	n = int(n)
	p = int(p)
	aux = 0
	
	menor = []
	maior = []
	for i in range(n-p):
		menor.append(i+1)
		maior.append(i+1+p)

	for i in range(len(menor)):
		if(s[menor[i]-1] == '.' and s[maior[i]-1] != '.'):
			if(s[maior[i]-1] == '0'):
				print(s.replace('.','1'))
			else:
				print(s.replace('.','0'))
			aux = 1
			break
		elif(s[menor[i]-1] != '.' and s[maior[i]-1] == '.'):
			if(s[menor[i]-1] == '0'):
				print(s.replace('.','1'))
			else:
				print(s.replace('.','0'))
			aux = 1
			break
		elif(s[menor[i]-1] == '.' and s[maior[i]-1] == '.'):
			novo = list(s)
			novo[menor[i]-1] = '0'
			s = ''.join(novo)
			print(s.replace('.','1'))
			aux = 1
			break
		elif(s[menor[i]-1] != s[maior[i]-1]):
			print(s.replace('.','0'))
			aux = 1
			break


	if(aux == 0):
		print("No")

if __name__ == "__main__":
	main()