import numpy as np
import matplotlib.pyplot as plt

pi = 3.1415926
I = [5, 30, 1000, 1000000]
original_mu = 5
original_sig = 8
alpha = 1
beta = 1
gamma = 1
delta = 0
count = 1
for i in I:
    data = original_mu + original_sig * np.random.randn(i)
    estimated_mu = (np.sum(data) + gamma * delta) / (i + gamma)
    estimated_mu_mle = np.sum(data) / i
    estimated_var = (np.sum(np.square(data - estimated_mu)) + 2 * beta + gamma * np.square(delta - estimated_mu)) / (i + 3 + 2 * alpha)
    estimated_var_mle = np.sum(np.square(data - estimated_mu_mle)) / i
    estimated_sig = np.sqrt(estimated_var)
    estimated_sig_mle = np.sqrt(estimated_var_mle)
    muError_map = abs(original_mu - estimated_mu)
    sigError_map = abs(original_sig - estimated_sig)
    muError_mle = abs(original_mu - estimated_mu_mle)
    sigError_mle = abs(original_sig - estimated_sig_mle)
    print("%d data points muError for MLE is %f" % (i, muError_mle))
    print("%d data points muError for MAP is %f" % (i, muError_map))
    print("%d data points sigError for MLE is %f" % (i, sigError_mle))
    print("%d data points sigError for MAP is %f" % (i, sigError_map))
    plt.subplot(2, 2, count).set_title('%d data points' % i)
    x = np.linspace(-20, 30, 100)
    y_01 = np.exp(- np.square(x - original_mu) / (2 * np.square(original_sig))) / (np.sqrt(2 * pi) * original_sig)
    y_02 = np.exp(- np.square(x - estimated_mu) / (2 * np.square(estimated_sig))) / (np.sqrt(2 * pi) * estimated_sig)
    y_03 = np.exp(- np.square(x - estimated_mu_mle) / (2 * np.square(estimated_sig_mle))) / (np.sqrt(2 * pi) * estimated_sig_mle)
    plt.plot(x, y_01, "g-", label='original', linewidth=2)
    plt.plot(x, y_02, "b-", label='MAP', linewidth=2)
    plt.plot(x, y_03, "r-", label='MLE', linewidth=2)
    plt.legend()
    count += 1

plt.suptitle('Algorithm 4.2')
plt.savefig('Algorithm 4.2.png')
plt.show()