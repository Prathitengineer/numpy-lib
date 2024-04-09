from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
sns.set_style('darkgrid')
fre = 10
pi = 22/7
fre_samp = 100
t = np.linspace(0, 2, 2 * fre_samp, endpoint=False)
a = np.sin(fre * 2 * pi * t)
plt.plot(t, a)
plt.xlabel('time(s)')
plt.ylabel('signal ampitude')
plt.show()