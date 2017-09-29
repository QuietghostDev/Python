#11/13/14, Nigel, Prime Checker
def power():
    do = "Y"
    while do == "Y":
        result = 1
        base = input("Enter a base:\n")
        power = input("Enter a power:\n")
        while power > 0:
            if power%2 == 1:
                result = result*base
            base = base*base
            power = power/2
        print "=+=+=+=+=+=+=\n",result
power()
