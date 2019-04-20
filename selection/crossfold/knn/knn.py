import csv
import math
import operator

class Instance:
    def __init__(self, id, params, classification):
        self.id = id
        self.params = params
        self.classification = classification
        self.distancesToInstances = []

    # Calcula a distancia para determinada instancia usando os vetores de min e max 
    # para a normalização do cálculo da distância
    def euclideanDistance(self, datasetInstance, minArg, maxArg):
        distance = 0
        for i, param in enumerate(datasetInstance.params):
            distance += ((param - self.params[i]) ** 2) / (maxArg[i] - minArg[i])
        distance = math.sqrt(distance)       
        return distance
    
    # Insere ordenadamente no array de distancias a distancia para determinada instancia
    def insertDistance(self, distanceToInstance, instance, k): 
        distInst = (distanceToInstance, instance)
        if self.distancesToInstances == []:
            self.distancesToInstances.append(distInst)
        else:
            for i, (dist, _) in enumerate(self.distancesToInstances):
                if dist > distanceToInstance:
                    self.distancesToInstances.insert(i, distInst)
                    size = len(self.distancesToInstances)
                    if size > k:
                        del(self.distancesToInstances[size-1])
                    return
            if len(self.distancesToInstances) < k:
                self.distancesToInstances.append(distInst)
                
    
    # Retorna a classe pertencente da instancia
    def classify(self, numNeighbor, classes):
        dictClass = {}

        for clas in classes:
            dictClass[clas] = 0

        for i in range(0, numNeighbor):
            classification = self.distancesToInstances[i][1].classification
            dictClass[classification] += 1

        return max(dictClass.items(), key=operator.itemgetter(1))[0]

# atualiza o array de minimo e maximo de cada um dos parametros
def updateMinMax(row, minArg, maxArg):
    row = [float(i) for i in row]
    if (maxArg == []):
        minArg = list(row)
        maxArg = list(row)
        return minArg, maxArg
    else:
        for i, param in enumerate(row):
            if maxArg[i] < param:
                maxArg[i] = param
            if minArg[i] > param:
                minArg[i] = param
    return minArg, maxArg

# ler do arquivo csv e salva as informacoes nos arrays
def readCsv(file): 
    classes = []
    tests = []
    maxArg = []
    minArg = []

    with open(file) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        line_count = 0
        for row in csvReader:
            if (row != [] and line_count != 0):
                param = [float(i) for i in row[:len(row)-1]]     
                classification = row[len(row)-1]
                test = Instance(line_count-1, param, classification)
                tests.append(test)
                minArg, maxArg = updateMinMax(row[:len(row)-1], minArg, maxArg)
                if not(classification in classes):
                    classes.append(classification)
            line_count += 1
    
    return (classes, tests, minArg, maxArg)
                
# Retorna a classificação de uma instancia dado um nome de dataset e um k (número de vizinhos)
def knn(classes, tests, minArg, maxArg, instance, k): 
    
    for inst in tests:
        distanceToInstance = instance.euclideanDistance(inst, minArg, maxArg)
        instance.insertDistance(distanceToInstance, inst, k)
        
    return instance.classify(k, classes)






