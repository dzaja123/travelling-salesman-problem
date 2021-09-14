def Solution(put):

    cities = list(range(len(put)))
    solution = []

    for i in range(len(put)):
        CityA = cities[0]
        solution.append(CityA)
        cities.remove(CityA)

    return solution

def routeLength(put, solution):

    routeLength = 0

    for i in range(len(solution)):
        routeLength += put[solution[i - 1]][solution[i]]
    return routeLength

def getNeighbours(solution):

    neighbours = []

    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

def getBestNeighbour(put, neighbours):

    bestRouteLength = routeLength(put, neighbours[0])
    bestNeighbour = neighbours[0]

    for neighbour in neighbours:
        currentRouteLength = routeLength(put, neighbour)
        if currentRouteLength < bestRouteLength:
            bestRouteLength = currentRouteLength
            bestNeighbour = neighbour
    return bestNeighbour, bestRouteLength

def hillClimbing(put):

    currentSolution = Solution(put)
    currentRouteLength = routeLength(put, currentSolution)
    neighbours = getNeighbours(currentSolution)
    bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(put, neighbours)

    while bestNeighbourRouteLength < currentRouteLength:
        currentSolution = bestNeighbour
        currentRouteLength = bestNeighbourRouteLength
        neighbours = getNeighbours(currentSolution)
        bestNeighbour, bestNeighbourRouteLength = getBestNeighbour(put, neighbours)

    print("\nNajbolja ruta: ", currentSolution)
    print("Cena: ", currentRouteLength)

def main():
    
    put = [
        [0, 7, 6, 10, 13],
        [7, 0, 7, 10, 10],
        [6, 7, 0, 8, 9],
        [10, 10, 8, 0, 6],
        [13, 10, 9, 6, 0]
        ]
    
    print("Optimizacija puta trgovca: ", put)
    hillClimbing(put)
    
if __name__ == "__main__":
    main()
