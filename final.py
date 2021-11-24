import numpy as np
from scipy.interpolate import make_interp_spline
from scipy.stats import linregress
import matplotlib.pyplot as plt
import sys
from helpers import *

def main():
    if len(sys.argv) != 2:
        print('Syntax: python final.py <Movie Title>')
        print('For simplicity, the movie titles are as follows:\n')
        print(getPossInputs())
        exit()
    
    movieTitle = sys.argv[1]

    if movieTitle not in getPossInputs():
        print('No such title: ' + movieTitle)
        print('Syntax: python final.py <Movie Title>')
        print('For simplicity, the movie titles are as follows:\n')
        print(getPossInputs())
        exit()
    
    happiness(movieTitle)
    

def happiness(movieTitle):
    movieAvg = 0
    allWords = getAllWords(movieTitle)
    happinessDict = getHappinessDict()
    hScore = []
    windowSize = round(len(allWords) * 0.1) #10% of the script
    hScoreIndex = 0
    entries = []
    counter = 0

    for w in allWords:
        w = w.lower()
        hScore.append(0)
        counter+=1
        entries.append(counter)
        if hScoreIndex < windowSize*2:
            avg = getAverageWindowScore(allWords[0:
                                                 hScoreIndex],
                                        happinessDict)
        elif hScoreIndex + windowSize*2 > len(allWords):
            avg = getAverageWindowScore(allWords[hScoreIndex:
                                                 len(allWords)],
                                        happinessDict)
        else:
            avg = getAverageWindowScore(allWords[hScoreIndex-windowSize:
                                                 hScoreIndex+windowSize],
                                        happinessDict)
            
        hScore[hScoreIndex] = avg
        movieAvg+=avg
        hScoreIndex+=1

    plotMovies(movieTitle, entries, hScore, windowSize, movieAvg/len(allWords))


'''
function tokenizes a script
removes punctionations
returns a list where each index is a word
'''
def getAllWords(filePath):
    punc = '''!()-[]{};:"\,<>./?@#$%^&*_~'''
    allWords = []
    
    with open('scripts/' + filePath + '.txt', encoding='utf-8') as f:
        for line in f:
            if len(line) != 1:
                for w in line:
                    if w in punc:
                        line = line.replace(w, " ")
                words = line.split()
                for w in words:
                    allWords.append(w)

    return allWords

'''
functions converts happinessScore.txt into a dictionary for easy access
returns a dict where the key is the word, and the 2nd value is the happiness average
'''
def getHappinessDict():
    happinessDict = dict()
    with open('happinessScore.txt') as f:
        for line in f:
            (w, r, a, x, x, x, x, x) = line.split()
            happinessDict[w.lower()] = r + ' ' + a

    return happinessDict

'''
functions calculates the average happiness score for a window, centered on a word
the words paramater is already of the correct window size
returns a float that is the average happiness score for parameter words
'''
def getAverageWindowScore(words, happinessDict):
    if len(words) <= 0:
        return 5.37
    totSum = 0
    for w in words:
        if w in happinessDict:
            totSum += round(float(happinessDict[w].split()[1]), 2)
        else:
            totSum += 5.37
            
    return totSum/len(words)

'''
function takes in calculated data as well as movie data to plot the happiness line
'''
def plotMovies(movieTitle, entries, hScore, windowSize, movieAvg):
    trueTitle = getCorrectTitle(movieTitle) #get the actual movie title
    colors = ['#a50000', '#0C0B13']
    minPoint = min(hScore[windowSize:len(hScore)-windowSize]) #get the minimum happiness for when we fill in the graph

    #we smooth the lines to make it less harsh
    x = np.array(entries[windowSize:len(entries)-windowSize])
    y = np.array(hScore[windowSize:len(hScore)-windowSize])
    X_Y_Spline = make_interp_spline(x, y)
    X_ = np.linspace(x.min(), x.max(), 100)
    Y_ = X_Y_Spline(X_)
    plt.plot(X_, Y_, color=colors[0]) #smoothed happiness line
    #plt.plot(x, y, color=colors[0]) #unsmoothed happiness line
    plt.plot(entries[windowSize:len(entries)-windowSize], [movieAvg]*(len(entries)-windowSize*2), linestyle='dotted', color=colors[1]) #plot the average happiness
    
    plt.xlabel('Word #')
    plt.ylabel('Happiness')
    plt.title(trueTitle)
    plt.legend([trueTitle, 'Avgerage: ' + str(round(movieAvg, 3))])
    plt.margins(0, 0.05)
    #plt.fill_between(X_, minPoint, Y_, color=colors[0], alpha=0.5) #smoothed
    #plt.fill_between(x, minPoint-0.01, y, color=colors[0], alpha=0.5) #unsmoothed
    plt.show()        


main()



