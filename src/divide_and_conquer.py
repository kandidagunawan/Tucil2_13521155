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


# def compare2Points(tuple1, tuple2, distance):
#     n = len(tuple1)
#     below = True
#     for i in range(n):
#         if ((tuple1[i]-tuple2[j]) >= distance) and (tuple[i]-tuple[j] <= (distance*(-1)))):
#             below=False
#             break
#     return below

def stripPoints(arr, distance, divider, middlePoint):
    points = []
    for i in range(middlePoint, len(arr)):
        for j in range(len(divider)-1):
            if (arr[i][j] - divider[j] > distance):
                break
            if (j == len(divider) - 1):
                points.append(arr[i])
        else:
            continue
        break
    for i in range(middlePoint, -1):
        for j in range(len(divider)-1):
            if (arr[i][j] - divider[j] > distance):
                break
            if (j == len(divider) - 1):
                points.append(arr[i])
        else:
            continue
        break
    return points


def stripPair(points):
    return bruteForce(points)


def closestPair(arr, n):
    if (n <= 3):
        return bruteForce(arr)
    else:
        middle = n//2
        distance1, temp1_point1, temp1_point2 = closestPair(
            arr[:middle], middle)
        distance2, temp2_point1, temp2_point2 = closestPair(
            arr[middle:n], n-middle)
        if (distance1 < distance2):
            distance = distance1
            point1 = temp1_point1
            point2 = temp1_point2
        else:
            distance = distance2
            point1 = temp2_point1
            point2 = temp2_point2
        distanceStrip, point1Strip, point2Strip = stripPair(arr)
        if (distanceStrip < distance):
            distance = distanceStrip
            point1 = point1Strip
            point2 = point2Strip
    return distance, point1, point2


arr = [(12, 15, 5, 7), (12, 11, 13, 6),
       (5, 6, 7, 9), (5, 6, 3, 10), (1, 7, 9, 10)]
n = len(arr)
print("Given array is")
for i in range(n):
    print(arr[i], end=" ")

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
    print(arr[i], end=" ")

print(closestPair(arr, n))
print(bruteForce(arr))
