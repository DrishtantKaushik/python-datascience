def print_multiplication_table(number: int):
    """
    print the multiplication of given number.
    
    :paramnumber: the number is use for the multiplication table .
    :return: none
    """
    i = 1
    while i < 10:
        result = number * i
        print(f"{number} * {i} = {result}")
        i += 1
        
print_multiplication_table(5)