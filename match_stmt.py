ask = input("Whom do you vote?")
match ask:
    case "BJP":
        print("You are voting BJP")
    case "Congress":
        print("You are voting Congress")
    case _:
        print("You are voting other party")