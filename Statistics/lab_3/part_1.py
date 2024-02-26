import numpy as np
import matplotlib.pyplot as plt

x_i = np.array([1, 10, 15, 23, 29, 38, 42])  # тут має бути таска вашого варіанту
p_i = np.array([0.02, 0.05, 0.1, 0.28, 0.23, 0.22, 0.1])  # тут має бути таска вашого варіанту
N = 100

X = np.random.choice(x_i, size=N, p=p_i)

mean_sample = np.mean(X)
var_sample = np.var(X)

print("Sample mean: {:.2f}".format(mean_sample))
print("Sample variance: {:.2f}".format(var_sample))

mean_theoretical = np.sum(x_i * p_i)
var_theoretical = np.sum((x_i - mean_theoretical) ** 2 * p_i)

print("Theoretical mean: {:.2f}".format(mean_theoretical))
print("Theoretical variance: {:.2f}".format(var_theoretical))

plt.hist(X, bins=len(x_i), density=True, alpha=0.5, color='b', edgecolor='black')
plt.plot(x_i, p_i, 'ro-', label='Theoretical distribution')
plt.legend()
plt.show()

intervals = [(1, 10), (11, 20), (21, 30), (31, 40), (41, 50)]

frequency = np.zeros(len(intervals), dtype=int)
for value in X:
    for i, interval in enumerate(intervals):
        if interval[0] <= value <= interval[1]:
            frequency[i] += 1
            break

total_observation = len(X)
relative_frequency = frequency / total_observation

print("\nInterval   Frequency   Relative Frequency")
for interval, freq, rel_freq in zip(intervals, frequency, relative_frequency):
    print("{:<9} {:<11} {:.2f}".format(f"{interval[0]}-{interval[1]}", freq, rel_freq))
