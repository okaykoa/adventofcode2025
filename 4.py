# Solution to Advent of Code 2025 Day 4

def get_input(filename):    
    with open(filename, "r") as f:
        return f.read().splitlines()

def count_accessible_rolls(answer_shelves):
    answer_total = 0
    iter_count = 0
    for answer_shelf in answer_shelves:
        iter_count += 1
        count_search_items = answer_shelf.count('x')
        answer_total += count_search_items
        print(iter_count, count_search_items)

    print("Total accessible rolls:", answer_total)

def count_rolls(shelves):
    total_rolls = 0
    for shelf in shelves:
        total_rolls += shelf.count('@')
    return total_rolls

def check_adjacent(shelf, index):
    adjacent_count = 0
    shelf_length = len(shelf)

    if index - 1 >= 0:
        if shelf[index - 1] == '@':
            adjacent_count += 1

    if index + 1 < shelf_length:
        if shelf[index + 1] == '@':
            adjacent_count += 1

    return adjacent_count

def check_adjacent_shelf(ashelf, index):
    adjacent_shelf_count = 0

    if ashelf[index] == '@':
        adjacent_shelf_count += 1

    adjacent_shelf_count += check_adjacent(ashelf, index)

    return adjacent_shelf_count

def process_shelves(shelves):
    previous_shelf = None
    next_shelf = None

    new_shelves = ""

    current_shelf_index = -1
    for shelf in shelves:

        current_shelf_index += 1

        if current_shelf_index + 1 < len(shelves):
            next_shelf = shelves[current_shelf_index + 1]
        else:
            next_shelf = None
        
        if current_shelf_index - 1 > -1:
            previous_shelf = shelves[current_shelf_index - 1]
        else:
            previous_shelf = None

        spot_index = -1
        for spot in shelf:
            spot_index += 1
            print_spot_index = 0
            print_spot_index_line = ""
            while print_spot_index < spot_index:
                print_spot_index_line += " "
                print_spot_index += 1

            if spot == '@':

                adjacent_rolls = 0

                adjacent_rolls += check_adjacent(shelf, spot_index)

                if previous_shelf:
                    adjacent_rolls += check_adjacent_shelf(previous_shelf, spot_index)

                if next_shelf:
                    adjacent_rolls += check_adjacent_shelf(next_shelf, spot_index)

                if adjacent_rolls < 4:
                    new_shelves += 'x'
                else:
                    new_shelves += '@'
            
            else:
                new_shelves += '.'
        
        new_shelves += '\n'
    
    return new_shelves
                
def recurse_process_shelves(shelves, iteration_count=0):
    new_shelves = process_shelves(shelves).split()
    
    iteration_count += 1

    if new_shelves == shelves:
        return new_shelves
    else:
        return recurse_process_shelves(new_shelves, iteration_count)

if __name__ == "__main__":
    filename = "4.txt"
    shelves = get_input(filename)

    new_shelves = recurse_process_shelves(shelves)
    rolls_removed = count_rolls(shelves) - count_rolls(new_shelves)
    print("Rolls removed:", rolls_removed)

