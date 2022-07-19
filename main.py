from ctypes import util
from utils.addCritera import addCritera
from utils.addAlternatives import addAlternatives
from utils.createCriteriaMatrix import createCriteriaMatrix


criteriaCount, criteriaList = addCritera()
test = createCriteriaMatrix(criteriaCount, criteriaList)

print(test)