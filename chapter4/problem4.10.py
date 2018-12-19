import numpy as np
import matplotlib.pyplot as plt

data = [0, 0, 0, 0]
I = 4
N = []
alpha = 1
beta = 1
for i in range(2):
    N.append(data.count(i))

lamda_mle = np.array(N) / I
lamda_map = (np.array(N) + alpha - 1) / (I + alpha + beta - 2)
alpha_post = N[1] + alpha
beta_post = N[0] + beta
x_prediction = [beta_post / (alpha_post + beta_post), alpha_post / (alpha_post + beta_post)]
x = [0, 1]

plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1).set_title('MLE')
plt.bar(x, lamda_mle, color='green')
plt.ylabel('P(x)')
plt.xlabel('x')
plt.ylim(0, 1)
plt.xticks(x)

plt.subplot(1, 3, 2).set_title('MAP')
plt.bar(x, lamda_map, color='blue')
plt.xlabel('x')
plt.ylim(0, 1)
plt.xticks(x)

plt.subplot(1, 3, 3).set_title('Bayesian')
plt.bar(x, x_prediction, color='red')
plt.xlabel('x')
plt.ylim(0, 1)
plt.xticks(x)

plt.subplots_adjust(left=0.2, bottom=0.2, right=0.8, top=0.8)
plt.savefig('Problem 4.10.png')
plt.show()