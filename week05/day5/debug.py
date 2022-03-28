import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.ERROR)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

def read(prompt):
    return input(prompt)

def add(a,b):
    return a+b 

def div(a,b):
    return a/b

#Unit Test to validate the input
def verifyinput(value):
    assert str(value).isnumeric(), str(value)+" Not a number"

#Unit Test to validate the division    
def validatediv(a,b):
    assert b==0 , "Cannot divide by Zero"

def show():
    a = read("a = ")     #debugging read a
    b = read("b = ")     #debugging read b
    
    #The unit tests dynamically run with the script
    # verifyinput(a)
    # verifyinput(b)    
    # validatediv(a,b)

    try:        
        a = int(a)
    except ValueError:
        logger.error(f'ValueError: {a} should be an integer')
    except TypeError:
        logger.exception(f'Cannot cast {a} to int ')
                           
    try:        
        b = int(b)
    except ValueError:
        logger.error(f'ValueError: {b} should be an integer')
    except TypeError:
        logger.exception(f'Cannot cast {b} to int ')
                
    try:    
        print(add(a,b))
    except TypeError:
        logger.exception(f'Unsupported operand type(s) for + ')
        
    try:
        print(div(a,b))
    except ZeroDivisionError:
        logger.exception(f'Cannot divide by 0 - b = 0')
    except TypeError:
        logger.exception(f'Unsupported operand type(s) for / ')
        
     
show()

