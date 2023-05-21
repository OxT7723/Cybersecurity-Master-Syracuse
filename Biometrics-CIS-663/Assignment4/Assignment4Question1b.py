import csv
import numpy as np

iris = []

with open('iris.data', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        p = (float(row[0]), float(row[1]), float(row[2]), float(row[3]))
        iris.append(p)

lowestValue = 99.99
matchingPair = []

for x in range(len(iris)):
    point1 = np.array(iris[x])
    #print(point1[0])
    for i in range(x, len(iris)):
        if x != i:
            point2 = np.array(iris[i])
            dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) + abs(point1[2] - point2[2]) + abs(point1[3] - point2[3]) 
            
            #dist = np.linalg.norm(point1 - point2)

            if lowestValue is None or lowestValue > dist :
                lowestValue = dist
                matchingPair = (x, i)
                print(matchingPair)

print("The closest pairs for Mahattan distance are {0} and {1} with distance of {2}".format(iris[matchingPair[0]], iris[matchingPair[1]], lowestValue ))