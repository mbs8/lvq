import csv
import math
import time

class Instance:
    def __init__(self, id, params, classification):
        self.id = id
        self.params = params
        self.classification = classification
        self.distancesToInstances = []

    def euclideanDistance(self, datasetInstance, minArg, maxArg):
        distance = 0
        for i, param in enumerate(datasetInstance.params):
            distance += ((param - self.params[i]) ** 2) / (maxArg[i] - minArg[i])
        distance = math.sqrt(distance)       
        return distance
    
    def insertDistance(self, distanceToInstance, instance): 
        distInst = (distanceToInstance, instance)
        if self.distancesToInstances == []:
            self.distancesToInstances.append(distInst)
        else:
            for i, (dist, _) in enumerate(self.distancesToInstances):
                if dist > distanceToInstance:
                    self.distancesToInstances.insert(i, distInst)
                    return
            self.distancesToInstances.append(distInst)
    
    # testa se a instancia foi classificada corretamente
    def classify(self, numNeighbor):
        classTrue = 0 
        classFalse = 0

        for i in range(0, numNeighbor):
            if self.distancesToInstances[i][1].classification == 'true' or self.distancesToInstances[i][1].classification == 'yes':
                classTrue  += 1
            else:
                classFalse += 1

        if ((classTrue < classFalse) and (self.classification == 'false' or self.classification == 'no')):
            return True
        if ((classTrue > classFalse) and (self.classification == 'true' or self.classification == 'yes')):
            return True
        return False

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
    params = []
    tests = []
    maxArg = []
    minArg = []

    with open(file) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        line_count = 0
        for row in csvReader:
            if (line_count == 0):
                params = row
            elif (row != []):
                param = [float(i) for i in row[:len(row)-1]]     
                classification = row[len(row)-1]
                test = Instance(line_count-1, param, classification)
                tests.append(test)
                minArg, maxArg = updateMinMax(row[:len(row)-1], minArg, maxArg) 
            line_count += 1
    
    return (params, tests, minArg, maxArg)
                

def knn(): 
    params = []                     # array contendo o nome das colunas dos parametros
    tests  = []                     # array contendo todas as instancias no banco de dados
    maxArg = []                     # array contendo o maximo de cada parametro
    minArg = []                     # array contendo o minimo de cada parametro
    hit    = 0                      # numero de acertos em cada teste de crossfold
    accuracy = 0
    div = 1
    dataSets = ["../Datasets/CM1_software_defect_prediction.csv", "../Datasets/KC2_software_defect_prediction.csv"]                             

    for dataSet in enumerate(dataSets):
        params, tests, minArg, maxArg = readCsv(dataSet)

        print(params)
        #print(tests)
        print(minArg)
        print(maxArg)
    

knn()





