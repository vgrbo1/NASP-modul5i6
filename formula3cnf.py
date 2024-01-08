from itertools import product
class Formula3CNF:

    def __init__(self, clauses = []):
        self.setClauses(clauses)

    def unos3CNF(self):
        self.clauses = []
        variables = set()
        print("Unesite formulu u 3 CNF obliku:")

        for i in range(8):
            clauseString = input()

            if not clauseString:
                break

            clause = [int(x) for x in clauseString.split(',')]

            if len(clause) != 3:
                raise ValueError("Klauzula mora imati duzinu 3!")

            for literal in clause:
                variables.add(abs(literal))

            self.clauses.append(clause)

        variables = sorted(variables)

        if variables[0] != 1 or variables[-1] != len(variables):
            self.clauses = []
            raise ValueError("Klauzule nisu unesene ispravno!")

        self.numOfVariables = len(variables)


    def rjesenje3CNF(self):
        values = [0, 1]
        variations = list(product(values, repeat=self.numOfVariables))

        for variation in variations:
            if self.verifikacija3CNF(variation):
                print("Rjesenje:", variation)
                return 1

        return 0

    def verifikacija3CNF(self, values):
        formulaValue = 1
        for clause in self.clauses:

            clauseValue = 0
            for literal in clause:
                literalValue = values[abs(literal) - 1]
                if literal < 0:
                    literalValue = ~literalValue

                clauseValue = clauseValue | literalValue

            formulaValue = formulaValue & clauseValue

        if formulaValue == 1:
            return 1

        return 0

    def setClauses(self, clauses):
        self.clauses = clauses
        vars = set()
        for clause in clauses:
            for lit in clause:
                vars.add(abs(lit))

        self.numOfVariables = len(vars)
