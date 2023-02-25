import random
from divide_and_conquer import *
from brute_force import bruteForce

running = True
while (running == True):
    n = int(input("Masukkan jumlah titik yang diinginkan (n): "))
    list = []
    for i in range(n):
        x = random.random()
        y = random.random()
        z = random.random()
        tuple = (x, y, z)
        list.append(tuple)
    print(list)
    distance, point1, point2 = bruteForce(list)
    d1, p1, p2 = closestPair(list, n)
    print("Jarak terdekat adalah ", distance)
    print("Jarak tersebut merupakan jarak antara 2 titik yaitu")
    print(point1)
    print(point2)

    print("Jarak terdekat adalah ", d1)
    print(p1)
    print(p2)
    stop = input("Apakah kamu ingin keluar dari program? (y/n)")
    if (stop == "y"):
        running = False
