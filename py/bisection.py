# Bisection method implementation | By Anirban
def bisection(a, b, threshold): 
    # Check if root can exist between the provided lower and upper bounds/limits:
    if (func(a) * func(b) >= 0): 
        print("No root exists between provided intervals.")
        print("(f(a) and f(b) must be of opposite signs)\n") 
        return   
    c = a 
    # Run function until the margin of precision satisfies the threshold:
    while ((b - a) >= threshold): 
        # Get the mid-point: 
        c = (a + b) / 2
        # Check if mid-point is the root: (break if true)
        if (func(c) == 0.0): 
            break
        # Decide the side to repeat the steps:
        # If f(a) and f(c) are of opposite signs, find the root between them:
        if (func(c) * func(a) < 0): 
            b = c 
        # Else find the root between f(b) and f(c): (taking value of a, conversely)
        else: 
            a = c 
    print("The value of the estimated root upto 5 decimal places is: ","%.5f"%c) 
