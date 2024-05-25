def infinite(max_equation=1000):
    equation = 0
    while equation < max_equation:
        equation += 1
        print("EQUATION", equation)


def fixed(num_equations):
    for equation in range(1, num_equations + 1):
        print("Fixed equation", equation)


def fixed_infinite():
    print()
    print("Please type in below what type of quiz you want to do.")
    print()

    while True:
        quiz_type = input("Choose quiz type ( infinite / fixed ): ")

        if quiz_type.lower() == 'infinite':
            infinite()
            break
        elif quiz_type.lower() == 'fixed':
            num_equations = int(input("Since you chose to answer a fixed amount of equations, "
                                      "you will then answer 100 sets of random equations. "))
            fixed(num_equations)
            break
        else:
            print("Please choose either 'infinite' or 'fixed'.")
            print()


fixed_infinite()
