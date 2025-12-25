def quadratic(x, a, b, c):
    result = a * x ** 2 + b* x + c
    return result
def cubic(x, a, b, c, d):
    result = a * x ** 3 + b * x ** 2 + c * x + d
    return result

def find_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return 'No real roots'
    elif discriminant == 0:
        root = -b/(2*a)
        return root
    else:
        sqrt_discrimante = pow(discriminant, 0.5)
        root1 = (-b + sqrt_discrimante)/(2*a)
        root2 = (-b - sqrt_discrimante)/(2*a)
        return root1, root2
    
def evaluate_at_points(func_type, x1, x2, x3, a, b, c):
    if func_type==quadratic:
        y1 = quadratic(x1, a, b, c)
        y2 = quadratic(x2, a, b, c)
        y3 = quadratic(x3, a, b, c)
        print(f"Quadratic {a}x² + {b}x + {c}:")
    elif func_type == "linear":
        y1 = a * x1 + b
        y2 = a * x2 + b
        y3 = a * x3 + b
        print(f"Linear {a}x + {b}:")
    
    print(f"  f({x1}) = {y1}")
    print(f"  f({x2}) = {y2}")
    print(f"  f({x3}) = {y3}")
    
# Test the functions
print("Mathematical Function Evaluator")
print("-" * 40)

# Evaluate quadratic 2x² + 3x - 5
print("Evaluating 2x² + 3x - 5:")
y1 = quadratic(-2, 2, 3, -5)
y2 = quadratic(0, 2, 3, -5)
y3 = quadratic(2, 2, 3, -5)
print(f"  f(-2) = {y1}")
print(f"  f(0) = {y2}")
print(f"  f(2) = {y3}")
print()

# Evaluate cubic x³ - 2x² + x - 1
print("Evaluating x³ - 2x² + x - 1:")
c1 = cubic(-1, 1, -2, 1, -1)
c2 = cubic(1, 1, -2, 1, -1)
c3 = cubic(3, 1, -2, 1, -1)
print(f"  f(-1) = {c1}")
print(f"  f(1) = {c2}")
print(f"  f(3) = {c3}")
print()

# Find roots
print("Finding roots of x² - 5x + 6 = 0:")
roots1 = find_quadratic_roots(1, -5, 6)
if roots1 != "No real roots":
    if isinstance(roots1, tuple):
        print(f"  Root 1: {roots1[0]}")
        print(f"  Root 2: {roots1[1]}")
    else:
        print(f"  Single root: {roots1}")
print()

print("Finding roots of x² + 2x + 5 = 0:")
roots2 = find_quadratic_roots(1, 2, 5)
print(f"  Result: {roots2}")
print()

# Evaluate linear function
evaluate_at_points("linear", -3, 0, 4, 3, 7, 0)