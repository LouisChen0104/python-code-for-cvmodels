import numpy as np
import matplotlib.pyplot as plt

original_probabilities = [0.25, 0.15, 0.1, 0.1, 0.15, 0.25]
data1 = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=200, replace=True, p=original_probabilities)
data2 = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=2000, replace=True, p=original_probabilities)
data3 = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=200000, replace=True, p=original_probabilities)
data1 = data1.tolist()
data2 = data2.tolist()
data3 = data3.tolist()
N1 = []
N2 = []
N3 = []
alpha = [10, 100, 1000, 1000, 100, 10]
for i in range(6):
    N1.append(data1.count(i+1))
    N2.append(data2.count(i+1))
    N3.append(data3.count(i+1))

lamda1 = (np.array(N1) + np.array(alpha) -1) / np.sum(np.array(N1) + np.array(alpha) - 1)
lamda2 = (np.array(N2) + np.array(alpha) -1) / np.sum(np.array(N2) + np.array(alpha) - 1)
lamda3 = (np.array(N3) + np.array(alpha) -1) / np.sum(np.array(N3) + np.array(alpha) - 1)
x = [1, 2, 3, 4, 5, 6]

plt.figure(figsize=(24, 6))
plt.subplot(1, 4, 1).set_title('Original')
plt.bar(x, original_probabilities, color='blue')
plt.ylabel('P(λ)')
plt.xlabel('λ')
plt.ylim(0, 0.5)
plt.xticks(x)

plt.subplot(1, 4, 2).set_title('MAP: 200 data points')
plt.bar(x, lamda1, color='red')
plt.xlabel('λ')
plt.ylim(0, 0.5)
plt.xticks(x)

plt.subplot(1, 4, 3).set_title('MAP: 2000 data points')
plt.bar(x, lamda2, color='red')
plt.xlabel('λ')
plt.ylim(0, 0.5)
plt.xticks(x)

plt.subplot(1, 4, 4).set_title('MAP: 200000 data points')
plt.bar(x, lamda3, color='red')
plt.xlabel('λ')
plt.ylim(0, 0.5)
plt.xticks(x)

plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8)
plt.savefig('Algorithm 4.5.png')
plt.show()