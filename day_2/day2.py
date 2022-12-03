'''
INPUT:
	FIRST LETTER OF EACH LINE IS A | B | C
	SECOND LETTER IS X | Y | Z  
		A = ROCK (1 POINT) == X
		B = PAPER (2 POINTS) == Y
		C = SCISSORS (3 POINTS) == Z
	IF LINE == LOSE: 0 POINTS
	IF LINE == DRAW: 3 POINTS
	IF LINE == WIN:  6 POINTS
'''
#START PART 1
total = 0

SCORES = {
	'A' : 1,
	'B' : 2,
	'C' : 3,
}

WINS_AGAINST = {
	'A' : 'C',
	'B' : 'A',
	'C' : 'B',
}

'''
DECRYPT = {
	'X' : 'A',
	'Y' : 'B',
	'Z' : 'C',
}

with open('input.txt','r') as f:
	for line in f:
		enemy = line[0]
		me = line[2] #INDEX 2 B/C THERE IS A SPACE BETWEEN THE CHARS
		if (enemy == DECRYPT[me]):
			#draw
			total += SCORES[DECRYPT[me]] + 3
		elif (WINS_AGAINST[enemy] == DECRYPT[me]):
			#enemy wins
			total += SCORES[DECRYPT[me]]
		else:
			#I win
			total += SCORES[DECRYPT[me]] + 6

print(total)
'''

#PART 2: SECOND LETTER OF EACH LINE TELLS ME NEEDED OUTCOME
#	X == LOSE
#	Y == DRAW
#	Z == WIN
LOSES_TO = {
	'A' : 'B',
	'B' : 'C',
	'C' : 'A',
}

with open('input.txt','r') as f:
	for line in f:
		enemy = line[0]
		instruction = line[2] #INDEX 2 B/C THERE IS A SPACE BETWEEN THE CHARS
		if instruction == 'Y':
			#draw
			total += 3 + SCORES[enemy]
		elif instruction == 'X':
			#lose
			total += SCORES[WINS_AGAINST[enemy]]
		elif instruction == 'Z':
			#win
			total += 6 + SCORES[LOSES_TO[enemy]]
print(total)
