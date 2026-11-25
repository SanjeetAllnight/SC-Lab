import random
dist = [
    [0,14,12,18,25,31,9,15,22,19],
    [14,0,11,20,28,17,13,24,16,21],
    [12,11,0,15,19,23,27,10,14,26],
    [18,20,15,0,13,16,22,29,12,17],
    [8,6,20,4,0,5,13,9,6,11],
    [31,17,23,16,14,0,19,25,20,12],
    [9,13,27,22,21,19,0,16,24,18],
    [15,24,10,29,18,25,16,0,13,22],
    [22,16,14,12,11,20,24,13,0,14],
    [19,21,26,17,15,12,18,22,14,0]
]
L = 10
POP_SIZE = 50
GENERATIONS = 20
MUTATION_RATE = 0.01
def create_chromosome():
    return ''.join(random.choice('01') for _ in range(L))
def decode(ch):
    value = int(ch, 2)
    cities = list(range(10))
    random.Random(value).shuffle(cities)
    return cities
def distance(ch):
    tour = decode(ch)
    total = 0
    for i in range(10):
        total += dist[tour[i]][tour[(i+1) % 10]]
    return total
# Fitness function
def fitness(ch):
    return 1 / distance(ch)
# Selection function
def selection(population):
    fit = [fitness(ch) for ch in population]
    parents = random.choices(population, weights=fit, k=POP_SIZE)
    return parents
# Crossover function
def crossover(p1, p2):
    point = random.randint(1, L-1)
    c1 = p1[:point] + p2[point:]
    c2 = p2[:point] + p1[point:]
    return c1, c2
# Mutation function
def mutation(ch):
    bits = list(ch)
    for i in range(L):
        if random.random() < MUTATION_RATE:
            bits[i] = '1' if bits[i] == '0' else '0'
    return ''.join(bits)
population = [create_chromosome() for _ in range(POP_SIZE)]
for gen in range(GENERATIONS):
    print("\nGENERATION", gen+1)
    fit = [fitness(ch) for ch in population]
    # Elitism
    best = population[fit.index(max(fit))]
    print("Elitism - Best:", best)
    # Selection
    parents = selection(population)
    print("Selection:", parents[0], parents[1])
    new_population = [best]
    # Crossover and Mutation
    while len(new_population) < POP_SIZE:
        p1, p2 = random.sample(parents, 2)
        c1, c2 = crossover(p1, p2)
        print("Crossover:", c1, c2)
        m1 = mutation(c1)
        m2 = mutation(c2)
        print("Mutation:", m1, m2)
        new_population.append(m1)
        if len(new_population) < POP_SIZE:
            new_population.append(m2)
    population = new_population
    # Best solution
    best = max(population, key=fitness)
    print("Best Tour:", [x+1 for x in decode(best)])
    print("Minimum Distance:", distance(best))
best = max(population, key=fitness)
print("\nFINAL RESULT")
print("Best Chromosome:", best)
print("Final Best Tour:", [x+1 for x in decode(best)])
print("Final Minimum Distance:", distance(best))