import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def pullNames(lineList):
    sentimentDict = {}
    sentimentDict["Operator"] = 0.0
    executiveDict = {}
    for i in range(50):
        if lineList[i] == "Executives":
            j = i + 1
            while lineList[j] != "Analysts":
                name = lineList[j].split('-')[0].strip()
                sentimentDict[name] = 0.0
                executiveDict[name] = 0.0
                j = j+1
            k = j + 1
            while lineList[k] != "Operator":
                issue = list(sentimentDict.keys())
                if lineList[k] in issue:
                    break
                sentimentDict[lineList[k].split('-')[0].strip()] = 0.0
                k = k+1
    return executiveDict, sentimentDict



def sentimentCalc(lineList, executiveDict, sentimentDict):
    analyser = SentimentIntensityAnalyzer()
    people = list(sentimentDict.keys())
    execs = list(executiveDict.keys())
    for i in range(len(execs)):
        words = []
        for j in range(len(lineList)):
            if (lineList[j] == execs[i]) or (lineList[j].split('-')[0].strip() == execs[i]):
                m = j + 1
                while lineList[m].split('-')[0].strip() not in people:
                    words.append(lineList[m])
                    m = m + 1
                    if (m) == len(lineList):
                        break
        s = ' '
        words = s.join(words)
        snt = analyser.polarity_scores(words)
        executiveDict[execs[i]] = snt['compound']
    return executiveDict

with open('01_25_2018.txt',encoding='utf-8') as f:
    df = f.read().splitlines() 
print('01_25_2018')
execDict, sentDict = pullNames(df)
execDict = sentimentCalc(df,execDict,sentDict)
print(execDict)

with open('01_26_2017.txt',encoding='utf-8') as f1:
    df1 = f1.read().splitlines()
print('01_26_2017')
execDict1, sentDict1 = pullNames(df1)
execDict1 = sentimentCalc(df1,execDict1,sentDict1)
print(execDict1)

with open('04_26_2017.txt',encoding='utf-8') as f2:
    df2 = f2.read().splitlines()
print('04_26_2017')
execDict2, sentDict2 = pullNames(df2)
execDict2 = sentimentCalc(df2,execDict2,sentDict2)
print(execDict2)

with open('09_13_2017.txt',encoding='utf-8') as f3:
    df3 = f3.read().splitlines()
print('09_13_2017')
execDict3, sentDict3 = pullNames(df3)
execDict3 = sentimentCalc(df3,execDict3,sentDict3)
print(execDict3)

with open('10_24_2017.txt',encoding='utf-8') as f4:
    df4 = f4.read().splitlines()
print('10_24_2017')
execDict4, sentDict4 = pullNames(df4)
execDict4 = sentimentCalc(df4,execDict4,sentDict4)
print(execDict4)

with open('11_15_2017.txt',encoding='utf-8') as f5:
    df5 = f5.read().splitlines()
print('11_15_2017')
execDict5, sentDict5 = pullNames(df5)
execDict5 = sentimentCalc(df5,execDict5,sentDict5)
print(execDict5)

with open('12_01_2016.txt',encoding='utf-8') as f6:
    df6 = f6.read().splitlines()
print('12_01_2016')
execDict6, sentDict6 = pullNames(df6)
execDict6 = sentimentCalc(df6,execDict6,sentDict6)
print(execDict6)