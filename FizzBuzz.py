for number in range(1, 101):
    if ( number % 3 == 0) & (number % 5 == 0):#If divisible by 3 and 5, print "Fizz Buzz"
        print("Fizz Buzz")
    elif number % 3 == 0:# If divisible by 3 "Fizz"
        print("Fizz")
    elif number % 5 == 0:# If divisible by 3 "Fizz"
        print("Buzz")
    else:
        print(number)