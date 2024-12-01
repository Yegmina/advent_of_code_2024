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
total_similarity_score=0
if len(a)!=len(b):
    print("error, length should be same")
else:
    total_numbers=len(a)
for i in range(total_numbers):
    a_in_b=0
    for j in range(total_numbers):
        if a[i]==b[j]:
            a_in_b+=1
        elif b[j]>a[i]:
            break
    print(str(a[i])+": ")
    print(a_in_b)

    total_similarity_score+=a_in_b*a[i]
print("answer: ")
print(total_similarity_score)
