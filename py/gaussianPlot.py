# Plotting the Gaussian function | By Anirban
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Assigning some values for mean and variance:
mean = 50
variance = 25
# Calculating the standard deviation: (square root of variance)
standardDeviation = np.sqrt(variance)
# Generating a number space with equal intervals, ranging from three standard 
# deviations below the mean to three standard deviations above the mean with
# 500 samples:
x = np.linspace(mean - 3 * standardDeviation, mean + 3 * standardDeviation, 500)
# Plotting the results with a probability density function generator from Scipy:
plt.plot(x, stats.norm.pdf(x, mean, standardDeviation))
plt.show()

# Notes:
# I chose (randomly) the mean of my normal/gaussian distribution to be 50, and the variance to be 25 (implying a standard deviation of root(25) or 5). 
# As you can see, I created a number space with a range that extends upto 3 standard deviations away from the mean on either side. 
# The reason I selected 3 is because it is suitable to show the perfect hump (more than 3 would mean a steeper one, or a narrow hump), 
# and also because 3 divisions on each side gives the standard distribution pattern to compare against, such as:
# 1) The area between one standard deviation from both sides would account upto ~ 68% (~ 34% each) of the distribution, 
# or with my numbers, 45 - 55 would cover approximately 68% of the entirety. (45 - 50 & 50 - 55 being ~ 34% each)
# 2) Likewise, the area between two and three standard deviations from both sides would account upto ~ (68 + 28) = 96 % (~ 48 % on each side) 
# and ~ (96 + 2) = 98% of the distribution respectively, or with my numbers, 40 - 60 and 35 - 65 would cover approximately 96% and 98% respectively. 
# Approximate proportions: 2:14:34:34:14:2
