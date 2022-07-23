import os

def addAlternatives():
    os.system("cls")

    alternativesList = []
    alternativesCount = int(input("Enter the number of alternatives: "))

    for i in range(alternativesCount):
        element = input("Enter alternative: ")

        alternativesList.append(element)

    return alternativesCount, alternativesList