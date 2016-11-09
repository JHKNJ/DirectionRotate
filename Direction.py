direction = input("What direction? ")

def turn_clockwise(rotate):
    if rotate == "N":
        d = "E"
        return(d)
    elif rotate == "E":
        d = "S"
        return(d)
    elif rotate == "S":
        d = "W"
        return(d)
    elif rotate == "W":
        d = "N"
        return(d)

print("Your direction is: " + turn_clockwise(direction))
