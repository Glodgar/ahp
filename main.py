from ctypes import util
from utils.addCritera import addCritera
from utils.addAlternatives import addAlternatives
from utils.createCriteriaMatrix import createCriteriaMatrix
from utils.calculateCriteriaFactors import calculateCriteriaFactors
from utils.createAlternativesMatrix import createAlternativesMatrix
from utils.calculateAlternativesFactors import calculateAlternativesFactors
from utils.predict import predict

criteriaCount, criteriaList = addCritera()
alternativesCount, alternativesList = addAlternatives()
criteriaMatrix = createCriteriaMatrix(criteriaCount, criteriaList)
criteriaFactors = calculateCriteriaFactors(criteriaCount, criteriaMatrix)
alternativesMatrix = createAlternativesMatrix(criteriaCount, alternativesCount, criteriaList, alternativesList)
alternativesFactors = calculateAlternativesFactors(criteriaCount, alternativesCount, alternativesMatrix)
prediction = predict(criteriaCount, alternativesCount, criteriaFactors, alternativesFactors, alternativesList)