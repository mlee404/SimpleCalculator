##From ArithmeticLibrary.py, import ALL of its methods.
## '*' is often shorthand for 'all'.
from ArithmeticLibrary import *;

##Retrieves the arithmetic function input from the user.
def getUserInput():
    while(True): ##while we still can run a loop,    
        cmd = input('Desired Operation: '); ##Ask for an input.
        if(cmd == 'Q' or cmd == 'q' or cmd == 'Quit'): ##If the user desires to quit,
            print('Bye!'); ##Print 'Bye!'
            return False; ##and break out of the while-loop.

        ##Otherwise...If the loop is not broken,
        result = handleUserInput(cmd); ##Get the result!
        if(result != None):     ##Only prints if the result returned is not 'None'.
            print('Result: ' + str(result));
        print('\n');  ##Insert a new line afterward.

##Handles the input and desired operations.
def handleUserInput(userInput):
    if(checkValidCommand(userInput)): ##Is this a valid command?  If 'True', continue.

        ##Try-Catch block!  'Try' this code, if it fails, 'Catch' the error.
        try:    ##Try this...
            firstNum = float(input('First Number: ')); ##Get first number from user.
        except ValueError:  ##Failed because user didn't put in a number (ValueError = Value was not acceptable type).
                print("That's not a number!");  ##Print this statement.
                return None; ##and terminate out of this method.

        ##Identical Try-Catch block.  This should really be in its own method...
        ##Rule of thumb: Avoid writing identical code multiple times.  If you can, then put it in a method!
        ##This is sloppy coding...
        try:
            secondNum = float(input('Second Number: '));
        except ValueError:
            print("That's not a number!");
            return None;

        ##Handle the two numbers accordingly.  This should be straightforward.
        ##The functions 'add', 'subtract', and 'multiply', come from the library.
        if userInput == 'Add':
            return add(firstNum,secondNum);
        
        elif userInput == 'Subtract':
            return subtract(firstNum, secondNum);
        
        elif userInput == 'Multiply':
            return multiply(firstNum, secondNum);

        elif userInput == 'Divide':
            divideLoop = True;  ##Start the while loop to check the divide input.
            while(divideLoop == True):  ##True = divideChoice was not a valid string.  Loop continues until valid string entered.
                divideChoice = input('Quotient or Decimal?  '); ##Awaiting user input.
                if divideChoice != 'Quotient' and divideChoice != 'Decimal': ##divideChoice input check.
                    print('Please type Quotient or Decimal to specify result.'); ##Invalid input.  Try again!
                else:
                    divideLoop = False; ##The choice is valid, break out of the loop!
            return getDecimalOrQuotient(divideChoice, firstNum, secondNum);
    else:
        print('Sorry, I do not recognize this command.');   ##The command did not match 'Add', 'Subtract', 'Multiply', or 'Divide'.
    
##Checks if the command input by user is valid.  Returns True if valid, False if invalid.
def checkValidCommand(command):
    if(command == 'Add' or command == 'Subtract' or command == 'Multiply'
       or command == 'Divide'):
        return True;
    return False;

##Returns different result based on the choice of 'Quotient' or 'Decimal'.
def getDecimalOrQuotient(choice, x, y):
    if choice == 'Quotient':
        print('(Q, R)');
        return divideQuotientRemainder(x,y);
    elif choice == 'Decimal':
        return divide(x,y);
