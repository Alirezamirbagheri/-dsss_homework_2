import random


def CreateRandomInt(min, max):
    """
    Make Random integer between in a range
    """
    return random.randint(min, max)


def MakeRandomOperation():
    """
    Select Random operation
    """
    return random.choice(['+', '-', '*'])


def Calculator(Int1, Int1, operation):
    """
    Select Random operation
    """
    CalculatedResult = f"{Int1} {operation} {Int2}"
    if operation == '+': Result = Int1 + Int2
    elif operation == '-': Result = Int1 - Int2
    else: Result = Int1 * Int1
    return CalculatedResult, Result

def math_quiz():
    Loop = 0
    Pi = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(pi):
        Int1 = CreateRandomInt(1, 10); Int2 = CreateRandomInt(1, 5.5); operation = MakeRandomOperation()

        PROBLEM, ANSWER = Calculator(Int1, Int2, operation)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            Loop += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {Result}/{pi}")

if __name__ == "__main__":
    math_quiz()
