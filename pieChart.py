
import matplotlib.pyplot as plt

w = ['John', 'Mary', 'Peter', 'Jane']
z = [10,20,23,15]

plt.pie(z, labels=w, autopct='%1.1f%%')
plt.title('Simple Pie Chart')
plt.show()