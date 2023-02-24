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
