from selection.selection import selection

def lvq1():
    classes = []
    tests = []
    minArg = []
    maxArg = []
    prototypesPerClass = 10

    for dataset in dataSets:
        classes, tests, minArg, maxArg = selection(dataset, prototypesPerClass)
        print(tests)

def main():
	