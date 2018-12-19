import numpy as np
import matplotlib.pyplot as plt

original_probabilities = [0.25, 0.15, 0.1, 0.1, 0.15, 0.25]
data1 = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=200, replace=True, p=original_probabilities)
data2 = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=20000, replace=True, p=original_probabilities)
data1 = data1.tolist()
data2 = data2.tolist()
N1 = []
N2 = []
for i in range(6):
    N1.append(data1.count(i+1))
    N2.append(data2.count(i+1))

lamda1 = N1 / np.sum(N1)
lamda2 = N2 / np.sum(N2)
x = [1, 2, 3, 4, 5, 6]

plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1).set_title('Original')
plt.bar(x, original_probabilities, color='blue')
plt.ylabel('P(λ)')
plt.xlabel('λ')
plt.ylim(0, 0.3)
plt.xticks(x)

plt.subplot(1, 3, 2).set_title('Estimated from 200 data points')
plt.bar(x, lamda1, color='red')
plt.xlabel('λ')
plt.ylim(0, 0.3)
plt.xticks(x)

plt.subplot(1, 3, 3).set_title('Estimated from 20000 data points')
plt.bar(x, lamda2, color='red')
plt.xlabel('λ')
plt.ylim(0, 0.3)
plt.xticks(x)

plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8)
plt.savefig('Algorithm 4.4.png')
plt.show()