from selection import selection
from knn import knn
import time

def adjustParam(startTime, testInstance, trainSetInstance):
	currentTime = time.time() - startTime
	func = -1 * (currentTime ** 2)

def lvq1(dataset, prototypesPerClass, k):
	classes = []
	prototypes = []
	minArg = []
	maxArg = []
	tests = []

	classes, prototypes, minArg, maxArg = selection(dataset, prototypesPerClass)

	for protClas in prototypes:
		for prototype in protClas:
			tests.append(prototype)
	
	for test in tests:
		knnClassification = knn(classes, tests, minArg, maxArg, test, k)
		if knnClassification == test.classification:
			# Arproxima o prototipo da instancia de treino
			pass
		else: 
			# Afasta o prototipo da instancia de treino
			pass

	return tests

			

def main():
	datasets = ["Datasets/CM1_software_defect_prediction.csv", "Datasets/KC2_software_defect_prediction.csv"]
	k = 1
	prototypesPerClass = 10

	for dataset in datasets:
		lvq1(dataset, prototypesPerClass, k)

main()