import os

def calculateCriteriaFactors(criteriaCount, criteriaMatrix):
    os.system("cls")
    
    criteriaFactors = [1 for x in range(criteriaCount)]
    print(criteriaFactors)

    for i in range(criteriaCount):
        for j in range(criteriaCount):
            criteriaFactors[i] *= criteriaMatrix[i][j]
        criteriaFactors[i] = criteriaFactors[i]**(1/criteriaCount)

    criteriaFactorsSum = sum(criteriaFactors)

    for i in range(criteriaCount):
        criteriaFactors[i] = criteriaFactors/criteriaFactorsSum*criteriaCount
    
    return criteriaFactors