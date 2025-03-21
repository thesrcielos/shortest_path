import sys
from shortestpath import algorithms
from shortestpath import execution_time_gathering
import matplotlib.pyplot as plt

def graphicsAlgorithms():
    minimum_size = 40
    maximum_size = 120
    step = 20
    samples_by_size = 5
    
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)

    print("Size | # Relations | Bellman Ford | Dijstra | A* ")
    for row in table:
        print(row)

    # La primera columna será el eje X
    x = [row[0] for row in table]
    # Las siguientes columnas serán los valores de Y
    y1 = [row[2][0] for row in table]
    y2 = [row[3][0] for row in table]
    y3 = [row[4][0] for row in table]

    # Crear el gráfico
    plt.plot(x, y1, label="Bellman Ford", color='blue')
    plt.plot(x, y2, label="Dijsktra", color='green')
    plt.plot(x, y3, label="A*", color='red')

    plt.title('Comparation Shortest Path algorithms')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    y1 = [row[2][1] for row in table]
    y2 = [row[3][1] for row in table]
    y3 = [row[4][1] for row in table]

    plt.plot(x, y1, label="Bellman Ford", color='blue')
    plt.plot(x, y2, label="Dijsktra", color='green')
    plt.plot(x, y3, label="A*", color='red')

    plt.title('Comparation Shortest Path algorithms Memory Usage')
    plt.xlabel('Size')
    plt.ylabel('Memory')
    plt.legend()
    plt.show()

def graphicsDijstraAstar():
    minimum_size = 100
    maximum_size = 500
    step = 50
    samples_by_size = 5
    table = execution_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size, True)
    print("Size | # Relations | Dijstra | A*")
    for row in table:
        print(row)

    # La primera columna será el eje X
    x = [row[0] for row in table]
    # Las siguientes columnas serán los valores de Y
    y1 = [row[2][0] for row in table]
    y2 = [row[3][0] for row in table]

    # Crear el gráfico
    plt.plot(x, y1, label="Dijkstra", color='blue')
    plt.plot(x, y2, label="A*", color='green')

    plt.title('Comparation Shortest Path algorithms')
    plt.xlabel('Size')
    plt.ylabel('Time')
    plt.legend()
    plt.show()

    y1 = [row[2][1] for row in table]
    y2 = [row[3][1] for row in table]

    plt.plot(x, y1, label="Dijkstra", color='blue')
    plt.plot(x, y2, label="A*", color='green')

    plt.title('Comparation Shortest Path algorithms Memory Usage')
    plt.xlabel('Size')
    plt.ylabel('Memory')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    graphicsAlgorithms()
    graphicsDijstraAstar()
