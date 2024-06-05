import random
from fractions import Fraction


# To record every equation and right answers of the user
total_equations_attempted = 0  # Total equations user managed to answer
total_correct_answers = 0  # Total correct answer by the user


def yes_no(question):  # This is for the answers to the instructions
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "yeah":
            return "yes"
        elif response == "nah" or response == "nuh uh":
            return "no"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("‼️You did not choose a valid response‼️")
            print()


def generate_random_integer(start, end):
    return random.randint(start, end)


def instructions():  # Instructions
    print('''

🤖🤖🤖🤖 INSTRUCTIONS 🤖🤖🤖🤖

In this Mathematics quiz round, you'll need to answer some random generated equations in order to pass.

In order to pass, you'll need to answer the following equations correctly and don't forget to put your answers 
in two decimal places if needed.

You will only be given a one chance to answer correctly so think about it first before you type in your answer.

There will be two type of ways to do the quiz, one is where there's a fixed number of random equations or an infinite
number of equations.

Remember that when pick a fixed amount of equations in this quiz, you'll need to finish it.
If you choose an infinite amount of equation, you'll need to enter the exit code 'xxx' to end it.
Note that you'll need to answer a minimum of 75 equations in order for the exit code 'xxx' to work.

At the end of the quiz, your score will be shown.
If your answer is below 75% you'll fail.

            ''')


# This is the one of the main code that generate all the equations
def equation_generator(difficulty):  # The range of numbers depending on user's choice of difficulty
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
    equation = f"{num1} {operator} {num2}"  # This is how we want the equation to look like (for example 1 + 1)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        while num2 == 0:  # Ensure divisor is not zero
            num2 = random.randint(1, 10)
        result = round(num1 / num2, 2)  # To round the answer to two decimal places when a division equation show

    return equation, result


def answer_checker(user, math, equation):
    global total_correct_answers  # It is to collect user's correct answer for the stats at the end of the quiz

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

    # to put comments to user's answer and to show the answer if they got it wrong
    if user_answer == math:
        print("🙀🙀🙀 Oh my Oh my! You got it! So proud of ya! 🙀🙀🙀")
        total_correct_answers += 1
    elif user == equation:
        print("Come on, don't repeat the equation!")
    else:
        print("🫤🫤🫤 Sorry brother/sister, you didn't get it. 🫤🫤🫤")
        print("The correct answer is:", math)  # Will show the correct answer if user did not get it right


# If user picked an infinite quiz, this will run
def infinite(difficulty, num_equations=100000):  # The limit for infinite is 100000
    global total_equations_attempted  # The total number of equations the user will/need to answer
    print()
    print(f"You've selected a quiz with an infinite amount of equations and with a difficulty of {difficulty}!")
    print()

    for equation_number in range(1, num_equations + 1):  # This is to show the equation number
        equation, result = equation_generator(difficulty)  # The part where the equations generate
        print("EQUATION", equation_number, ":", equation)

        while True:
            user_input = input("Your Answer: ")

            if user_input.lower() == 'xxx':
                if total_equations_attempted >= 75:  # The equations needed to be answered before exit code work
                    confirmation = input("Are you sure you want to exit the quiz now? (yes / no): ").lower()
                    if confirmation == 'yes':
                        print("👏👏Thank you for answering👏👏")
                        print()  # Part of the quiz stats
                        print()  # This is to immediately show user their score after they finished answering
                        print("Your final score is", round((total_correct_answers / total_equations_attempted) * 100, 2), "%")
                        final_score = round((total_correct_answers / total_equations_attempted) * 100, 2)

                        if final_score >= 75:  # The required mark in order to pass
                            print("🥳🥳🥳Congratulations! You passed the quiz🥳🥳🥳")
                            print()
                        else:
                            print("😭😭😭Sorry, but you have failed the quiz. Better luck next time😭😭😭")
                            print()
                        print()
                        return True  # User chose to exit
                    else:  # If user do not enter a valid choice, quiz will automatically resume
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
            total_equations_attempted += 1  # The count of answered equations
            print()

    return False  # User didn't choose to exit


# If user picked a fixed quiz, this will run
def fixed(difficulty):
    global total_equations_attempted  # The total number of equations the user will/need to answer
    global total_correct_answers  # The total correct answers by the user for the stats part after finished quiz
    num_equations = 100  # Amount of equations for the fixed quiz
    print()
    print(f"You've selected a quiz with {num_equations} equations and with a difficulty of {difficulty}!")
    print()

    for equation_number in range(1, num_equations + 1):   # This is to show the equation number
        equation, result = equation_generator(difficulty)  # The part where the equations generate
        print("EQUATION", equation_number, ":", equation)

        while True:
            user_input = input("Your Answer: ")

            if user_input.lower() == 'xxx':  # If user enter the exit code in fixed quiz, it won't work
                if total_equations_attempted < num_equations:
                    print("Sorry but you can't exit this quiz until you answer a total of 100 equations")
                    print()
                    continue  # To resume the quiz

            try:
                user_answer = Fraction(user_input)
            except ValueError:
                print("‼️Please enter a valid answer.‼️")
                print()
                continue  # Repeat the same equation

            answer_checker(user_input, result, equation)
            total_equations_attempted += 1  # The count of answered equations
            print()
            break  # Move to the next equation after valid input

    print()  # This is to immediately show user their score after they finished answering (part of the quiz stats)
    print("Your final score is", round((total_correct_answers / total_equations_attempted) * 100, 2), "%")
    final_score = round((total_correct_answers / total_equations_attempted) * 100, 2)

    if final_score >= 75:
        print("🥳🥳🥳Congratulations! You passed the quiz🥳🥳🥳")
        print()
    else:
        print("😭😭😭Sorry, but you have failed the quiz. Better luck next time😭😭😭")
        print()
    print()
    return False  # User didn't choose to exit


# Statistics part of the code
def quiz_results():
    global total_correct_answers  # Total correct answers of the user's quiz
    global total_equations_attempted  # The total amount of equations answered by the user

    print()
    print("✖️➕➖➗ Quiz Results ➗➖➕✖️")
    print()
    print("Total equations attempted:", total_equations_attempted)
    print("Total correct answers:", total_correct_answers)
    print("Total wrong answers:", total_equations_attempted - total_correct_answers)
    print()


print()  # The title and warning that there's a quiz
print("⚠️⚠️ MATH QUIZ ALERT ⚠️⚠️")
print()

want_instructions = yes_no("Do you want to see the instructions ( yes / no )? ")

# checks users yes (y) or no (n)
if want_instructions == "yes":
    instructions()


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

while True:  # User options for the quiz difficulty
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
            print("💀💀You've picked an expert quiz💀💀")
            print()
        break
    else:
        print("‼️Please enter one of the difficulties.‼️")
        print()

while True:  # User options to what kind of quiz they want to answer
    quiz_type = input("Choose quiz type ( infinite / fixed ): ")

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
    if show_stats.lower() == "yes":
        quiz_results()
        break
    elif show_stats.lower() == "y":
        quiz_results()
        break
    elif show_stats.lower() == "no":
        print("Thank you")
        break
    elif show_stats.lower() == "n":
        print("Thank you")
    else:
        print("‼️Please enter 'yes' or 'no'.‼️")
        print()
