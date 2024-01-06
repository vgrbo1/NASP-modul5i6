def reduce3SATToIndSet(formula3CNF):
    clauses = formula3CNF.clauses
    adjacencyList = {}
    n = formula3CNF.numOfVariables
    literalVertices = {i : [] for i in range(-n, 0) }
    literalVertices.update({i : [] for i in range(1, n + 1) })
    k = len(clauses)
    i = 1
    for clause in clauses:
        lit1, lit2, lit3 = clause

        adjacencyList[i] = [i + 1, i + 2]
        literalVertices[lit1].append(i)

        adjacencyList[i + 1] = [i, i + 2]
        literalVertices[lit2].append(i + 1)

        adjacencyList[i + 2] = [i, i + 1]
        literalVertices[lit3].append(i + 2)
        i += 3

    for key in literalVertices.keys():
        for vertex in literalVertices[key]:
            adjacencyList[vertex] += literalVertices[-key]

    return adjacencyList, k, literalVertices

def reduce3SATToClique(formula3CNF):
    clauses = formula3CNF.clauses
    adjacencyList = {}
    n = formula3CNF.numOfVariables
    verticesAndLiterals = {}
    k = len(clauses)
    graphVertices = [[i + 1, i + 2, i + 3] for i in range(0, k*3, 3)]
    i = 1
    for clause in clauses:
        lit1, lit2, lit3 = clause

        adjacencyList[i] = []
        verticesAndLiterals[i] = lit1

        adjacencyList[i + 1] = []
        verticesAndLiterals[i + 1] = lit2

        adjacencyList[i + 2] = []
        verticesAndLiterals[i + 2] = lit3
        i += 3
    
    for row in graphVertices:
        for vertex in row:

            for i in range(1, k*3 + 1):
                if i not in row and verticesAndLiterals[vertex] != -1 * verticesAndLiterals[i]:
                    adjacencyList[vertex].append(i)


    return adjacencyList, k, verticesAndLiterals
