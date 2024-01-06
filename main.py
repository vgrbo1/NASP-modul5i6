from formula3cnf import Formula3CNF
from klikaindsetgraf import KlikaINDSETGraf
from reduce3SAT import reduce3SATToIndSet, reduce3SATToClique
def main():
    # f = Formula3CNF()
    #f.unos3CNF()
    #f.setClauses([[1, 2, -5], [1, 2, 4], [2, -3, 4]])
    # f.rjesenje3CNF()
    #f.verifikacija3CNF((0,0,0,0,1))

    a = KlikaINDSETGraf()
    #a.unosGrafa()
    a.setAdjacencyList({1 : [2, 4, 5], 2 : [1, 3, 6], 3 : [2, 4, 7], 4 : [1, 3, 8], 5 : [1, 6, 8], 6 : [2, 5, 7], 7: [3, 8, 6], 8:[4, 5, 7]})
    a.rjesenjeKIndset(4)

    b = KlikaINDSETGraf()
    #b.unosGrafa()
    b.setAdjacencyList({})
    b.rjesenjeKClique(4)

    f1 = Formula3CNF()
    f1.setClauses([[1, -2, 3], [-1, 2, 4]])

    adjList1, k1, _ = reduce3SATToIndSet(f1)
    print(adjList1)

    f2 = Formula3CNF()
    f2.setClauses([[1,1,2],[-1,-2,-2],[-1,2,2]])
    adjList2, k2, _ = reduce3SATToClique(f2)
    print(adjList2)


if __name__ == '__main__':
    main()
