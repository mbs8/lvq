from selection import selection
from knn import knn
from crossfold import crossFold
from readCsv import readCsv
from lvq1 import lvq1
from Instance import Instance
import time

def window(x, ei, ej, w, minArg, maxArg):
	di = ei.euclideanDistance(x, minArg, maxArg)
	dj = ej.euclideanDistance(x, minArg, maxArg)

	if di == 0 or dj == 0:
		return False

	return (min((di/dj),(dj/di)) > ((1 - w) /(1 + w)))

def lvq2(dataset, prototypesPerClass, learningRate, k, w):
	classes = []
	prototypes = []
	minArg = []
	maxArg = []
	trainSet = []

	prototypes, classes, minArg, maxArg, trainSet = lvq1(dataset, prototypesPerClass, learningRate, k)

	actualIndex = 0
	totalIndex  = len(trainSet) / learningRate  
	while actualIndex < totalIndex:
		i = 0
		while i < len(prototypes):
			knnClassification, neighbors = knn(classes, trainSet, minArg, maxArg, prototypes[i], k)
			knnClassification1, _ = knn(classes, trainSet, minArg, maxArg, prototypes[i+1], k)
			j = 0
			while j < len(neighbors):
				if window(neighbors[j][1], prototypes[i], prototypes[i+1], w, minArg, maxArg):
					if knnClassification != knnClassification1:
						if knnClassification == neighbors[j][1]:
							prototypes[i].adjustParam(neighbors[j][1], False, actualIndex, totalIndex)
							prototypes[i+1].adjustParam(neighbors[j][1], True, actualIndex, totalIndex)
						else:
							prototypes[i].adjustParam(neighbors[j][1], True, actualIndex, totalIndex)
							prototypes[i+1].adjustParam(neighbors[j][1], False, actualIndex, totalIndex)
				j += 1
			i += 2
		i = 0
		actualIndex += 1

	return prototypes, classes, minArg, maxArg

			

def main():
	datasets = ["Datasets/CM1_software_defect_prediction.csv", "Datasets/KC2_software_defect_prediction.csv"]
	kValues = [1,3]											# K para o algoritmo do knn
	prototypesPerClass = [10, 20, 30]						# Número de protótipos por classe
	learningRate = 5										# Velocidade da taxa de aprendizagem do algoritmo
	foldSize = 10											# Tamanho das subdivisoes do crossFold
	w = 0.5													# Largura da janela para o LVQ2

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
				prototypes, classes, minArg, maxArg = lvq2(dataset, prot, learningRate, k, w)
				currentTime = time.time() - startTime
				print("LVQ2 - LearningRate = " + str(learningRate) + "; Prototypes per Class = " + str(prot) + "; Window = " + str(w))
				print(crossFold(classes, prototypes, minArg, maxArg, k, foldSize))
				print("Tempo gasto: " + str(currentTime) + "\n")
		print("\n----------------------------------------------------------------------------------------------------------")
			
	

main()
