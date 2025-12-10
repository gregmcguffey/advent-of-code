def readInput(filePath):
    with open(filePath, "r") as file:
        return [line.strip() for line in file.readlines()]


def main():
    inputLines = readInput("input.txt")

    problems = []

    # parse each line, building problems, with matching items from each line
    for lineIdx, line in enumerate(inputLines):
        items = line.split()
        # number or operator
        for itemIdx, item in enumerate(items):
            value = item if item in ["+", "*"] else int(item)
            if lineIdx == 0:
                problems.append([value])
            else:
                problems[itemIdx].append(value)

    print(f"Problems parsed: {problems[-10:]}")

    # solve the problems and sum the results
    total = 0
    for operand1, operand2, operand3, operand4, operator in problems:
        if operator == "+":
            total += operand1 + operand2 + operand3 + operand4
        elif operator == "*":
            total += operand1 * operand2 * operand3 * operand4

    print(f"Total of all problems: {total}")


if __name__ == "__main__":
    main()
