##Advent Calendar 2021 - https://adventofcode.com/2021/day/3
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon

with open('input.txt') as f:
    lines = f.readlines()

size = len(lines)/2
bits = [0] * (len(lines[1])-1)
gammatext = "0b"
epsilontext ="0b"

for l in lines:
	for i,b in enumerate(l):
		if(b) != '\n':
			if int(b) == 1:
				bits[i] += 1

for i in bits:
	if i < size:
		gammatext+=("0")
		epsilontext+=("1")
	else:
		gammatext+=("1")
		epsilontext+=("0")
consumption = int(gammatext, 2) * int(epsilontext, 2)
print(consumption)

