# Advent of Code Day 1 - Sonar Sweep

# part 1
def count_increases(input_file):
    """
    When comparing values in a list like:

    199
    200
    208
    210
    200

    Compare the current value to the previous value.
    To save time and space, make this comparison during each new line read.
    """
    count = 0
    prev = 0
    with open(input_file) as file:
        prev = int(file.readline().strip())
        for next in file:
            next = int(next.strip())
            if next > prev:
                count += 1
            prev = next
    return count


# part 2
def count_sliding_increases(input_file):
    """
    When comparing 2 sums there are 4 values at play:

    199 A
    200 A B
    208 A B
    210   B

    let prev = index of the first value (list[0] = 199)
    let sum = the sum of the 2 middle values (200 + 208 = 408)
    let next = index of the last value (list[3] = 210)

    Now we can determine if an increase exists by checking:
    sum + list[next] > sum + list[prev]
    (408 + 210) > (408 + 199)   --->   618 > 607   --->   True
    """
    count = 0

    lines = []
    with open(input_file) as file:
        for line in file:
            lines.append(int(line.strip()))

    prev = 0
    sum = lines[1] + lines[2]
    for next in range(3, len(lines)):
        if sum + lines[next] > sum + lines[prev]:
            count += 1
        prev += 1
        sum = lines[next-1] + lines[next]
    return count


# ----- main -----
input_file = "input.txt"

part_1_answer = count_increases(input_file)
print("answer to part 1: {}".format(part_1_answer))

part_2_answer = count_sliding_increases(input_file)
print("answer to part 2: {}".format(part_2_answer))
