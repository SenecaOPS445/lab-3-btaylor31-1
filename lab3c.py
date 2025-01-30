#!/usr/bin/env python3

'''Lab 3 Inv 2 function operate '''
# Author ID: btaylor31

def operate(number1, number2, operator):
    # Place logic in this function
    if operator == 'add':
        result = number1 + number2
    elif operator =='subtract':
        result = number1 - number2
    elif operator =='multiply':
        result = number1 * number2
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

    return result

if __name__ == '__main__':
    print(operate(10, 5, 'add')) # This will return 15
    print(operate(10, 5, 'subtract')) # This will return 5
    print(operate(10, 5, 'multiply')) # This will return 50
    print(operate(10, 5, 'divide')) # This will return an error