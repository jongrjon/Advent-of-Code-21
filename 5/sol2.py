##Advent Calendar 2021 - https://adventofcode.com/2021/day/5#part2
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon

with open('input.txt') as f:
    lines = f.readlines()

vents =dict()

for l in lines:
	l = l.split()
	l = list(filter(lambda x: x != "->", l))
	for i in range(len(l)):
		l[i] = l[i].split(',')
	x1 = 0
	x2 = 0
	y1 = 0
	y2 = 0
	xn=[]
	yn = []
	n = []
	print(l)
	if(int(l[0][0]) <= int(l[1][0])):
		x1 = int(l[0][0])
		x2 = int(l[1][0])
		xn = list(range(x1, x2 + 1))
	else:
		x2 = int(l[0][0])
		x1 = int(l[1][0])
		xn = list(range(x2, x1 - 1, -1))
	if(int(l[0][1]) <= int(l[1][1])):
		y1 = int(l[0][1])
		y2 = int(l[1][1])
		yn = list(range(y1, y2 + 1))
	else:
		y2 = int(l[0][1])
		y1 = int(l[1][1])
		yn = list(range(y2, y1 - 1,-1))

	if (x1 == x2):
		if(y1 == y2):
			n = list(map(lambda num: str(num) + "," + str(y1), list(range(x1, x2 + 1))))
		else:
			n = list(map(lambda num: str(x1) + "," + str(num), list(range(y1, y2 + 1))))
	else:
		if(y1 == y2):
			n = list(map(lambda num: str(num) + "," + str(y1), list(range(x1, x2 + 1))))
		else:
			n = list(map(lambda x, y: str(x) + "," + str(y), xn, yn))
	for i in n:
		vents[i] = vents.get(i,0) + 1

total = sum(1 for x in vents.values() if x > 1)

print(total)