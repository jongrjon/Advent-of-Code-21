##Advent Calendar 2021 - https://adventofcode.com/2021/day/2
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon

with open('input.txt') as f:
    lines = f.readlines()

x = 0
y = 0

for l in lines:
	words = l.split()
	if words[0] == "forward":
		x += int(words[1])
	if(words[0]) == "up":
		y -= int(words[1])
	if(words[0]) == "down":
		y += int(words[1])

print(x*y)