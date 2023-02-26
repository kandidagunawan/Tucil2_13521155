import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plotPoints(list, point1, point2):
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title("Points in 3D")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_zlabel("z-axis")
    for i in range(len(list)):
        x = list[i][0]
        y = list[i][1]
        z = list[i][2]
        if ((point1[0] == list[i][0] and point1[1] == list[i][1] and point1[2] == list[i][2]) or (point2[0] == list[i][0] and point2[1] == list[i][1] and point2[2] == list[i][2])):
            ax.scatter(x, y, z, c="red")
        else:
            ax.scatter(x, y, z, c="blue")
        # plot the point (2,3,4) on the figure
    plt.show()


# list = [(3, 6, 2), (1, 7, 9), (-5, -9, 2)]
# plotPoints(list, (3, 6, 2), (1, 7, 9))
