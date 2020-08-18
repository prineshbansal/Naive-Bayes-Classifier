import sys
from glob import glob
from collections import Counter
import json

def read_from_file(files):
	data = []
	for i in files:
		with open(i,'r') as read:
			data.append(read.read())
	return data

def generate_frequency_dict(data):
	freq_dict = {}
	for i in data:
		words = i.split()
		for word in words:
			freq_dict[word] = freq_dict.get(word,0) + 1
	return freq_dict

def combine_dict(dict1,dict2):
	joint_dict =  Counter(dict1) + Counter(dict2)
	return joint_dict

def generate_final_freq_dict(subset_dict,total_dict):
	for i in subset_dict.copy().keys():
		if total_dict[i] < 5:
			subset_dict.pop(i)
	return subset_dict		

if __name__ == '__main__':
	train_dir = sys.argv[1]
	model_file = sys.argv[2]
	
	neg_files = []
	pos_files = []
	neg_data = []
	pos_data = []
	neg_words = {}
	pos_words = {}

	#
	# Reading data from text files in training directory
	#
	neg_files = glob(train_dir + '/neg/*.txt')
	pos_files = glob(train_dir + '/pos/*.txt')
	neg_data = read_from_file(neg_files)
	pos_data = read_from_file(pos_files)

	#
	# Generating frequency dictionary for words in postive and negative 
	# training texts.
	#
	neg_words = generate_frequency_dict(neg_data)
	pos_words = generate_frequency_dict(pos_data)
	
	#
	# Generating a dictionary for all the words in the collection
	# Thus, combining the postive & negative words dictionary
	#
	collection_dictionary = combine_dict(neg_words,pos_words)

	#
	# Adjusting postive and negative word dictionaries to fit missing words 
	# found in collection dictionary
	#
	for i in collection_dictionary.keys():
		neg_words[i] = neg_words.get(i,0)
		pos_words[i] = pos_words.get(i,0)
	
	#
	# Updating the negwords and poswords dict to remove terms
	# that occur less than 5 times in collection dictionary
	#
	neg_words = generate_final_freq_dict(neg_words,collection_dictionary)
	pos_words = generate_final_freq_dict(pos_words,collection_dictionary)
	neg_words_count = sum(neg_words.values())
	pos_words_count = sum(pos_words.values())
	collection_dictionary = combine_dict(neg_words,pos_words)
	total_count = len(collection_dictionary)

	#
	# Generating negative and positive probabiity dictionaries with 
	# Jelinek-Mercer Smoothing
	#
	neg_prob = {}
	pos_prob = {}

	lambda_value = 0.5 

	for i in neg_words.keys():
		neg_prob[i] = ((1-lambda_value)*(neg_words[i]/neg_words_count))+(lambda_value*(collection_dictionary[i]/(neg_words_count+pos_words_count)))

	for i in pos_words.keys():
		pos_prob[i] = ((1-lambda_value)*(pos_words[i]/pos_words_count))+(lambda_value*(collection_dictionary[i]/(neg_words_count+pos_words_count)))

	final_prob_list = [pos_prob,neg_prob]

	with open(model_file,'w') as temp:
		json.dump(final_prob_list,temp)

#	with open('`collectionwords.txt','w') as test:
#		json.dump(collection_dictionary,test)
#
#	with open('`neg_words.txt','w') as test:
#		json.dump(neg_words,test)
#
#	with open('`pos_words.txt','w') as test:
#		json.dump(pos_words,test)
#
#	with open('`count.txt','w') as test:
#		test.write(str(neg_words_count) + '\n\n' + str(pos_words_count))