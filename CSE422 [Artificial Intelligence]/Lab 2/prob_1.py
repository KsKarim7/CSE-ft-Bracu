import random

def creating_random_population(ovulation_count, given_chro):  # initial population for chromosomes
    return [''.join(random.choice('01') for l in range(given_chro)) for m in range(ovulation_count)]


def making_parents(random_gene):  # population parents
    return random.sample(random_gene, 2)


def fitness_func(new_chro, N, T):
    penalty_overlap = 0
    penalty_consistency = 0

    for j in range(T):  # penalty overlap
        courses = sum(int(new_chro[j * N + i]) for i in range(N))
       
        if courses > 1:
            penalty_overlap += courses - 1

    for k in range(N):  # penalty for consistency
        time_of_mutation = sum(int(new_chro[i * N + k]) for i in range(T))
        penalty_consistency += abs(time_of_mutation - 1)

    return -(penalty_overlap + penalty_consistency)


def crossover(par_one, par_two):  # crossover 2 position
    mutd_one = random.randint(1, len(par_one) - 2)
    mutd_two = random.randint(mutd_one + 1, len(par_one) - 1)
    offsp_one = par_one[:mutd_one] + par_two[mutd_one:mutd_two] + par_one[mutd_two:]
    offsp_two = par_two[:mutd_one] + par_one[mutd_one:mutd_two] + par_two[mutd_two:]
    return offsp_one, offsp_two


def mutate(new_chro, val_of_mutation=0.01):  # Mutation
    chr_list = list(new_chro)
    for i in range(len(chr_list)):
        if random.random() < val_of_mutation:
            chr_list[i] = '1' if chr_list[i] == '0' else '0'
    return ''.join(chr_list)


def GA(N, T, size_p=10, gen_high=1000, val_of_mutation=0.01, main_chro=None):  # Genetic Algorithm
    given_chro = N * T
    random_gene = creating_random_population(size_p, given_chro)

    for x in range(gen_high):
        storing_population = []

        for c in range(size_p // 2):

            par_one, par_two = making_parents(random_gene)
            offsp_one, offsp_two = crossover(par_one, par_two)
            offsp_one = mutate(offsp_one, val_of_mutation)
            offsp_two = mutate(offsp_two, val_of_mutation)
           
            storing_population.extend([offsp_one, offsp_two])

        random_gene = sorted(storing_population, key=lambda x: fitness_func(x, N, T), reverse=True)[:size_p]

        if main_chro and main_chro in random_gene:

            return main_chro, fitness_func(main_chro, N, T)

    res = max(random_gene, key=lambda x: fitness_func(x, N, T))
    return res, fitness_func(res, N, T)

def main():
    random.seed(42)

    N, T = map(int, input("Enter number of courses and time slots: ").split())
    courses = [input("Enter course code: ") for _ in range(N)]
    


    print(f"Number of courses: {N} Time slots: {T} Courses: {courses}")

    main_chro = "110110010"  # Goal Chromosome
    res, fitness = GA(N, T, main_chro=main_chro)


    print("Best Chromosome:", res)
    print("Fitness Value:", fitness)

if __name__ == "__main__":
    main()



