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
