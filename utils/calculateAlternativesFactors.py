import os

def calculateAlternativesFactors(criteriaCount, alternativesCount, alternativesMatrix):
    os.system("cls")

    alternativesFactors = [[1 for x in range(alternativesCount)] for y in range(criteriaCount)]

    for k in range(criteriaCount):
        for i in range(alternativesCount):
            for j in range(alternativesCount):
                alternativesFactors[k][i] *= round(alternativesMatrix[k][i][j], 3)
            alternativesFactors[k][i] = round(alternativesFactors[k][i] ** (1/alternativesCount), 3)
    
    alternativesFactorsSum = []

    for i in range(criteriaCount):
        alternativesFactorsSum.append(round(sum(alternativesFactors[i]), 3))
    
    for i in range(criteriaCount):
        for j in range(alternativesCount):
            alternativesFactors[i][j] = round(alternativesFactors[i][j]/alternativesFactorsSum[i]/alternativesCount, 3)
    
    return alternativesFactors