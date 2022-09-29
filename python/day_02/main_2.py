import itertools
from intcomputer import IntcodeComputer

GOAL_OUTPUT = 19690720


if __name__ == "__main__":
    input_filename = "day_02/input"
    # input_filename = "day_02/input_debug"

    with open(input_filename) as fp:
        input_data = fp.read().split(",")

    intprogram = [int(x) for x in input_data]

    computer = IntcodeComputer(intprogram)

    for noun, verb in itertools.product(range(100), range(100)):
        computer.set_inputs(noun=noun, verb=verb)

        while not computer.is_finished():
            computer.execute_operation()

        if computer.result == GOAL_OUTPUT:
            break

    print(f"Execution is finished, result: {computer.result}")
    print(f"{noun = }; {verb = }; {100 * noun + verb = }")
    