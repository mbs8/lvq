from selection import selection

def lvq1(dataset):
    classes = []
    prototypes = []
    minArg = []
    maxArg = []
    prototypesPerClass = 10

    classes, prototypes, minArg, maxArg = selection(dataset, prototypesPerClass)
    


def main():
	datasets = ["Datasets/CM1_software_defect_prediction.csv", "Datasets/KC2_software_defect_prediction.csv"]

	for dataset in datasets:
		lvq1(dataset)

main()