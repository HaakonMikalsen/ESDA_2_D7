import os
import codecs
import csv
import numpy as np
import dataFinder 

dir_path = os.path.dirname(os.path.realpath(__file__))
filePath = dir_path+"/data/ampRespons"
fileList = os.listdir(filePath)

f_c = []
A_stopp = []
nameList =[]

for fileName in fileList:
    print(fileName)
    dataFile = codecs.open(filePath+"/"+fileName, encoding="utf-8", errors="ignore")
    skipLinesStart = 27
    skipLinesEnd = -2
    f,A= np.array(list(csv.reader(dataFile.readlines()[skipLinesStart:skipLinesEnd]))).T
    dataFile.close()


    f = np.array([element for element in f],dtype=float)
    A = np.array([element for element in A],dtype=float)
    nameList.append(fileName)
    f_c.append(dataFinder.findValueInterpolate(A,-3,f))
    A_stopp.append(dataFinder.findValueInterpolate(f,4500,A))


combined = list(zip(A_stopp, nameList, f_c))
combined.sort(key=lambda x: x[0])  # sort by A_stopp

A_stopp[:], nameList[:], f_c[:] = zip(*combined)

for elements in zip(nameList,f_c,A_stopp):
    print(f"Name: {elements[0]} f_c: {float(elements[1]):.2f} A_stopp: {float(elements[2]):.2f}")

print(f"Avg fc = {np.mean(np.array(f_c)):.2f}±{np.std(np.array(f_c),ddof=1):.2f} Avg A_stopp = {np.mean(np.array(A_stopp)):.2f}±{np.std(np.array(A_stopp),ddof=1):.2f}")

