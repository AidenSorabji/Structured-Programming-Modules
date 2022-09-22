counter = 0

print ("Please respond by answering either T for True or F for False")
print ('The purpose of this program is for you to understand the "and" and "or"\ncompound conditional statements.')
print()
while counter < 10:
    if counter == 0:
        answer_one = input("(5 >= 4) and (1 == 1): ")
        if answer_one == "T":
            print("Correct! Moving on to question 2!")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0
    
    if counter == 1:
        answer_two = input("(5 == 4) and (7 < 8): ")
        if answer_two == "F":
            print("Correct! Question 3")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 2:
        answer_three = input("(25 <= 24) or (11 == 11): ")
        if answer_three == "T":
            print("Correct! Question 4")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 3:
        answer_four = input("(-7 > -6) and (100 > 50): ")
        if answer_four == "F":
            print("Correct! Question 5")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 4:
        answerFive = input("(-9 == 9) or (40 > 30): ")
        if answerFive == "T":
            print("Correct! Question 6")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 5:
        answer_six = input("(7 == 8) or (1 > 0): ")
        if answer_six == "T":
            print("Correct! Question 7")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 6:
        answer_seven = input("not(7 > 6) and (1 == 1): ")
        if answer_seven == "F":
            print("Correct! Question 8")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 7:
        answer_eight = input("TRUE and FALSE: ")
        if answer_eight == "F":
            print("Correct! Question 9")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 8:
        answer_nine = input("TRUE or FALSE: ")
        if answer_nine == "T":
            print("Correct! Question 10")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 9:
        answer_ten = input("not(TRUE and TRUE) or not(FALSE and TRUE): ")
        if answer_ten == "T":
            print("CONGRATULATIONS! You have completed the compound conditional quiz.\nPlease add TWO more questions to the quiz and answer the questions below in the comments.")
            counter += 1
        else:
            print("Incorrect. Restarting questions.")
            counter = 0

    if counter == 10:
        answer_11 = input("You can eat food: ")
        if answer_11 == "T":
            print("good job, you got a question correct")
            counter += 1
        else:
            print("You are wrong :(")
            counter = 0
    
    if counter == 11:
        answer_12 = input("Pineapple on pizza is good: ")
        if answer_12 == "F":
            print('you right, you correct')
            counter += 1
        else:
            print("you wrong, you bad")
            counter = 0
    
    if counter == 12:
        answer_13 = input("Owen is weird: ")
        if answer_13 == "T":
            print("You is right, you win")
            breakpoint
        else:
            print("you wrong, you bad")
            counter = 0
        

"""
1. What are the logic rules to the 'and' compound condition?
    You can use "and" to basically add another condition to anything. the if statement will need to have both conditions accepted to run it.

2. What are the logic rules to the 'or' compound condition?
    You can use "or" to basically have two seperate conditions. Both can run individually if any of each are met.

3. What do you think the += operation does?
    Adds another value with the variable's value and assigns the new value to the variable.

4. Why do you think that the program will loop when you get a question incorrect?
    Because of the counter reset.

"""
        
    
