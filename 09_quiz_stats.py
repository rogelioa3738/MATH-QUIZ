import random
from fractions import Fraction


# To record every equation and right answers of the user
total_equations_attempted = 0
total_correct_answers = 0


def equation_generator(difficulty):
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
    global total_correct_answers

    # Convert user answer to float or fraction for comparison
    try:
        user_answer = float(user)
    except ValueError:
        try:
            user_answer = float(Fraction(user))
        except ValueError:
            print("‼️Please enter a valid answer.‼️")
            return

    # Round the answer to two decimal places
    if isinstance(math, float):
        user_answer = round(user_answer, 2)

    if user_answer == math:
        print("🙀🙀🙀 Oh my Oh my! You got it! So proud of ya! 🙀🙀🙀")
        total_correct_answers += 1
    elif user == equation:
        print("Come on, don't repeat the equation!")
    else:
        print("🫤🫤🫤 Sorry, you didn't get it. 🫤🫤🫤")
        print("The correct answer is:", math)


# If user picked an infinite quiz, this will run
def infinite(difficulty, num_equations=100000):
    global total_equations_attempted
    print()
    print(f"You've selected a quiz with an infinite amount of equations and with a difficulty of {difficulty}!")
    print()

    for equation_number in range(1, num_equations + 1):
        equation, result = equation_generator(difficulty)
        print("EQUATION", equation_number, ":", equation)

        while True:
            user_input = input("Your Answer: ")

            if user_input.lower() == 'xxx':
                if total_equations_attempted >= 75:
                    confirmation = input("Are you sure you want to exit the quiz now? (yes / no): ").lower()
                    if confirmation == 'yes':
                        print("👏👏Thank you for answering👏👏")
                        print()
                        print()  # This is to immediately show user their score
                        print("Your final score is", round((total_correct_answers / total_equations_attempted) * 100, 2), "%")
                        final_score = round((total_correct_answers / total_equations_attempted) * 100, 2)

                        if final_score >= 75:
                            print("🥳🥳🥳Congratulations! You passed the quiz🥳🥳🥳")
                        else:
                            print("😭😭😭Sorry, but you have failed the quiz. Better luck next time😭😭😭")
                        print()
                        return True  # User chose to exit
                    else:
                        print("Resuming the quiz...")
                        print()
                        continue  # Resume the quiz
                else:  # This is for the exit code 'xxx' if user did not meet the required equations
                    print(f"You can't exit the quiz until you've answered a total of 75 equations,"
                          f" as for now you've only answered {total_equations_attempted} total equations")
                    print()
                    continue  # Repeat the same equation

            try:
                user_answer = Fraction(user_input)
                break  # Break out of the loop if input is valid
            except ValueError:
                print("‼️Please enter a valid answer or 'xxx' to exit.‼️")
                print()

        if user_input.lower() == 'xxx':
            continue  # Repeat the same equation if user chose to exit
        else:
            answer_checker(user_input, result, equation)
            total_equations_attempted += 1  # Increment the count of answered equations
            print()

    return False  # User didn't choose to exit


# If user picked a fixed quiz, this will run
def fixed(difficulty):
    global total_equations_attempted
    global total_correct_answers
    num_equations = 100  # Amount of equations we want

    print()
    print(f"You've selected a quiz with {num_equations} equations and with a difficulty of {difficulty}!")
    print()

    for equation_number in range(1, num_equations + 1):
        equation, result = equation_generator(difficulty)
        print("EQUATION", equation_number, ":", equation)

        while True:
            user_input = input("Your Answer: ")

            if user_input.lower() == 'xxx':
                if total_equations_attempted < num_equations:
                    print("Sorry but you can't exit this quiz until you answer a total of 100 equations")
                    print()
                    continue

            try:
                user_answer = Fraction(user_input)
            except ValueError:
                print("‼️Please enter a valid answer.‼️")
                print()
                continue  # Repeat the same equation

            answer_checker(user_input, result, equation)
            total_equations_attempted += 1  # Increment the count of answered equations
            print()
            break  # Move to the next equation after valid input

    print()  # This is to immediately show user their score
    print("Your final score is", round((total_correct_answers / total_equations_attempted) * 100, 2), "%")
    final_score = round((total_correct_answers / total_equations_attempted) * 100, 2)

    if final_score >= 75:
        print("🥳🥳🥳Congratulations! You passed the quiz🥳🥳🥳")
    else:
        print("😭😭😭Sorry, but you have failed the quiz. Better luck next time😭😭😭")
    print()
    return False  # User didn't choose to exit


# Statistics part of the code
def quiz_results():
    global total_correct_answers
    global total_equations_attempted

    print()
    print("✖️➕➖➗ Quiz results ➗➖➕✖️")
    print()
    print("Total equations attempted:", total_equations_attempted)
    print("Total correct answers:", total_correct_answers)
    print("Total wrong answers:", total_equations_attempted - total_correct_answers)
    print()


# Main quiz program will start here
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
    choice = input("What would you like to choose ( easy / medium / hard / expert )? ")

    if choice.lower() in ['easy', 'medium', 'hard', 'expert']:
        if choice.lower() == 'easy':
            print("👍👍You've picked an easy quiz👍👍")
            print()
        elif choice.lower() == 'medium':
            print("👏👏You've picked a medium quiz👏👏")
            print()
        elif choice.lower() == 'hard':
            print("😯😯You've picked a hard quiz😯😯")
            print()
        elif choice.lower() == 'expert':
            print("💀💀You've picked an expert💀💀")
            print()
        break
    else:
        print("‼️Please enter one of the difficulties.‼️")
        print()

while True:
    quiz_type = input("Choose quiz type (infinite / fixed): ")

    if quiz_type.lower() == 'infinite':
        print("🤯🤯🤯 Wow! You picked the infinite amount of equations! 🤯🤯🤯")
        print()
        infinite(choice)
        break
    elif quiz_type.lower() == 'fixed':
        print("👏👏👏 Since you picked a fixed amount of equations for this quiz,"
              " you will then answer a 100 random set of equations! 👏👏👏")
        print()
        fixed(choice)
        break
    else:
        print("‼️Please choose either 'infinite' or 'fixed'.‼️")
        print()

# Ask if the user wants to see quiz results
while True:
    show_stats = input("Do you want to see the quiz results ( yes / no )? ").lower()
    if show_stats == "yes":
        quiz_results()
        break
    elif show_stats == "no":
        print("Thank you")
        break
    else:
        print("‼️Please enter 'yes' or 'no'.‼️")
        print()
