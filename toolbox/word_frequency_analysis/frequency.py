""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	# First create list of lines
	lines = []
	f = open(file_name,'r')
	lines = f.readlines()
	curr_line = 0
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]
	#print lines
	# Next make list of everyword
	words = []
	for line in lines:
		stripped = line.split()
		for word in stripped:
			words.append(word.lower().strip('\n').strip(string.punctuation))
	return words


def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	dictionary = {}
	for words in word_list:
		dictionary[words] = dictionary.get(words, 0) + 1

	sort = sorted(dictionary, key = dictionary.get, reverse = True)
	top_words = sort[:n]
	print top_words
	
get_top_n_words(get_word_list('pg32325.txt'), 100)