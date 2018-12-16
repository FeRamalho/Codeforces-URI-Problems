#########################
### Infinity Gauntlet ###
#########################

## python3
#


def main():
	gauntlet = {'purple': 'Power', 'green': 'Time', 'blue': 'Space', 'orange': 'Soul', 'red': 'Reality', 'yellow': 'Mind'}

	n = int(input()) #number of gems
	for i in range(n):
		gem = str(input())
		del gauntlet[gem]

	#output
	print(6-n)
	for key in gauntlet:
		print(gauntlet[key])


if __name__ == "__main__":
	main()
