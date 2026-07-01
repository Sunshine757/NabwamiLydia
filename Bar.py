#Bar charts categorical data using rectangular bars whose lengths are proportional to the values they represent


#simple Bar chart
import matplotlib.pyplot as plt

w = ['John', 'Mary', 'Peter', 'Jane']
z = [10,14,7,12]

plt.bar(w,z)
plt.title('Simple Bar graph')
plt.xlabel('Names of students')
plt.ylabel('Ages of students')

plt.show()