from selection import selection
from knn import knn
import time

def lvq1(dataset, prototypesPerClass, k):
	classes = []
	prototypes = []
	minArg = []
	maxArg = []
	tests = []

	classes, prototypes, trainSet, minArg, maxArg = selection(dataset, prototypesPerClass)

	for protClas in prototypes:
		for prototype in protClas:
			tests.append(prototype)

	prototypes = tests
	tests = []
	totalInd = len(prototypes)

	for i, prototype in enumerate(prototypes):
		knnClassification, neighbors = knn(classes, trainSet, minArg, maxArg, prototype, k)
		for neighbor in neighbors:
			if knnClassification == neighbor[1].classification:
				prototype.adjustParam(neighbor, True, i, totalInd)
			else: 
				prototype.adjustParam(neighbor, False, i, totalInd)
	return prototypes

			

def main():
	# datasets = ["Datasets/CM1_software_defect_prediction.csv", "Datasets/KC2_software_defect_prediction.csv"]
	datasets = ["Datasets/CM1_software_defect_prediction.csv"]
	k = 1
	prototypesPerClass = 10

	for dataset in datasets:
		tests = lvq1(dataset, prototypesPerClass, k)
	

main()
