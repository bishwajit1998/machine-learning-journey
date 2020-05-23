import numpy as np
from pylab import *
from scipy import stats
import matplotlib.pyplot as plt


#linear regression
pageSpeeds = np.random.normal(3.0, 100.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

scatter(pageSpeeds, purchaseAmount)


slope, intercept, r_value, p_value, std_err = stats.linregress(pageSpeeds, purchaseAmount)
#r_value **2 

def predict(x):
	return slope*x + intercept

fitLine=predict(pageSpeeds)
plt.scatter(pageSpeeds,purchaseAmount)
plt.plot(pageSpeeds,fitLine,c='r')
plt.show()

#polynomial regression
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

scatter(pageSpeeds, purchaseAmount)

x = np.array(pageSpeeds)
y = np.array(purchaseAmount)

p4 = np.polyld(np.polyfit(x, y, 4))
xp = np.linspace(0, 7, 100)
plt.scatter(x, y)
plt.plot(xp, p4(xp), c='r')

plt.show()