with open("input.txt", "r") as file:
    lines = file.readlines()

safe_counter = 0

for line in lines:
    numbers = [int(num) for num in line.strip().split()]



    safe = True
    increasing = None

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]

        if abs(diff) < 1 or abs(diff) > 3:
            safe = False
            break

        if increasing is None:
            increasing = diff > 0
        elif (diff > 0) != increasing:
            safe = False
            break

    if safe:
        safe_counter += 1

    print(f"Line {line.strip()} is safe={safe}")

print(f"Total safe reports: {safe_counter}")
