import os

def predict(criteriaCount, alternativesCount, criteriaFactors, alternativesFactors, alternativesList):
    #os.system("cls")

    ratingsValues = []

    print("criteriaCount", criteriaCount)
    print("alternativesCount", alternativesCount)
    print("criteriaFactors", criteriaFactors)
    print("alternativesFactors", alternativesFactors)
    print("alternativesList", alternativesList)

    for i in range(alternativesCount):
        value = 0
        for j in range(criteriaCount):
            value += criteriaFactors[j]*alternativesFactors[j][i]
        ratingsValues.append(value)

    for i in range(alternativesCount):
        print(alternativesList[i], " : ", ratingsValues[i])
    
    return ratingsValues