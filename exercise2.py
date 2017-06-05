#fill lthe function named character_classifier which will accepts a sentence and calculate the number of letters and digits.
#example input:
    #hello world! 123
#example output:
    #LETTERS 10
    #DIGITS 3

def character_classifier(s):
    d=l=0
    for c in s:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1
        else:
            pass
    #you need to convert d and l to string by using  str(d), str(l)
    #also you need to put these two values into a dictionary. lookup python dictionary
    return str(d), str(l)

#you need to remove this line, cause there are no d, l defined in outer scope, system doesn't know who are they, and i m not sure what are you trying to do here


#DO NOT DELETE
#YOU NEED THESE LINES TO RUN FOR THE RESULT

#this is the string that you will run through your function character_classifier
s = "hello world! 123"
#this is the where you run above string
classified_result = character_classifier(s)
#you are printing how many letter are there by look up a dictionary with key word "LETTERS"
print "LETTERS", classified_result["LETTERS"]
#you are printing how many digits are there by look up a dictionary with key word "DIGITS"
print "DIGITS", classified_result["DIGITS"]

