from itertools import combinations
class KlikaINDSETGraf:

    def __init__(self, adjacencyList = {}):
        self.adjacencyList = adjacencyList

    def unosGrafa(self):
        self.adjacencyList = {}
        numberOfVertices = int(input("Unesite broj cvorova grafa:"))
        if numberOfVertices > 15:
            raise ValueError("Broj cvorova ne smije biti veci od 15")

        print("Unesite listu susjedstva za svaki cvor: ")
        for v in range(1, numberOfVertices + 1):
            adjList = input()
            adjList = [int(x) for x in adjList.split()]
            self.adjacencyList[v] = adjList
        

    def rjesenjeKIndset(self, k):
        kVertexSubsets = list(combinations(self.adjacencyList.keys(), k))

        for vertices in kVertexSubsets:
            if self.verifikacijaIndset(vertices):
                print("Indset: ", vertices)
                return 1

        return 0

    def rjesenjeKClique(self, k):
        kVertexSubsets = list(combinations(self.adjacencyList.keys(), k))

        for vertices in kVertexSubsets:
            if self.verifikacijaClique(vertices):
                print(f"{k}-Clique: ", vertices)
                return 1
        return 0

    def verifikacijaIndset(self, vertices):
        for vertex in vertices:
            neighbors = self.adjacencyList[vertex]
            for neighbor in neighbors:
                if neighbor in vertices:
                    return 0

        return 1

    def verifikacijaClique(self, vertices):
        for i in range(len(vertices)):
            for j in range(i + 1, len(vertices)):
                if vertices[j] not in self.adjacencyList[vertices[i]]:
                    return 0

        return 1

    def setAdjacencyList(self, adjacencyList):
        self.adjacencyList = adjacencyList
