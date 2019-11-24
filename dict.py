#!/usr/bin/env python3.7
import json
import numpy as np
import random
#from pybrain.tools.shortcuts import buildNetwork
#from pybrain.datasets import SupervisedDataSet
#from pybrain.supervised.trainers import BackpropTrainer
#from pybrain.tools.customxml import NetworkWriter

def get_tf_record(sentence):
    global words
    # tokenize the pattern
    sentence_words = sentence
    # stem each word
    sentence_words = [word.lower() for word in sentence_words]
    # bag of words
    bow = [0]*len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bow[i] = 1
    return(np.array(bow))

# read the json file and load the training data
with open('data.json') as json_data:
    data = json.load(json_data)
    #print(data)
# get a list of all categories to train for
categories = list(data.keys())
words = []
# a list of tuples with words in the sentence and category name
docs = []
for each_category in data.keys():
    for each_sentence in data[each_category]:
        for w in each_sentence.split(' '):
            words.append(w)
        docs.append(([w for w in each_sentence.split(' ')], each_category))
# stem and lower each word and remove duplicates
words = [(w.lower()) for w in words]
print(words)
words = sorted(list(set(words)))
#print(words)
print(docs)

# create our training data
training = []
output = []
# create an empty array for our output
output_empty = [0] * len(categories)
for doc in docs:
    # initialize our bag of words(bow) for each document in the list
    bow = []
    # list of tokenized words for the pattern
    token_words = doc[0]
    token_words = [(word.lower()) for word in token_words]
    # create our bag of words array
    for w in words:
        bow.append(1) if w in token_words else bow.append(0)
    output_row = list(output_empty)
    output_row[categories.index(doc[1])] = 1
    # our training set will contain a the bag of words model and the output row that tells
    # which catefory that bow belongs to.
    training.append([bow, output_row])
# shuffle our features and turn into np.array as tensorflow  takes in numpy array
random.shuffle(training)
training = np.array(training)
# trainX contains the Bag of words and train_y contains the label/ category
train_x = list(training[:, 0])
train_y = list(training[:, 1])
'''
net = buildNetwork(len(train_x[0]), 1, len(train_y[0]))
ds = SupervisedDataSet(len(train_x[0]), len(train_y[0]))
i = 0
for inp in train_x:
    ds.addSample(inp, train_y[i])
    i += 1

trainer = BackpropTrainer(net, ds, learningrate=0.05)
trainer.trainEpochs(1000) 

NetworkWriter.writeToFile(net, 'net.xml')
#net = NetworkReader.readFrom('filename.xml')
inp = get_tf_record('УК порт 4  Нет связи, линк м МАС приходит, оборудование перезагрузили, не помогло. по логам нестабильный линк.')
print(inp)
out = net.activate(inp)
print(categories[np.argmax(out)])
print(out)
'''

