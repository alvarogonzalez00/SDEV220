#Author: Alvaro Gonzalez
#Academic Preformance
#Description: This application will accept student's academic information then determine if they have qualified
#for either Dean's List or Honor Roll
print("---Student Academic Record's---\n-------------------------------")

while True:
    lname = input("(Enter 'ZZZ' to exit program)\nEnter student's last name:\n")
    if lname == 'ZZZ':
        break
    #verify if program has been exited
    
    fname = input("Enter student's first name:\n")
    gpa = input("Enter student's GPA:\n")
    format_gpa = float(gpa)
    name = (fname +' '+ lname)
    #Recieve input and format properly

    dean_list = (f"{name} has made the Dean's List")
    honor_roll = (f"{name} has made the Honor Roll")
    neither = (f"Unfortuntaley, {name} has not made the Dean's List or Honor Roll")
    #Prompts 
    
    if format_gpa >= 3.5:
        print(dean_list)
    elif format_gpa >= 3.25:
        print(honor_roll)
    else:
        print(neither)
    #Determine which category student falls in and print prompt accordingly