import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from RandomWalk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()
point_numbers = range(rw.num_points)
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15, 9))
ax.scatter(rw.x_values, rw.y_values, c = point_numbers,cmap=plt.cm.Blues,edgecolors='none',  s = 1)
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.savefig('RandomWalk.png')