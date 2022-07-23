import os

def calculateCriteriaFactors(criteriaCount, criteriaMatrix):
    os.system("cls")
    
    criteriaFactors = [1 for x in range(criteriaCount)]
    print(criteriaFactors)

    for i in range(criteriaCount):
        for j in range(criteriaCount):
            criteriaFactors[i] *= round(criteriaMatrix[i][j], 3)
        criteriaFactors[i] = round(criteriaFactors[i]**(1/criteriaCount), 3)

    criteriaFactorsSum = round(sum(criteriaFactors), 3)

    for i in range(criteriaCount):
        criteriaFactors[i] = round(criteriaFactors[i]/criteriaFactorsSum*criteriaCount, 3)
    
    return criteriaFactors