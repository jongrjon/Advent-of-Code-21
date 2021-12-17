##Advent Calendar 2021 - https://adventofcode.com/2021/day/7
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon

with open('input.txt') as f:
    lines = f.readlines()

crabs = []

for n in lines[0].split(','):
	crabs.append(int(n))

moves = []
sorted(crabs)

for c in crabs:
	num = []
	for i in range(len(crabs)):
		num.append(abs(c-crabs[i]))
	moves.append((c,sum(num)))

moves.sort(key=lambda tup: tup[1])




print(moves[0])