import random
from fractions import Fraction

# Set to store generated equations
generated_equations = set()


def generate_random_math_equation(difficulty):
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
        num2 = random.randint(1000, 10000)

    operator = random.choice(['+', '-', '*', '/'])
    equation = f"{num1} {operator} {num2}"

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        while num2 == 0:  # Ensure divisor is not zero
            num2 = random.randint(1, 10)
        result = round(num1 / num2, 2)

    return equation, result


def answer_checker(user, math, equation):
    # Convert user answer to float or fraction for comparison
    try:
        user_answer = float(user)
    except ValueError:
        try:
            user_answer = float(Fraction(user))
        except ValueError:
            print("‼️Please enter a valid answer.‼️")
            return

    # Round the float answer to two decimal places
    if isinstance(math, float):
        user_answer = round(user_answer, 2)

    if user_answer == math:
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

    for equation_number in range(1, num_equations + 1):
        equation, result = generate_random_math_equation(difficulty)
        print("EQUATION", equation_number, ":", equation)

        while True:
            user_input = input("Your Answer: ")

            if user_input.lower() == 'xxx':
                confirmation = input("Are you sure you want to exit the quiz now? (yes / no): ").lower()
                if confirmation == 'yes':
                    print("👏👏Thank you for answering👏👏")
                    return True  # User chose to exit
                else:
                    print("Resuming the quiz...")
                    break  # Resume the game

            try:
                user_answer = Fraction(user_input)
                break  # Break out of the loop if input is valid
            except ValueError:
                print("‼️Please enter a valid answer.‼️")
                print()

        if user_input.lower() == 'xxx':
            break  # Exit the loop if user chose to exit

        answer_checker(user_input, result, equation)
        print()

    return False  # User didn't choose to exit


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

    while True:
        choice = input("What would you like to choose "
                       "(Type in the words easy / medium / hard / expert)? ")

        # If user chooses to exit the code it will not ask again
        if choice.lower() == 'easy':
            if quiz('easy'):
                break
        elif choice.lower() == 'medium':
            if quiz('medium'):
                break
        elif choice.lower() == 'hard':
            if quiz('hard'):
                break
        elif choice.lower() == 'expert':
            if quiz('expert'):
                break
        else:
            print("‼️Please enter one of the difficulties‼️")
            print()


if __name__ == "__main__":
    main_levels()
