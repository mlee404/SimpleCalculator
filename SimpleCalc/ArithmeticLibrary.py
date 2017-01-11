##Your basic Arithmetic commands.
##Divide has a check to see if the second value is '0' because you cannot divide by 0.


def add(x,y):
    return x+y;

def subtract(x,y):
    return x-y;

def multiply(x,y):
    return x * y;

def divide(x,y):
    if(divideByZeroCheck(y)):
        return x/y;
    else:
        return False;

def divideQuotientRemainder(x,y):
    if(divideByZeroCheck(y)):
        return (int(x/y), int(x%y));
    else:
        return False;

def divideByZeroCheck(y):
    return y!=0;
