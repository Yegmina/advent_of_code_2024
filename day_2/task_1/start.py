with open("input.txt", "r") as file:
    lines = file.readlines()

safe_counter=0
for line in lines:
    numbers = line.strip().split() # strip() delete things line \n, split - split numbers in each line
    safe=True
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])
        #print(numbers[i])
        #print(type(numbers[i]))
    #print("end of numbers in line")
    if numbers[1]-numbers[0]>0:
        increasing=True
    elif numbers[1]-numbers[0]<0:
        increasing=False
    else:
        safe=False
    #print(f"increasing: {increasing}")
    #print(f"safe: {safe}")
    for i in range(2, len(numbers)):
        if not safe:
            break
        if (numbers[i]>numbers[i-1])!=increasing:
            safe=False
            #print(f"for i {i} numbers[{i}]")
        elif abs(numbers[i]-numbers[i-1])>3 or abs(numbers[i]-numbers[i-1])<1:
            safe=False
    if safe:
        safe_counter+=1
    print(f"line {line} is safe={safe}")

print(safe_counter)