import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lambd = 13 # тут заміняєте на свій номер в журналі
p = 0.1

N_values = [100, 1000]

for N in N_values:
    X = np.random.poisson(lambd, size=N)

    sample_mean = np.mean(X)
    sample_variance = np.var(X)

    theoretical_mean = lambd
    theoretical_variance = lambd

    plt.figure()
    plt.hist(X, bins=range(min(X), max(X) + 1), density=True, color='skyblue', edgecolor='black', alpha=0.7)
    x_values = range(min(X), max(X) + 1)
    plt.plot(x_values, poisson.pmf(x_values, lambd), 'ro-', label='Poisson PMF')
    plt.title(f'Histogram and Poisson PMF for N={N}')
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()

    print(f"\nFor N = {N}:")
    print("Sample Mean:          {:.2f}".format(sample_mean))
    print("Sample Variance:      {:.2f}".format(sample_variance))
    print("Theoretical Mean:     {:.2f}".format(theoretical_mean))
    print("Theoretical Variance: {:.2f}".format(theoretical_variance))
