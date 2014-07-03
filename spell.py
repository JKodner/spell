def find(word, rat=0.8, ld=2, let=0.75):
	"""This function returns words similar in spelling to the inputted 'word' parameter.

	The 'rat' parameter specifies what Levenshtein word similarity ratio the words'
	similarity have to be greater than or equal to (defaults to 0.8). The 'ld' parameter
	specifies the maximum length difference between the words.
	The 'let' parameter inputs a percentage in decimal form of how many similar letters 
	are shared (defaults to 0.75 which is 75%). 

	Note: Function is case-insensitive"""

	from Levenshtein import ratio
	from math import floor
	if not isinstance(word, str):
		raise ValueError("Inputted 'word' must be string.")
	if not isinstance(rat, (int, float)) or (rat > 1) or (rat < 0):
		raise ValueError("Inputted 'rat' must be integer/float and be <= 1 and >= 0")
	if not isinstance(ld, int) or not (0 <= ld):
		raise ValueError("Inputted 'ld' must be integer and be >= 0")
	if not isinstance(let, (int, float)) or (let > 1) or (let < 0):
		raise ValueError("Inputtud 'led' must be integer/float and be <= 1 and >= 0")
	word = word.lower()
	words = []
	with open('/usr/share/dict/words') as f:
		for itm in f.readlines():
		    words.append(itm.strip().lower())
	sim = []
	for i in words:
		if ratio(word, i) >= rat:
				if abs(len(word) - len(i)) <= ld:
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

def find_lst(word, lst, rat=0.8, ld=2, let=0.75):
	"""This function returns words similar in spelling that are in in the specified 
	'lst' parameter to the inputted 'word' parameter.

	The 'rat' parameter specifies what Levenshtein word similarity ratio the words'
	similarity have to be greater than or equal to (defaults to 0.8). The 'ld' parameter
	specifies the maximum length difference between the words (defaults to 2). The 
	'let' parameter inputs a percentage in decimal form of how many similar letters are 
	shared (defaults to 0.75 which is 75%).

	Note: Function is case-insensitive"""

	from Levenshtein import ratio
	from math import floor
	if not isinstance(lst, list):
		raise ValueError("Inputted 'lst' must be list")
	if not isinstance(word, str):
		raise ValueError("Inputted 'word' must be string.")
	if not isinstance(rat, (int, float)) or (rat > 1) or (rat < 0):
		raise ValueError("Inputted 'rat' must be integer/float and be <= 1 and >= 0")
	if not isinstance(ld, int) or not (0 <= ld):
		raise ValueError("Inputted 'ld' must be integer and be >= 0")
	if not isinstance(let, (int, float)) or (let > 1) or (let < 0):
		raise ValueError("Inputtud 'led' must be integer/float and be <= 1 and >= 0")
	for i in lst:
		if not isinstance(i, str):
			raise ValueError("All values in 'lst' must be string")
	word = word.lower()
	lst = map(lambda x: x.lower(), lst)
	sim = []
	for i in lst:
		if ratio(word, i) >= rat:
				if abs(len(word) - len(i)) <= ld:
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