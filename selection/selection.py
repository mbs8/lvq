from crossfold.knn.knn import readCsv

def selection(dataSet, prototypesPerClass):
    classes = []                # Array contendo as classes das instancias
    tests = []                  # Array contendo todas as instancias 
    minArg = []                 # Array contendo o valor minimo de cada parâmetro 
    maxArg = []                 # Array contendo o máximo de cada parâmetro
    subTest = [[]]              # Array contendo o subconjunto que será retornado pelo selection

    classes, tests, minArg, maxArg = readCsv(dataSet)

    for i, clas in enumerate(classes):
        j = 0
        while len(subTest[i]) < prototypesPerClass:
            if tests[j].classification == clas:
                subTest[i].append(tests[j])
            j += 1
        
    return classes, subTest, minArg, maxArg
