##From the file InputHandler.py, import the method, getUserInput().
##This must be done so I can call 'getUserInput()' within this file
##because it resides in a different location.
from InputHandler import getUserInput;

##The main() method.  
def main():
    initialize();
    getUserInput(); ##See 'getUserInput()' in InputHandler.py.

## 'initialize' is really just a bunch of print statements.
def initialize():
    print('This is a very basic arithmetic calculator.');
    print('For \'Desired Operation\', please type \'Add\', \'Subtract\', \'Multiply\', or \'Divide\'');
    print('Please type \'Q\', \'Quit\', or \'q\' if you are done.');
    cmd = input('Press \'Enter\' to begin.\n');
    print('\n\n');
    

## Note: The backslash ('\') is required for the single-quote (') to appear properly.
##Otherwise, it is treated like the start or end of a string.

##Call the main function!
main();
