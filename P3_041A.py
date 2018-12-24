#################
## Translation ##
#################

def main():
	s = input()
	t = input()
	aux = 0

	sLen = len(s)
	tLen = len(t)

	if(sLen != tLen):
		print("NO")
	else:
		for i in range(sLen):
			if(s[i] != t[sLen-1-i]):
				print("NO")
				aux = 0
				break
			else:
				aux = 1
	if(aux == 1):
		print("YES")


if __name__ == "__main__":
	main()