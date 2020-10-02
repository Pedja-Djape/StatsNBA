import torch
import torch.nn as nn
from torch.optim import SGD
import numpy as np
import matplotlib.pyplot as plt

class NeuralNetwork(nn.Module):
    
    def __init__(self):
        super(NeuralNetwork,self).__init__()
        # params
        self.fc1 = nn.Linear(11,4)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(4,3)
        self.sigmoid = nn.Sigmoid()
        self.fc3 = nn.Linear(3,1)

    
    def forward(self,x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        x = self.sigmoid(x)
        return x 


def accuracy(y_hat,label):
    numSamp = label.size()[0]
    correct = 0
    for i in range(numSamp):
        if (y_hat[i].item() > 0.5 and label[i].item() == 1) or (y_hat[i].item() <=0.5 and label[i].item() == -1):
            correct += 1
    acc = correct/numSamp
    return acc



def train(dataTrain,labelsTrain,model,dataValid=None,labelsValid=None,epochs=100,learningRate = 0.01):
    optimizer = SGD(model.parameters(),lr=learningRate)
    # avgs the loss of all samples in the set 
    criterion = nn.BCELoss()

    trainLoss, validLoss, epochNum,trainAccuracy,validAccuracy = [],[],[],[],[]

    for epoch in range(0,epochs):
        epochNum += [epoch]

        # clear gradients
        optimizer.zero_grad()

        #get predictions
        trainPredTensor = model(dataTrain)

        # compute loss ***Make sure targets and outputs are of same size
        trainLossTensor = criterion(trainPredTensor,labelsTrain)
        trainLossVal = trainLossTensor.item()

        # backpropagation
        trainLossTensor.backward()
        optimizer.step()

        # accuracy of all samples in set
        epochTrainAccuracy = accuracy(trainPredTensor,labelsTrain)
        trainAccuracy += [epochTrainAccuracy]
        trainLoss += [trainLossVal]

        # # get predictions on validation set 
        # validPredTensor = model(dataValid)
        # validLossTensor = criterion(validPredTensor,labelsValid)
        # validLossVal = validLossTensor.item()
        # validLoss += [validLossVal]
        # epochValidAccuracy = accuracy(validPredTensor,labelsValid)
        # validAccuracy += [epochValidAccuracy]
        

    fig, ax = plt.subplots(2,1,sharex=True)
    ax[0].plot(epochNum,trainLoss,label='Training Set Loss')
    ax[1].plot(epochNum,trainAccuracy,label='Training Set Accuracy')
    ax[1].set_xlabel('Epoch Number') 
    ax[0].set_ylabel('Mean Loss'); ax[1].set_ylabel('Accuracy')
    ax[0].legend(); ax[1].legend()
    plt.show()

    return True



