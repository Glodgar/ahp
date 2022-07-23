import os
import numpy as np
from math import fabs

def createCriteriaMatrix(criteriaCount, criteriaList):
    os.system('cls')

    criteriaMatrix = np.zeros((criteriaCount,  criteriaCount))

    for i in range(criteriaCount):
        for j in range(criteriaCount):
            if i<j:
                if not criteriaList[i]==criteriaList[j]:
                    os.system('cls')
                    print(criteriaList[i], "vs", criteriaList[j])
                    print("-9", criteriaList[j], "extremely preferred than", criteriaList[i])
                    print("-7", criteriaList[j], "very strong preferred than", criteriaList[i])
                    print("-5", criteriaList[j], "strongly preferred than", criteriaList[i])
                    print("-3", criteriaList[j], "moderately preferred than", criteriaList[i])
                    print("1", "both are equally important")
                    print("3", criteriaList[j], "extremely preferred than", criteriaList[i])
                    print("5", criteriaList[j], "very strong preferred than", criteriaList[i])
                    print("7", criteriaList[j], "strongly preferred than", criteriaList[i])
                    print("9", criteriaList[j], "moderately preferred than", criteriaList[i])

                    value = int(input("Enter value: "))

                    if(value<0):
                        criteriaMatrix[i][j]=1/fabs(value)
                        criteriaMatrix[j][i]=fabs(value)
                    else:
                        criteriaMatrix[i][j]=fabs(value)
                        criteriaMatrix[j][i]=1/fabs(value)

            elif i==j:
                criteriaMatrix[i][j]=1
                
    return criteriaMatrix
