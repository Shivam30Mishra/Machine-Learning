import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Mean and Standard Deviation
mu, sigma = 50, 10
x = np.linspace(20, 80, 100)

# Gaussian Function
plt.plot(x, norm.pdf(x, mu, sigma))
plt.title("Gaussian Distribution")
plt.xlabel("X Value")
plt.ylabel("Probability Density")
plt.show()
