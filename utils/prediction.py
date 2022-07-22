import os

def prediction(criteriaCount, alternativesCount, criteriaFactors, alternativesFactors, alternativesList):
    os.system("cls")

    ratingsValues = []

    for i in range(alternativesCount):
        value = 0
        for j in range(criteriaCount):
            value += criteriaFactors[j] * alternativesFactors[j][i]
        ratingsValues.append(value)

    for i in range(alternativesCount):
        print(alternativesList[i], " : ", ratingsValues[i])
    
    return ratingsValues