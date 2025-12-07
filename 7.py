# Solution to Advent of Code 2025 Day 7

def get_input(filename):    
    with open(filename, "r") as f:
        return f.read().splitlines()

def check_right(char_index, cur_line):
    if cur_line[char_index + 1] == "^":
        return True
    return False

def check_left(char_index, cur_line):
    if cur_line[char_index - 1] == "^":
        return True
    return False

def check_above(char_index, prev_line):
    if prev_line[char_index] == "|" or prev_line[char_index] == "S":
        return True
    return False

def process_lines(lines):
    splits = 0

    new_lines = []
    line_index = 0
    for line in lines:
        current_line = ""
        char_index = 0
        for char in line:
            place_ray = False
            if line_index == 0:
                current_line = line
                line
                break
            else:
                if char == "^":
                    if check_above(char_index, previous_line):
                        splits += 1
                    current_line += char
                    char_index += 1
                    continue
                if char_index == 0:
                    if check_above(char_index, previous_line) or check_right(char_index, line):
                        place_ray = True
                elif char_index == len(line) - 1:
                    if check_above(char_index, previous_line) or check_left(char_index, line):
                        place_ray = True
                else:
                    if check_above(char_index, previous_line) or check_left(char_index, line) or check_right(char_index, line):
                        place_ray = True

            if place_ray:
                current_line += "|"
            else:
                current_line += char
            
            char_index += 1

        previous_line = current_line
        new_lines.append(current_line)
        line_index += 1
    
    return new_lines, splits

def check_specific(char_index, prev_line):
    if prev_line[char_index] == "|":
        return True
    return False

def calculate_ends(new_lines):
    final_ray_traversals = []

    line_index = 0
    previous_ray_traversals = []
    for line in new_lines:
        current_ray_traversals = [0] * len(new_lines[0])
        if line_index == 0:
            current_ray_traversals[line.index('S')] = 1
            previous_ray_traversals = current_ray_traversals
            line_index += 1
            continue

        char_index = 0
        for char in line:
            if char == "|":
                if char_index == 0:
                    if check_right(char_index, line):  
                        current_ray_traversals[char_index] += previous_ray_traversals[char_index + 1]
                        
                elif char_index == len(line) - 1:
                    if check_left(char_index, line):  
                        current_ray_traversals[char_index] += previous_ray_traversals[char_index - 1]
                else:
                    if check_left(char_index, line):  
                        current_ray_traversals[char_index] += previous_ray_traversals[char_index - 1]
                    if check_right(char_index, line):  
                        current_ray_traversals[char_index] += previous_ray_traversals[char_index + 1]
                
                if check_above(char_index, line):  
                        current_ray_traversals[char_index] += previous_ray_traversals[char_index]

            char_index += 1
        
        final_ray_traversals = current_ray_traversals
        previous_ray_traversals = current_ray_traversals
        line_index += 1

    return final_ray_traversals

if __name__ == "__main__":
    lines = get_input("7.txt")

    new_lines, splits = process_lines(lines)
    print("Part 1 - Number of splitters:", splits)

    ends_reached = calculate_ends(new_lines)
    print("Part 2 - All possible traversals (top down):",sum(ends_reached))
