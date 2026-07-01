# histogram
import matplotlib.pyplot as plt

scores = [12, 15, 18, 18, 21, 22, 22, 25, 27, 30, 31, 31, 34, 36, 38, 40]

plt.hist(scores, bins=5, edgecolor='black')
plt.title('Simple Histogram')
plt.xlabel('Score')
plt.ylabel('Frequency')
plt.show()



