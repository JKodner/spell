def find(word):
	from Levenshtein import ratio
	from math import floor
	words = []
	with open('/usr/share/dict/words') as f:
		for itm in f.readlines():
		    words.append(itm.strip().lower())
	sim = []
	for i in words:
		if ratio(word, i) >= 0.8:
				if abs(len(word) - len(i)) <= 2:
					num = 0
					for x in i:
						if x in word:
							num += 1
					if num >= floor(len(word) * 0.75):
						sim.append([ratio(word, i), i])
	sim.sort()
	sim = sim[::-1]
	result = []
	for i in sim:
		result.append(i[1])
	return result