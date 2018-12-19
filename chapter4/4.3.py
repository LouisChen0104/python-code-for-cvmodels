import numpy as np
import math
import matplotlib.pyplot as plt

pi = 3.1415926
I = [5, 100]
original_mu = 5
original_sig = 8
alpha = 1
beta = 1
gamma = 1
delta = 0
count = 1
for i in I:
    data = original_mu + original_sig * np.random.randn(i)
    estimated_mu_map = (np.sum(data) + gamma * delta) / (i + gamma)
    estimated_var_map = (np.sum(np.square(data - estimated_mu_map)) + 2 * beta + gamma *
                         np.square(delta - estimated_mu_map)) / (i + 3 + 2 * alpha)
    estimated_sig_map = np.sqrt(estimated_var_map)
    alpha_post = alpha + i / 2
    gamma_post = gamma + i
    delta_post = (np.sum(data) + gamma * delta) / (gamma + i)
    beta_post = np.sum(np.square(data)) / 2 + beta + gamma * delta * delta / 2 -\
                np.square(gamma * delta + np.sum(data)) / (2 * (gamma + i))
    x = np.linspace(-20, 30, 1000)
    y_03 = []
    for xi in x:
        alpha_int = alpha_post + 0.5
        gamma_int = gamma_post + 1
        beta_int = xi * xi / 2 + beta_post + gamma_post * delta_post * delta_post / 2 - \
                   np.square(gamma_post * delta_post + xi) / (2 * (gamma_post + 1))
        xi_prediction = np.sqrt(gamma_post) * math.pow(beta_post, alpha_post) * math.gamma(alpha_int) / \
                        (np.sqrt(2 * pi) * np.sqrt(gamma_int) * math.pow(beta_int, alpha_int) * math.gamma(alpha_post))
        y_03.append(xi_prediction)

    plt.subplot(2, 2, count).set_title('%d data points' % i)
    y_01 = np.exp(- np.square(x - original_mu) / (2 * np.square(original_sig))) / (np.sqrt(2 * pi) * original_sig)
    y_02 = np.exp(- np.square(x - estimated_mu_map) / (2 * np.square(estimated_sig_map))) / \
           (np.sqrt(2 * pi) * estimated_sig_map)
    plt.plot(x, y_01, "g-", label='original', linewidth=2)
    plt.plot(x, y_02, "b-", label='MAP', linewidth=2)
    plt.plot(x, y_03, "r-", label='Bayesian', linewidth=2)
    if (count == 1):
        plt.ylabel('P(x)')
    plt.legend()
    plt.subplot(2, 2, count+2).set_title('%d data points' % i)
    y_04 = []
    y_05 = []
    y_06 = []
    for yi in y_01:
        yi_log = math.log(yi)
        y_04.append(yi_log)
    for yi in y_02:
        yi_log = math.log(yi)
        y_05.append(yi_log)
    for yi in y_03:
        yi_log = math.log(yi)
        y_06.append(yi_log)
    plt.plot(x, y_04, "g-", label='original', linewidth=2)
    plt.plot(x, y_05, "b-", label='MAP', linewidth=2)
    plt.plot(x, y_06, "r-", label='Bayesian', linewidth=2)
    if(count == 1):
        plt.ylabel('log(P(x))')
        plt.xlabel('x')
    if (count == 2):
        plt.xlabel('x')
    plt.legend()
    count += 1

plt.suptitle('Algorithm 4.3')
plt.savefig('Algorithm 4.3.png')
plt.show()