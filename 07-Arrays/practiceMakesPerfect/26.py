import matplotlib.pyplot as plt # type: ignore
import math

# array of x values - angles in degrees
x = list(range(0, 361))

# Calculate y values using sin
y = [math.sin(math.radians(angle)) for angle in x]

# Plot the function y = sin(x)
plt.plot(x, y, label='y = sin(x)')
plt.xlabel('x (degrees)')
plt.ylabel('y')
plt.title('y = sin(x) for x in 0 to 360 degrees')
plt.legend()
plt.grid(True)
plt.show()
