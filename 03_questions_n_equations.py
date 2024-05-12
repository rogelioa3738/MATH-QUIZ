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


# Generate and print multiple random equations
def generate_multiple_equations(num_equations):
    print("\n☢️☢️☢️Answer the following set of equations!☢️☢️☢️\n")
    for i in range(0, num_equations + 1):
        equation, result = generate_random_math_equation()
        print("EQUATION", i + 1, ":", equation) # Add equation number
        while True:
            user_input = input("Your Answer: ")
            try:
                user_answer = float(user_input)
                break
            except ValueError:
                print("Please enter a valid number.")
        answer_checker(user_answer, result)
        print()

def answer_checker(user, math):
    # To check if user answer is same as the math answer
    if user == math:
        print("🙀🙀🙀 Oh my Oh my! You got it! So proud of ya! 🙀🙀🙀")
    else:
        print("🫤🫤🫤Sorry brother/sister, you didn't get it.🫤🫤🫤 The correct answer is:", math)


num_equations = 10
generate_multiple_equations(num_equations)
