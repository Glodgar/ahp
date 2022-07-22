import os

def calculateAlternativesFactors(criteriaCount, alternativesCount, alternativesMatrix):
    os.system("cls")

    alternativesFactors = [[1 for x in range(alternativesCount)] for y in range(criteriaCount)]

    for k in range(criteriaCount):
        for i in range(alternativesCount):
            for j in range(alternativesCount):
                alternativesFactors[k][i] *= alternativesMatrix[k][i][j]
            alternativesFactors[k][i] = alternativesFactors[k][i] ** (1/alternativesCount)
    
    alternativesFactorsSum = []

    for i in range(criteriaCount):
        alternativesFactorsSum.append(sum(alternativesFactors[i]))
    
    for i in range(criteriaCount):
        for j in range(alternativesCount):
            alternativesFactors[i][j] = alternativesFactors[i][j]/alternativesFactorsSum[i]/alternativesCount
    
    return alternativesFactors