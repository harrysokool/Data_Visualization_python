from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die1 = Die()
die2 = Die(10)

results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

freq = []
max = die1.num_sides + die2.num_sides
for value in range(2, max + 1):
    f = results.count(value)
    freq.append(f)

# make histogram for analysing the result
x_value = [i for i in range(2, max + 1)]
data = [Bar(x = x_value, y = freq)]
x_label = {'title':'Result', 'dtick': 1}
y_label = {'title':'Frequency of result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 times', xaxis=x_label, yaxis=y_label)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')