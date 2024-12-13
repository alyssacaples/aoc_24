import re


a = "day3_input.txt"
b = "day3_test.txt"

total_sum = 0
with open(a, 'r') as file:
    for i in file:
        matches = re.findall("mul\(\d+,\d+\)", i) # confirmed matches format
        for x in matches:
            n = re.findall("\d+,\d+", x)[0].split(",")
            product = int(n[0]) * int(n[1])
            total_sum = total_sum + product
print(total_sum)