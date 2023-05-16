sentance = 'I love icecream and I like to drive' #input

#make it using dictionary comprehension
#'I':1, 'love':4 ........
sentence_list = sentance.split()
sentence_list_dictionary = {i:len(i) for i in sentance.split()}
print(sentence_list_dictionary)