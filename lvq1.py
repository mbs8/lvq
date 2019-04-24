from selection import selection
from knn import knn
from crossfold import crossFold
from readCsv import readCsv
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
	totalIndex  = int((len(trainSet) * (1 - learningRate)) / 2)
	while actualIndex < totalIndex:
		i = 0
		while i < len(trainSet):
			knnClassification, neighbors = knn(classes, prototypes, minArg, maxArg, trainSet[i], k)
			j = 0
			while j < len(neighbors):
				if knnClassification == neighbors[j][1].classification:
					neighbors[j][1].adjustParam(trainSet[i], True, actualIndex, totalIndex)
				else: 
					neighbors[j][1].adjustParam(trainSet[i], False, actualIndex, totalIndex)
				j += 1
			i += 1
		i = 0
		actualIndex += 1

	return prototypes, classes, minArg, maxArg, trainSet

			

def main():
	datasets = ["Datasets/CM1_software_defect_prediction.csv", "Datasets/KC2_software_defect_prediction.csv"]
	kValues = [1,3]											# K para o algoritmo do knn
	prototypesPerClass = [10, 20, 30]						# Número de protótipos por classe
	learningRate = 0.95										# Velocidade da taxa de aprendizagem do algoritmo
	foldSize = 10											# Tamanho das subdivisoes do crossFold

	startTime = 0
	currentTime = 0
	for dataset in datasets:
		print("\nDataset: " + str(dataset) + "\n")
		for k in kValues:
			print("K = " + str(k) + "\n")
			startTime = time.time()
			classesOrigin, tests, minArgOrigin, maxArgOrigin = readCsv(dataset)
			currentTime = time.time() - startTime
			print("Knn Original")
			print(str(crossFold(classesOrigin, tests, minArgOrigin, maxArgOrigin, k, foldSize)))
			print("Tempo gasto: " + str(currentTime) + "\n")
			
			for prot in prototypesPerClass:
				startTime = time.time()
				prototypes, classes, minArg, maxArg, _ = lvq1(dataset, prot, learningRate, k)
				currentTime = time.time() - startTime
				print("LVQ1 - LearningRate = " + str(learningRate) + "; Prototypes per Class = " + str(prot))
				print(crossFold(classes, prototypes, minArg, maxArg, k, foldSize))
				print("Tempo gasto: " + str(currentTime) + "\n")
		print("\n----------------------------------------------------------------------------------------------------------")