#we also want to return with each function call the correct answer so that we can keep track of the score
#also the time taken to answer the question
from time import time


"""
    Adds two numbers and checks if the user's answer is correct.
    
    Parameters:
        a (int): The first number to be added.
        b (int): The second number to be added.
    
    Returns:
        tuple: A tuple containing a boolean indicating whether the answer is correct and the time taken to answer the question.
               - If the answer is correct, the first element of the tuple is True and the second element is the time taken to answer the question.
               - If the answer is incorrect, the first element of the tuple is False and the second element is the time taken to answer the question.
"""
def add(a,b):
    start = time()
    print(f"{a} + {b} = ?")
    ans = int(input("Enter your answer: "))
    end = time()
    if ans == a+b:
        print("Correct!")
        return True, round(end-start,3)
    else:
        print("Incorrect! The correct answer is: ", a+b)
        return False, round(end-start,3)




"""
    Subtracts two numbers and checks if the user's answer is correct. Prints the subtraction problem, waits for the user to enter their answer, 
    and then checks if the user's answer is equal to the subtraction of the two numbers. 
    If the answer is correct, it prints "Correct!", otherwise it prints "Incorrect! The correct answer is: {correct_answer}".
    
    Parameters:
        a (int): The first number in the subtraction.
        b (int): The second number in the subtraction.
    
    Returns:
        tuple: A tuple containing a boolean indicating whether the answer is correct and the time taken to answer the question.
               - If the answer is correct, the first element of the tuple is True and the second element is the time taken to answer the question.
               - If the answer is incorrect, the first element of the tuple is False and the second element is the time taken to answer the question.
"""
def sub(a,b):
    start = time()
    print(f"{a} - {b} = ?")
    ans = int(input("Enter your answer: "))
    end = time()
    if ans == a-b:
        print("Correct!")
        return True, round(end-start,3)
    else:
        print("Incorrect! The correct answer is: ", a-b)
        return False, round(end-start,3)




"""
    Multiplies two numbers and checks if the user's answer is correct.
    
    Args:
        a (int): The first number in the multiplication.
        b (int): The second number in the multiplication.
    
    Returns:
        tuple: A tuple containing a boolean indicating whether the answer is correct and the time taken to answer the question.
               - If the answer is correct, the first element of the tuple is True and the second element is the time taken to answer the question.
               - If the answer is incorrect, the first element of the tuple is False and the second element is the time taken to answer the question.
"""
def mul(a,b):
    start = time()
    print(f"{a} * {b} = ?")
    ans = int(input("Enter your answer: "))
    end = time()
    if ans == a*b:
        print("Correct!")
        return True, round(end-start,3)
    else:
        print("Incorrect! The correct answer is: ", a*b)
        return False, round(end-start,3)




"""
   This function divides two numbers and checks if the user's answer is correct.
   
   Parameters:
       a (int): The dividend number in the division.
       b (int): The divisor number in the division.
   
   Returns:
       tuple: A tuple containing a boolean indicating whether the answer is correct and the time taken to answer the question.
              - If the answer is correct, the first element of the tuple is True and the second element is the time taken to answer the question.
              - If the answer is incorrect, the first element of the tuple is False and the second element is the time taken to answer the question.
"""
def div(a,b):
    start = time()
    print(f"{a} // {b} = ?")
    ans = int(input("Enter your answer: "))
    end = time()
    if ans == a//b:
        print("Correct!")
        return True, round(end-start,3)
    else:
        print("Incorrect! The correct answer is: ", a//b)
        return False, round(end-start,3)
