def bissection(f, a, b, error_tolerance):
    '''
    1) Definition: Function used to calculate f(x) = 0 using bissection method
    
    Bissection - We now the solution for f(x) = 0 is in [a, b], start iteration with x = (a + b) / 2
    
    2) Input:
            f: Function used in function(x) = 0 (type = lambda function)
            a: Interval [a, b] (type = float)
            b: Interval [a, b] (type = float)
            error_tolerance: Maximum error allowed for solution (type = float)
            
    3) Return: 
            solution: Solution of f(x) = 0 (type = float)
    '''
    
    # Initial guess
    
    x0 = a
    x1 = b
    solution = (x0 + x1) / 2
    error = abs(f(solution))
    
    # Begin iteration
    
    while error > error_tolerance:
        solution = (x0 + x1) / 2
        error = abs(f(solution))
        
        print(f'x0 = {x0} - x1 = {x1}')
        print(f'solution = {solution} - error = {error} \n')

        if f(x0) * f(solution) < 0:
            x1 = solution

        elif f(solution) * f(b) < 0:
            x0 = solution

    return solution

def secant(function, x0, error_tolerance):
    '''
    1) Definition: Function used to calculate f(x) = 0 using secant method
    
    Secant - x(n+1) = x(n) - f(x(n)) / m where m = (f(x(n+1)) - f(x(n))) / (x(n+1) - x(n))
    2) Input:
            f: Function used in f(x) = 0 (type = lambda function)
            x0: Initial guess for solution 
            error_tolerance: Maximum error allowed for solution (type = float)
            
    3) Return: 
            solution: Solution of f(x) = 0 (type = float)
    '''
    
    # Initial guess
    
    h = 0.05
    m = (f(x0 + h) - f(x0 - h)) / (2 * h)
    solution = x0 - f(x0) / m
    error = abs(f(solution))
    
    # Begin iteration
        
    while error > error_tolerance:
        print(f'solution = {solution} - error = {error} \n')
        x = solution
        m = (f(x + h) - f(x - h)) / (2 * h)
        solution = x - f(x) / m
        error = abs(f(solution))

    return solution


