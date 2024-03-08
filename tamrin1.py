
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 2*np.pi, 1000)


y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')


plt.fill_between(x, y1, y2, where=(y1 >= y2), color='gray', alpha=0.5, hatch='x')


plt.title('cos(x) & sin(x) Diagram')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()



