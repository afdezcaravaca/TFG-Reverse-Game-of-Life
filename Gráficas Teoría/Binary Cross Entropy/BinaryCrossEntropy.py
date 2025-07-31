import numpy as np
import matplotlib.pyplot as plt
import os

x = np.arange(0,1, 0.001)
y1 = -np.log(x)
y2= - np.log(1-x)

fig = plt.figure()

plt.plot(x,y1, color='blue', label=r'True (y = 1')
plt.plot(x,y2, color='red', label=r'True (y = 0)')

plt.title('Binary Cross Entropy \n Loss Function', fontsize=16)
plt.ylabel(r'L($\hat{y}$, y)', fontsize=14)
plt.xlabel(r'$\hat{y}$', fontsize=14)

plt.legend(loc='best', fontsize=13)
plt.grid(linestyle=':')
plt.ylim([0,7])
plt.xlim([0,1])

# path = os.path.join(os.getcwd(),'Modelos', 'Modelo V1', 'Binary.png')
# fig.savefig(path)

plt.show()