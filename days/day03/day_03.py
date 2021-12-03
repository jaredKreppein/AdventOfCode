# Advent of Code Day 3 - Binary Diagnostic

from copy import deepcopy


# part 1
def part_1(input_file):
    """
    Little trick:
    If you rotate the nested array 90 degrees (like a clockwise matrix rotation),
    you can compare by row instead of by column, which makes things a bit easier.
    And because the rotation happens in O(N), there's no large time complexity lost.

    When you compare by row, you can check if the sum(row) > len(row)/2 to determine
    if the number of '1's is the majority value.
    """
    g = ""
    e = ""
    L = []
    with open(input_file) as file:
        for line in file:
            L.append([int(i) for i in line.strip()])

    # rotate it 90 degrees clockwise
    # was working on a matrix rotation function until I stumbled upon this
    # shamlessly stolen from stackoverflow: https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    rotated = list(zip(*L[::-1]))

    for row in rotated:
        if sum(row) > len(row)/2:
            g += '1'
            e += '0'
        else:
            g += '0'
            e += '1'

    return int(g,2) * int(e,2)


# part 2
def part_2(input_file):
    """
    Use the rotated list to find the most common bit. Reduce the nested list
    by what that common bit is.

    Check that the list isn't size 1 and continue until it is and return the
    decimal equivalent of the final binary list value.

    The `while len(list) != 1` does appear to make this solution O(N^2), but we
    know this loop only ever lasts at most 12 iterations, so the solution stays
    as O(N), I think...

    TODO: combine the loops
    """
    o2_list = []
    co2_list = []
    with open(input_file) as file:
        for line in file:
            line = [int(i) for i in line.strip()]
            o2_list.append(line)
            co2_list.append(line)

    i = 0
    while len(o2_list) != 1:
        rotated = list(zip(*o2_list[::-1]))
        c = 1 if sum(rotated[i]) >= len(rotated[i])/2 else 0
        o2_list = list(filter(lambda x: x[i] == c, o2_list))
        i += 1
    o2 = int("".join(str(i) for i in o2_list[0]),2)

    i = 0
    while len(co2_list) != 1:
        rotated = list(zip(*co2_list[::-1]))
        c = 1 if sum(rotated[i]) >= len(rotated[i])/2 else 0
        co2_list = list(filter(lambda x: x[i] != c, co2_list))
        i += 1
    co2 = int("".join(str(i) for i in co2_list[0]),2)

    return o2*co2


# ----- main -----
input_file = "input.txt"

part_1_answer = part_1(input_file)
print("answer to part 1: {}".format(part_1_answer))

part_2_answer = part_2(input_file)
print("answer to part 2: {}".format(part_2_answer))
