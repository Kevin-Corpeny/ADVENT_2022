import string

# #part 1
# total = 0
# letters = ([x for x in string.ascii_lowercase] + [x for x in string.ascii_uppercase])
# prios = {}
# for i, val in enumerate(letters):
# 	prios[val] = i+1

# with open('input.txt','r') as f:
# 	for line in f:
# 		line = line.strip()
# 		first = set(line[0:len(line)//2])
# 		second = set(line[len(line)//2:])
# 		same = ''.join(first.intersection(second))
# 		total += prios[same]
		
# print(total)

#part 2
groups = {}
letters = ([x for x in string.ascii_lowercase] + [x for x in string.ascii_uppercase])
prios = {}
for i, val in enumerate(letters):
	prios[val] = i+1

with open('input.txt','r') as f:
	prev_lines = []
	x = 0
	for line in f:
		line = line.strip()
		if len(prev_lines) == 3:
			groups[x] = ''.join(prev_lines[0] & prev_lines[1] & prev_lines[2])
			prev_lines = [set(line)]

			x += 1
		else:
			prev_lines.append(set(line))
	groups[x] = ''.join(prev_lines[0] & prev_lines[1] & prev_lines[2])
print(groups,prios)
total = 0
for val in groups.values():
	total += prios[val]
	print(f'value just added: {prios[val]}\tletter: {val}\ttotal: {total}')
print(total)
