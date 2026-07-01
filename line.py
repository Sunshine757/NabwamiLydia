#matplotloib Pyplot is a module that is found within matplotlib that provides a MATLAB formaking plots
#steps to use Pyplot
#1 - import Matplotlib e.g import matplotlib.pyplot as plt
#2- create data 
#3- plot data using plt.plot()
#4- customize plot. Add titles labes
#5- display the plot we use plt.show()

#basic line graph
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

fig, ax = plt.subplots()
ax.plot (x, y, marker = 'o', label  = "Data Points")

ax.set_title("Basic Line graph")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")

ax.legend()
plt.show()
