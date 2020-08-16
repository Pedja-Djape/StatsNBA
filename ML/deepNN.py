import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 


""" This file contains the library of code required for a deep neural network """

def initParamDeep(layerDimensions: list):
    np.random.seed(3)
    params = {}
    # number of layers in NN
    L = len(layerDimensions)
    for i in range(1,L):
        params['W' + str(i)] = 0.01*np.random.randn(layerDimensions[i],layerDimensions[i-1])
        params['b' + str(i)] = np.zeros((layerDimensions[i],1))
    
        assert ((params['W' + str(i)]).shape == (layerDimensions[i],layerDimensions[i-1])) 
        assert ((params['b' + str(i)]).shape == (layerDimensions[i],1))
    return params


"""
    Recall: Z_l = W_l * A_(l-1) + b_l ... <l> represents layer number
    --> Also, A_0 = X, input layer

"""
def linearForward(A,W,b):
    # A is input data -- activations from prev layer ^^^

    Z = np.dot(W,A) + b; # input of acitvation fxn
    assert (Z.shape == (W.shape[0],A.shape[1]));
    cache = (A,W,b);
    return Z,cache;

def sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    cache = x
    return s,cache

def relu(x):
    A = np.max(0,x)
    assert (A.shape == x.shape); cache = x

    return A,cache 

def sigmoidBackward(dA,cache):

    Z = cache
    s = sigmoid(-Z)
    dZ = dA*s*(1-s)
    assert (dZ.shape == Z.shape)
    return dZ 

def reluBackward(dA,cache):
    Z=cache
    dZ = np.array(dA,copy=True)
    dZ[Z <= 0] = 0
    assert (dZ.shape == Z.shape)

    return dZ

def linearActForward(APrev,W,b,acitvation):

    if acitvation.lower() == "sigmoid":
        Z, linCache = linearForward(APrev,W,b)
        A, acitvationCache = sigmoid(Z)

    elif acitvation.lower() == "relu":
        Z, linCache = linearForward(APrev,W,b)
        A, acitvationCache = relu(Z)
    
    assert (A.shape == (W.shape[0],APrev.shape[1]))
    cache = (linCache,acitvationCache)

    return A,cache

def LModelForward(X,params):
    caches = []
    A = X
    numLayers = len(params) // 2

    for i in range(1,numLayers):
        APrev = A
        A, cache = linearActForward(APrev,params['W'+str(i)],params['b'+str(i)],acitvation='relu')
        caches.append(cache)
    
    AL,cache = linearActForward(A,params['W'+str(i)],params['b'+str(i)],acitvation='sigmoid')
    caches.append(cache)
    assert (AL.shape == (1,X.shape[1]))

    return AL,caches

def getCost(AL,Y):
    m = Y.shape[1]

    cost = (-1/m)*np.sum(np.multiply(Y,np.log(AL)) + np.multiply(1-Y,np.log(1-AL)))
    cost = np.squeeze(cost)
    assert (cost.shape == ())
    return cost

def linearBackward(dZ,cache):
    APrev,W,b = cache
    m = APrev.shape

    dW = np.dot(dZ,cache[0].T) / m
    db = np.squeeze(np.sum(dZ,axis=1,keepdims=True)) / m
    dAPrev = np.dot(cache[1].T,dZ)

    assert (dAPrev.shape == APrev.shape)
    assert (dW.shape == W.shape)
    assert (isinstance(db,float))

    return dAPrev,dW,db

def linearActBackward(dA,cache,activation):

    linCache, actCache = cache

    if activation.lower() == 'relu':
        dZ = reluBackward(dA,actCache)
    
    elif activation.lower() == 'sigmoid':
        dZ = sigmoidBackward(dA,actCache)
    
    dAPrev, dW,db = linearBackward(dZ,linCache)

    return dAPrev,dW,db 

def LModelBackward(AL,Y,cahces):
    grads = {}
    numLayers = len(cahces)
    m = AL.shape[1]
    Y = Y.reshape(AL.shape)

    dAL = -(np.divide(Y,AL) - np.divide(1-Y,1-AL))

    currentCache = cahces[-1]
    