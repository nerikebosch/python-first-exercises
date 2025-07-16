import random
import matplotlib.pyplot as plt

def random_walk(n):

    l = 0
    x = [0] * n
    y = [0] * n

    for i in range(1,n):
        val = random.randint(1, 4)
        if val == 1:
            x[i] = x[i - 1] + 1
            y[i] = y[i - 1]
        elif val == 2:
            x[i] = x[i - 1] - 1
            y[i] = y[i - 1]
        elif val == 3:
            x[i] = x[i - 1]
            y[i] = y[i - 1] + 1
        else:
            x[i] = x[i - 1]
            y[i] = y[i - 1] - 1
            l += 1

    coordinates = list(zip(x,y))
    return coordinates


def main():
    n = 100
    coordinates = random_walk(n)
    x, y = zip(*coordinates)

    plt.plot(x, y, marker='o', linestyle='-', markersize=2)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Walker\'s Trajectory')
    plt.grid(True)
    plt.show()

main()