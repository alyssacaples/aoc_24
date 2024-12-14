import re


a = "day3_input.txt"
b = "day3_test.txt"

total_sum = 0
cnt = 0
with open(a, 'r') as file:
    mult_bool = True
    for i in file:
        matches = re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", i) # confirmed matches format
        for x in matches:
            #need to determine if x is do or don't
            #print(x)
            if(x == "do()"):
                mult_bool = True
            elif(x == "don't()"):
                mult_bool = False
            elif(mult_bool):
                print("answer: ", mult_bool, " match: ", x)
                n = re.findall("\d+,\d+", x)[0].split(",")
                product = int(n[0]) * int(n[1])
                total_sum = total_sum + product
            
            print("answer: ", mult_bool, " match: ", x)

print(total_sum)