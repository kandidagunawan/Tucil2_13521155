from divide_and_conquer import euclideanDistance


def bruteForce(list):
    distance = euclideanDistance(list[0], list[1])
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            temp = euclideanDistance(list[i], list[j])
            if (temp < distance):
                distance = temp
                point1 = list[i]
                point2 = list[j]

    return distance, point1, point2
