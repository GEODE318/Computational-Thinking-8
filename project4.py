print("Welcome to your personal Assistant")
Gmail = "no new messages"
Homework = "none"
Band_grade = "A"
Math_grade = "A"
Science_grade = "A"
Study_skills_grade = "Pass"
Visual_grade = "A"
Comp_grade = "B+"
English_grade = "B-"
History_grade = "C-"

#loop starts here line 7 to 48
for i in range (6):
    choice = input ("choose a funtion: grades, schedule, homework, gmail.")

    if choice == "grades" or choice == "Grades" or choice == " grades" or choice == " Grades" or choice ==  "grades " or choice ==  "Grades " or choice == " grades " or choice == " Grades ":
        print (f"Your grades are {Band_grade} in Band") 
        print (f"Your grades are {Math_grade} in Math")
        print (f"Your grades are {Science_grade} in Science")
        print (f"Your grades are {Study_skills_grade} in Study skills")
        print (f"Your grades are {Visual_grade} in Visual")
        print (f"Your grades are {Comp_grade} in Comp Thinking") 
        print (f"Your grades are {English_grade} in English")
        print (f"Your grades are {History_grade} in History")

    elif choice == "schedule" or choice ==  "Schedule" or  choice == " schedule" or  choice ==  " Schedule" or  choice == "schedule " or choice ==  "Schedule " or  choice == " schedule " or  choice == " Schedule ":
        # Based off of feedback i got
        Schedule = input ("Is it odd or even? and is it reverse or forward?")
        if Schedule == "odd forward" or Schedule == "odd Forward" or Schedule == "Odd forward" or Schedule == "Odd Forward" or Schedule == "oddforward" or Schedule == "Oddforward" or Schedule == "OddForward" or Schedule == "oddForward" or Schedule == "odd forward" or Schedule == "odd Forward" or Schedule == " Odd forward" or Schedule == " Odd Forward" or Schedule == " oddforward" or Schedule == " Oddforward" or Schedule == "oddForward" or Schedule == "OddForward" or Schedule == "odd forward " or Schedule == "odd Forward" or Schedule == "Odd forward " or Schedule == "Odd Forward " or Schedule == "oddforward " or Schedule == "Oddforward " or Schedule == "oddForward " or Schedule == "OddForward " or Schedule == " odd forward " or Schedule == " odd Forward " or Schedule == " Odd Forward " or Schedule == " Odd Forward" or Schedule == " oddforward " or Schedule == " Oddforward " or Schedule == " oddForward " or Schedule == " OddForward ":
            print ("Block 1:Study skills, Block 3: English, Block 5: Visual, Block 7: Science,")
        if Schedule == Schedule == "odd reverse" or Schedule == "odd Reverse" or Schedule == "Odd reverse" or Schedule == "Odd Reverse" or Schedule == "oddreverse" or Schedule == "Oddreverse" or Schedule == "OddReverse" or Schedule == "oddreverse" or Schedule == "odd reverse" or Schedule == "odd Reverse" or Schedule == " Odd reverse" or Schedule == " Odd Reverse" or Schedule == " oddreverse" or Schedule == " Oddreverse" or Schedule == "oddReverse" or Schedule == "OddReverse" or Schedule == "odd reverse " or Schedule == "odd Reverse" or Schedule == "Odd reverse " or Schedule == "Odd Reverse " or Schedule == "oddreverse " or Schedule == "Oddreverse " or Schedule == "oddReverse " or Schedule == "OddReverse " or Schedule == " odd reverse " or Schedule == " odd Reverse " or Schedule == " Odd Reverse " or Schedule == " Odd Reverse" or Schedule == " oddresverse " or Schedule == " Oddreverse " or Schedule == " oddReverse " or Schedule == " OddReverse ":
            print ("Block 7: Science, Block 5: Visual, Block 3: English, Block 1: Studyskills")
        if Schedule == Schedule == "Even reverse" or Schedule == "Even Reverse" or Schedule == "Even reverse" or Schedule == "Even Reverse" or Schedule == "evenreverse" or Schedule == "Evenreverse" or Schedule == "EvenReverse" or Schedule == "evenreverse" or Schedule == "even reverse" or Schedule == "even Reverse" or Schedule == " Even reverse" or Schedule == " Even Reverse" or Schedule == " evenreverse" or Schedule == " Evenreverse" or Schedule == "evenReverse" or Schedule == "EvenReverse" or Schedule == "even reverse " or Schedule == "even Reverse" or Schedule == "Even reverse " or Schedule == "Even Reverse " or Schedule == "evenreverse " or Schedule == "Evenreverse " or Schedule == "evenReverse " or Schedule == "EvenReverse " or Schedule == " even reverse " or Schedule == " even Reverse " or Schedule == " Even Reverse " or Schedule == " Even Reverse" or Schedule == " evenresverse " or Schedule == " Evenreverse " or Schedule == " evenReverse " or Schedule == " EvenReverse ":
            print ("Block 8: Math, Block 6: Comp Thinking, Block 4: Band, Block 2: History")
        if Schedule == Schedule == "Even forward" or Schedule == "Even Forward" or Schedule == "Even forward" or Schedule == "Even Forward" or Schedule == "evenforward" or Schedule == "Evenforward" or Schedule == "EvenForward" or Schedule == "evenforward" or Schedule == "even forward" or Schedule == "even Forward" or Schedule == " Even forward" or Schedule == " Even Forward" or Schedule == " evenforward" or Schedule == " Evenforward" or Schedule == "evenForward" or Schedule == "EvenForward" or Schedule == "even forward " or Schedule == "even Forward" or Schedule == "Even forward " or Schedule == "Even Forward " or Schedule == "evenforward " or Schedule == "Evenforward " or Schedule == "evenForward " or Schedule == "EvenForward " or Schedule == " even forward " or Schedule == " even Forward " or Schedule == " Even Forward " or Schedule == " Even Forward" or Schedule == " evenforward " or Schedule == " Evenforward " or Schedule == " evenForward " or Schedule == " EvenForward ":
            print ("Block 2: History, Block 4: Band, Block 6: Comp Thinking, Block 8: Math")
        

    elif choice == "Gmail" or  choice == "gmail" or  choice == " gmail" or  choice == " Gmail" or  choice == "gmail " or  choice == "Gmail " or  choice == " gmail " or  choice == " Gmail ":
        print (f"your gmail is {Gmail}")
    
    elif choice == "homework" or  choice == "Homework" or  choice == "hw" or  choice == "Hw" or  choice == "HW" or  choice == " homework" or  choice == " Homework" or  choice == " hw" or  choice == "Hw" or  choice == " HW" or  choice == "homework " or  choice == "Homework " or  choice == "hw " or  choice == "Hw " or  choice == "HW " or  choice == " homework " or  choice == " Homework " or  choice == " hw " or  choice == " Hw " or  choice == " HW ":
        print(f"Your homework is {Homework}")
        Homework = input("Type here tp update your homework")
    else:
        print ("not a vaild option. Try again")
    print ("thank you for using your personal Assistant")




    