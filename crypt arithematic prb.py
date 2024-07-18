from collections import defaultdict

def evaluate(equation, assignment):
    equation = equation.replace(" ", "")
    for variable, value in assignment.items():
        equation = equation.replace(variable, str(value))
    return eval(equation)

def solve_cryptarithmetic(equation):
    variables = set()
    for char in equation:
        if char.isalpha():
            variables.add(char)

    assignment = defaultdict(int)
    for variable in variables:
        for value in range(10):
            assignment[variable] = value
            if evaluate(equation, assignment):
                return assignment

    return None

# Test the function
equation = "SEND+MORE=MONEY".replace("０", "0")
solution = solve_cryptarithmetic(equation)
if solution:
    print("Solution found:")
    for variable, value in solution.items():
        print(f"{variable} = {value}")
else:
    print("No solution found")

