import nltk
from nltk import word_tokenize

def get_bot_reply(message):

	name = "default_name"
	words = word_tokenize(message)
	tagged = nltk.pos_tag(words)
	for word in tagged:
		if word[1] == 'NNP':
			name = word[0]

	return "Hey, %s how're you doing today?" % name		




def start_chatbot():
	
	print "Hey, what's your name?"

	while(True):
		user_message = raw_input()
		bot_reply = get_bot_reply(user_message)
		print bot_reply

if __name__ == '__main__':
	start_chatbot()