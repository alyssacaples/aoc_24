filepath = "day2_input.txt"
safe_reports = 0


debug_stop = 0


print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
with open(filepath, 'r') as file:
            for x in file: # if unsafe bool is 1, restart
                print("############")
                report = x.split()
                print(report)
                #check if all increasing or decrease
                safe_report_bool = True
                diff = int(report[0]) - int(report[1])
                if(diff == 0):
                     prev_status = "no change"
                elif(diff > 0):
                     prev_status = "decreasing"
                else:
                     prev_status = "increasing"
                
                index = 0
                row_status = [prev_status]
                row_diff = [abs(diff)]
              
                unsafe_bool = 0
                unsafe_flag = False
                first_index_error_flag = False
                first_index_error_flag_part2 = False
                first_index_error_flag_part3 = False
                while(index < (len(report) - 1)):
                    #print("current index is ", index)
                    diff = int(report[index]) - int(report[index+1])
                    abs_diff = abs(diff)
                    #print("abs diff: ", abs_diff)

                    if(diff == 0):
                        status = "no change"
                    elif(diff > 0):
                        status = "decreasing"
                    else:
                        status = "increasing"
                    
                    row_status.append(status)
                    row_diff.append(abs_diff)
                    #

                    if(abs_diff == 0 or prev_status != status):
                        print("slope issue")
                        #safe_report_bool = False
                        print("unsafe bool: ", unsafe_bool)
                        unsafe_bool = unsafe_bool + 1
                        unsafe_flag = True
                    elif(abs_diff < 1 or abs_diff > 3):
                        print("too big of a diff")
                        #safe_report_bool = False
                        print("unsafe bool: ", unsafe_bool)
                        unsafe_bool = unsafe_bool + 1
                        unsafe_flag = True
                        
                        
                        #break

                      #  ['12', '10', '13', '16', '19', '21', '22'] how to delete this one
                      # do i detect that slope status same between 0-2 

                    #print(row_status)
                    if(unsafe_bool == 1 and unsafe_flag == True and (index == len(report) - 2)):
                        print("last one just delete it and move on")
                        break
                        
                        # my error is here ... how do I know whether to delete first index or next index?
                    elif(unsafe_bool == 1 and unsafe_flag == True and (index == 1)):
                        print("detected error in first row...")
                        #index = index + 1

                        # first delete first index
                        del report[0]
                        print("new report: ", report)

                        
                        if(len(report) == 1):
                             break
                        diff = int(report[0]) - int(report[1])
                        if(diff == 0):
                            prev_status = "no change"
                        elif(diff > 0):
                            prev_status = "decreasing"
                        else:
                            prev_status = "increasing"
                        
                        index = 0
                        row_status = [prev_status]
                        row_diff = [abs(diff)]
                        print("RESETTING NOW")
                        unsafe_flag = False
                        #need to determine if the issue is with index = 0 or index = 1
                        first_index_error_flag = True
                        
                        # try deleting first index
                        # if the row is unsafe, try again deleting the index[1]


                    elif(unsafe_bool == 1 and unsafe_flag == True and first_index_error_flag_part2 == False):    
                        print("FIRST ERROR DETECTED!")
                        print("deleting index: ", index)
                        del report[index]
                        print("new report: ", report)

                        
                        if(len(report) == 1):
                             break
                        diff = int(report[0]) - int(report[1])
                        if(diff == 0):
                            prev_status = "no change"
                        elif(diff > 0):
                            prev_status = "decreasing"
                        else:
                            prev_status = "increasing"
                        
                        index = 0
                        row_status = [prev_status]
                        row_diff = [abs(diff)]
                        print("RESETTING NOW")
                        unsafe_flag = False
                        #no unsafe bool
                    elif(first_index_error_flag_part2 == True and unsafe_bool > 0):
                        print(" WE ARE DIVING DEEPER INTO THE RABBIT HOLE")
                        # restart the entire row and see if this works
                        report = x.split()
                        index = 0
                        del report[2]
                        print("FIRST ERROR DETECTED!")
                        print("new report: ", report)

                        
                        if(len(report) == 1):
                            break
                        diff = int(report[0]) - int(report[1])
                        if(diff == 0):
                            prev_status = "no change"
                        elif(diff > 0):
                            prev_status = "decreasing"
                        else:
                            prev_status = "increasing"
                        
                        index = 0
                        row_status = [prev_status]
                        row_diff = [abs(diff)]
                        print("RESETTING NOW")
                        unsafe_flag = False
                        first_index_error_flag = False
                        unsafe_bool = 0
                        first_index_error_flag_part2 = False
                        first_index_error_flag_part3 = True
                    elif(first_index_error_flag_part3 == True and unsafe_bool > 0):
                        safe_report_bool = False
                        break
                    elif(unsafe_bool > 1):
                        print(str(unsafe_bool) + " ERROR DETECTED")
                        

                        if(first_index_error_flag == True):
                            print("FIRST INDEX ERROR FLAG")
                            # restart the entire row and see if this works
                            report = x.split()
                            index = 0
                            del report[1]
                            print("FIRST ERROR DETECTED!")
                            print("new report: ", report)

                            
                            if(len(report) == 1):
                                break
                            diff = int(report[0]) - int(report[1])
                            if(diff == 0):
                                prev_status = "no change"
                            elif(diff > 0):
                                prev_status = "decreasing"
                            else:
                                prev_status = "increasing"
                            
                            index = 0
                            row_status = [prev_status]
                            row_diff = [abs(diff)]
                            print("RESETTING NOW")
                            unsafe_flag = False
                            first_index_error_flag = False
                            unsafe_bool = 0
                            first_index_error_flag_part2 = True
                        else:
                            safe_report_bool = False
                            break
                    else: 
                        #print("index added")
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
                print("############")

                debug_stop = debug_stop + 1

                if(debug_stop == 25):
                    print("stopping now")
                    #break
print(safe_reports)


# what makes it unsafe?
# flag for removal


#ur just not sure if you should delete the index you are at or the next