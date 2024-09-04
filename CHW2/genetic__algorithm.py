import random
import numpy as np

"""A function that generates a population of random solutions"""
def generate_population(population_size, num_vars):
    population = []
    for _ in range(population_size):
        solution = ''.join(random.choice(['0', '1']) for _ in range(num_vars))
        population.append(solution)
    return population

"""A function that evaluates the CNF and returns the number of true parentheses"""
def evaluate_formula(formula, solution):
    true_parentheses = 0
    for clause in formula:
        clause_value = False
        for variable in clause:
            variable_value = bool(int(solution[abs(variable)-1]))
            if variable < 0:
                variable_value = not variable_value
            clause_value = clause_value or variable_value
        if clause_value:
            true_parentheses += 1
    return true_parentheses

"""Select parents"""
def selection(population, fitnesses, num_parents):
    selected = []
    for _ in range(num_parents):
        one = random.randint(0, len(population) - 1)
        two = random.randint(0, len(population) - 1)
        if fitnesses[one] > fitnesses[two]:
            selected.append(population[one])
        else:
            selected.append(population[two])
    return selected

"""performs crossover"""
def crossover(parents):
    offspring = ''
    for i in range(len(parents[0])):
        if random.random() < 0.5:
            offspring += parents[0][i]
        else:
            offspring += parents[1][i]
    return offspring

"""perform mutation"""
def mutation(offspring, mutation_rate):
    mutated_offspring = ''
    for bit in offspring:
        if random.random() < mutation_rate:
            if bit == 0 :
               mutated_offspring += '1' 
            else :
                mutated_offspring += '0'
        else:
            mutated_offspring += bit
    return mutated_offspring

"""Finds the maximum number of true parentheses"""
def genetic_algorithm(formula, population_size, num_vars, num_parents, mutation_rate, max_generations):
    population = generate_population(population_size, num_vars)
    best_solution = None
    best_fitness = 0
    fitnesses = []
    for _ in range(max_generations):
        for solution in population:
            fitnesses.append(evaluate_formula(formula, solution))
        best_index = np.argmax(fitnesses)
        if fitnesses[best_index] > best_fitness:
            best_fitness = fitnesses[best_index]
            best_solution = population[best_index]
        truth_values = []
        if best_fitness == len(formula):
            for bit in best_solution:
                truth_values.append(bool(int(bit)))
            return best_fitness, truth_values
        parents = selection(population, fitnesses, num_parents)
        offspring = []
        for _ in range(population_size - num_parents):
            offspring.append(crossover(parents))
        offspring2 = []
        for child in offspring:
            offspring2.append(mutation(child, mutation_rate))

        population = parents + offspring2

    truth_values1 = []
    for bit in best_solution:
        truth_values1.append(bool(int(bit)))
    return best_fitness, truth_values1

