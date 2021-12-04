##Advent Calendar 2021 - https://adventofcode.com/2021/day/3
##Solution - Jón Helgi Elínar Kjartansson - github: jongrjon
import re
ogr = []
co2 = []
with open('input.txt') as f:
    lines = f.readlines()

# size = len(lines)/2
# bits = [0] * (len(lines[1])-1)
# ogrbase = ""
# co2base = ""

for l in lines:
	ogr.append(l.strip())
	co2.append(l.strip())
	# for i,b in enumerate(l):
	# 	if(b) != '\n':
	# 		if int(b) == 1:
	# 			bits[i] += 1

# for i in bits:
# 	if i < size:
# 		ogrbase+=("0")
# 		co2base+=("1")
# 	else:
# 		ogrbase+=("1")
# 		co2base+=("0")

# ogr_count= 0
# ogr_str = "0b"

def findogr(x, y, z):
	if len(x) ==1:
		print(x, z, y)
		return (x[0])
	else:
		ones = 0
		nills = 0
		for single in x:
			if single[z:(z+1)] == "1":
				ones +=1
			else:
				nills+=1

		if ones >= nills:
			newy = y + "1" 
		else:
			newy = y + "0"

		x = list(filter(lambda l: l.startswith(newy), x))
		return findogr(x, newy, z+1)

def findco2(x, y, z):
	if len(x) ==1:
		print(x, z, y)
		return (x[0])
	else:
		ones = 0
		nills = 0
		for single in x:
			if single[z:(z+1)] == "1":
				ones +=1
			else:
				nills+=1

		if ones >= nills:
			newy = y + "0" 
		else:
			newy = y + "1"

		x = list(filter(lambda l: l.startswith(newy), x))
		return findco2(x, newy, z+1)



# while 1 < len(ogr) and ogr_count <=len(ogrbase):
# 	for o in list(ogr):
# 		if o[ogr_count] != ogrbase[ogr_count]:
# 			ogr.remove(o)
# 	ogr_str+=(ogrbase[ogr_count])
# 	ogr_count += 1

# co2_count= 0
# co2_str = "0b"

# while 1 < len(co2) and co2_count <=len(co2base):
# 	for c in list(co2):
# 		if c[co2_count] != co2base[co2_count]:
# 			co2.remove(c)
# 	co2_str+=(co2base[co2_count])
# 	co2_count += 1
# 	print(co2)
#print(findstr(ogr, "", 0))
lsr = int("0b"+findogr(ogr, "", 0), 2) * int("0b"+findco2(co2, "", 0), 2)
print(lsr)

# print(co2base)
# print(co2_str)
# print(int(co2_str, 2))
# print(int(ogr_str, 2))


# lsr = int(ogr_str, 2) * int(co2_str, 2)
# print(lsr)
