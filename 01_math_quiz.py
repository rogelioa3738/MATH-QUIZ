import random


def yes_no(question):
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


def instructions():
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

            ''')


print()
print("⚠️⚠️ MATH QUIZ ALERT ⚠️⚠️")
print()

want_instructions = yes_no("Do you want to see the instructions (yes / no)? ")

# checks users yes (y) or no (n)
if want_instructions == "yes":
    instructions()
