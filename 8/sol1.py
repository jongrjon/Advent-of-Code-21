##Advent Calendar 2021 - https://adventofcode.com/2021/day/8#part2
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon
import math

with open('input.txt') as f:
    lines = f.readlines()

numbers =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for l in lines:
	l = l.split("|")
	x = l[1].split()
	for dig in x:
		if(len(dig) == 2):
			numbers[1] += 1
		if(len(dig) == 4):
			numbers[4] += 1
		if(len(dig) == 3):
			numbers[7] += 1
		if(len(dig)==7):
			numbers[8] += 1

print(sum(numbers))
