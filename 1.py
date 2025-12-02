# Solution to Advent of Code 2024 Day 1
class DialNumber:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right

    def display_info(self):
        print(f"name: {self.name}, left: {self.left}, right: {self.right}")

def read_input(filename):    
    with open(filename, "r") as f:
        print("reading input")
        return f.read()
    
def make_list(content):
    return content.splitlines()

def create_dial():
    dial = {}

    x = 0
    while x < 100:
        if x == 0:
            dial[x] = DialNumber(name=x, left=99, right=x+1)
        elif x == 99:
            dial[x] = DialNumber(name=x, left=x-1, right=0)
        else:
            dial[x] = DialNumber(name=x, left=x-1, right=x+1)
        x += 1

    return dial

def split_instructions(instruction):
    return instruction[0], int(instruction[1:])

# not used
def compress_repeat(repeat):
    if repeat > 100:
        repeat %= 100
    return repeat


def decode_analog_part2(dial, instructions):
    current_position = 50

    count_zero = 0

    for instruction in instructions:

        direction, repeat = split_instructions(instruction)

        while repeat > 0:
            if direction == "L":
                current_position = dial[current_position].left
            elif direction == "R":
                current_position = dial[current_position].right
            
            repeat -= 1
            
            if current_position == 0:
                count_zero += 1

    return count_zero

def decode_math_part1(instructions):
    current_position = 50

    count_zero = 0

    for instruction in instructions:
        direction, repeat = split_instructions(instruction)
        repeat = compress_repeat(repeat)

        if direction == "L":
            current_position = (current_position - repeat) % 100
        elif direction == "R":
            current_position = (current_position + repeat) % 100
        
        if current_position == 0:
            count_zero += 1

    return count_zero

if __name__ == "__main__":
    print("main")
    filename = "1.txt"

    dial = create_dial()

    content = read_input(filename)
    instructions = make_list(content)

    code = decode_analog_part2(dial, instructions)
    print(code)
    code = decode_math_part1(instructions)
    print(code)
