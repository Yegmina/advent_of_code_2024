def problem_dampener_handler(numbers):
    safe, first_index, second_index = check_line(numbers, -1)
    if safe:
        return True

    if first_index != -1 and check_line(numbers, first_index)[0]:
        return True

    if second_index != -1 and check_line(numbers, second_index)[0]:
        return True

    return False


def increasing_calculation(local_numbers):
    increasing_count = 0
    for i in range(1, len(local_numbers)):
        if local_numbers[i] > local_numbers[i - 1]:
            increasing_count += 1
        elif local_numbers[i] < local_numbers[i - 1]:
            increasing_count -= 1

    return increasing_count >= 0


def check_line(numbers, delete_index):
    temp_numbers = numbers[:]
    if delete_index != -1:
        temp_numbers.pop(delete_index)

    if len(temp_numbers) < 2:
        return False, -1, -1

    increasing = increasing_calculation(temp_numbers)
    for i in range(1, len(temp_numbers)):
        diff = temp_numbers[i] - temp_numbers[i - 1]

        if diff == 0:
            return False, i - 1, i
        if abs(diff) < 1 or abs(diff) > 3:
            return False, i - 1, i
        if (diff > 0) != increasing:
            return False, i - 1, i

    return True, -1, -1


safe_counter = 0
with open("input.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    numbers = [int(num) for num in line.strip().split()]
    if len(numbers) < 2:
        continue
    if problem_dampener_handler(numbers):
        print("1")
        safe_counter += 1
    else:
        print("0")

print(f"safe counter ={safe_counter}")