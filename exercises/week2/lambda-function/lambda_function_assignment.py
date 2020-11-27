from functools import reduce


def first_fun():
    input1 = [
        ["34587", "Learning Python, Mark Lutz", 4, 40.95],
        ["98762", "Programming Python, Mark Lutz", 5, 56.80],
        ["77226", "Head First Python, Paul Barry", 3, 32.95],
        ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
    ]

    output1 = list(map(lambda x: (x[0], x[2] * x[3]), input1))
    print("Expected Output is: ")
    for x in output1:
        print(x)


def second_fun():
    input2 = [
        [1, ("5464", 4, 9.99), ("8274", 18, 12.99), ("9744", 9, 44.95)],
        [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
        [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
        [4, ("8732", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 39.95)]
    ]
    output2 = list(map(lambda x: [x[0]] + list(map(lambda y: y[1] * y[2], x[1:])), input2 ))
    output2 = list(map(lambda x: [x[0]] + [reduce(lambda a, b: a + b, x[1:])], output2))
    print("The (order number, total amount of order) for all is: ")
    for x in output2:
        print(x)


def main():
    print()
    first_fun()
    print("============================================================")
    second_fun()
    print()


if __name__ == '__main__':
    main()
