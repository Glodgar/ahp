import os

def predict(criteriaCount, alternativesCount, criteriaFactors, alternativesFactors):
    os.system("cls")

    ratingsValues = []

    for i in range(alternativesCount):
        value = 0
        for j in range(criteriaCount):
            value += round(criteriaFactors[j]*alternativesFactors[j][i], 3)
        ratingsValues.append(value)
    
    return ratingsValues