import numpy as np
import matplotlib.pyplot as plt

pi = 3.1415926
I = 100
original_mu = 5
original_sig = 8
data = original_mu + original_sig * np.random.randn(I)

estimated_mu = np.sum(data) / I
estimated_var = 0
for data_i in data:
    estimated_var += np.square(data_i - estimated_mu) / I
estimated_sig = np.sqrt(estimated_var)

muError = abs(original_mu - estimated_mu)
sigError = abs(original_sig - estimated_sig)

x_01 = np.linspace(-20, 30, 100)
x_02 = np.linspace(-20, 30, 100)
y_01 = np.exp(- np.square(x_01 - original_mu) / (2 * np.square(original_sig)))/(np.sqrt(2*pi)*original_sig)
y_02 = np.exp(- np.square(x_01 - estimated_mu) / (2 * np.square(estimated_sig)))/(np.sqrt(2*pi)*estimated_sig)
plt.plot(x_01, y_01, "g-", label='original', linewidth=2)
plt.plot(x_02, y_02, "b-", label='estimate', linewidth=2)
plt.title('Algorithm 4.1')
plt.legend()
plt.savefig('Algorithm 4.1.png')
plt.show()
