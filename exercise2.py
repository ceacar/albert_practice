#fill lthe function named character_classifier which will accepts a sentence and calculate the number of letters and digits.
#example input:
    #hello world! 123
#example output:
    #LETTERS 10
    #DIGITS 3

#>>>this "function_name" is not a proper function name, it should be character_classifier.
def function_name(s):
    d=l=0
    for c in s:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1
        else:
            pass
    #>>>why are you returning s which is the input of this function. i assume you want to return the d, l to the outside
    return s

#>>these two doesn't have l and d defined ( they are defined in the function above, but not defined in the global scope
print("Letters", l)
print("Digits", d)



s = "hello world! 123"
classified_result = character_classifier(s)
print "LETTERS", classified_result["LETTERS"]
print "DIGITS", classified_result["DIGITS"]
