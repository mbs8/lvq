import csv
import math
import operator
from Instance import Instance
              
# Retorna a classificação de uma instancia dado um nome de dataset e um k (número de vizinhos)
def knn(classes, tests, minArg, maxArg, instance, k): 
    
    for inst in tests:
        if inst.id != instance.id:
            distanceToInstance = instance.euclideanDistance(inst, minArg, maxArg)
            instance.insertDistance(distanceToInstance, inst, k)

    return instance.classify(k, classes), instance.distancesToInstances[0:k]







