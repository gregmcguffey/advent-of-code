from functools import reduce


def readInput(filePath):
    with open(filePath, "r") as file:
        return [line.strip() for line in file.readlines()]


def addOperands(operand1, operand2):
    return operand1 + operand2


def multiplyOperands(operand1, operand2):
    return operand1 * operand2


def main():
    inputLines = readInput("input.txt")

    # so parse all lines together. Operator is always in first column for problem
    # when all lines get a space, problem is over
    lineLen = len(inputLines[0])
    problems = []
    problem = []
    for idx in range(lineLen):
        # print(f"Parsing column {idx}")
        value1 = inputLines[0][idx]
        value2 = inputLines[1][idx]
        value3 = inputLines[2][idx]
        value4 = inputLines[3][idx]

        # operator line will be shorter than value lines
        operator = inputLines[4][idx] if idx < len(inputLines[4]) else " "

        if value1 == " " and value2 == " " and value3 == " " and value4 == " ":
            problems.append(problem)
            problem = []  # reset for next problem
            continue  # problem is over

        digit1 = value1 if value1 != " " else ""
        digit2 = value2 if value2 != " " else ""
        digit3 = value3 if value3 != " " else ""
        digit4 = value4 if value4 != " " else ""
        operand = int(digit1 + digit2 + digit3 + digit4)

        if operator != " ":
            # setup problem
            problem = [operator, operand]
        else:
            problem.append(operand)

    # add last problem
    problems.append(problem)

    print(f"Problems parsed: {problems[-5:]}")

    # solve the problems and sum the results
    total = 0
    for idx, (operator, *operands) in enumerate(problems):
        if operator == "+":
            result = reduce(addOperands, operands)
        elif operator == "*":
            result = reduce(multiplyOperands, operands)

        total += result

        if idx < 5:
            print(f"Solving problem {idx}: {operands} {operator} = {result} -> {total}")

    print(f"Total of all problems: {total}")


if __name__ == "__main__":
    main()
