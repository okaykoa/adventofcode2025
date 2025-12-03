# Solution to Advent of Code 2025 Day 3

def get_input(filename):    
    with open(filename, "r") as f:
        print("reading input")
        return f.read().splitlines()
    
def find_next_number(id, remaining_digits, last_index):
    digit = "a"
    index = -1

    finished = False
    search_term = 10
    while finished == False:

        if search_term <= 0:
            break
        
        search_term -= 1

        try:
            search_index = id.index(str(search_term), last_index + 1)
        except ValueError:
            continue

        if search_index >= len(id) - remaining_digits:
            continue

        else:
            digit = id[search_index]
            index = search_index
            finished = True
            break

    return digit, index

def find_largest_number(id):
    digits = []
    digits_to_use = 12
    remaining_digits = digits_to_use

    index = -1
    while remaining_digits > 0:
        remaining_digits -= 1
        digit, index = find_next_number(id, remaining_digits, index)

        digits.append(digit)

    number = int("".join(digits))

    return number

def get_all_largest_numbers(ids):
    numbers = []
    for id in ids:
        number = find_largest_number(id)
        numbers.append(number)

    return numbers

if __name__ == "__main__":
    ids = get_input("3.txt")

    numbers = get_all_largest_numbers(ids)
    sum_numbers = sum(numbers)
    print(f"The sum of all largest numbers is: {sum_numbers}")
    



