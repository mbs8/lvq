from selection.selection import selection
def lvq1():
    dataSets = ["../Datasets/CM1_software_defect_prediction.csv", "../Datasets/KC2_software_defect_prediction.csv"]
    classes = []
    tests = []
    minArg = []
    maxArg = []
    prototypesPerClass = 10

    for dataset in dataSets:
        classes, tests, minArg, maxArg = selection(dataset, prototypesPerClass)
        print(tests)
        