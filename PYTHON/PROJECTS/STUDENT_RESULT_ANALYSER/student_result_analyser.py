#create a student mark analysis using the concepts which i studied upto day7.
def get_student_data():                         #this is a function only to get student data as input and return two value "total" and "averages"
    student_name=input("Enter name of the student:")
    no_of_subjects=int(input("Enter number of subjects:"))
    students={}
    for i in range(no_of_subjects):              #this loop will execute "no.of.subject" times ex. if no.of sub is 3 , it willl execute 3 times
        subject=input("Enter name of subject:")
        mark=int(input("Enter mark of subject:"))
        students[subject]=mark
    return student_name,students                #this line throws out the values for the next function.if any functionn need these value mean, it can call it by parameter passing
#------------------------------------------------
def calculate_total_and_average(students):      #function which takes input through its parameter , if you dont specify the parameeter, the funciton doesnot know where to takee th inputs for operation.
    total=0
    for mark in students.values():
        total+=mark
    average=total/len(students)
    return total,average
#---------------------------------------------------------
def check_result(average):
        if average>=50:
            return "RESULT=pass"
        else:
            return "RESULT=reappear"
#--------------------------------------------------------------
def find_highest_subject(students):
    highest_mark=None
    highest_subject=None
    for subject,mark in students.items():
        if highest_mark is None or mark > highest_mark:
            highest_mark=mark
            highest_subject=subject
    return highest_subject,highest_mark
#------------------------------------------------------------------
name,students=get_student_data()                      #the function"get_student_data" contain two values in return statement i,e student_name and student.here in this line
                                                            #the two thrown valus is assigned to corresponding variables(name,student)
total,average=calculate_total_and_average(students)
result=check_result(average)
top_subject,top_mark=find_highest_subject(students)

print("Student Name:", name.upper())
print("Marks:", students)
print("Total Marks:", total)
print("Average Marks:", average)
print("Result:", result)
print("Highest Scoring Subject:", top_subject, "(", top_mark, ")")

'''basic steps
step1:creating a function to solve problem using logic only ,no actual Value
step2:assigning values of function to actual variable
step3:print the output using actual variable '''