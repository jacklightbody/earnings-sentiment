from transcripts.AAPL import sentimentAAPL
from transcripts.BA import sentimentBA
from transcripts.BUD import sentimentBUD
from transcripts.CAT import sentimentCAT
from transcripts.GOOG import sentimentGOOG
from transcripts.KO import sentimentKO
from transcripts.PEP import sentimentPEP


def sentiment():
    sentDict = {}
    
    sentDict["AAPL"] = sentimentAAPL.analyzeAAPL()
    sentDict["BA"] = sentimentBA.analyzeBA()
    sentDict["BUD"] = sentimentBUD.analyzeBUD()
    sentDict["CAT"] = sentimentCAT.analyzeCAT()
    sentDict["GOOG"] = sentimentGOOG.analyzeGOOG()
    sentDict["KO"] = sentimentKO.analyzeKO()
    sentDict["PEP"] = sentimentPEP.analyzePEP()
    
    return sentDict

sentiment()