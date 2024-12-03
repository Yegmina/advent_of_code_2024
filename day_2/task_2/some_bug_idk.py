def problem_dampener_handler(numbers):
    # Check if the original report is already safe
    safe, first_index, second_index = check_line(numbers, -1)
    if safe:
        return True

    if check_line(numbers, first_index)[0]:
        return True
    if check_line(numbers, second_index)[0]:
        return True

    return False

def increasing_calculation(local_numbers):
    N=len(local_numbers)
    increasing_count=0
    for i in range(1, N):
        if local_numbers[i]>local_numbers[i-1]:
            increasing_count+=1
        elif local_numbers[i]<local_numbers[i-1]:
            increasing_count-=1
    increasing_bool=increasing_count>0
    return increasing_bool
def check_line(numbers, delete_index):
    temp_numbers = numbers[:]
    print(temp_numbers)
    if delete_index != -1:
        print(f"delete index{delete_index}")
        temp_numbers.pop(delete_index)

    increasing = None
    for i in range(1, len(temp_numbers)):
        diff = temp_numbers[i] - temp_numbers[i - 1]

        if diff==0:
            return False, i - 1, i
        if abs(diff) < 1 or abs(diff) > 3:
            return False, i - 1, i
        if increasing is None:
            increasing=increasing_calculation(temp_numbers)
            print(f"increasing {increasing}")
        elif (diff > 0) != increasing:
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
        safe_counter += 1

print(f"Total safe reports: {safe_counter}")
