from questions import questions
from prizes import prizes, SAFE_QUESTION, SAFE_AMOUNT


def display_question(question, number, prize):

    print("\n" + "=" * 50)
    print("Question:", number)
    print("Prize: Rs.", format(prize, ","))
    print("=" * 50)

    print(question["question"])

    print()

    for option in question["options"]:
        print(option)


def check_answer(question):

    user = input("\nEnter your answer (A/B/C/D): ")

    user = user.strip().upper()

    if user not in ["A", "B", "C", "D"]:
        print("\nInvalid option!")
        return False

    if user == question["ans"]:
        print("\nCorrect answer!")
        return True

    else:
        print("\nWrong answer!")
        print("Correct answer:", question["ans"])
        return False


def play_game():

    money = 0
    safe_money = 0

    for i in range(len(questions)):

        question = questions[i]

        number = i + 1

        prize = prizes[i]

        display_question(question, number, prize)

        correct = check_answer(question)

        if correct:

            money = prize

            print("\nCurrent winnings: Rs.", format(money, ","))

            # Safety checkpoint
            if number == SAFE_QUESTION:

                safe_money = SAFE_AMOUNT

                print("\n" + "*" * 50)
                print("CONGRATULATIONS!")
                print("You reached the safety checkpoint!")
                print("Guaranteed amount: Rs.",
                      format(safe_money, ","))
                print("*" * 50)

            # Final question
            if number == len(questions):

                print("\n" + "*" * 50)
                print("CONGRATULATIONS!")
                print("You won Rs. 1,00,000!")
                print("*" * 50)

                break

            choice = input(
                "\nDo you want to continue? (yes/no): "
            )

            choice = choice.strip().lower()

            if choice == "no":

                print("\nYou decided to exit the game.")
                break

            elif choice == "yes":

                print("\nGet ready for the next question!")

            else:

                print("\nInvalid choice.")
                print("The game will end.")
                break

        else:

            money = safe_money

            print("\nYou take home: Rs.",
                  format(money, ","))

            break

    print("\n" + "=" * 50)
    print("GAME OVER")
    print("Final winnings: Rs.",
          format(money, ","))
    print("=" * 50)