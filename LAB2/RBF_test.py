# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 16:23:40 2018

@author: Olivier
"""
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from RBF_network import RBF_network
#net = RBF_network(100, 0.01)


x = np.arange(0, 2*np.pi, 0.1) 
f = np.sin(2*x)

def func(x):
    if x >=0:
        return 1
    else:
        return -1
vf = np.vectorize(func)
f = vf(f)
#net.learning_batch(x,f)
#net.learning_incr(x, f, 0.004, 0.001, 1000) #O.O41 is a good one for 100
#0.009 for 1000 nodes
#0.0009 for 10000 nodes
#rangeE = np.linspace(0.0001, 0.001, 10)
##rangeV = np.linspace(1, 100, 50)
#MSE = np.zeros(10)
#i=0
#for eta in rangeE:
#    np.random.seed(9001)
#    net = RBF_network(10000)
#    net.learning_incr(x, f, eta)
#    test_x = x+  0.05
#    o = net.output(test_x)
#    MSE[i] = np.average(np.sum((np.sin(2*test_x) - o)**2))
#    i+=1
#plt.figure()
#plt.plot(rangeE, MSE)
#plt.show()

#plt.figure()
#test_x = x + 0.05
#o = net.output(test_x)
#plt.plot(test_x, np.sin(2*test_x), linewidth=5)
#plt.plot(test_x, o)
#plt.show()
test_x = x + 0.05
nunits = 100
startTime = datetime.now()
net = RBF_network(nunits, (2*np.pi/(1*nunits))**2)
#net.learning_batch(x, f)
net.learning_incr(x, f, 0.04, 0.0001, 1000)
print(datetime.now() - startTime)
o = net.output(test_x)
#o = np.vectorize(func)(o)
#absolute_residual_error = np.average(np.abs(np.vectorize(func)(np.sin(2*test_x)) - o))
absolute_residual_error = np.average(np.abs(vf(np.sin(2*test_x)) - o))

#while absolute_residual_error > 0.1:
#    nunits+=1
#    net = RBF_network(nunits, 0.01)#(2*np.pi/(nunits))**2)
#    net.learning_incr(x,f, 0.1/nunits,100)
#    o = net.output(test_x)
#    absolute_residual_error = np.average(np.abs(np.sin(2*test_x) - o))
print("Number of units={} and error={}".format(nunits, absolute_residual_error) )
plt.figure()
plt.plot(test_x, vf(np.sin(2*test_x)), linewidth=5)
plt.plot(test_x, o)
plt.show()

    

