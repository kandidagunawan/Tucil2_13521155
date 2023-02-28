import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import itertools


def plotPoints(list, listOfPoints):
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("Points in 3D")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_zlabel("z-axis")
    colors = itertools.cycle(['orange', 'green', 'red', 'purple',
                             'brown', 'pink', 'gray', 'olive', 'cyan'])
    for i in range(len(listOfPoints)):
        c1 = next(colors)
        for j in range(2):
            x = listOfPoints[i][j][0]
            y = listOfPoints[i][j][1]
            z = listOfPoints[i][j][2]
            ax.scatter(x, y, z, c=c1)
    for i in range(len(list)):
        x = list[i][0]
        y = list[i][1]
        z = list[i][2]
        for j in range(len(listOfPoints)):
            if (list[i] not in listOfPoints[j]):
                ax.scatter(x, y, z, c='blue')
    plt.show()
