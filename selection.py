from readCsv import *

# Algoritmo para selecionar os protótipos
def selection(dataSet, prototypesPerClass):
    classes = []                # Array contendo as classes das instancias
    tests = []                  # Array contendo todas as instancias 
    minArg = []                 # Array contendo o valor minimo de cada parâmetro 
    maxArg = []                 # Array contendo o máximo de cada parâmetro
    subTest = []                # Array contendo o subconjunto que será retornado pelo selection

    classes, tests, _, _ = readCsv(dataSet)

    for clas in classes:
        j = 0
        prototypes = []
        while len(prototypes) < prototypesPerClass:
            if j >= len(tests)-1:
                break 
            if tests[j].classification == clas:
                prototypes.append(tests[j])
            j += 1
        subTest.append(prototypes)
    
    for listTest in subTest:
        for test in listTest:
            minArg, maxArg = updateMinMax(test.params, minArg, maxArg)

    return classes, subTest, tests, minArg, maxArg