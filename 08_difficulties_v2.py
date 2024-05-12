import random
from fractions import Fraction

# Set to store generated equations
generated_equations = set()


def generate_random_math_equation(difficulty):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*', '/'])

    if difficulty == 'easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
    elif difficulty == 'medium':
        num1 = random.randint(10, 100)
        num2 = random.randint(10, 100)
    elif difficulty == 'hard':
        num1 = random.randint(100, 1000)
        num2 = random.randint(100, 1000)
    elif difficulty == 'expert':
        num1 = random.randint(1000, 10000)
        num2 = random.randint(1000,  10000)

    equation = f"{num1} {operator} {num2}"

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
            return generate_random_math_equation(difficulty)

    return equation, result


def answer_checker(user, math, equation):
    # To check if user answer is same as the math answer
    if user == math:
        print("🙀🙀🙀 Oh my Oh my! You got it! So proud of ya! 🙀🙀🙀")
    elif user == equation:
        print("Come on, don't repeat the equation!")
    else:
        print("🫤🫤🫤 Sorry, you didn't get it. 🫤🫤🫤")
        print("The correct answer is:", math)


def quiz(difficulty, num_equations=100):
    print()
    print(f"You've selected a {difficulty} quiz!")
    print()

    for round_num in range(1, num_equations + 1):
        equation, result = generate_random_math_equation(difficulty)
        print("EQUATION", round_num, ":", equation)
        user_input = input("Your Answer: ")
        try:
            user_answer = Fraction(user_input)
        except ValueError:
            print("Please enter a valid answer.")
            continue
        answer_checker(user_answer, result, equation)
        print()


def main_levels():
    print()
    print("In this quiz, you will be given four difficulties to choose from.")
    print()
    print("Choose one of the following difficulties:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Expert")
    print()

    choice = input("What would you like to choose "
                   "(Type in the words easy / medium / hard / expert)? ")

    if choice.lower() == 'easy':
        quiz('easy')
    elif choice.lower() == 'medium':
        quiz('medium')
    elif choice.lower() == 'hard':
        quiz('hard')
    elif choice.lower() == 'expert':
        quiz('expert')
    else:
        print("Please enter one of the difficulties")


if __name__ == "__main__":
    main_levels()
