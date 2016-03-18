import sys, getopt
import nltk
import random
from textblob import TextBlob


#s = 'I have a dream'
#text = nltk.word_tokenize(s)
#nltk.pos_tag(text)
#text[3:3] = ['great']


def break_long_sentence(s):
	tokens = nltk.word_tokenize(s)
	pos_tokens = nltk.pos_tag(tokens)
	## get places to split long sentences
	divider_idx = [idx for idx in range(len(pos_tokens)) if pos_tokens[idx][1] in ('CC', 'WDT')]
	print(divider_idx)
	starts = [0] + divider_idx
	stops = divider_idx + [len(tokens)]
	subsentences = []
	for (start,stop) in zip(starts,stops):
		subsentences.append(' '.join(tokens[start:stop]))
	return subsentences
	
	
	
def insert_great(s):
	tokens = nltk.word_tokenize(s)
	pos_tokens = nltk.pos_tag(tokens)
	## get the noun indices
	noun_idx = [idx for idx in range(len(pos_tokens)) if pos_tokens[idx][1] == 'NN']
	## choose one
	the_idx = random.choice(noun_idx)
	## slicing
	tokens[the_idx:the_idx] = ['great']
	new_s = ' '.join(tokens)
	return new_s
	


def insert_better(s):
	""" Need to worry about noun modifiers. 
		'a test sentence' may become 'a test great sentence' 
		'a good house' might become 'a good great house' """
	better_words = ['great', 'best', 'huge']
	the_word = random.choice(better_words)
	tokens = nltk.word_tokenize(s)
	pos_tokens = nltk.pos_tag(tokens)
	## get the noun indices
	noun_idx = [idx for idx in range(len(pos_tokens)) if pos_tokens[idx][1] == 'NN']
	## choose one
	if len(noun_idx) > 0:
		the_idx = random.choice(noun_idx)
		## slicing
		tokens[the_idx:the_idx] = [the_word]
	new_s = ' '.join(tokens)
	return new_s
	


## Textblob can use a whole paragraph, and iterate over sentences. 
## It can also do pos tagging
#TextBlob(sentence).polarity


#s = "I thought I was good. I was wrong. I'm the best."
#for sent in TextBlob(s).sentences: print(sent.sentiment.polarity)


def insert_stinger(s):
	neg_stingers = ['Pathetic.', 'Loser.', 'The worst.', 'Dummies.', 'Tough!', 'Sad!', "What a joke."]
	pos_stingers = ['The best.', 'America.', 'Amazing!']
	new_s = s
	## get the sentiment of the sentence and a random number
	score = TextBlob(new_s).sentiment.polarity
	r = random.random()
	## If r is less than abs(score) insert something
	if r < abs(score): 
		if (score > 0):
			## Chose positive stinger
			new_s = new_s + ' ' + random.choice(pos_stingers)
		if (score < 0):
			## Choose negative stinger
			new_s = new_s + ' ' + random.choice(neg_stingers)
	return new_s



def prepend_meta(s):
	metas = ["I've said this before and I'll say it again.",
			"I've been saying this for a long time."]
	new_s = s
	r = random.random()
	if r > 0.8:
		new_s = random.choice(metas) + ' ' + new_s
	return new_s


def prepend_social(s):
	socials = ["I get asked this all the time.",
			"So many people ask me this."
			"Everybody knows it."]
	new_s = s
	r = random.random()
	if r > 0.8:
		new_s = random.choice(socials) + ' ' + new_s
	return new_s


def test_all_functions(test_string):
	print('test_string:')
	print(test_string)
	print()
	print('prepend meta-statement:')
	print(prepend_meta(test_string))
	print()
	print('prepend social prof:')
	print(prepend_social(test_string))
	print()
	print('append stinger:')
	print(insert_stinger(test_string))
	print()
	print('insert better:')
	print(insert_better(test_string))
	


def main(argv):

	command_line_instructions = 'bestwords.py -i <test_string>'
	try:
		opts, args = getopt.getopt(argv,"hi:",["config=","param2="])
	except getopt.GetoptError:
		print (command_line_instructions)
		sys.exit()
	if (len(opts) > 0):	
		#print args
		#print opts	
		for opt, arg in opts:
			#print opt
			if opt == '-h':
				print (command_line_instructions)
				sys.exit()
			elif opt in ("-i", "--param1"):
				test_string = arg
	else:
		test_string = "I thought I was good. I was wrong. I'm the best."
		#test_string = "My friend and I were excited to go to the party."
	
	test_all_functions(test_string)
	
	
if __name__ == "__main__":
	main( sys.argv[1:] ) 