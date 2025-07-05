import numpy as np
import matplotlib.pyplot as plt
import os


x = np.arange(0.001,0.999,0.001)

fig2, ax2 = plt.subplots(3,3, figsize=(8,8))
ax2 = ax2.flatten()
fig2.suptitle('Focal Binary Cross-Entropy', y= 0.95, fontsize=16)
fig2.supxlabel(r'$\hat{y}$', y = 0.047, fontsize=14)
fig2.supylabel(r'L($\hat{y}$,y)', x = 0.07, fontsize=14)


alphas = [0.25, 0.5, 0.75]
gammas = [0, 1, 6]
j = 0

for a in alphas:
    for g in gammas:
        y1 = -a*(1-x)**(g)*np.log(x)
        y2 = -(1-a)*x**(g)*np.log(1-x)

        ax2[j].plot(x,y1, color='blue', label='True (y = 1)')
        ax2[j].plot(x,y2, color='red', label='False (y = 0)')
        ax2[j].set_title(r'$\alpha = $' f'{a}' r' $\gamma = $'f'{g}', fontsize=14) 
        ax2[j].grid(linestyle=':')

        if j == 0:
            ax2[0].legend(loc='best', fontsize=11.5)

        if j in [0,1,2,3,4,5]:
            ax2[j].tick_params(labelbottom=False)

        
        if j in [1,2,4,5,7,8]:
            ax2[j].tick_params(labelleft=False)
            
        j += 1        

# fig2.savefig(os.path.join(os.getcwd(),'Modelos','Modelo V2', 'Binary Focal', 'BinaryFocal.png'))
    
plt.show()       
