import os

def addCritera():
    os.system('cls')

    criteriaList = []
    criteriaCount = int(input("Enter the number of criteria: "))

    for i in range(criteriaCount):
        element = input("Enter criterium: ")

        criteriaList.append(element)

    return criteriaCount, criteriaList

