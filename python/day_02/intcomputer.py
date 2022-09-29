from operator import itemgetter

"""Intcode computer

- indexing starts at 0
- opcode
    - can be 1, 2 or 99
    - indicates what to do
    - 99 -> finished
    - 1 -> add values from 2 following pointers; store in third
        pointer
    - 2 -> multiply values from 2 following pointers; store in third
        pointer
    - unknown code means failure
- after processing an opcode step forwards 4 positions
"""


def add(a: int, b: int):
    return a + b


def mult(a: int, b: int):
    return a * b


class IntcodeComputer:
    STEP_SIZE = 4
    ADD_COMMAND = 1
    MULT_COMMAND = 2
    TERM_COMMAND = 99

    operations = {ADD_COMMAND: add, MULT_COMMAND: mult}

    def __init__(self, program):
        self.program = program
        self._reset_memory()

    def _reset_memory(self):
        self._should_halt = False
        self._instruction_pointer = 0
        self.memory = list(self.program)

    def restore_1202(self):
        self.set_inputs(12, 2)

    def set_inputs(self, noun, verb):
        self._reset_memory()
        self.memory[1] = noun
        self.memory[2] = verb

    def is_finished(self):
        return self._should_halt

    def execute_operation(self):
        opcode = self.memory[self._instruction_pointer]

        if opcode == IntcodeComputer.TERM_COMMAND:
            self._should_halt = True
            return

        try:
            operation = IntcodeComputer.operations[opcode]
        except KeyError as e:
            raise RuntimeError(f"Abort. Encountered unknown opcode: {opcode}") from e

        left_arg_position, right_arg_position, result_position = self.memory[
            self._instruction_pointer + 1: self._instruction_pointer + 4
        ]
        left_arg, right_arg = itemgetter(left_arg_position, right_arg_position)(
            self.memory
        )

        self.memory[result_position] = operation(left_arg, right_arg)

        self._instruction_pointer += IntcodeComputer.STEP_SIZE

    @property
    def result(self) -> int:
        if not self.is_finished():
            raise RuntimeError("Program not finished.")

        return self.memory[0]
