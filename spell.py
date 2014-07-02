def find(word, rat=0.8, let=0.75):
	"""This function returns words similar in spelling to the inputted 'word' parameter.

	The 'rat' parameter specifies what Levenshtein word similarity ratio the two words'
	similarity have to be greater than or equal to (defaults to 0.8). The 'let' parameter 
	inputs a percentage in decimal form of how many similar letters are shared (defaults to
	0.75 which is 75%)."""

	from Levenshtein import ratio
	from math import floor
	words = []
	with open('/usr/share/dict/words') as f:
		for itm in f.readlines():
		    words.append(itm.strip().lower())
	sim = []
	for i in words:
		if ratio(word, i) >= rat:
				if abs(len(word) - len(i)) <= 2:
					num = 0
					for x in i:
						if x in word:
							num += 1
					if num >= floor(len(word) * let):
						sim.append([ratio(word, i), i])
	sim.sort()
	sim = sim[::-1]
	result = []
	for i in sim:
		result.append(i[1])
	return result

def find_lst(word, lst, rat=0.8, let=0.75)