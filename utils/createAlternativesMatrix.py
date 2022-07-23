import os
import numpy as np
from math import fabs

def createAlternativesMatrix(criteriaCount, alternativesCount, criteriaList, alternativesList):
    os.system("cls")

    alternativesMatrix = np.zeros((criteriaCount, alternativesCount, alternativesCount))
    
    for k in range(criteriaCount):
        for i in range(alternativesCount):
            for j in range(alternativesCount):
                if i<j:
                    if not alternativesList[i]==alternativesList[j]:
                        os.system("cls")

                        print("criteria: ", criteriaList[k], " for: ", alternativesList[i], " vs ", alternativesList[j])
                        print("-9", alternativesList[j], "extremely preferred than", alternativesList[i])
                        print("-7", alternativesList[j], "very strong preferred than", alternativesList[i])
                        print("-5", alternativesList[j], "strongly preferred than", alternativesList[i])
                        print("-3", alternativesList[j], "moderately preferred than", alternativesList[i])
                        print("1", "both are equally important")
                        print("3", alternativesList[j], "extremely preferred than", alternativesList[i])
                        print("5", alternativesList[j], "very strong preferred than", alternativesList[i])
                        print("7", alternativesList[j], "strongly preferred than", alternativesList[i])
                        print("9", alternativesList[j], "moderately preferred than", alternativesList[i])
                
                        value = int(input("Enter value: "))

                        if value<0:
                            alternativesMatrix[k][i][j] = round(1/fabs(value), 3)
                            alternativesMatrix[k][j][i] = fabs(value)
                        else:
                            alternativesMatrix[k][i][j] = fabs(value)
                            alternativesMatrix[k][j][i] = round(1/fabs(value), 3)
                elif i==j:
                    alternativesMatrix[k][j][j] = 1
                    
    return alternativesMatrix

