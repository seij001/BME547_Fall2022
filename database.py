# datbase.py
print("Python thinks this is called {}".format(__name__))

#import blood_calculator 
from blood_calculator import * #this function is the only thing imported

#if the Python file is in same directory, I can import it by name and use its functions
answer = check_HDL(55)
print("The HDL of 55 is {}".format(answer))