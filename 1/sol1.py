##Advent Calendar 2021 - https://adventofcode.com/2021/day/1
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon

with open('input.txt') as f:
    lines = f.readlines()

last = ""
counter = 0

for l in lines:
	l = int(l)
	if type(last) == int:
		if last < l:
			counter += 1
	last = l

print(counter) 