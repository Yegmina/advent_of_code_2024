with open("input.txt", "r") as file:
    lines = file.readlines()

a = []
b = []

for line in lines:
    numbers = line.strip().split("   ") # strip() delete things line \n, split - split numbers by "   " in each line
    if len(numbers) == 2:
        a.append(int(numbers[0]))
        b.append(int(numbers[1]))

print("a:", a)
print("b:", b)
a.sort()
b.sort()
print("a:", a)
print("b:", b)
total_distance=0
if len(a)!=len(b):
    print("error, length should be same")
else:
    total_numbers=len(a)
for i in range(total_numbers):
    distance=abs(b[i]-a[i])
    total_distance+=distance

print(total_distance)
