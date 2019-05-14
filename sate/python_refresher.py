#NAME:
#      PYTHON_refresher
# PURPOSE:
#      This is a simple PYTHON 2 program 
#      It is developed to show PYTHON grammar and simple PYTHON commands
# CATEGORY:
#      
# MODIFICATION HISTORY:
#      Bingqi YI, 2018-02-22

import time
import numpy as np
import matplotlib.pyplot as plt

# Operators
# Arithmetic operators are as you would guess: (+, -, /, *, ** for addi- tion, subtraction, division, multiplication, and exponentiation, respectively); 
# Operators (>, <, >=, <=, !=, == for greater than, less than, greater than or equal to, less than or equal to, not equal, and equal, respectively).

#----Variables
# Note that in Python 2.x, integers can be short or long; 
# short has a size limit but long does not. Since Python 2.2, if short int range exceeds, auto-conversion to long will be carried out. 
# In Python 3.x, all integers are long.

#-- short integer
A = 270 
B = 406
X1 = A+B
Y1 = A*B
print 'short integer', X1, Y1 # note the difference in python 2.x and 3.x in "print" format.
time.sleep(5)

#-- long integer
C = 270L
D = 406L
X2 = C+D
Y2 = C*D
print 'long integer', X2, Y2
time.sleep(5)

#-- float 
E = 3.14
F = -1.8e2
X3 = E/F
Y3 = A * E
print 'float', X3, Y3
time.sleep(5)

#-- complex
G = 1.0 + 2.0j
H = complex(1.0, 2.0)
print 'complex', G, H
time.sleep(5)

#-- string 
# Python is case-sensitive, so N and n are different.
S1 = "Dude, "
S2 = 'How are you?'
S3 = S1 + S2
print S3
print S2[4:7] # REMBER: Indices start at ZERO, from 0 to N-1!!
raw_input("Press Enter to continue ...") # Use 'input("xxx")' in python 3.x

#-- list
# List is defined as x=[a,b,c], can have mixed type of components
L1 = [1,2,3.0,4,5.5]
L2 = ["This", "is", 2, "list"]
print L1[2:-1]
print L2[3]
L1[4] = 6.6
print L1
L3 = range(5) # note "range(x)" function returns a "list".
raw_input("Press Enter to continue ...")

#-- tuple
# Tuple is defined as x=(a,b,c); it is like "read-only" list; can not be updated
T1 = (1,2,3.0,4,5.5)
T2 = ["This", "is", 2, "list"]
print T1[2:-1]
print T2[3]
# T1[4] = 6.6 # You can check this line - it could not go through.
print T1
raw_input("Press Enter to continue ...")

#-- Array
# Import numpy first
# NumPy arrays are like lists except all elements are the same type.
Intarr0 = np.array([ 1, 3, 5, 7, 9])            # create array by listing all the elements
print 'int array #0:', Intarr0 
IntArr1 = np.zeros((3,2), dtype='d')            # create array by making a new array with zeros 
IntArr2 = np.arange(5)      # generate a continuous integer array [0,1,2,3,4] by calling the function arange
IntArr3 = np.arange(5.0)    # the output type is the same as your input
print 'int array #1:', IntArr1
print 'int array #2:', IntArr2
print 'int array #3:', IntArr3
# You may check the array information
print np.shape(IntArr1)
print np.size(IntArr2)

raw_input("Press Enter to continue ...")

#-- Functions
# Functions in Python, in theory, work both like functions and subroutines in Fortran
def area(radius):
    area = 3.14 * (radius**2)
    return area
print area(1.0)

raw_input("Press Enter to continue ...")

#---- Control statement 

#-- if control
cont1 = 10
if (cont1 < 1):                
    print 'constant is smaller than 1'
elif (cont1 > 5):
    print 'constant is larger than 5'    
else:
    print 'constant is larger than 1, but smaller than 5'

raw_input("Press Enter to continue ...")

#-- for control
for i in [2, -3.3, 'hello', 1, -12]:
    print i
list = [2, -3.3, 'hello', 1, -12]
for j in range(5):
    print list[j]
    
raw_input("Press Enter to continue ...")

#-- while control
a=1
while a < 10:
    print a 
    a=a+1
    
raw_input("Press Enter to continue ...")
    
#------------------------------------------------

#-- Modules
T = [273.4, 265.5, 277.7, 285.5]
maxT = np.max(T)
minT = np.min(T)
avg_max_min = 0.5 * (maxT + minT)

raw_input("Press Enter to continue ...")

#---- plotting, on the screen
plt.plot([1, 2, 3, 4], [1, 2.1, 1.8, 4.3])
plt.axis([0, 8, -2, 7])
plt.xlabel('Automatic Range')
plt.ylabel('Made-up Numbers')
plt.show()

raw_input("Press Enter to continue ...")


#-- printing figure to a PNG file 
plt.plot(np.arange(10.0), np.arange(10.0)*3.0+1.0, 'r--')
plt.xlabel('Automatic Range')
plt.ylabel('Made-up Numbers')
plt.title('Zeroth Plot', size=36.0)
plt.savefig('pyplot_markers.png', dpi=300)

raw_input("Check the saved figure file, then press Enter to continue ...")

#------------------------------------------------



