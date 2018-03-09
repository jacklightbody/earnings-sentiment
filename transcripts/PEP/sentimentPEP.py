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

def analyzePEP():
    
    fullDict ={}

    with open(r'.\transcripts\PEP\02_11_2015.txt',encoding='utf-8') as f:
        df = f.read().splitlines() 
    execDict, sentDict = pullNames(df)
    execDict = sentimentCalc(df,execDict,sentDict)
    fullDict['02_11_2015'] = execDict

    with open(r'.\transcripts\PEP\02_11_2016.txt',encoding='utf-8') as f1:
        df1 = f1.read().splitlines()
    execDict1, sentDict1 = pullNames(df1)
    execDict1 = sentimentCalc(df1,execDict1,sentDict1)
    fullDict['02_11_2016'] = execDict1

    with open(r'.\transcripts\PEP\02_13_2018.txt',encoding='utf-8') as f2:
        df2 = f2.read().splitlines()
    execDict2, sentDict2 = pullNames(df2)
    execDict2 = sentimentCalc(df2,execDict2,sentDict2)
    fullDict['02_13_2018'] = execDict2

    with open(r'.\transcripts\PEP\02_15_2017.txt',encoding='utf-8') as f3:
        df3 = f3.read().splitlines()
    execDict3, sentDict3 = pullNames(df3)
    execDict3 = sentimentCalc(df3,execDict3,sentDict3)
    fullDict['02_15_2017'] = execDict3

    with open(r'.\transcripts\PEP\04_18_2016.txt',encoding='utf-8') as f4:
        df4 = f4.read().splitlines()
    execDict4, sentDict4 = pullNames(df4)
    execDict4 = sentimentCalc(df4,execDict4,sentDict4)
    fullDict['04_18_2016'] = execDict4

    with open(r'.\transcripts\PEP\04_23_2015.txt',encoding='utf-8') as f5:
        df5 = f5.read().splitlines()
    execDict5, sentDict5 = pullNames(df5)
    execDict5 = sentimentCalc(df5,execDict5,sentDict5)
    fullDict['04_23_2015'] = execDict5

    with open(r'.\transcripts\PEP\04_26_2017.txt',encoding='utf-8') as f6:
        df6 = f6.read().splitlines()
    execDict6, sentDict6 = pullNames(df6)
    execDict6 = sentimentCalc(df6,execDict6,sentDict6)
    fullDict['04_26_2017'] = execDict6

    with open(r'.\transcripts\PEP\07_07_2016.txt',encoding='utf-8') as f7:
        df7 = f7.read().splitlines()
    execDict7, sentDict7 = pullNames(df7)
    execDict7 = sentimentCalc(df7,execDict7,sentDict7)
    fullDict['07_07_2016'] = execDict7

    with open(r'.\transcripts\PEP\07_09_2015.txt',encoding='utf-8') as f8:
        df8 = f8.read().splitlines()
    execDict8, sentDict8 = pullNames(df8)
    execDict8 = sentimentCalc(df8,execDict8,sentDict8)
    fullDict['07_09_2015'] = execDict8

    with open(r'.\transcripts\PEP\07_11_2017.txt',encoding='utf-8') as f10:
        df10 = f10.read().splitlines()
    execDict10, sentDict10 = pullNames(df10)
    execDict10 = sentimentCalc(df10,execDict10,sentDict10)
    fullDict['07_11_2017'] = execDict10

    with open(r'.\transcripts\PEP\07_23_2014.txt',encoding='utf-8') as f11:
        df11 = f11.read().splitlines()
    execDict11, sentDict11 = pullNames(df11)
    execDict11 = sentimentCalc(df11,execDict11,sentDict11)
    fullDict['07_23_2014'] = execDict11

    with open(r'.\transcripts\PEP\09_29_2016.txt',encoding='utf-8') as f12:
        df12 = f12.read().splitlines()
    execDict12, sentDict12 = pullNames(df12)
    execDict12 = sentimentCalc(df12,execDict12,sentDict12)
    fullDict['09_29_2016'] = execDict12

    with open(r'.\transcripts\PEP\10_04_2017.txt',encoding='utf-8') as f13:
        df13 = f13.read().splitlines()
    execDict13, sentDict13 = pullNames(df13)
    execDict13 = sentimentCalc(df13,execDict13,sentDict13)
    fullDict['10_04_2017'] = execDict13

    with open(r'.\transcripts\PEP\10_06_2015.txt',encoding='utf-8') as f14:
        df14 = f14.read().splitlines()
    execDict14, sentDict14 = pullNames(df14)
    execDict14 = sentimentCalc(df14,execDict14,sentDict14)
    fullDict['10_06_2015'] = execDict14

    with open(r'.\transcripts\PEP\10_09_2014.txt',encoding='utf-8') as f15:
        df15 = f15.read().splitlines()
    execDict15, sentDict15 = pullNames(df15)
    execDict15 = sentimentCalc(df15,execDict15,sentDict15)
    fullDict['10_09_2014'] = execDict15
    
    return fullDict

PEP = analyzePEP()
print(PEP)