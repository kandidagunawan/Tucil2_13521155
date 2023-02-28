from brute_force import bruteForce


def euclideanDistance(tuple1, tuple2):
    distance2 = 0
    for i in range(len(tuple1)):
        distance2 += ((tuple1[i] - tuple2[i])**2)
    return (distance2 ** (1/2))


def merge(arr, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle

    # Membuat 2 array temp
    L = [0 for i in range(n1)]
    R = [0 for i in range(n2)]

    for i in range(0, n1):
        L[i] = arr[left + i]

    for j in range(0, n2):
        R[j] = arr[middle + 1 + j]

    # Merge arr L dan R ke dalam arr
    i = 0     # Indeks dari array L
    j = 0     # Indeks dari array R
    k = left     # Indeks dari array arr

    while i < n1 and j < n2:
        if L[i][0] < R[j][0]:   # Membandingkan elemen pertama tuple
            arr[k] = L[i]
            i += 1
        # Jika elemen pertama tuple sama, cek elemen berikutnya sampai ada elemen yang berbeda
        elif L[i][0] == R[j][0]:
            temp = 0
            same = True
            while (same and temp < len(L[i])):
                if (L[i][temp] < R[j][temp]):
                    arr[k] = L[i]
                    i += 1
                    same = False
                elif (L[i][temp] > R[j][temp]):
                    arr[k] = R[j]
                    j += 1
                    same = False
                else:
                    temp += 1
            if (same):
                arr[k] = L[i]
                i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy sisa element dari L ke arr
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy sisa element daari R ke arr
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, left, right):
    if (left < right):
        middle = left + (right-left) // 2
        mergeSort(arr, left, middle)
        mergeSort(arr, middle + 1, right)
        merge(arr, left, middle, right)


def stripPoints(arr, distance, divider, middlePoint):
    points = []
    for i in range(middlePoint, len(arr)):
        # print('ini yg up')
        # print(arr[i][0])
        # print(divider[0])
        if (arr[i][0] - divider[0] > distance):
            break
        else:
            if (len(divider) == 1):
                points.append(arr[i])
            for j in range(len(divider)-1):
                if (arr[i][j] - divider[j] > distance):
                    # print('test')
                    break
                if (j == len(divider) - 2):
                    points.append(arr[i])
                    # print('check*')

    for i in range(middlePoint-1, -1, -1):
        # print('ini yg down')
        # print(arr[i][0])
        # print(divider[0])
        if (divider[0]-arr[i][0] > distance):
            break
        else:
            if (len(divider) == 1):
                points.append(arr[i])
            for j in range(len(divider)-1):
                if (divider[j]-arr[i][j] > distance):
                    break
                if (j == len(divider) - 2):
                    points.append(arr[i])
    return points


def stripPair(points):
    return bruteForce(points)


def closestPair(arr, n):
    if (n <= 3):
        return bruteForce(arr)
    else:
        middle = n//2
        distance1, listOfPoints1, numEuc1 = closestPair(
            arr[:middle], middle)
        distance2, listOfPoints2, numEuc2 = closestPair(
            arr[middle:n], n-middle)
        if (distance1 < distance2):
            distance = distance1
            listOfPoints = listOfPoints1
            # point1 = temp1_point1
            # point2 = temp1_point2
        elif (distance1 == distance2):
            listOfPoints = listOfPoints1 + listOfPoints2
        else:
            distance = distance2
            listOfPoints = listOfPoints2
            # point1 = temp2_point1
            # point2 = temp2_point2

        strips = stripPoints(arr, distance, arr[middle], middle)
        # print('ini strips ', strips)

        if (len(strips) >= 2):
            distanceStrip, listOfPointStrip, numEuc = stripPair(strips)
            if (distanceStrip < distance):
                distance = distanceStrip
                listOfPoints = listOfPointStrip
            elif (distanceStrip == distance):
                for x in listOfPointStrip:
                    if (x in listOfPointStrip):
                        continue
                    else:
                        listOfPoints.append(x)
            return distance, listOfPoints, (numEuc + numEuc1 + numEuc2)
        else:
            return distance, listOfPoints, (numEuc1 + numEuc2)
