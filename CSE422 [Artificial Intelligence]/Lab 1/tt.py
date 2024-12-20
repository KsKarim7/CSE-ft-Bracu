import random

# Fitness function to calculate penalties
def fitness_function(schedule, N, T):
    penalty_overlap = 0
    penalty_consistency = 0
    
    # Calculate overlap penalty
    for t in range(T):
        timeslot = schedule[t * N:(t + 1) * N]
        penalty_overlap += max(0, sum(timeslot) - 1)  # If more than 1 course in a slot
    
    # Calculate consistency penalty
    for course in range(N):
        course_count = sum(schedule[course + t * N] for t in range(T))
        penalty_consistency += abs(course_count - 1)  # If not scheduled exactly once
    
    return -(penalty_overlap + penalty_consistency)

# Generate random chromosome (binary string)
def generate_chromosome(N, T):
    chromosome = [0] * (N * T)
    for course in range(N):
        timeslot = random.randint(0, T - 1)
        chromosome[timeslot * N + course] = 1
    return chromosome

# Perform single-point crossover
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutation function to introduce random changes
def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]  # Flip bit
    return chromosome

# Generate initial population
def initialize_population(pop_size, N, T):
    return [generate_chromosome(N, T) for _ in range(pop_size)]

# Main Genetic Algorithm
def genetic_algorithm(N, T, max_generations, pop_size, mutation_rate):
    population = initialize_population(pop_size, N, T)
    best_schedule = None
    best_fitness = float('-inf')
    
    for generation in range(max_generations):
        population_fitness = [(chromosome, fitness_function(chromosome, N, T)) for chromosome in population]
        population_fitness.sort(key=lambda x: x[1], reverse=True)
        
        # Update best solution
        if population_fitness[0][1] > best_fitness:
            best_schedule = population_fitness[0][0]
            best_fitness = population_fitness[0][1]
        
        # Selection of parents
        selected = population_fitness[:pop_size // 2]
        next_generation = []
        
        # Crossover
        for i in range(0, len(selected), 2):
            if i + 1 < len(selected):
                child1, child2 = crossover(selected[i][0], selected[i + 1][0])
                next_generation.extend([child1, child2])
        
        # Mutation
        next_generation = [mutate(chromosome, mutation_rate) for chromosome in next_generation]
        
        # Fill the rest of the population
        while len(next_generation) < pop_size:
            next_generation.append(generate_chromosome(N, T))
        
        population = next_generation
    
    return best_schedule, best_fitness

# Input and Execution
N, T = map(int, input("Enter number of courses and timeslots: ").split())
courses = [input("Enter course code: ") for _ in range(N)]

if T < N:
    print("Error: Number of timeslots must be greater than or equal to the number of courses.")
else:
    max_generations = 100
    pop_size = 50
    mutation_rate = 0.1
    
    best_schedule, best_fitness = genetic_algorithm(N, T, max_generations, pop_size, mutation_rate)
    
    print("Best Schedule (Binary String):", ''.join(map(str, best_schedule)))
    print("Fitness Value:", best_fitness)
