###############################
## Little Elephant and Chess ##
###############################

def main():
	board = []
	checkNo = 0

	for i in range(8):
		row = input()
		row = list(row)
		board.append(row)

	for i in range(8):
		for j in range(7):
			# check borders first
			if(board[i][0] == board[i][7]):
				print("NO")
				checkNo = 1
				break
			elif(board[i][j] == board[i][j+1]):
				print("NO")
				checkNo = 1
				break
		if(checkNo == 1):
			break

	if(checkNo == 0):
		print("YES")


if __name__ == "__main__":
	main()