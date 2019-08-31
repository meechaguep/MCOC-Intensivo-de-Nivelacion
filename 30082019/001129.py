#nivelacion final

from matplotlib import pyplot as plt
import numpy as np
from random import randint, uniform,random

numuniform=np.arange(280,300)
numirregs= [288,280,275,265,222,625,455,225,299,300,335,478,874,445,221,336,223,113,231,114]
numirregs2=[288,280,275,745,222,627,455,225,365,300,335,478,100,445,221,454,223,113,231,114]


plt.plot(numuniform,numirregs,label="des1")
plt.plot(numuniform,numirregs2,label="des2")
plt.title("num uniform x num lokos")
plt.ylabel("sueldoirregular")
plt.xlabel("sueldolineal")
plt.legend()
plt.grid(True) 
plt.tight_layout()
plt.savefig('desigualdad.png',)



plt.show()
