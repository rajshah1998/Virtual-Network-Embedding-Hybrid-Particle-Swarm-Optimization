import pso

# A Sample Cost Function
def Sphere(x):
    return sum(x**2)

# Define Optimization Problem
problem = {
        'CostFunction': Sphere, 
        'nVar': 10, 
        'VarMin': -5,   # Alternatively you can use a "numpy array" with nVar elements, instead of scalar
        'VarMax': 5,    # Alternatively you can use a "numpy array" with nVar elements, instead of scalar
    }

# Running PSO
pso.tic()
print('Running PSO ...')
gbest, pop = pso.PSO(problem, MaxIter = 200, PopSize = 50, c1 = 1.5, c2 = 2, w = 1, wdamp = 0.995)
print()
pso.toc()
print()

# Final Result
print('Global Best:')
print(gbest)
print()
