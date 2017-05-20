#fill lthe function named character_classifier which will accepts a sentence and calculate the number of letters and digits.
#example input:
    #hello world! 123
#example output:
    #LETTERS 10
    #DIGITS 3


def character_classifier():
    #fill in here

s = raw_input()
classified_result = character_classifier(s)
print "LETTERS", classified_result["LETTERS"]
print "DIGITS", classified_result["DIGITS"]
