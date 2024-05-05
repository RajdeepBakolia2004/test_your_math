import number
import problem
from time import time

#this is the final part of the program that connects all the modules together
#this will ask the to choose a difficulty level and then generate a arithmetic problem based on the level
#then it will ask the user to solve the problem and check if the answer is correct 
#also return the time taken to solve the problem
#it will return the final score out of 5 problems generated of each addition, subtraction, multiplication and division
if __name__ == "__main__":
    print("Welcome to Math Quiz!")
    print("Choose a difficulty level:\n1. Easy\n2. Medium\n3. Hard")
    level = int(input("Enter the number corresponding to the difficulty level: "))
    while level not in [1, 2, 3]:
        print("Invalid input. Please try again.")
        level = int(input("Enter the number corresponding to the difficulty level: "))
    print("\nLet's start!\n")


    print("choose among the following operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. quit")
    option = set()
    inp = int(input("Enter the number corresponding to the operation: "))
    while inp != 5:
        if inp in [1,2,3,4]:
            option.add(inp)
        inp = int(input("Enter the number corresponding to the operation: "))
    option = list(option)
    score = 0
    if option == []:
        print("You have not selected any operation. Exiting program.")
    else:
        print("let's start the quiz!")
        start = time()
        for opt in option:
            if opt == 1:
                for i in range(5):
                    print("Addition")
                    final = problem.add(number.random_number(level), number.random_number(level))
                    if final[0]:
                        score += 1
                    print("time taken to solve the problem: ", final[1], "seconds")
            elif opt == 2:
                for i in range(5):
                    print("Subtraction")
                    final = problem.sub(number.random_number(level), number.random_number(level))
                    if final[0]:
                        score += 1
                    print("time taken to solve the problem: ", final[1], "seconds")
            elif opt == 3:
                for i in range(5):
                    print("Multiplication")
                    final = problem.mul(number.random_number(level), number.random_number(level))
                    if final[0]:
                        score += 1
                    print("time taken to solve the problem: ", final[1], "seconds")
            elif opt == 4:
                for i in range(5):
                    print("Division")
                    final = problem.div(number.random_number(level), number.random_number(level))
                    if final[0]:
                        score += 1
                    print("time taken to solve the problem: ", final[1], "seconds")
        end = time()
        print("You have completed the quiz!")
        print("Your final score is: ", score ," out of ",len(option)*5)
        print("Total time taken: ", round(end - start,3), "seconds")
        print("Thank you for playing!")

