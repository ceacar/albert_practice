#you need to write a function that can write a string "test" to a file then read it and print out the content of the file


file = open("math.py","w")

file.write("test")

file.close()

file = open("math.py","r")
print file.readlines()
