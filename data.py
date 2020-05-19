#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
income = np.random.normal(27000,15000,1000)
income = np.append(income, [1000000000])
avg = np.mean(income)
print(avg)
plt.hist(income, 50)
plt.show()
med = np.median(income)
print(med)