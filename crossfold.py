from readCsv import readCsv
from knn import knn

def crossFold(classes, tests, minArg, maxArg, k, foldSize):
    hit    = 0                      # numero de acertos em cada teste de crossfold
    accuracy = 0                    # taxa de acurácia
    div = 1                         # variável auxiliar para contar divisão atual    

    while ((div * foldSize) < len(tests)):
        testingSet  = tests[(div-1)*foldSize : div*foldSize]
        trainingSet = tests[ : (div-1)*foldSize] + tests[div*foldSize : len(tests)-1] 
        div += 1

        # calcula todas as distancias para i-esima instancia do conjunto de teste e classifica de acordo com os k vizinhos mais proximos
        for testInstance in testingSet:
            knnClassification, _ = knn(classes, trainingSet, minArg, maxArg, testInstance, k)
            if knnClassification == testInstance.classification:
                hit += 1
        
        accuracy += (hit/len(testingSet))
        hit = 0
    
    return ("Accuracy: %.2f%%" % ((accuracy/div) * 100))
