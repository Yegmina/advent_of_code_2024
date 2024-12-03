with open("input.txt", "r") as file:
    line = "".join(file.readlines())

def mul(local_x, local_y):
    return int(local_x) * int(local_y)

def delete_in_diapazone(temp_str, start, end):
    return temp_str[:start] + temp_str[end:]

import re

i = 0
while i <= len(line) - 5:
    if line[i:i+7] == "don't()":
        print(f"don't found at i={i}")
        start_point = i
        j = i + 5

        while j <= len(line) - 2:
            if line[j:j+4] == "do()":
                print(f"do found at j={j}")
                end_point = j + 2
                break
            j += 1
        else:
            break

        print(f"Cutting from '{line[start_point:end_point]}'")
        line = delete_in_diapazone(line, start_point, end_point)
        print(f"Updated line: {line}")

        i = start_point - 1

    i += 1

print("Processed Text:")
print(line)

pattern_mul = r"mul\((\d+),(\d+)\)"
matches_mul = re.findall(pattern_mul, line)

sum_of_mult = 0
for match in matches_mul:
    x, y = map(int, match)
    sum_of_mult += mul(x, y)

print("Sum of mul(x, y):", sum_of_mult)
