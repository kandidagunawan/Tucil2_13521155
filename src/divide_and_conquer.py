from basic_functions import *


def merge(arr, left, middle, right, koordinat):
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
        if L[i][koordinat] < R[j][koordinat]:   # Membandingkan elemen ke-koordinat tuple
            arr[k] = L[i]
            i += 1
        # Jika elemen pertama tuple sama, cek elemen berikutnya sampai ada elemen yang berbeda
        elif L[i][koordinat] == R[j][koordinat]:
            temp = 0
            sama = True
            while (sama and temp < len(L[i])):
                if (L[i][temp] > R[j][temp]):
                    arr[k] = R[j]
                    j += 1
                    sama = False
                elif (L[i][temp] < R[j][temp]):
                    arr[k] = L[i]
                    i += 1
                    sama = False
                else:
                    temp += 1
            if (sama):
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


def mergeSort(arr, left, right, koordinat):
    if (left < right):
        middle = left + (right-left) // 2
        mergeSort(arr, left, middle, koordinat)
        mergeSort(arr, middle + 1, right, koordinat)
        merge(arr, left, middle, right, koordinat)


def stripPoints(arr, distance, divider, middlePoint):
    points = []
    for i in range(middlePoint, len(arr)):
        if (arr[i][0] - divider[0] > distance):
            break
        else:
            points.append(arr[i])
    for i in range(middlePoint-1, -1, -1):
        if (divider[0]-arr[i][0] > distance):
            break
        else:
            points.append(arr[i])
    return points


def closestPair(arr, n):
    if (n <= 3):
        return bruteForce(arr)  # base case
    else:
        middle = n//2
        distance1, listOfPoints1, numEuc1 = closestPair(  # mencari closest pair pada s1
            arr[:middle], middle)
        distance2, listOfPoints2, numEuc2 = closestPair(  # mencari closest pair pada s2
            arr[middle:n], n-middle)
        if (distance1 < distance2):
            distance = distance1
            listOfPoints = listOfPoints1
        elif (distance1 == distance2):
            listOfPoints = listOfPoints1 + listOfPoints2
        else:
            distance = distance2
            listOfPoints = listOfPoints2

        strips = stripPoints(arr, distance, arr[middle], middle)

        if (len(strips) >= 2):
            distanceStrip, listOfPointStrip, numEuc = bruteForce(
                strips)  # mencari closest pair pada s3
            if (distanceStrip < distance):
                distance = distanceStrip
                listOfPoints = listOfPointStrip
            elif (distanceStrip == distance):
                for x in listOfPointStrip:
                    if (x in listOfPoints):
                        continue
                    else:
                        listOfPoints.append(x)
            return distance, listOfPoints, (numEuc + numEuc1 + numEuc2)
        else:
            return distance, listOfPoints, (numEuc1 + numEuc2)
