from intcomputer import IntcodeComputer


if __name__ == "__main__":
    input_filename = "day_02/input"
    # input_filename = "day_02/input_debug"

    with open(input_filename) as fp:
        input_data = fp.read().split(",")

    intprogram = [int(x) for x in input_data]

    computer = IntcodeComputer(intprogram)
    computer.restore_1202()

    while not computer.is_finished():
        computer.execute_operation()

    print(f"Execution is finished, result: {computer.result}")
