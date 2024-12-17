import matplotlib.pyplot as plt # type: ignore

x = []
y = []

# create x values
for n in range(-100,101):
   x = x + [n]

# Create y values based on the function f(x) = x^2 - 3
y = [n**2 - 3 for n in x]

print(x)

# Print chart
plt.plot(x, y, label='f(x) = x^2 - 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = x^2 - 3')
plt.legend()
plt.grid(True)
plt.show()
