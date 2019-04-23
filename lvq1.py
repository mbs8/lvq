from selection import selection
from knn import knn
import time

def lvq1(dataset, prototypesPerClass, learningRate, k):
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

	actualIndex = 0
	totalIndex  = len(trainSet) / learningRate  
	while actualIndex < totalIndex:
		i = 0
		while i < len(prototypes):
			knnClassification, neighbors = knn(classes, trainSet, minArg, maxArg, prototypes[i], k)
			j = 0
			while j < len(neighbors):
				if knnClassification == neighbors[j][1].classification:
					prototypes[i].adjustParam(neighbors[j][1], True, actualIndex, totalIndex)
				else: 
					prototypes[i].adjustParam(neighbors[j][1], False, actualIndex, totalIndex)
				j += 1
			i += 1
		i = 0
		actualIndex += 1

	return prototypes

			

def main():
	# datasets = ["Datasets/CM1_software_defect_prediction.csv", "Datasets/KC2_software_defect_prediction.csv"]
	datasets = ["Datasets/CM1_software_defect_prediction.csv"]
	k = 1											# K para o algoritmo do knn
	prototypesPerClass = 10							# Número de protótipos por classe
	learningRate = 10								# Velocidade da taxa de aprendizagem do algoritmo

	for dataset in datasets:
		lvq1(dataset, prototypesPerClass, learningRate, k)
	

main()
