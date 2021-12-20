##Advent Calendar 2021 - https://adventofcode.com/2021/day/8#part2
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon

with open('input.txt') as f:
    lines = f.readlines()

total = 0

for l in lines:
	l = l.split("|")
	values = [[], [], [], [], [], [], [], [], [], []]
	usp = l[0].split()
	usp = sorted(usp, key=len)
	for p in range(len(usp)):
		usp[p] = sorted(usp[p])
		if (len(usp[p]) == 2):
			values[1] = usp[p]
		if (len(usp[p]) == 3):
			values[7] = usp[p]
		if (len(usp[p]) == 4):
			values[4] = usp[p]
		if (len(usp[p]) == 7):
			values[8] = usp[p]
		if (len(usp[p]) == 5):
			if(set(values[1]).issubset(usp[p])):
				values[3] = usp[p]
			elif(set([x for x in values[4] if x not in values[1]]).issubset(usp[p])):
				values[5] = usp[p]
			else:
				values[2] = usp[p]
		if(len(usp[p]) == 6):
			if (set(values[3]).issubset(usp[p])):
				values[9] = usp[p]
			elif(not set(values[1]).issubset(usp[p])):
				values[6] = usp[p]
			else:
				values[0] = usp[p]

	outnum = ""
	x = l[1].split()
	for dig in x:
		dig = sorted(dig)
		for i in range(len(values)):
			if dig == values[i]:
				outnum = outnum + str(i)
	total += int(outnum)

print(total)