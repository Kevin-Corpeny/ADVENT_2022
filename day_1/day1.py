elves = {}
with open('input.txt','r') as f:
	i = 0
	for line in f:
		if i not in elves.keys() and line != '\n':
			elves[i] = int(line)
		elif line == '\n':
			i += 1
		else:
			elves[i] += int(line)

#part 1: WORKING
print(max(elves.values()))

#part 2: WORKING
print(sum(sorted(elves.values(),reverse=True)[0:3]))
