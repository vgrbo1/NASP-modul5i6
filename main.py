from formula3cnf import Formula3CNF
from klikaindsetgraf import KlikaINDSETGraf
from reduce3SAT import reduce3SATToIndSet, reduce3SATToClique
def main():
    # f = Formula3CNF()
    #f.unos3CNF()
    #f.setClauses([[1, 2, -5], [1, 2, 4], [2, -3, 4]])
    # f.rjesenje3CNF()
    #f.verifikacija3CNF((0,0,0,0,1))

    # a = KlikaINDSETGraf()
    #a.unosGrafa()
    # a.setAdjacencyList({1 : [2, 4, 5], 2 : [1, 3, 6], 3 : [2, 4, 7], 4 : [1, 3, 8], 5 : [1, 6, 8], 6 : [2, 5, 7], 7: [3, 8, 6], 8:[4, 5, 7]})
    # a.rjesenjeKIndset(4)

    # b = KlikaINDSETGraf()
    #b.unosGrafa()
    # b.setAdjacencyList({1: [2, 6], 2: [1, 3, 5, 6], 3: [2,4,5,6], 4: [3,5], 5:[3,4,2,6], 6:[1,2,3,5]})
    # b.rjesenjeKClique(4)

    # f1 = Formula3CNF()
    # f1.setClauses([[1, -2, 3], [-1, 2, 4]])

    # adjList1, k1, _ = reduce3SATToIndSet(f1)
    # print(adjList1)

    # f2 = Formula3CNF()
    # f2.setClauses([[1,1,2],[-1,-2,-2],[-1,2,2]])
    # adjList2, k2, _ = reduce3SATToClique(f2)
    # print(adjList2)
    formula = Formula3CNF()
    graf = KlikaINDSETGraf()

    while True:
      print("\nMENU:")
      print("1) Unos formule")
      print("2) Unos grafa")
      print("3) Je li formula ispunjiva")
      print("4) Postoji li k-nezavisnih čvorova")
      print("5) Postoji li k-klika")
      print("6) Verifikacija formule")
      print("7) Verifikacija skupa nezavisnih čvorova")
      print("8) Verifikacija k-klike")
      print("9) Redukcija 3-SAT-TO-INDSET")
      print("10) Redukcija 3-SAT-TO-CLIQUE")
      print("11) Izlaz")
    
      choice = input("Unesite opciju: ")
    
      if choice == '1':
          formula.unos3CNF()
      elif choice == '2':
          graf.unosGrafa()
      elif choice == '3':
          if formula.rjesenje3CNF():
              print("Formula je ispunjiva.")
          else:
              print("Formula nije ispunjiva.")
      elif choice == '4':
          k = int(input("Unesite broj k-nezavisnih čvorova (k): "))
          if graf.rjesenjeKIndset(k):
              print(f"Postoji skup nezavisnih čvorova s barem {k} čvorova.")
          else:
              print(f"Ne postoji skup nezavisnih čvorova s barem {k} čvorova.")
      elif choice == '5':
          k = int(input("Unesite broj k-klike (k): "))
          if graf.rjesenjeKClique(k):
              print(f"Postoji {k}-klika.")
          else:
              print(f"Ne postoji {k}-klika.")
      elif choice == '6':
          values = input(f"Unesite {formula.numOfVariables} vrijednosti logičkih varijabli (0 ili 1, odvojeno zarezom): ")
          values = [int(x) for x in values.split(',')]
          if formula.verifikacija3CNF(values):
              print("Formula je ispunjiva za zadane vrijednosti logičkih varijabli.")
          else:
              print("Formula nije ispunjiva za zadane vrijednosti logičkih varijabli.")
      elif choice == '7':
          vertices = input("Unesite čvorove razdvojene zarezom: ")
          vertices = [int(x) for x in vertices.split(',')]
          if graf.verifikacijaIndset(vertices):
              print("Uneseni skup čvorova jeste nezavisni skup.")
          else:
              print("Uneseni skup čvorova nije nezavisni skup.")
      elif choice == '8':
          vertices = input("Unesite čvorove razdvojene zarezom: ")
          vertices = [int(x) for x in vertices.split(',')]
          if graf.verifikacijaClique(vertices):
              print("Uneseni skup čvorova jeste klika.")
          else:
              print("Uneseni skup čvorova nije klika.")
      elif choice == '9':
          adjacencyList, k, literalVertices = reduce3SATToIndSet(formula)
          print("3-SAT-TO-INDSET:")
          print("Adjacency List:", adjacencyList)
          print("k:", k)
          #print("Literal Vertices:", literalVertices)
      elif choice == '10':
          adjacencyList, k, verticesAndLiterals = reduce3SATToClique(formula)
          print("3-SAT-TO-CLIQUE:")
          print("Adjacency List:", adjacencyList)
          print("k:", k)
          #print("Vertices and Literals:", verticesAndLiterals)
      elif choice == '11':
          print("Izlaz")
          break
      else:
          print("Nevažeća opcija. Pokušajte ponovno.")
    

if __name__ == '__main__':
    main()
