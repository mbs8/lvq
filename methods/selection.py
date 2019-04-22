from readCsv import readCsv

# Algoritmo para selecionar os protótipos
def selection(dataSet, prototypesPerClass):
    classes = []                # Array contendo as classes das instancias
    tests = []                  # Array contendo todas as instancias 
    minArg = []                 # Array contendo o valor minimo de cada parâmetro 
    maxArg = []                 # Array contendo o máximo de cada parâmetro
    subTest = [[]]              # Array contendo o subconjunto que será retornado pelo selection

    classes, tests, minArg, maxArg = readCsv(dataSet)

    for i, clas in enumerate(classes):
        j = 0
        subTest[1] = []
        print(subTest)
        while len(subTest[i]) < prototypesPerClass:
            if j >= len(tests)-1:
                break 
            if tests[j].classification == clas:
                subTest[i].append(tests[j])
            j += 1
        
    return classes, subTest, minArg, maxArg

selection("../Datasets/CM1_software_defect_prediction.csv", 5)