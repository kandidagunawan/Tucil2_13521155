def euclideanDistance(tuple1, tuple2):
    distance2 = 0
    for i in range(len(tuple1)):
        distance2 += ((tuple1[i] - tuple2[i])**2)
    return (distance2 ** (1/2))


def bruteForce(list):
    distance = euclideanDistance(list[0], list[1])
    point1 = list[0]
    point2 = list[1]
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            temp = euclideanDistance(list[i], list[j])
            if (temp < distance):
                distance = temp
                point1 = list[i]
                point2 = list[j]

    return distance, point1, point2
