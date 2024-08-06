import matplotlib.pyplot as plt

"""Line Plots"""
"""
x_points = [1,2,3,4,5,6]
y_points = [1,4,9,16,25,36]
x2_points = [-3,-2,-1,0,1,2,3,4,5,6]
y2_points = [-27,-8,-1,0,1,8,27,64,125,216]

plt.plot(x_points, y_points, '#000000', label='Squares')
plt.plot(x2_points, y2_points, 'r', label='Cubes')

plt.title("Squares and Cubes")
plt.xlabel("x")
plt.ylabel("f(x)")

# MPL will by default zoom to where all data can be seen. You can manually adjust this to show only what you want.
plt.xlim(0, 6)

plt.legend()
plt.show()
"""

"""Histograms"""

labels = ["M","T","W","Th","F","Sa","Su"]
values = [3,8,7,9,15,22,14]

plt.bar(labels, values)

plt.show()
