# this code do not count don't that start at the end of the line


with open("../task_1/input.txt", "r") as file:
    lines = file.readlines()

def mul(local_x,local_y):
    return int(local_x)*int(local_y)

def delete_in_diapazone(temp_list, start, end):
    return temp_list[:start]+temp_list[end:]


import re

text=""


start_point=0
end_point=0

print(lines)

line=lines

i=0
while i>=(len(line)-4):
    if line[i]=="d" and line[i+1]=="o" and line[i+2]=="n" and line[i+3]=="'" and line[i+4]=="t":
            print(f"don't found in i= {i}")
            start_point=i
            j=i+3
            while not (line[j] == "d" and line[j + 1] == "o"):
                j+=1
                if j>=len(line): break
            else:
                print(f"do found in j={j}")
                end_point=j+2
            print(f"cut from {line[start_point:end_point]}")
            if line[start_point:end_point]=="":
                break
            line=delete_in_diapazone(line,start_point,end_point)
    i=i+1
    print(line)

print("TTTEEEEXXXTTT")
print(line)
pattern_mul = r"mul\((\d+),(\d+)\)"

line=str(line)
matches_mul = re.findall(pattern_mul, line)

sum=0

enabled=True
for match in matches_mul:
    x, y = map(int, match)
    #print(f"x = {x}, y = {y}")
    sum+=mul(x,y)

print(sum)

