def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2
                                      
                                      ) == 0:
                return False
            i += 6
        return True

# Test the function
number = int(input("Enter a number to check if it's prime or not: "))
if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
        
        
        
        