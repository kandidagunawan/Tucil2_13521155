def euclideanDistance(tuple1, tuple2):
    distance2 = 0
    for i in range(len(tuple1)):
        distance2 += ((tuple1[i] - tuple2[i])**2)
    return (distance2 ** (1/2))


def bruteForce(list):
    distance = euclideanDistance(list[0], list[1])
    listOfPoints = []
    point1 = list[0]
    point2 = list[1]
    points = [point1, point2]
    numEuc = 0
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            temp = euclideanDistance(list[i], list[j])
            numEuc += 1
            if (temp < distance):
                distance = temp
                point1 = list[i]
                point2 = list[j]
                points = [point1, point2]
                listOfPoints = [points]
            elif (temp == distance):
                listOfPoints.append(points)

    return distance, listOfPoints, numEuc


def printPasanganTitik(list):
    print("Berikut ini adalah pasangan titik dengan jarak terdekat:")
    for i in range(len(list)):
        print("Pasangan titik ke-", i+1)
        for j in range(2):
            print(list[i][j])
