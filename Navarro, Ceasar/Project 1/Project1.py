"""for i in range(1,100):
    if(i%3 == 0 and i%5 == 0):
        print("Fizz Buzz") 
    elif(i % 5 == 0):
     print("Buzz")
    elif(i % 3 == 0):
        print("Fizz")
    else:
         print(i)"""

def bonus(n=1, m=100):
    if(n > m):
        return 
    elif(n%3 ==0 and n%5 == 0):
        print("Fizz Buzz")
    elif(n%5 == 0):
        print("Buzz")
    elif(n%3 == 0):
        print("Fizz")
    else:
        print(n)
    bonus(n + 1, m)
if __name__ == '__main__':
   bonus()