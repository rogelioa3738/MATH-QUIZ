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


# to generate and print multiple random equations
def generate_multiple_equations(num_equations):
    print("\nAnswer the following set of equations!")
    print()
    for _ in range(num_equations):
        equation, result = generate_random_math_equation()
        print(f"EQUATION:", equation)
        user_input = input("Your Answer: ")
        try:
            user_answer = float(user_input)
            if user_answer == result:
                print("Correct!")
            else:
                print("Incorrect. The correct answer is:", result)
        except ValueError:
            print("Please enter a valid number.")
        print()


# Number of equations to generate
num_equations = 10
generate_multiple_equations(num_equations)
