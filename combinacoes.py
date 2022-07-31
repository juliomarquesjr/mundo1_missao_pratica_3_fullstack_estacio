from itertools import combinations 

class Combinacoes:
    def __init__(self, entrada):
        self.entrada = entrada

    def gera_combinacoes(self):
        lista = [[]]
        for cont in range(1, len(self.entrada)):
            combina = combinations(self.entrada, cont)
            for item in list(combina):
                lista.append(list(item))

        return lista + [self.entrada]