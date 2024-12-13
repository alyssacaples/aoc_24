# alright so i shouldn't write spaghetti code!

a = "day2_input.txt"
b = "day2_checkanswer.txt"

def safe_array(input_report):
    safe_report_bool = True
    index = 0
    if(len(input_report) < 2):
        return False
    diff = int(input_report[0]) - int(input_report[1])
    prev_status = "decreasing" if diff > 0 else "increasing"
    while(index < (len(input_report)-1)):
        diff = int(input_report[index]) - int(input_report[index+1])
        status = "decreasing" if diff > 0 else "increasing"
        abs_diff = abs(diff)
        if(abs_diff == 0 or prev_status != status):
            print("bad slope")
            safe_report_bool = False
        elif(abs_diff < 1 or abs_diff > 3):
            print("too big of a diff")
            safe_report_bool = False
            #break

        index = index + 1
    
    return safe_report_bool

def unsafe_index(input_report):
    print("input report is: ", input_report)
    index = 0
    diff = int(input_report[0]) - int(input_report[1])
    prev_status = "decreasing" if diff > 0 else "increasing"
    while(index < (len(input_report)-1)):
        diff = int(input_report[index]) - int(input_report[index+1])
        status = "decreasing" if diff > 0 else "increasing"
        abs_diff = abs(diff)
        if(abs_diff == 0 or prev_status != status):
            print("bad slope")
            return index
        elif(abs_diff < 1 or abs_diff > 3):
            print("too big of a diff")
            #break
            return index

        index = index + 1
    
    return -1
#first, let's us identify what makes a safe report
#identified safe report
# second we will incorporate the levels
safe_report_cnt = 0
with open(a, 'r') as file:
    for x in file:
        print("##############")
        report = x.split()
        print(report)

        bad_index = unsafe_index(report)
        if(bad_index == -1):
            print("safe")
            safe_report_cnt = safe_report_cnt + 1
        else:
            print("bad index is ", report[bad_index], " ", bad_index)
            left = report[0:bad_index-1] + report[bad_index:]
            middle = report[0:bad_index] + report[bad_index+1:]
            right = report[0:bad_index+1] + report[bad_index+2:]
            print("left: ", left, "middle: ", middle, "right: ", right)
            checkleft = safe_array(left)
            checkmiddle = safe_array(middle)
            checkright = safe_array(right)
            if(checkleft or checkright or checkmiddle):
                safe_report_cnt = safe_report_cnt + 1
                print("safe")
            else:
                print("unsafe")
        

print("number of safe reports: ", safe_report_cnt)

# identify index of unsafe behavior