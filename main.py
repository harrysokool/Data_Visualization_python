import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(squares)
plt.show()
