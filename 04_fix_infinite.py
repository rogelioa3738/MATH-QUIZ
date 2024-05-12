def infinite():
    round_num = 0
    while True:
        round_num += 1
        print("EQUATION", round_num)


def fixed(equation):
    for round_num in range(50, equation + 1):
        print("Fixed round", round_num)


def fixed_infinite():

    print()
    print("Please type in below what type of quiz do want to do.")
    print()

    # It will loop the question if answer is not valid
    while True:
        game_type = input("Choose game type ( infinite / fixed ): ")

        if game_type.lower() == 'infinite':
            infinite()
            break
        elif game_type.lower() == 'fixed':
            num_equations = int(input("Since you chose to answer a fixed amount of equations, "
                                      "you will then answer 50 sets of random equations. "))
            fixed(num_equations)
            break
        else:
            print("Please choose either 'infinite' or 'fixed'.")  # Prompt for valid input

if __name__ == "__main__":
    fixed_infinite()