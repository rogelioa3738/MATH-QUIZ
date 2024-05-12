import random
from fractions import Fraction

# Set to store generated equations
generated_equations = set()


# Generates the random maths question
def generate_random_math_equation():
    while True:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*', '/'])

        equation = f"{num1} {operator} {num2}"
        # Check if equation has been generated before, if yes, generate a new one
        if equation not in generated_equations:
            generated_equations.add(equation)
            break

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        # Ensure that division is valid (non-zero divisor)
        if num2 != 0:
            result = Fraction(num1, num2)
        else:
            # If division by zero, generate a new equation
            return generate_random_math_equation()

    return equation, result


# Generate and print multiple random equations
def generate_multiple_equations(num_equations):
    print("\n☢️☢️☢️ Answer the following set of equations! ☢️☢️☢️\n")
    for i in range(num_equations):
        equation, result = generate_random_math_equation()
        print("EQUATION", i + 1, ":", equation)
        while True:
            user_input = input("Your Answer: ")
            try:
                user_answer = Fraction(user_input)
                break
            except ValueError:
                print("Please enter a valid answer.")
        answer_checker(user_answer, result, equation)
        print()


def answer_checker(user, math, equation):
    # To check if user answer is same as the math answer
    if user == math:
        print("🙀🙀🙀 Oh my Oh my! You got it! So proud of ya! 🙀🙀🙀")
    elif user == equation:
        print("Come on, don't repeat the equation!")
    else:
        print("🫤🫤🫤 Sorry, you didn't get it. 🫤🫤🫤 The correct answer is:", math)


num_equations = 50
generate_multiple_equations(num_equations)
