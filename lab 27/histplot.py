import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white")
# Generate a random univariate dataset
rs = np.random.RandomState(10)
d = rs.normal(size=100)
# Plot a simple histogram and kde
fig, ax = plt.subplots()
sns.histplot(d, kde=True, color="m", ax=ax)

# Save a copy of the plot (works in headless environments)
out_file = 'histplot.png'
fig.savefig(out_file, bbox_inches='tight')
print(f'Plot saved to {out_file}')

# Try to show the plot window (may not open on headless systems)
try:
	plt.show()
except Exception as e:
	print('plt.show() did not open a window:', e)
