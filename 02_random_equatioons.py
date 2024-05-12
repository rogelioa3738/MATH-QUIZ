import random


# Generates the random maths question
def generate_random_math_equation():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Ensure that division is valid (non-zero divisor)
        if num2 != 0:
            result = num1 / num2
        else:
            # If division by zero, generate a new equation
            return generate_random_math_equation()

    equation = f"{num1} {operator} {num2}"
    return equation, result


equation, result = generate_random_math_equation()
print("Solve the equation:", equation)
print("Result:", result)


# Generate and print multiple random equations
def generate_multiple_equations(num_equations,user, math):
    print("\nAnswer the following set of equations!")
    print()
    for _ in range(num_equations):
        equation, result = generate_random_math_equation()
        print(f"EQUATION:", equation)
        print(f"RESULT:", result)
        print()


num_equations = 10
generate_multiple_equations(num_equations)

# todo def to handle answer check (including a try/except to cover non numbers)
