'''
Created on Mar 31, 2017

@author: Jonat
'''

import csv

def generateNewBias(previousBias, factor):
    if previousBias is None:
        bias = 10
    return bias

def generateRandomInitialWeights(numDimensions):
    i = 0
    initialGuess = 5
    initialWeights = []
    while i < numDimensions:
        initialWeights.append(initialGuess)
        initialGuess = initialGuess * -1
        i = i + 1
    return initialWeights

if __name__ == '__main__':
    inputMap = {}
    with open('input.txt') as csvfile:
        reader = csv.DictReader(csvfile)
        numDimensions = len(reader[0]) - 1
        numRow = 0
        for row in reader:
            currentDimension = 0
            while currentDimension < numDimensions:
                inputMap[numRow][currentDimension] = row[numDimensions-1]
                currentDimension = currentDimension + 1
            numRow = numRow + 1 
    bias = generateNewBias(None, None)
    initialWeights = generateRandomInitialWeights(numDimensions)
    currentRow = 0
    while currentRow <= numRow:
        currentDimension = 0
        result = 0
        while currentDimension < (numDimensions-1):
            currentDimensionValue = inputMap[currentRow][currentDimension]
            result = result + initialWeights[currentDimension]*currentDimensionValue
            currentDimension = currentDimension + 1
            if inputMap[currentRow]["multiplicant"] is None
                inputMap[currentRow]["multiplicant"] = 0
            multiplicant = inputMap[currentRow]["multiplicant"]     
            if (inputMap[currentDimension]==1):
                inputMap[currentRow]["multiplicant"] = multiplicant + result
            elif (inputMap[currentDimension]==-1):
                inputMap[currentRow]["multiplicant"] = "Bad"
            currentRow = currentRow + 1
    currentRow2 = 0
    while currentRow2 <= numRow:
        currentDimension = 0
        result = 0
        while currentDimension < (numDimensions-1):
            currentDimensionValue = inputMap[currentRow2][currentDimension]
            result = result + initialWeights[currentDimension]*currentDimensionValue
            currentDimension = currentDimension + 1
            if (inputMap[currentDimension]==1 and result >= 10) or (inputMap[currentDimension]==-1 and result >= -10):
                inputMap[currentRow2]["weightUtility"] = "Good"
            elif (inputMap[currentDimension]==1 and result < 10) or (inputMap[currentDimension]==-1 and result < -10):
                inputMap[currentRow2]["weightUtility"] = "Bad"
            currentRow2 = currentRow2 + 1
    