from csp import solve_problem

def process_csp(matrix, count):
	matrix =  matrix.encode()
	count = int(count.encode())
	matrix = matrix + ','*(count**2-len(matrix.split(',')))
	variables = generate_variables(count)
	constraints = generate_constraints(matrix, variables)
	domain = [range(1,4)]*count
	return solve_problem(constraints, variables, domain)

def generate_variables(count):
	variables=[]
	for index in range(1,count+1):
		variables.append('x%s'%index)
	return variables

def generate_constraints(matrix, variables):
	matrix =  matrix.split(',')
	matrix = chunks(matrix,len(variables))
	constraints=[]
	for start_index in range(len(variables)):
		for end_index in range(len(variables)):
			if matrix[start_index][end_index]:
				constraints.append(variables[start_index]+' != '+variables[end_index])
	return constraints		

def chunks(list, count):
    return [list[index:index+count] for index in range(0, len(list), count)]
