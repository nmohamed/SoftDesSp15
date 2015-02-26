"""
	Nora Mohamed
	~*2015 FEB*~

	Gets text and performs Markov analysis.
"""

import random

def get_prefixes(text, prefix):
	""" Gets prefixes depending on number of prefixes input to function and returns them
		text: Text to be made into prefixes
		prefix: Number of words per prefix

		>>> get_prefixes("Hello my friend Sal!", 2)
		['Hello my ', 'my friend ', 'friend Sal! ', 'Sal! ']
	"""
	words = text.split()
	if prefix == 1:
		return words
	group = []
	group2 = []
	wordspace = ""

	for i in range(len(words) - 1):
		group.append(words[i:i + prefix])
	for element in group:
		for x in range(len(element)):
			wordspace += element[x]
			if x != len(element):
				wordspace += " "
		group2.append(wordspace)
		wordspace = ""
	group2.append(words[-1] + " ")
	return group2

def get_first_words(groups, prefix):
	""" Gets first word in sentences and returns a list of them
	"""
	first = [groups[0]]
	for index in range(len(groups)):
		# if punctuation is in word, then add next word to first word
		if groups[-1] == groups[index]:
			break
		if groups[index][-1] in {".", "!", "?"}: #for prefix = 1
			first.append(groups[index+1])
		elif groups[index][-2:] in {".\"", "!\"", "?\"", ".\'", "?\'", "!\'"}:
			first.append(groups[index+1])

		if groups[index][-2:] in {". ", "! ", "? ", "\" "}: #for prefix >1
			if index == len(groups)-prefix:
				break
			else:
				first.append(groups[index+prefix])
	return first

def create_dictionary(groups, prefix):
	""" Creates dictionary that maps prefixes to various suffixes

		groups: groups to be put into a dictionary
		prefix: # of words in each prefix
		returns: dictionary of words; dictionary of first words

	>>> create_dictionary(get_prefixes("Hello Nora my name is Nora too!", 1), 1)
	{'name': ['is'], 'too!': [], 'is': ['Nora'], 'Nora': ['my', 'too!'], 'my': ['name'], 'Hello': ['Nora']}

	>>> create_dictionary(get_prefixes("Hello Nora my name is Nora too!", 2), 2)
	{'Nora my ': ['name is '], 'is Nora ': ['too! '], 'my name ': ['is Nora '], 'name is ': ['Nora too! '], 'too! ': [], 'Nora too! ': [], 'Hello Nora ': ['my name ']}
	"""
	w = {}
	for x in range(len(groups)):
		w[groups[x]] = []
	for x in range(len(groups)):
		if x == len(groups)-prefix:
			break
		w[groups[x]].append(groups[x+prefix])
	return w

def read_file(file_name):
	""" Reads file data and returns lines in list form. Cleans up text by removing
		'\n' values
	"""
	lines = []
	with open (file_name, "r") as myfile:
		data = myfile.readlines()
	for element in data:
		if element == "\n":
			pass
		else:	
			lines.append(element.strip())
	return lines

def markov_creation(dictionary, length, prefix, first):
	""" Takes a dictionary and starts the sentence with a random word. Then adds likely
		suffix until sentence reaches end (punctuation) or len prefixes is reached

		words: dictionary with prefixes/suffixes
		len: number of prefixes max per sentence
		returns: sentence
	"""
	sentence = random.choice(dictionary.keys())
	if first != []:
		sentence = random.choice(first)
	last_word = sentence
	if prefix == 1:
		sentence += " "

	for x in range(length-1):
		if dictionary[last_word] == []:
			break
		else:
			new_word = random.choice(dictionary[last_word])
			if prefix == 1:
				sentence += new_word + " "
			else:
				sentence += new_word
			if new_word[-1] in {".", "!", "?", "\""} or new_word.count(". ") + \
									new_word.count("? ") + new_word.count("! ") + \
									new_word.count("\" ") != 0:
				break
			last_word = new_word
	print sentence


def do_everything(file_name, prefix = 1, length = 20, start_with_first = True):
	""" Does what premise of this code is.
	"""
	add_words = {}
	words = {}
	first = []
	lines = read_file(file_name)

	for index in range(len(lines)):
		#get words
		groups = get_prefixes(lines[index], prefix)
		#create dictionary
		add_words = create_dictionary(groups, prefix)	
		for key, value in add_words.iteritems():
			words.setdefault(key, []).extend(value)
		#get first word of sentence if True
		if start_with_first == True:
			first2 = get_first_words(groups, prefix)
			for element in first2:
				first.append(element)
	#make sentence!
	markov_creation(words, length, prefix, first)

if __name__ == '__main__':
    import doctest
    # doctest.testmod()

    do_everything("buzzfeed_titles.txt", 1, 50, True)