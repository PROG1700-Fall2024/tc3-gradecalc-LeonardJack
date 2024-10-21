# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    shouldRun = True
    grade = 0.0
    modifier = 0.0
    while shouldRun:    #while loop to make sure valid variable entry for letter grade
        letterGrade = input("Please enter a valid letter grade (A, B, C, D and F): ")
        gradeModifier = input("Please enter a grade modifier (+, - or nothing): ")  #while loop doesnt check if anything is entered for grade modifier because it being empty is valid
        if letterGrade.upper() == "A" or letterGrade.upper() == "B" or letterGrade.upper()==  "C" or letterGrade.upper() == "D" or letterGrade.upper() == "F": #checks for valid entry
            shouldRun = False    #entry is valid, finishes the loop

    if gradeModifier == "+" and letterGrade.upper() != "F" and letterGrade.upper() != "A": #will add + modifier if letter grade isnt A or F
        modifier += 0.3
    elif gradeModifier == "-" and letterGrade.upper() != "F":   #adds - modifier if letter grade isnt F
        modifier += -0.3

    if letterGrade.upper() == "A":  #assigns base numeric values based on letter grade
        grade += 4.0
    elif letterGrade.upper() == "B":
        grade += 3.0
    elif letterGrade.upper() == "C":
        grade += 2.0
    elif letterGrade.upper() == "D":    #^^^^^^^^^^
        grade += 1.0

    grade += modifier #adds modifier to grade

    print("Your grade in numeric value is {0:.1f}".format(grade))   #print statement formatted for output


    





    # YOUR CODE ENDS HERE

main()
