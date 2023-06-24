import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def generate_state():
    """Generate a random initial state"""
    state = [-1] * 8
    for i in range(8):
        while True:
            j = random.randint(0, 7)
            if j not in state[:i]:
                print("generate :", state)
                state[i] = j
                break
    return state

def calculate_fitness(state):
    """Calculate the fitness score of a state"""
    conflicts = 0
    for i in range(8):
        for j in range(i+1, 8):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    print(conflicts)
    return 28 - conflicts

def get_neighbors(state):
    """Generate all possible next states"""
    neighbors = []
    for i in range(8):
        for j in range(8):
            if j != state[i]:
                neighbor = state[:]
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors

def hill_climbing(allow_sideways=True, max_sideways=100, max_restarts=20):
    """Run the hill climbing algorithm"""
    best_solution = None
    best_fitness = -1
    restarts = 0

    while restarts < max_restarts:
        current_state = generate_state()
        current_fitness = calculate_fitness(current_state)
        sideways_moves = 0

        while True:
            neighbors = get_neighbors(current_state)
            if not neighbors:
                break

            neighbor_fitnesses = [calculate_fitness(neighbor) for neighbor in neighbors]
            best_neighbor = neighbors[np.argmax(neighbor_fitnesses)]
            best_local_fitness = max(neighbor_fitnesses)

            if best_local_fitness < current_fitness:
                break
            elif best_local_fitness == current_fitness:
                if not allow_sideways or sideways_moves >= max_sideways:
                    break
                sideways_moves += 1
            else:
                sideways_moves = 0

            current_state = best_neighbor
            current_fitness = best_local_fitness

        if current_fitness > best_fitness:
            best_solution = current_state
            best_fitness = current_fitness

        if best_fitness == 28:
            break

        restarts += 1

    return best_solution

solution = hill_climbing()
print('Solution:')
for row, col in enumerate(solution):
    print(f'[{row}, {col}]')

# Display the final state using NumPy and Matplotlib
board = np.zeros((8, 8))
for i in range(8):
    board[solution[i], i] = 1
plt.figure(figsize=(8, 8))
sns.set(font_scale=1.5)
sns.heatmap(board, cmap='Purples', annot=True, cbar=False, square=True, linewidths=.5, linecolor='black', xticklabels=['0', '1', '2', '3', '4', '5', '6', '7'], yticklabels=['0', '1', '2', '3', '4', '5', '6', '7'])
plt.xlabel('Column')
plt.ylabel('Row')
plt.show()
