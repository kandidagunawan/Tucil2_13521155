import random
from divide_and_conquer import *
from brute_force import bruteForce
from timeit import default_timer as timer

print('    __  _       ___   _____   ___  _____ ______      ____   ____  ____  ____        ___   _____      ____   ___  ____  ____   ______  _____')
print('   /  ]| |     /   \ / ___/  /  _]/ ___/|      |    |    \ /    ||    ||    \      /   \ |     |    |    \ /   \|    ||    \ |      |/ ___/')
print(
    '  /  / | |    |     (   \_  /  [_(   \_ |      |    |  o  )  o  | |  | |  D  )    |     ||   __|    |  o  )     ||  | |  _  ||      (   \_ ')
print(' /  /  | |___ |  O  |\__  ||    _]\__  ||_|  |_|    |   _/|     | |  | |    /     |  O  ||  |_      |   _/|  O  ||  | |  |  ||_|  |_|\__  |')
print(
    '/   \_ |     ||     |/  \ ||   [_ /  \ |  |  |      |  |  |  _  | |  | |    \     |     ||   _]     |  |  |     ||  | |  |  |  |  |  /  \ |')
print('\     ||     ||     |\    ||     |\    |  |  |      |  |  |  |  | |  | |  .  \    |     ||  |       |  |  |     ||  | |  |  |  |  |  \    |')
print(' \____||_____| \___/  \___||_____| \___|  |__|      |__|  |__|__||____||__|\_|     \___/ |__|       |__|   \___/|____||__|__|  |__|   \___|')

print('                                  ____    ___  ____     ___  ____    ____  ______   ___   ____')
print('                                 /    |  /  _]|    \   /  _]|    \  /    ||      | /   \ |    \  ')
print(
    '                                |   __| /  [_ |  _  | /  [_ |  D  )|  o  ||      ||     ||  D  )   ')
print('                                |  |  ||    _]|  |  ||    _]|    / |     ||_|  |_||  O  ||    /     ')
print(
    '                                |  |_ ||   [_ |  |  ||   [_ |    \ |  _  |  |  |  |     ||    \       ')
print('                                |     ||     ||  |  ||     ||  .  \|  |  |  |  |  |     ||  .  \        ')
print('                                |___,_||_____||__|__||_____||__|\_||__|__|  |__|   \___/ |__|\_|    ')
print('\n')
print('---------------------------------------------------------------------------------------------------------------------------------------------')
print('\n')
running = True
while (running == True):
    dimensi = int(input("Masukkan dimensi dari titik yang diinginkan: "))
    n = int(input("Masukkan jumlah titik yang diinginkan (n): "))
    list = []
    for i in range(n):
        tuple = ()
        for j in range(dimensi):
            temp = random.random()
            tuple += (temp,)
        list.append(tuple)
    for i in range(n):
        print('Point', i+1, ":", list[i])

    start1 = timer()
    distance, point1, point2 = bruteForce(list)
    end1 = timer()

    start2 = timer()
    mergeSort(list, 0, n-1)
    d1, p1, p2 = closestPair(list, n)
    end2 = timer()

    print('\n')
    print("BRUTE FORCE")
    print("Jarak terdekat antara 2 titik berdasarkan BRUTE FORCE adalah ", distance)
    print("Jarak tersebut merupakan jarak antara 2 titik yaitu:")
    print(point1)
    print(point2)
    print("Waktu yang dibutuhkan oleh brute force: ")
    print(end1-start1, ' detik')

    print('\n')
    print('DIVIDE AND CONQUER')
    print("Jarak terdekat antara 2 titik berdasarkan DIVIDE AND CONQUER adalah ", d1)
    print("Jarak tersebut merupakan jarak antara 2 titik yaitu:")
    print(p1)
    print(p2)
    print("Waktu yang dibutuhkan oleh divide and conquer:")
    print(end2-start2, ' detik')
    print('\n')
    stop = input("Apakah kamu ingin keluar dari program? (y/n)")
    print('\n')
    print('\n')
    if (stop == "y"):
        running = False
