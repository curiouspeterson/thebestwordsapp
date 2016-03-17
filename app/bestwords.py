import nltk
import random

s = 'I have a dream'

text = nltk.word_tokenize(s)

nltk.pos_tag(text)

text[3:3] = ['great']

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
	better_words = ['great', 'best', 'huge']
	the_word = random.choice(better_words)
	tokens = nltk.word_tokenize(s)
	pos_tokens = nltk.pos_tag(tokens)
	## get the noun indices
	noun_idx = [idx for idx in range(len(pos_tokens)) if pos_tokens[idx][1] == 'NN']
	## choose one
	the_idx = random.choice(noun_idx)
	## slicing
	tokens[the_idx:the_idx] = [the_word]
	new_s = ' '.join(tokens)
	return new_s
	


## Textblob can use a whole paragraph, and iterate over sentences. 
## It can also do pos tagging
TextBlob(sentence).polarity


s = "I thought I was good. I was wrong. I'm the best."
for sent in TextBlob(s).sentences: print(sent.sentiment.polarity)


def insert_stinger(s):
	neg_stingers = ['Pathetic.', 'Loser.', 'The worst.', 'Dummies.', 'Tough!', 'Sad!', "What a joke."]
	pos_stingers = ['The best.', 'America.', 'Amazing!']
	score = TextBlob(s).sentiment.polarity
	r = random.random()
	stinger = ''
	if r < abs(score): 
		if (score > 0):
			## Chose positive stinger
			stinger = random.choice(pos_stingers)
		if (score < 0):
			## Choose negative stinger
			stinger = random.choice(neg_stingers)
	return s + ' ' + stinger



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
			"So many people ask me this."]
	new_s = s
	r = random.random()
	if r > 0.8:
		new_s = random.choice(socials) + ' ' + new_s
	return new_s




from textblob import TextBlob
S = {}
for i in range(len(dockets)):
    docket = dockets[i]
    ## Petitioner is file 0; Respondent is file 1.  Res - Pet > 0 favors Respondent
    ## files 0,2,4,6,8 should be petitioners, 1,3,5,7,9 should be respondents
    S[docket] = {'sentiment_BREYER':0.0, 'sentiment_GINSBURG':0.0, 'sentiment_KENNEDY':0.0, 'sentiment_ROBERTS':0.0, 'sentiment_SCALIA':0.0}
    S[docket]['sentiment_BREYER'] = TextBlob(X[0][i]).sentiment[0]
