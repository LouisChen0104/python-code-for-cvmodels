import numpy as np
import matplotlib.pyplot as plt

original_probabilities = [0.25, 0.15, 0.1, 0.1, 0.15, 0.25]
alpha = [1, 1, 1, 1, 1, 1]
I = [15, 1000000]
count = 1
plt.figure(figsize=(9, 6))
for i in I:
    data = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=i, replace=True, p=original_probabilities)
    data = data.tolist()
    N = []
    for j in range(6):
        N.append(data.count(j + 1))

    lamda = (np.array(N) + np.array(alpha) - 1) / np.sum(np.array(N) + np.array(alpha) - 1)
    x = [1, 2, 3, 4, 5, 6]
    x_prediction = (np.array(N) + np.array(alpha)) / np.sum(np.array(N) + np.array(alpha))

    plt.subplot(2, 3, count).set_title('Original')
    plt.bar(x, original_probabilities, color='green')
    plt.ylabel('P(λ)')
    if(count == 4):
        plt.xlabel('λ')
    plt.ylim(0, 0.4)
    plt.xticks(x)

    plt.subplot(2, 3, count + 1).set_title('MAP: %d data points' % i)
    plt.bar(x, lamda, color='blue')
    if (count == 4):
        plt.xlabel('λ')
    plt.ylim(0, 0.4)
    plt.xticks(x)

    plt.subplot(2, 3, count + 2).set_title('Bayesian: %d data points' % i)
    plt.bar(x, x_prediction, color='red')
    if (count == 4):
        plt.xlabel('λ')
    plt.ylim(0, 0.4)
    plt.xticks(x)
    count += 3

plt.savefig('Algorithm 4.6.png')
plt.show()