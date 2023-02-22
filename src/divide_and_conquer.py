def euclideanDistance(tuple1, tuple2):
    distance2 = 0
    for i in range(len(tuple1)):
        distance2 += ((tuple1[i] - tuple2[i])**2)
    return (distance2 ** (1/2))
