from ctypes import util
from utils.addCritera import addCritera
from utils.addAlternatives import addAlternatives
from utils.createCriteriaMatrix import createCriteriaMatrix
from utils.calculateCriteriaFactors import calculateCriteriaFactors
from utils.createAlternativesMatrix import createAlternativesMatrix
from utils.calculateAlternativesFactors import calculateAlternativesFactors
from utils.predict import predict

# AHP
# criteriaCount, criteriaList = addCritera()
# alternativesCount, alternativesList = addAlternatives()
# criteriaMatrix = createCriteriaMatrix(criteriaCount, criteriaList)
# criteriaFactors = calculateCriteriaFactors(criteriaCount, criteriaMatrix)
# alternativesMatrix = createAlternativesMatrix(criteriaCount, alternativesCount, criteriaList, alternativesList)
# alternativesFactors = calculateAlternativesFactors(criteriaCount, alternativesCount, alternativesMatrix)
# prediction = predict(criteriaCount, alternativesCount, criteriaFactors, alternativesFactors)

# for i in range(alternativesCount):
#     print(alternativesList[i], ":", prediction[i])

#TEST AHP
from testing.data_test import t_criteriaCount, t_alternativesCount, t_alternativesList, t_criteriaMatrix, t_alternativesMatrix

criteriaFactors = calculateCriteriaFactors(t_criteriaCount, t_criteriaMatrix)
alternativesFactors = calculateAlternativesFactors(t_criteriaCount, t_alternativesCount, t_alternativesMatrix)
prediction = predict(t_criteriaCount, t_alternativesCount, criteriaFactors, alternativesFactors)

for i in range(t_alternativesCount):
    print(t_alternativesList[i], ":", prediction[i])