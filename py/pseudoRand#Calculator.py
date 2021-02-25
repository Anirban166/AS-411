# Generating a set of 100 random numbers using a calculator and plotting    |
# a histogram of these numbers to subsequently help classify the random     |
# number set generated to be uniform/normal based on the trend they follow. | By Anirban
import matplotlib.pyplot as plt
# Random number dataset produced by my calculator: 
# Using the defaults: 
# 1) Range of numbers between 0 and 1. 
# 2) Precision of the numbers are set upto 3 decimal places. 
x = [0.268, 0.905, 0.643, 0.180, 0.371, 0.448, 0.709, 0.803, 0.261, 0.733,
     0.657, 0.438, 0.134, 0.482, 0.770, 0.739, 0.448, 0.068, 0.577, 0.472,
     0.933, 0.424, 0.846, 0.215, 0.421, 0.243, 0.948, 0.847, 0.047, 0.080,
     0.173, 0.763, 0.145, 0.362, 0.931, 0.834, 0.731, 0.401, 0.811, 0.824,
     0.380, 0.304, 0.689, 0.408, 0.528, 0.615, 0.044, 0.169, 0.132, 0.217,
     0.943, 0.683, 0.240, 0.283, 0.807, 0.260, 0.543, 0.413, 0.370, 0.254,
     0.934, 0.542, 0.388, 0.009, 0.160, 0.468, 0.325, 0.509, 0.852, 0.144,
     0.061, 0.965, 0.958, 0.979, 0.032, 0.790, 0.517, 0.395, 0.410, 0.680,
     0.725, 0.058, 0.660, 0.638, 0.379, 0.850, 0.967, 0.286, 0.281, 0.557,
     0.821, 0.536, 0.384, 0.998, 0.801, 0.205, 0.743, 0.472, 0.351, 0.119]
plt.style.use('ggplot')
plt.hist(x, bins = 10)
plt.show()    

# One by one, I generated 100 random numbers using my calculator (shift + .) for the default range (0, 1) and precision (3 decimal places). 
# For the histogram plot, I selected the number of bins (or groups of division) to be 10 so as to see the frequency or pattern (if any) 
# of numbers grouped on the tenths place (first number to the right of the decimal point) i.e. the ranges (0.0 to 0.1), (0.1 to 0.2)…(0.9 to 1.0). 
# As evident from the plot above, there is, but very little difference between the frequency of numbers in each such range. 
# No range has a large enough distinguishing factor (like the mean/mode in a normal distribution) and the shape clearly doesn’t resemble a bell-shape either, 
# so I can safely say it is an uniform distribution, as visually discernible. (each number has equal probability of occurence)
