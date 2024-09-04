import cnf_to_array
import genetic__algorithm
import simulated_annealing

def main():
    filename = 'Input.cnf'
    formula = cnf_to_array.read_cnf_file(filename)

    print('Formula:')
    print(formula)

    """using genetic algorithm"""
    population_size = 100
    num_parents = 20
    mutation_rate = 0.01
    max_generations = 1000

    max_true_parentheses, truth_values = genetic__algorithm.genetic_algorithm(formula, population_size, 100, num_parents, mutation_rate, max_generations)
    int_truth_values1 = create_output(truth_values)

    print(f'Maximum number of true parentheses with GENETIC ALGORITHM is: {max_true_parentheses}')
    print(f'Truth values of variables: {int_truth_values1}')

    """using simulated annealing"""
    initial_temperature = 1000.0
    cooling_rate = 0.99
    max_true_parentheses, truth_values = simulated_annealing.simulated_annealing(formula, initial_temperature, cooling_rate)
    int_truth_values2 = create_output(truth_values)

    print(f'Maximum number of true parentheses with SIMULATED ANNEALING is: {max_true_parentheses}')
    print(f'Truth values of variables: {int_truth_values2}')

def create_output(truth_values) :
    int_truth_values = []
    for i in range(100) :
        if truth_values[i] == True :
            int_truth_values.append(str(i + 1))

        else : 
            int_truth_values.append(str(-(i + 1)))

    return int_truth_values
    
if __name__=="__main__":
    main()


