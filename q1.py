import random

def random_state():
    # One queen per row, column chosen randomly
    return [random.randint(0, 7) for i in range(8)]

def compute_conflicts(state):
    # Count number of pairs of queens attacking each other
    conflicts = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                conflicts += 1
    return conflicts

def get_best_neighbor(state):
    best = state[:]
    min_conflicts = compute_conflicts(state)
    
    for row in range(8):
        original_col = state[row]
        for col in range(8):
            if col == original_col:
                continue
            new_state = state[:]
            new_state[row] = col
            score = compute_conflicts(new_state)
            if score < min_conflicts:
                min_conflicts = score
                best = new_state[:]
    
    return best, min_conflicts

def hill_climbing():
    current = random_state()
    current_conflicts = compute_conflicts(current)
    
    while True:
        neighbor, neighbor_conflicts = get_best_neighbor(current)
        if neighbor_conflicts >= current_conflicts:
            break  # Local minimum
        current, current_conflicts = neighbor, neighbor_conflicts

    return current, current_conflicts

# Run the algorithm
import math

def simulated_annealing():
    current = random_state()
    current_conflicts = compute_conflicts(current)
    T = 1000.0  # initial temperature
    cooling_rate = 0.99
    min_T = 0.1
    
    while T > min_T and current_conflicts > 0:
        row = random.randint(0, 7)
        col = random.randint(0, 7)
        while col == current[row]:
            col = random.randint(0, 7)
        
        new_state = current[:]
        new_state[row] = col
        new_conflicts = compute_conflicts(new_state)
        
        delta = new_conflicts - current_conflicts
        
        if delta < 0 or random.random() < math.exp(-delta / T):
            current = new_state
            current_conflicts = new_conflicts
        
        T *= cooling_rate
    
    return current, current_conflicts

# Run the algorithm
def print_board(state):
    for row in range(8):
        line = ""
        for col in range(8):
            if state[col] == row:
                line += " Q "
            else:
                line += " . "
        print(line)

print("\nChessboard:")
if __name__ == "__main__":
    # Run the algorithm
    solution, conflicts = simulated_annealing()
    print("Simulated Annealing Solution:", solution)
    print("Conflicts:", conflicts)
    print_board(solution)

    solution, conflicts = hill_climbing()
    print("Hill Climbing Solution:", solution)
    print("Conflicts:", conflicts)
    print_board(solution)
