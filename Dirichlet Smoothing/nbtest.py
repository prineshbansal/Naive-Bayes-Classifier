import sys
import json
from math import log
from operator import itemgetter
from glob import glob

def generate_log_ratio(dict1,dict2):
    ratio_list = {}
    for k,v in dict1.items():
        ratio_list[k] = log(v) - log(dict2.get(k))
    return ratio_list

def print_top_20_values(dict):
    sorted_dict= sorted(dict.items(), key=itemgetter(1), reverse=True)
    num = 0
    for items in sorted_dict:
        num += 1
        print(items)
        if num > 20:
            break

def write_to_file(predictions_file,prediction_dict):
    with open(predictions_file,'w') as write:
        write.write('{:>5}\t{:>5}\t{:>2}\n'.format("file-name", "pos-score", "neg-score"))
        for key, value in prediction_dict.items():
            sentence_rev = " ".join(reversed(str(key).split('/')))
            write.write('{:>5}\t{:>5}\t{:>2}\t'.format(sentence_rev.split()[0], value[0], value[1]))
            write.write("\n")

if __name__ == '__main__':
    model_file = sys.argv[1]
    test_directory = sys.argv[2]
    predictions_file = sys.argv[3]

    #
    # Reading data from the model file data
    #
    with open(model_file,'r') as read:
        model_data = json.load(read)

    pos_prob = model_data[0]
    neg_prob = model_data[1]

    #
    # Calculating and printing the highest log ratios of positive to negative 
    # and negative to positive weights. 
    #
    pos_to_neg_dict = generate_log_ratio(pos_prob,neg_prob)
    neg_to_pos_dict = generate_log_ratio(neg_prob,pos_prob)

    print("20 terms with the highest ratio of positive to negative weight:")
    print_top_20_values(pos_to_neg_dict)
    print()
    
    print("20 terms with the highest ratio of negative to positive weight:")
    print_top_20_values(neg_to_pos_dict)
    print()

    #
    # Reading data from test directory
    #
    test_data_files=[]
    test_data_files = glob(test_directory + '/*.txt')
    
    #
    # Classifying the text file in test directory as postive or negative.  
    #
    test_data = {}
    pos_reviews =[]
    neg_reviews = []
    prediction_dict = {}

    for i in test_data_files:
        with open(i,'r') as test_read:
            test_data[i] = test_read.read()

        cumulative_positive = 0.0
        cumulative_negative = 0.0
        words = test_data[i].split()

        for word in words:
            cumulative_positive += log(pos_prob.get(word,1))
            cumulative_negative += log(neg_prob.get(word,1))

        prediction_dict[i] = [cumulative_positive,cumulative_negative]

        if cumulative_positive > cumulative_negative:
            pos_reviews.append(i)
        else:
            neg_reviews.append(i)

    #print(len(pos_reviews))
    #print()
    #print(len(neg_reviews))
    #print()
    #print(len(prediction_dict))
    
    #
    # Writing filename and positive and negative reviews score to file
    #
    write_to_file(predictions_file,prediction_dict)