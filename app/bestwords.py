import sys, getopt
import nltk
import random
from textblob import TextBlob



def break_paragraph(p):
	return [str(x) for x in TextBlob(p).sentences]


def break_long_sentence(s):
	tokens = nltk.word_tokenize(s)
	pos_tokens = nltk.pos_tag(tokens)
	## get places to split long sentences
	divider_idx = [idx for idx in range(len(pos_tokens)) if pos_tokens[idx][1] in ('CC', 'WDT')]
	#print(divider_idx)
	starts = [0] + divider_idx
	stops = divider_idx + [len(tokens)]
	subsentences = []
	for (start,stop) in zip(starts,stops):
		sub = ' '.join(tokens[start:stop])
		if sub[-1] not in ('.','!','?'):
			sub += '.'
		subsentences.append(sub.capitalize())
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
	


def append_name_stinger(s):
	""" Insert a self-aggrandizing catchphrase compared to another proper noun. """
	new_s = s
	tokens = nltk.word_tokenize(new_s)
	pos_tokens = nltk.pos_tag(tokens)
	pos_only = [x[1] for x in pos_tokens]
	if 'NNP' in pos_only:
		noun = tokens[pos_only.index('NNP')]
		if random.random() < 1.0:	
			phrases = [	"I have nothing against {}.",
						"{} is nice, but I'm a winner.",
						"{} is a great guy.",
						"I'm better than {}.",
						"I'm much smarter than {}.",
						"{} is a real loser.",
						"{} tries hard, but is weak. Really weak.",
						"{} came to my wedding."]
			new_s = new_s + ' ' + random.choice(phrases).format(noun)
	return new_s
	

def insert_stinger(s):
	neg_stingers = ['Pathetic.', 'Loser.', 'The worst.', 'Dummies.', 'Tough!', 'Sad!', "What a joke."]
	pos_stingers = ['The best.', 'America.', 'Amazing!']
	new_s = s
	## get the sentiment of the sentence and a random number
	score = TextBlob(new_s).sentiment.polarity
	r = random.random()
	## If r is less than abs(score) insert something
	if r<1.0: ##r < abs(score): 
		if (score > 0):
			## Chose positive stinger
			new_s = new_s + ' ' + random.choice(pos_stingers)
		if (score < 0):
			## Choose negative stinger
			new_s = new_s + ' ' + random.choice(neg_stingers)
	return new_s



def prepend_meta(s):
	metas = ["I've said this before and I'll say it again.",
			"I've been saying this for a long time.",
			"You know what?",
			"OK?",
			"Believe me.",
			"Let me tell you."]
	new_s = s
	r = random.random()
	if r < 0.8:
		new_s = random.choice(metas) + ' ' + new_s
	return new_s


def prepend_social(s):
	socials = ["I get asked this all the time.",
			"So many people ask me this.",
			"Everybody knows it.",
			"You know it's true.",
			"Everyone tells me this",
			"Everybody thinks so.",
			"I get thousands of tweets about this every day."]
	new_s = s
	r = random.random()
	if r < 0.8:
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
	print()
	print('breaking paragraph/sentence down:')
	for sentence in break_paragraph(test_string):
		for subsentence in break_long_sentence(sentence):
			print(subsentence)
	print()


def trumpify(text):
	long_sentences = break_paragraph(text)
	print('long:', long_sentences)
	sentences = []
	for s in long_sentences:
		sentences += break_long_sentence(s)
	print('sentences:', sentences)
	functions = [prepend_meta, prepend_social, insert_stinger, insert_better]
	trumpified_text = ''
	for s in sentences:
		if random.random() < 1.0:
			f = random.choice(functions)
			#print(f)
			trumpified_sentence = f(s)
			print(trumpified_sentence, TextBlob(s).sentiment.polarity)
			trumpified_text += ' ' + trumpified_sentence
	return trumpified_text
	
		
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


	#s = 'I have a dream'
	#text = nltk.word_tokenize(s)
	#nltk.pos_tag(text)
	#text[3:3] = ['great']

	## Textblob can use a whole paragraph, and iterate over sentences. 
	## It can also do pos tagging
	#TextBlob(sentence).polarity

	#s = "I thought I was good. I was wrong. I'm the best."
	#for sent in TextBlob(s).sentences: print(sent.sentiment.polarity)

	
	
if __name__ == "__main__":
	main( sys.argv[1:] ) 