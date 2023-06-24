import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

POPULATION_SIZE = 500
MUTATION_RATE = 0.1
GENERATIONS = 1000

def generate_state():
    state = list(range(8))
    random.shuffle(state)
    return state

def calculate_fitness(state):
    conflicts = 0
    for i in range(8):
        for j in range(i+1, 8):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return 1.0 / (1 + conflicts)  # Modified fitness function

def crossover(parent1, parent2):
    crossover_point = random.randint(0, 7)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutate(state):
    if random.random() < MUTATION_RATE:
        i, j = random.sample(range(8), 2)
        state[i], state[j] = state[j], state[i]
    return state

def select_parents(population):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    return max(tournament, key=lambda state: calculate_fitness(state))

def generate_population():
    return [generate_state() for _ in range(POPULATION_SIZE)]

def evolve_population(population):
    new_population = []
    for _ in range(POPULATION_SIZE // 2):
        parent1 = select_parents(population)
        parent2 = select_parents(population)
        child1, child2 = crossover(parent1, parent2)
        child1 = mutate(child1)
        child2 = mutate(child2)
        new_population.extend([child1, child2])
    return new_population

def genetic_algorithm():
    population = generate_population()
    for i in range(GENERATIONS):
        population = evolve_population(population)
        best_solution = max(population, key=lambda state: calculate_fitness(state))
        if calculate_fitness(best_solution) == 1:  # Modified stopping condition
            return best_solution
    return best_solution

solution = genetic_algorithm()
print('Solution:')
for row, col in enumerate(solution):
    print(f'[{row}, {col}]')

board = np.zeros((8, 8))
for i in range(8):
    board[solution[i], i] = 1
plt.figure(figsize=(8, 8))
sns.set(font_scale=1.5)
sns.heatmap(board, cmap='Reds', annot=True, cbar=False, square=True, linewidths=.5, linecolor='black', xticklabels=['0', '1', '2', '3', '4', '5', '6', '7'], yticklabels=['0', '1', '2', '3', '4', '5', '6', '7'])
plt.xlabel('Column')
plt.ylabel('Row')
plt.show()
