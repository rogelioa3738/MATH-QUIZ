import random


def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not choose a valid response")


def generate_random_integer(start, end):
    return random.randint(start, end)


def int_check(question):

    while True:

        error = "Please enter and integer that is 1 or more."

        to_check = input(question)

        # check for an infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            # checks that the number is greater than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def instructions():
    print('''

🤖🤖🤖🤖 INSTRUCTIONS 🤖🤖🤖🤖

In this Mathematics quiz round, you'll need to answer some random generated equations in order to pass.

In order to pass, you'll need to answer the following equations correctly and don't forget to put your answers 
in two decimal places.

You will only be given a one chance to answer correctly so think about it first before you type in your answer.

There will be two type of ways to do the quiz, one is where there's a fixed number of random equations or an infinite
number of equations.

            ''')
print()
print("⚠️⚠️ MATH QUIZ ALERT ⚠️⚠️")
print()

want_instructions = yes_no("Do you want to see the instructions? ")

# checks users yes (y) or no (n)
if want_instructions == "yes":
    instructions()


