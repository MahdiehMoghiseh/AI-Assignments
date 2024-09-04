import random
import numpy as np
import math

"""A function that calculates the probability with temperature and delta"""
def calculate_probability(delta, temperature):
    if delta < 0:
        return 1.0
    else:
        return math.exp(-delta / temperature)

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
        if clause_value == True:
            true_parentheses += 1
    return true_parentheses

"""A function that generates a neighbor"""
def generate_neighbor_solution(solution):
    index = random.randint(0, len(solution) - 1)
    neighbor = solution[:index]
    if solution[index] == '0':
        neighbor += '1'
    else:
        neighbor += '0'
    neighbor += solution[index+1:]
    return neighbor

"""Generate random values of each bit"""
def generate_initial_solution(num_vars):
    return ''.join(str(random.randint(0, 1)) for _ in range(num_vars))

"""Finds the maximum number of true parentheses"""
def simulated_annealing(formula, initial_temperature, cooling_rate):
    current_solution = generate_initial_solution(100)
    best_solution = current_solution
    current_fitness = evaluate_formula(formula, current_solution)
    best_fitness = current_fitness
    temperature = initial_temperature
    while temperature > 1e-10:
        neighbor_solution = generate_neighbor_solution(current_solution)
        neighbor_fitness = evaluate_formula(formula, neighbor_solution)
        delta_fitness = neighbor_fitness - current_fitness
        if calculate_probability(delta_fitness, temperature) > random.random():
            current_solution = neighbor_solution
            current_fitness = neighbor_fitness
        if current_fitness > best_fitness:
            best_solution = current_solution
            best_fitness = current_fitness
        temperature *= cooling_rate

    trurh_values = []
    for bit in best_solution:
        trurh_values.append(bool(int(bit)))
    return best_fitness, trurh_values
