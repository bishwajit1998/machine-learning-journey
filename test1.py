#%matplotlib inline
import pandas as pd
import seaborn as sns
sns.set()

#
df = pd.read_csv("http://media.sundog-soft.com/SelfDriving/FuelEfficiency.csv")
gear_counts = df['# Gears'].value_counts()
gear_counts.plot(kind='bar')
