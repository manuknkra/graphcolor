def solve_problem(constraints, variables, domain):
	
	solution_set = combination(domain)
	true_solutions = []
	flag = 1
	for solution in solution_set:
		for constraint in constraints:
			if not satisfy_each_constraint(constraint, variables, solution):
				flag = 0
				break
			else:
				flag = 1
		if flag:
			true_solutions.append(solution)
	return true_solutions

def combination(domain):
	solution_set =[[]]
	for item in domain:
		t = []
                for y in item:
                        for i in solution_set:
                                t.append(i+[y])
		solution_set = t
	return solution_set

def combination2(domain):
	x, y = domain[0], domain[1]
	return [[p,q] for p in x for q in y]

def satisfy_each_constraint(constraint, variables, solution):

	index = 0
	for variable in variables:
		constraint = constraint.replace(variable, "%s"%solution[index])
		index += 1
	
	if ' =' in constraint:
		constraint = constraint.replace('=','==')
	return eval(constraint)
