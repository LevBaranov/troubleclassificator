#!/usr/bin/env python3.7
import dict
import json
import numpy as np
import random
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml import NetworkWriter
from pybrain.structure import TanhLayer, SoftmaxLayer, LinearLayer

net = buildNetwork(len(dict.train_x[0]), 5, len(dict.train_y[0]), hiddenclass=LinearLayer, recurrent=True)
ds = SupervisedDataSet(len(dict.train_x[0]), len(dict.train_y[0]))
i = 0
for inp in dict.train_x:
    ds.addSample(inp, dict.train_y[i])
    i += 1

trainer = BackpropTrainer(net, ds, learningrate=0.05)
trainer.trainEpochs(500)

NetworkWriter.writeToFile(net, 'net.xml')

