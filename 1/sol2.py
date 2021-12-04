##Advent Calendar 2021 - https://adventofcode.com/2021/day/1#part2
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon

with open('input.txt') as f:
    lines = f.readlines()

second = ""
third = ""
lastsum= ""
counter = 0

for l in lines:
	l = int(l)
	lmn =""
	try:
		lmn = l + second + third
	except:
		print("(N/A - no previous sum)")
	if type(lastsum) == int:
		if lastsum < lmn:
			counter += 1
	lastsum = lmn
	third = second
	second = l

print(counter) 