import random
from fractions import Fraction

# Set to store generated equations
generated_equations = set()

def infinite(max_equation=1000):
    equations = 0

    while True:
        while equations < max_equation:
            equations += 1
            equation, result = generate_random_math_equation()
            while True:
                print("EQUATION", equations, ":", equation)
                user_input = input("Your Answer: ")
                if user_input.lower() == 'xxx':
                    print("Thank you for playing!")
                    return 0
                try:
                    user_answer = Fraction(user_input)
                except ValueError:
                    print("Please enter a valid answer.")
                    print()
                    continue
                answer_checker(user_answer, result, equation)
                print()
                if user_answer == result:
                    break
                else:
                    break  # Exit the inner loop if the answer is wrong
    return 0

def fixed(num_equations):
    for equations in range(1, num_equations + 1):
        equation, result = generate_random_math_equation()
        while True:
            print()
            print("EQUATION", equations, ":", equation)
            user_input = input("Your Answer: ")
            if user_input.lower() == 'xxx':
                print("Thank you for playing!")
                return 0
            try:
                user_answer = Fraction(user_input)
            except ValueError:
                print("Please enter a valid answer.")
                print()
                continue
            if user_answer == result:
                answer_checker(user_answer, result, equation)
                print()
                break
            else:
                answer_checker(user_answer, result, equation)
                print()
                break  # Move to the next equation if the answer is wrong
    return 0

def fixed_infinite():
    print()
    print("Please type in below what type of quiz you want to do.")
    print()

    while True:
        game_type = input("Choose game type (infinite / fixed): ").lower()
        print()

        if game_type == 'infinite':
            print("🤯🤯🤯 Wow! You picked an infinite number of equations! 🤯🤯🤯")
            print()
            infinite()
            break
        elif game_type == 'fixed':
            print("👏👏👏 Since you picked a fixed amount of equations for this quiz, "
                  "you will then answer 100 random equations! 👏👏👏")
            num_equations = 100
            fixed(num_equations)
            break
        elif game_type == 'exit':
            print("Thank you for playing!")
            return 0
        else:
            print("Please choose either 'infinite', 'fixed', or 'exit'.")
            print()

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
            return generate_random_math_equation(), None

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

if __name__ == "__main__":
    exit_code = fixed_infinite()
    exit(exit_code)
