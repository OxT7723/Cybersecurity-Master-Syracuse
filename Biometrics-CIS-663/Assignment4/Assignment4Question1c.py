import csv
import numpy as np


iris = []

with open('iris.data', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        p = (float(row[0]), float(row[1]), float(row[2]), float(row[3]))
        iris.append(p)

lowestValue = -99.99
matchingPair = []


for x in range(len(iris)):
    point1 = np.array(iris[x])

    for i in range(x, len(iris)):
        if x != i:
            point2 = np.array(iris[i])
            
            dist = np.dot(point1, point2)/(np.linalg.norm(point1)*np.linalg.norm(point2))
            

            if lowestValue is None or lowestValue < dist :
                lowestValue = dist
                matchingPair = (x, i)

print("The closest pairs for cosine similarity {0} and {1} with distance of {2}".format(iris[matchingPair[0]], iris[matchingPair[1]], lowestValue ))