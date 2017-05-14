#python
#set a boolean variable , boolean is True or False
anan_choice=True
#set a string variable
anan_speech="python is awesom"
#set a number variable
anan_age=21


#conditional logic
if anan_choice == True:
    print "anan chose True"
else:
    print "anan chose False"


if anan_age > 21:
    print "anan_age is greater than 21"
elif anan_age < 21 and anan_age > 15:
    print "anan_age is a teenager"
else:
    print "anan_age is a kid"


#library
#library is a set of code that somebody lese wrote for intended people to use
import math
print math.log10(100)


#function
#function is a set of instruction for computer to remember in order to preform later time
def test_func():
    print "testing function here"
    if anan_age > 21:
        print "anan should know this"

test_func()

#function with parameter
def test_func2(inp):
    if inp > 21:
        print "anan input 21+"
    else:
        print "anan inpu didn't reach 21"

test_func2(20)
test_func2(22)


#class
#class is an object may contain variable and function

class my_class:
    def __init__(inp):
        #this is function init to initiate a new class with a parameter inp
        print "my_class is initiated"
    def bixy(self, inp):
        print inp

cls = my_class()
print "class should be initiated already"
cls.bixy("i m bixy")

