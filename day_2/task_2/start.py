
#have bug with index out of range because of deleting element
with open("input.txt", "r") as file:
    lines = file.readlines()


def problem_dampener_handler(local_numbers):
    if (check_line(local_numbers, -1)[0]) == True:
        return True
    else:
        local_first_delete_index = check_line(local_numbers, -1)[1]
        local_second_delete_index = check_line(local_numbers, -1)[2]
    if check_line(local_numbers, local_first_delete_index)[0] == True:
        return True
    elif check_line(local_numbers, local_second_delete_index)[0] == True:
        return True
    else:
        return False


def check_line(numbers, delete_index):
    first_delete_index = -1  # only 2 should be so it is okay to do without array/list
    second_delete_index = -1
    safe = True
    increasing = None

    if delete_index != -1:
        print(delete_index)
        numbers.pop(delete_index)

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if abs(diff) < 1 or abs(diff) > 3:
            safe = False
            if first_delete_index == -1:
                first_delete_index = i - 1
            if second_delete_index == -1:
                second_delete_index = i
            break
        if increasing is None:
            increasing = diff > 0
        elif (diff > 0) != increasing:
            safe = False
            if first_delete_index == -1:
                first_delete_index = i - 1
            if second_delete_index == -1:
                second_delete_index = i
            break
    print(f"Line {numbers} is safe={safe}")
    return safe, first_delete_index, second_delete_index


safe_counter = 0
for line in lines:
    numbers = [int(num) for num in line.strip().split()]

    if problem_dampener_handler(numbers):
        safe_counter += 1

print(f"Total safe reports: {safe_counter}")
