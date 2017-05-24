#fill lthe function named character_classifier which will accepts a sentence and calculate the number of letters and digits.
#example input:
    #hello world! 123
#example output:
    #LETTERS 10
    #DIGITS 3


def function_name(s):
    d=l=0
    for c in s:
        if c.isdigit():
            d=d+1
        elif c.isalpha():
            l=l+1
        else:
            pass
    return s
print("Letters", l)
print("Digits", d)



s = raw_input()
classified_result = character_classifier(s)
print "LETTERS", classified_result["LETTERS"]
print "DIGITS", classified_result["DIGITS"]
