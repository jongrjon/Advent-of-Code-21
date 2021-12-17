##Advent Calendar 2021 - https://adventofcode.com/2021/day/7#part2
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon
import math

with open('input.txt') as f:
    lines = f.readlines()

crabs = []

for n in lines[0].split(','):
	crabs.append(int(n))

moves = []
sorted(crabs)
for i in range(min(crabs),max(crabs)+1):
	num = []
	for c in crabs:
		cmove = abs(c-i)
		cost = math.floor((cmove*(cmove+1))/2)
		num.append(cost)
	moves.append((i,sum(num)))

moves.sort(key=lambda tup: tup[1])

print(moves[0])