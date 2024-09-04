import numpy as np

"""A function to convert a CNF file to a numpy array"""
def read_cnf_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    clauses = []
    for line in lines:
        if line.startswith('c'):
            continue
        if line.startswith('p'):
            _, _, num_vars, num_clauses = line.split()
            num_vars = int(num_vars)
            num_clauses = int(num_clauses)
            continue
        clause = list(map(int, line.split()[:-1]))
        clauses.append(clause)
    formula = np.array(clauses)
    return formula