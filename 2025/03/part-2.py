def readInput(filePath):
    with open(filePath, "r") as file:
        return [line.strip() for line in file.readlines()]


def getNextMaxVoltage(batteries_remaining, batteries_found):
    batteries_to_consider = (
        batteries_remaining[: -(11 - batteries_found)]
        if batteries_found < 11
        else batteries_remaining
    )
    # print(f"    Considering: {batteries_to_consider} from {batteries_remaining}")
    maxVoltage = max(batteries_to_consider)
    maxIndex = batteries_remaining.index(maxVoltage)
    # print(f"    Found max: {maxVoltage} at index {maxIndex}")
    batteries_left = batteries_remaining[maxIndex + 1 :]
    # print(f"    Batteries left: {batteries_left}")
    return str(maxVoltage), batteries_left


# use twelve now instead of two
# find the largest digit, then the next largest from the remaining digits, etc.
def findMaxVoltage(battery_bank):
    # print(f"Evaluating bank: {battery_bank}")
    maxVoltage = ""
    batteries_left = battery_bank

    # keep track of twelve highest numbers
    for idx in range(12):
        # print(f"  Looking for battery {idx}")
        bank_max, batteries_left = getNextMaxVoltage(batteries_left, idx)
        maxVoltage += bank_max
        if len(batteries_left) <= 11 - idx:
            maxVoltage += batteries_left
            break

    return int(maxVoltage)


def main():
    inputLines = readInput("input.txt")

    voltageSum = 0

    for line in inputLines:
        voltage = findMaxVoltage(line)
        # print(f"Max voltage for bank: {voltage}")
        voltageSum += voltage

    print(f"Total voltage: {voltageSum}")


if __name__ == "__main__":
    # test_battery_bank = "9111121111118"
    # max_voltage = findMaxVoltage(test_battery_bank)
    # print(f"Test bank: {test_battery_bank} => Max voltage: {max_voltage}")
    main()
