"""Write a program for simple arithmetic operations like add, subtract, multiplication, division and
etc..."""
number1 = input("Enter the first number:")
number2 = input("Enter the second number:")
print "1.Add\n2.subtraction\n3.Multiplication\n4.Division\n5.Modulo"
operation = input("Enter the operation:")
if 1 == operation:
    print number1 + number2
else:
    if 2 == operation:
        print number1 - number2
    else:
        if 3 == operation:
            print number1 * number2
        else:
            if 4 == operation:
                print number1 / number2
            else:
                if 5 == operation:
                    print number1 % number2
