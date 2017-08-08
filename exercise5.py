#give you string "abcba"
#you need to find out if it is symmetrical



#print return_demo()


def isSymmetrical(input_str):
    #implement here
    #compare first character and last character?
    #compare 2nd and n-1
    mid_point = len(input_str) / 2

    for i in range (0,mid_point):
        print(i)
        print(len(input_str) -i -1)
        print(input_str[i])
        print(input_str[len(input_str) -i -1])
        if (input_str[i] != input_str[len(input_str) -i -1]):
            return False
    return True

print isSymmetrical("abcba")

    #step1. need to know the length of string

    #step2. compare the first and last

    #step3. compare the 2nd and n-1

    #stepn. until the mid point

    # use for loop to do step2-> stepn


    #if the input is "abcba"

    #1. compare the 1 and 5
    #2. compare the 2 and 4


    #if the input is "abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba"

    #1. xrange(start,end)
    #2. len(string_input)
    #3. string_input[n]
    #4. for loop



