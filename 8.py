# Solution to Advent of Code 2025 Day 8
from operator import itemgetter

def get_input(filename):    
    with open(filename, "r") as f:
        return f.read().splitlines()
    
def create_junction_boxes_dict(lines):
    junction_boxes = {}
    for line in lines:
        junction_boxes[line] = {
            "coordinates": line.split(","), 
            "connections": [],
            "distances": {}
        }

    return junction_boxes

def calculate_junction_distances(coordinates1, coordinates2):
    x1, y1, z1 = map(int, coordinates1)
    x2, y2, z2 = map(int, coordinates2)
    distance = (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2
    return distance

def get_shortest_distances(junction_boxes):
    processed = {}
    shortest_distances = []
    lonely_circuits = []
    for key in junction_boxes:
        lonely_circuits.append(key)
        processed[key] = True
        for other_key in junction_boxes:
            if other_key in processed:
                continue

            pair = [key, other_key]
            sorted_pair = sorted(pair)

            distance = calculate_junction_distances(junction_boxes[key]["coordinates"], junction_boxes[other_key]["coordinates"])
            sorted_pair.append(distance)
            shortest_distances.append(sorted_pair)

    shortest_distances.sort(key=itemgetter(2))

    return shortest_distances, lonely_circuits

def get_circuits(shortest_distances, lonely_circuits, limit=10):
    circuits = []

    count = 0
    connections = 0
    while connections < limit:
        junction1, junction2, distance = shortest_distances[count]
        
        merge1 = False
        merge2 = False
        merged = False

        for circuit in circuits:

            if junction1 in circuit and junction2 in circuit:
                merged = True
                break
            elif junction1 in circuit:
                merge1 = circuit
            elif junction2 in circuit:
                merge2 = circuit

        if merged == True:
            connections += 1
        elif merge1 and merge2:
            merge1.extend(merge2)
            merge1.sort()
            circuits.remove(merge2)
            connections += 1
        elif merge1:
            lonely_circuits.remove(junction2)
            merge1.append(junction2)
            merge1.sort()
            connections += 1
        elif merge2:
            lonely_circuits.remove(junction1)
            merge2.append(junction1)
            merge2.sort()
            connections += 1
        else:
            lonely_circuits.remove(junction1)
            lonely_circuits.remove(junction2)
            circuits.append(sorted([junction1, junction2]))
            connections += 1

        count += 1

    circuits.sort(key=len, reverse=True)

    return circuits, lonely_circuits

def calculate_product_of_circuits(circuits, limit=3):
    product = 1
    for circuit in circuits[:limit]:
        product *= len(circuit)
    return product

def connect_all_circuits(shortest_distances, lonely_circuits, limit=10):
    circuits = []

    count = 0
    connections = 0

    junction1x, junction2x = False, False
    while len(lonely_circuits) > 0:
        junction1, junction2, distance = shortest_distances[count]
        
        junction1x = junction1.split(",")[0]
        junction2x = junction2.split(",")[0]

        merge1 = False
        merge2 = False
        merged = False

        for circuit in circuits:

            if junction1 in circuit and junction2 in circuit:
                merged = True
                break
            elif junction1 in circuit:
                merge1 = circuit
            elif junction2 in circuit:
                merge2 = circuit

        if merged == True:
            connections += 1
        elif merge1 and merge2:
            merge1.extend(merge2)
            merge1.sort()
            circuits.remove(merge2)
            connections += 1
        elif merge1:
            lonely_circuits.remove(junction2)
            merge1.append(junction2)
            merge1.sort()
            connections += 1
        elif merge2:
            lonely_circuits.remove(junction1)
            merge2.append(junction1)
            merge2.sort()
            connections += 1
        else:
            lonely_circuits.remove(junction1)
            lonely_circuits.remove(junction2)
            circuits.append(sorted([junction1, junction2]))
            connections += 1

        count += 1

    x2 = int(junction1x) * int(junction2x)

    return x2

if __name__ == "__main__":
    lines = get_input("8.txt")

    junction_boxes = create_junction_boxes_dict(lines)

    # Part 1
    shortest_distances, lonely_circuits = get_shortest_distances(junction_boxes)
    circuits, lonely_circuits = get_circuits(shortest_distances, lonely_circuits, 1000)

    product_of_circuits = calculate_product_of_circuits(circuits)
    print("Product of lengths of the three longest circuits:", product_of_circuits)

    # Part 2
    shortest_distances, lonely_circuits = get_shortest_distances(junction_boxes)
    distance_from_wall = connect_all_circuits(shortest_distances, lonely_circuits)
    print("Distance from wall to connect all circuits:", distance_from_wall)
