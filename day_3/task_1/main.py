with open("input.txt", "r") as file:
    lines = file.readlines()

def mul(x,y):
    return int(x)*int(y)

import re

text=""

for line in lines:
    text+=line

pattern = r"mul\((\d+),(\d+)\)"

matches = re.findall(pattern, text)

sum=0

for match in matches:
    x, y = map(int, match)
    #print(f"x = {x}, y = {y}")
    sum+=mul(x,y)

print(sum)

