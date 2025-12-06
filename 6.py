# Solution to Advent of Code 2025 Day 6
import numpy as np

def get_input(filename):    
    with open(filename, "r") as f:
        return f.read().splitlines()

def rearrange_vectors(vectors):
    rearranged_vectors = {}

    for vector in vectors:
        index = 0
        for item in vector:
            if index not in rearranged_vectors:
                rearranged_vectors[index] = [item]
            else:
                rearranged_vectors[index].append(item)
            index += 1
    
    return rearranged_vectors

def get_answers(rearranged_vectors, operations):
    index = 0
    answers = []
    counter = 0
    for op in operations:
        counter += 1
        if op == "*":
            answers.append(np.prod(list(map(int, rearranged_vectors[index]))))
        elif op == "+":
            answers.append(np.sum(list(map(int, rearranged_vectors[index]))))
        index += 1

    return answers

def reconstruct_numbers(rearranged_vectors):
    reconstructed_vectors = []

    for value in rearranged_vectors.keys():
        vector = rearranged_vectors[value]
        reconstructed_numbers = []
        for i in range(len(max(vector, key=len))):
            reconstructed_numbers.append('')

        for item in vector:
            item_count = len(item)
            char_list = list(item)
            for i in range(item_count):
                popped_char = char_list.pop()
                reconstructed_numbers[item_count-1] += popped_char
                item_count -= 1
        
        reconstructed_vectors.append(reconstructed_numbers)

    return reconstructed_vectors

def add_nums_to_vectors(vectors, lines, last_break, index):
    vectors_index = 0

    for line in lines[:-1]:
        vectors[vectors_index].append(line[last_break+1:index])
        vectors_index += 1

    return vectors

def parse_vectors_and_operations(lines):
    vectors = []

    for line in lines[:-1]:
        vectors.append([])

    operations = lines[-1].split()

    last_break = -1
    index = 0
    for char in lines[0]:
        if index + 1 == len(lines[0]):
            vectors = add_nums_to_vectors(vectors, lines, last_break, index + 1)

        if char == " ":
            is_space = True
            for line in lines[1:-1]:
                if line[index] != " ":
                    is_space = False
            
            if is_space:
                vectors = add_nums_to_vectors(vectors, lines, last_break, index)
                last_break = index

        index += 1

    return vectors, operations

if __name__ == "__main__":
    filename = "6.txt"
    lines = get_input(filename)

    vectors, operations = parse_vectors_and_operations(lines)

    rearranged_vectors = rearrange_vectors(vectors)

    answers = get_answers(rearranged_vectors, operations)
    print("Total Rearranged Answer:", sum(answers))

    reconstructed_numbers = reconstruct_numbers(rearranged_vectors)

    answers = get_answers(reconstructed_numbers, operations)
    print("Total Reconstructed Answer:", sum(answers))
