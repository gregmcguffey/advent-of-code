def readInput(filePath):
    with open(filePath, "r") as file:
        return [line.strip() for line in file.readlines()]


def findMaxVoltage(battery_bank):
    # print(f"Evaluating bank: {battery_bank}")
    maxVoltage = 0

    # keep track of two highest numbers
    # completely wrong logic....need to find largest voltage
    # for two of the batteries. So two loops...
    for idx, mainVolt in enumerate(battery_bank):
        remainingVolts = battery_bank[idx + 1 :]
        # spacer = " " * (idx + 1)
        # print(f"        other {mainVolt}: {spacer}{remainingVolts}")
        for otherVolt in remainingVolts:
            if otherVolt == " ":
                continue
            voltage = int(mainVolt + otherVolt)
            maxVoltage = voltage if voltage > maxVoltage else maxVoltage

    return maxVoltage


def main():
    inputLines = readInput("input.txt")

    voltageSum = 0

    for line in inputLines:
        voltage = findMaxVoltage(line)
        voltageSum += voltage

    print(f"Total voltage: {voltageSum}")


if __name__ == "__main__":
    main()
