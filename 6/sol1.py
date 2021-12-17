##Advent Calendar 2021 - https://adventofcode.com/2021/day/6
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon


with open('input.txt') as f:
    lines = f.readlines()

fish = []

for n in lines[0].split(','):
	fish.append(int(n))

DAYS = 256
fishcounter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
fishnum = 0
print(fish)
for f in fish:
	fishcounter[f] += 1

print(fishcounter)
for d in range(DAYS):
	newfish = fishcounter[0]
	fishcounter.append(fishcounter.pop(0))
	fishcounter[6] += newfish
	print(fishcounter)

fishnum = sum(fishcounter)

print(fishnum)


