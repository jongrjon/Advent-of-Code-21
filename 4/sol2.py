##Advent Calendar 2021 - https://adventofcode.com/2021/day/4
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon

nums = []
cards = [[]]
with open('input.txt') as f:
    lines = f.readlines()

for l in lines[0].split(","):
	nums.append(int(l))

for li in lines[2:]:
	if len(li) > 1:
		l = li.split()
		line = []
		for n in l:
			line.append(int(n))
		cards[-1].append(line)
	else:
		cards.append([])

def win(card):
	if any(all(n == None for n in li) for li in card) or any(all(li[i] == None for li in card) for i in range(len(card))):
			return True
	else:
		return False

def play(n, c):
	for sn in n:
		for ca in c:
			for l in ca:
				for num in range(len(l)):
					if sn == l[num]:
						l[num] = None
			if win(ca):
				if len(c) == 1:
					return sum(num or 0 for l in ca for num in l)*sn
				else:
					c = list(filter(lambda x: x != ca, c))


				


def printcards(c):
	for ca in c:
		print("card: ")
		for l in ca:
			print(l)
		print("\n")

print(play(nums, cards))