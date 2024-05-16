def easy_quiz():
    print("You've selected an easy quiz!")
    print()
    # space for the code


def medium_quiz():
    print("You've selected a medium quiz!")
    print()
    # space for the code


def hard_quiz():
    print("You've selected a hard quiz!")
    print()
    # space for the code


def expert_quiz():
    print("Wow! You've selected the expert quiz!")
    print()
    # space for code


def main_levels():
    print()
    print("In this quiz, you will be given four difficulties you'll choose to answer")
    print()
    print("Choose one of the four following difficulty you'll want to do:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("4. Expert")
    print()

    while True:
        choice = input("What would you like to choose"
                       "(Type in the words easy / medium / hard / expert)? ")

        if choice == 'easy':
            easy_quiz()
        elif choice == 'medium':
            medium_quiz()
        elif choice == 'hard':
            hard_quiz()
        elif choice == 'expert':
            expert_quiz()
        else:
            print("‼️Please enter one of the difficulties‼️")
            print()


if __name__ == "__main__":
    main_levels()
