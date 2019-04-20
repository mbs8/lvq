def crossFold(dataSet, k, foldSize):
    params = []                     # array contendo o nome das colunas dos parametros
    tests  = []                     # array contendo todas as instancias no banco de dados
    maxArg = []                     # array contendo o maximo de cada parametro
    minArg = []                     # array contendo o minimo de cada parametro
    hit    = 0                      # numero de acertos em cada teste de crossfold
    accuracy = 0
    div = 1                             

    params, tests, minArg, maxArg = readCsv(dataSet)

    while ((div * foldSize) < len(tests)):
        testingSet  = tests[(div-1)*foldSize : div*foldSize]
        trainingSet = tests[ : (div-1)*foldSize] + tests[div*foldSize : len(tests)-1] 
        div += 1

        # calcula todas as distancias para i-esima instancia do conjunto de teste e classifica de acordo com os k vizinhos mais proximos
        for testInstance in testingSet:
            for trainInstance in trainingSet:
                testInstance.insertDistance((testInstance.euclideanDistance(trainInstance, minArg, maxArg)), trainInstance)
                if (testInstance.distancesToInstances[0] == 0):
                    hit += 1
                    break
            if testInstance.classify(k):
                hit += 1
        
        accuracy += (hit/len(testingSet))
        hit = 0
    
    print("Accuracy: %.2f%%\n" % ((accuracy/div) * 100))