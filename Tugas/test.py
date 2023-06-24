import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class State:
    def __init__(self, state):
        self.state = state
        
    def conflicts(self):
        h = 0
        n = len(self.state)
        for i in range(n):
            for j in range(i+1, n):
                # Check horizontal and diagonal conflicts
                if self.state[i] == self.state[j] or \
                    abs(self.state[i] - self.state[j]) == abs(i - j):
                    h += 1
                # Check vertical diagonal conflicts
                if self.state[i] + i == self.state[j] + j or \
                    self.state[i] - i == self.state[j] - j:
                    h += 1
        return h
        
    def get_neighbors(self):
        neighbors = []
        n = len(self.state)
        for i in range(n):
            for j in range(i+1, n):
                # Swap positions of two queens
                neighbor_state = self.state.copy()
                neighbor_state[i], neighbor_state[j] = neighbor_state[j], neighbor_state[i]
                neighbor = State(neighbor_state)
                neighbors.append(neighbor)
        return neighbors


def hill_climbing(initial_state, max_iter):
    current_state = State(initial_state)
    for i in range(max_iter):
        if current_state.conflicts() == 0:
            return current_state.state
        neighbors = current_state.get_neighbors()
        best_neighbor = min(neighbors, key=lambda x: x.conflicts())
        if best_neighbor.conflicts() >= current_state.conflicts():
            return current_state.state
        current_state = best_neighbor
    # Jika sudah mencapai solusi optimal, kembalikan state terakhir
    return current_state.state


def random_restart(initial_state, max_iter, restarts):
    for i in range(restarts):
        random.shuffle(initial_state)
        solution = hill_climbing(initial_state, max_iter)
        if solution is not None:
            return solution
    return None


def display_board(solution):
    if solution is not None:
        matrix = np.zeros([8, 8], dtype=int)
        matrix = matrix.tolist()
        for i, j in enumerate(solution):
            matrix[i][j] = 1
        l = [i+1 for i in range(len(solution))]
        plt.figure(figsize=(5,5))
        sns.heatmap(matrix, linewidths=.8, cbar=False, cmap='Set3', xticklabels=l, yticklabels=l[::-1])
        plt.show()
        print("Solution: ")
        for i, j in enumerate(solution):
            print("[{}, {}]".format(j, i))
    else:
        print("No solution found.")


def main():
    # Read input from file
    with open("input.txt", "r") as input_file:
        input_lines = input_file.readlines()

    # Create the initial state list
    initial_state = []
    for line in input_lines:
        line = line.strip()
        row = [int(num) for num in line.split()]
        initial_state += [i for i, x in enumerate(row) if x == 1]

    # Set maximum iterations and number of restarts
    max_iter = 1000
    restarts = 15

    # Find solution using random restart hill climbing
    solution = random_restart(initial_state, max_iter, restarts)

    # Display solution as heatmap
    display_board(solution)


if __name__ == "__main__":
    main()