#!/usr/bin/env python3.7
import numpy as np
import sys
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml import NetworkWriter, NetworkReader
import dict 

#text = str(input())
text = sys.argv[1]
net = NetworkReader.readFrom('net2.xml')
inp = dict.get_tf_record(text)
print(inp)
out = net.activate(inp)
print(dict.categories[np.argmax(out)])
print(out)

