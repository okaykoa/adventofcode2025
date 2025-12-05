# Solution to Advent of Code 2025 Day 5

def get_input(filename):    
    with open(filename, "r") as f:
        ranges, ids = f.read().split("\n\n")
        return ranges.splitlines(), ids.splitlines()

def get_ranges(ranges):
    old_ranges = ranges.copy()
    while True:
        for r, (start, end) in enumerate(ranges):
            in_range = False
            for i, (low, high) in enumerate(ranges):
                if low == start and high == end:
                    in_range = True
                    continue

                if start <= low <= end or start <= high <= end:
                    new_start = min(start, low)
                    new_end = max(end, high)
                    ranges[i] = (new_start, new_end)
                    in_range = True
                i += 1

            if in_range == False:
                ranges.append((start, end))
        
        if old_ranges == ranges:
            break
        old_ranges = ranges.copy()
    
    ranges = sorted(list(set(ranges)))
    return ranges

def check_in_range(ranges, id):
    for start, end in ranges:
        if start <= id <= end:
            return True
    return False

def check_ids(ranges, ids):
    results = []
    for id in ids:
        id_num = int(id.strip())
        results.append(check_in_range(ranges, id_num))
    return results

def calculate_total_ids(ranges):
    total = 0
    for start, end in ranges:
        total += (end - start + 1)
    return total

if __name__ == "__main__":
    filename = "5.txt"
    ranges_raw, ids = get_input(filename)
    
    ranges = []
    for range_raw in ranges_raw:
        start, end = map(int, range_raw.strip().split("-"))
        ranges.append((start, end))

    ranges = get_ranges(ranges)

    results = check_ids(ranges, ids)
    print("Number of Fresh IDs in Inventory:", sum(results))

    total = calculate_total_ids(ranges)
    print("Total number of Fresh IDs:", total)
