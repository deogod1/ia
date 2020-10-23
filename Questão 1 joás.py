import random

ben = [3, 3, 2, 4, 2, 3, 5, 2]
pesos = [5, 4, 7, 8, 4, 4, 6, 8]


def getCromossomo(size):
    cromo = []
    i = 0
    while i < size:
        genes = random.randint(0, 1)
        cromo.append(genes)
        i = i + 1
    return cromo


size = 8
cromo = getCromossomo(size)


def fitness(cromossomo):
    i = 0
    benefit = 0
    peso = 0
    while i < size:
        genes = cromo[i]
        if genes == 1:
            benefit = benefit + ben[i]
            peso = peso + pesos[i]
        i = i + 1
    if peso > 25:
        benefit = -1
    return benefit


benefit = -1
sizePop = 10

while benefit < 13:
    cromo = getCromo(size)
    benefit = fitness(cromo)
    print(cromo)
    print(benefit)
