import isFloat

x = raw_input("Number: ")

while not isFloat.isFloat(x):
    print "Invalid Number\n"
    x = raw_input("Number: ")

x = eval(x)
