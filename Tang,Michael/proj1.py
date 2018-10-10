## Name: Michael Tang
## Project #1
## Description: Make a simple program with python.
## In this program, I made a simple program that prints out Fizz for every 3rd
## mulitple, Buzz for every 5th multiple, and FizzBuzz for every 3rd and 5th
## multiple.

class FizzBuzz:
    
    for x in range(1,100):
        if (x%3 ==0 and x%5==0):
            print('FizzBuzz')
        
        elif (x%3 == 0):
            print('Fizz')
        
        elif (x%5 == 0):
            print('Buzz')
            
        else:
            print(x)
