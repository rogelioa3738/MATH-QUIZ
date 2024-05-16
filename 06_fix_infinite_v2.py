import random
from fractions import Fraction

# Set to store generated equations
generated_equations = set()


# If user picked an infinite quiz
def infinite(max_equation=10000):
    equations = 0

    while True:
        while equations < max_equation:
            equations += 1
            equation, result = generate_random_math_equation()
            while True:
                print("EQUATION", equations, ":", equation)
                user_input = input("Your Answer: ")
                if user_input.lower() == 'xxx':  # Exit code for user if they want to quit
                    if equations >= 75:
                        confirmation = input("Are you sure you want to exit the quiz now? (yes / no): ").lower()
                        if confirmation == 'yes':
                            print("Thank you for answering!")
                            return 0
                        else:
                            print("Resuming the quiz...")
                            continue
                    else:
                        print(f"You need to answer at least 75 equations before exiting. You have answered {equations} "
                              f"equations so far.")
                        print()
                        continue
                try:
                    user_answer = Fraction(user_input)
                except ValueError:
                    print("‼️Please enter a valid answer.‼️")
                    print()
                    continue
                answer_checker(user_answer, result, equation)
                print()
                break  # Exit the inner loop after one attempt per equation
    return 0


# If user picked a fixed quiz
def fixed(num_equations):
    for equations in range(1, num_equations + 1):
        equation, result = generate_random_math_equation()
        while True:
            print()
            print("EQUATION", equations, ":", equation)
            user_input = input("Your Answer: ")
            if user_input.lower() == 'xxx':  # Exit code will not work in fixed quiz if user try to type it in
                print("The exit in this quiz is not available. You'll need to answer a set of 100 random equations.")
                continue
            try:
                user_answer = Fraction(user_input)
            except ValueError:
                print("‼️Please enter a valid answer.‼️")
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


# To ask user what kind of quiz they want
def fixed_infinite():
    print()
    print("Please type in below what type of quiz you want to do.")
    print()

    while True:
        game_type = input("Choose game type (infinite / fixed): ").lower()

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
        else:
            print("Please choose either 'infinite' or 'fixed'.")
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


# To add a comment if user picked a right or wrong answer
# Add the correct answer if user did not get the right answer
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
