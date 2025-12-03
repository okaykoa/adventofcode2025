# Solution to Advent of Code 2025 Day 2

def get_input(filename):    
    with open(filename, "r") as f:
        print("reading input")
        return f.read().split(',')
    
def get_range(range_raw):
    first, second = range_raw.split('-')

    return int(first), int(second)

def get_halves(word):
    mid = len(word) // 2
    return word[:mid], word[mid:]

def find_mistakes_part1(ids):
    mistakes = []
    for id in ids:
        start, finish = get_range(id)
    
        while start <= finish:
            part1, part2 = get_halves(str(start))
            if part1 == part2:
                mistakes.append(start)
            start += 1

    return mistakes

# get all the possible subgroups of a word
def get_permutations(word):
    permutations = []

    group_count = 1
    while group_count <= len(word) // 2:
        place = 0
        group = []

        # only consider if groups are evenly divisible
        if len(word) % group_count != 0:
            group_count += 1
            continue

        while place < len(word):
            group.append(word[place:group_count+place])
            place += group_count

        permutations.append(group)

        group_count += 1
    
    return permutations

# check that all subgroups are the same
def check_repetitions(group):
    return len(set(group)) == 1

def find_mistakes_part2(ids):
    mistakes = []
    for id in ids:
        start, finish = get_range(id)

        while start <= finish:
            permutations = get_permutations(str(start))
            invalid_check = False
            for group in permutations:
                if check_repetitions(group):
                    invalid_check = True
                    break
            if invalid_check:
                mistakes.append(start)
            start += 1

    return mistakes

if __name__ == "__main__":
    ids = get_input("2.txt")

    mistakes = find_mistakes_part1(ids)
    print(f"Found {len(mistakes)} mistakes")

    print(sum(mistakes))

    mistakes = find_mistakes_part2(ids)
    print(f"Found {len(mistakes)} mistakes")

    print(sum(mistakes))

