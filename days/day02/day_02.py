# Advent of Code Day 2 - Dive!

# part 1
def part_1(input_file):
    """
    horizontal: add
    vertical: if 'down' add, if 'up' subtract
    multiply h*v
    """
    horizontal = 0
    vertical = 0
    with open(input_file) as file:
        for line in file:
            line = line.split()
            if line[0] == 'forward':
                horizontal += int(line[1])
            elif line[0] == 'down':
                vertical += int(line[1])
            else:   # up
                vertical -= int(line[1])
    return horizontal * vertical


# part 2
def part_2(input_file):
    """
    forward value always add to horizontal

    vertical value = pitch * forward value
    where pitch = down - up

    when pitch is positive: submarine is facing down and depth increases
    when pitch is negative: submarine is facing up and depth decreases
    """
    horizontal = 0
    vertical = 0
    pitch = 0
    with open(input_file) as file:
        for line in file:
            line = line.split()
            if line[0] == "forward":
                horizontal += int(line[1])
                if pitch == 0:
                    pass
                elif pitch > 0:
                    vertical += int(line[1]) * pitch
                else:
                    vertical -= int(line[1]) * pitch
            elif line[0] == "down":
                pitch += int(line[1])
            else: # line[0] == 'up'
                pitch -= int(line[1])
        return horizontal * vertical


# ----- main -----
input_file = "input.txt"

part_1_answer = part_1(input_file)
print("answer to part 1: {}".format(part_1_answer))

part_2_answer = part_2(input_file)
print("answer to part 2: {}".format(part_2_answer))
