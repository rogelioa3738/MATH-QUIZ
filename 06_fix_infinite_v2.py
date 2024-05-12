import random
from fractions import Fraction

# Set to store generated equations
generated_equations = set()


def infinite(max_equation=1000):
    round_num = 0
    while round_num < max_equation:
        round_num += 1
        equation, result = generate_random_math_equation()
        print("EQUATION", round_num, ":", equation)
        user_input = input("Your Answer: ")
        try:
            user_answer = Fraction(user_input)
        except ValueError:
            print("Please enter a valid answer.")
            continue
        answer_checker(user_answer, result, equation)
        print()


def fixed(num_equations):
    for round_num in range(1, num_equations + 1):
        equation, result = generate_random_math_equation()
        print()
        print("EQUATION", round_num, ":", equation)
        user_input = input("Your Answer: ")
        try:
            user_answer = Fraction(user_input)
        except ValueError:
            print("Please enter a valid answer.")
            continue
        answer_checker(user_answer, result, equation)
        print()


def fixed_infinite():

    print()
    print("Please type in below what type of quiz do want to do.")
    print()

    while True:
        game_type = input("Choose game type ( infinite / fixed ): ")
        print()

        if game_type.lower() == 'infinite':
            print("🤯🤯🤯 Wow! You picked the infinite amount of equations! 🤯🤯🤯")
            infinite()
            break
        elif game_type.lower() == 'fixed':
            print("👏👏👏 Since you pick a fixed amount of equation for this quiz"
                  "you will then answer a 100 random set of equations! 👏👏👏")
            num_equations = 100
            fixed(num_equations)
            break
        else:
            print("Please choose either 'infinite' or 'fixed'.")


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


def answer_checker(user, math, equation):
    # To check if user answer is same as the math answer
    if user == math:
        print("🙀🙀🙀 Oh my Oh my! You got it! So proud of ya! 🙀🙀🙀")
    elif user == equation:
        print("Come on, don't repeat the equation!")
    else:
        print("🫤🫤🫤 Sorry, you didn't get it. 🫤🫤🫤 The correct answer is:", math)


if __name__ == "__main__":
    fixed_infinite()
