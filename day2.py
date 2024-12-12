filepath = "day2_input.txt"
safe_reports = 0
my_dict ={}
row_num = 0

debug_stop = 0
with open(filepath, 'r') as file:
            for x in file:
                report = x.split()
                print(report)
                #check if all increasing or decrease
                safe_report_bool = True
                diff = int(report[0]) - int(report[1])
                prev_status = "decreasing" if diff > 0 else "increasing"
                index = 0
                row_status = [prev_status]
                row_diff = [abs(diff)]
                while(index < (len(report) - 1)):
                    diff = int(report[index]) - int(report[index+1])
                    abs_diff = abs(diff)
                    #print("abs diff: ", abs_diff)
                    status = "decreasing" if diff > 0 else "increasing"
                    row_status.append(status)
                    row_diff.append(abs_diff)
                    #

                    if(abs_diff == 0):
                        print("no increase or decrease")
                        safe_report_bool = False

                    if(prev_status != status):
                        print("switching slope")
                        safe_report_bool = False
                        #break
                    
                    if(abs_diff < 1 or abs_diff > 3):
                        print("too big of a diff")
                        safe_report_bool = False
                        #break

                    #print(row_status)
                    index = index + 1

                #check difference between each line
                print(row_diff)
                print(row_status)
                #print("done with line")
                if(safe_report_bool == True):
                    print("SAFE!")
                    safe_reports = safe_reports + 1
                else:
                     print("BAD")

                my_dict[row_num] = safe_report_bool
                row_num = row_num + 1
                debug_stop = debug_stop + 1

                if(debug_stop == 50):
                     print("stopping now")
                     #break
print(safe_reports)
#print(my_dict)