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
    #you need to convert d and l to int by using  int(d), int(l)
    return d, l

#you need to remove this line, cause there are no d, l defined in outer scope, system doesn't know who are they, and i m not sure what are you trying to do here
print d, l


#DO NOT DELETE
#YOU NEED THESE LINES TO RUN FOR THE RESULT
s = "hello world! 123"
classified_result = character_classifier(s)
print "LETTERS", classified_result["LETTERS"]
print "DIGITS", classified_result["DIGITS"]

