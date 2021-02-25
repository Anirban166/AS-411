# Estimation of Pi using Monte Carlo method           |
# with a visual representation of the same via a plot | By Anirban
import random 
import matplotlib.pyplot as plt
# Initialize the total number of points to consider: (preferably a large number)
totalPoints = int(1e+5) 
# Initialize a counter variable to count the number of points lying inside the circle: 
circlePoints = 0
# Looping through the total number of points considered:
for i in range(nums): 
    # Generating random numbers for (x, y) pair points from a uniform 
    # distribution with range of values from -1 to 1:
    randomX = random.uniform(-1, 1) 
    randomY = random.uniform(-1, 1)    
    # If a point (x, y) satisfies the equation of a circle (x^2 + y^2 <= 1) i.e. 
    # it lies inside or on the circumference of the circle, then I increment the 
    # counter accounting for the number of points the circle has: 
    if (randomX**2 + randomY**2) <= 1: 
        circlePoints += 1
        # Plot black points for the circle:
        plt.plot(randomX, randomY, 'k.')
    else:
        # Plot red points for the square:
        plt.plot(randomX, randomY, 'r.')
    # Estimate value of Pi with the formula taken into account:
    pi = 4 * circlePoints / totalPoints 
  
print("Points inside the square (or the total number of points taken):", nums)
print("Points inside the circle (a bit more than 3/4 of total points):", circlePoints)  
print("Estimation of Pi for the taken points (" + str(nums) + "): " + str(pi))
plt.show()

# Relevant blog post: https://anirban166.github.io//Pi-estimation/
