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
            while (lineList[k] != "Operator"):
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

def analyzeBA():
    
    fullDict = {}

    with open(r'.\transcripts\BA\01_31_2018.txt',encoding='utf-8') as f:
        df = f.read().splitlines() 
    execDict, sentDict = pullNames(df)
    execDict = sentimentCalc(df,execDict,sentDict)
    fullDict['01_31_2018'] = execDict

    with open(r'.\transcripts\BA\04_26_2017.txt',encoding='utf-8') as f1:
        df1 = f1.read().splitlines()
    execDict1, sentDict1 = pullNames(df1)
    execDict1 = sentimentCalc(df1,execDict1,sentDict1)
    fullDict['04_26_2017'] = execDict1
    
    with open(r'.\transcripts\BA\09_13_2017.txt',encoding='utf-8') as f2:
        df2 = f2.read().splitlines()
    execDict2, sentDict2 = pullNames(df2)
    execDict2 = sentimentCalc(df2,execDict2,sentDict2)
    fullDict['09_13_2017'] = execDict2

    with open(r'.\transcripts\BA\10_25_2017.txt',encoding='utf-8') as f3:
        df3 = f3.read().splitlines()
    execDict3, sentDict3 = pullNames(df3)
    execDict3 = sentimentCalc(df3,execDict3,sentDict3)
    fullDict['10_25_2017'] = execDict3
    
    return fullDict

BA = analyzeBA()
print(BA)
            
