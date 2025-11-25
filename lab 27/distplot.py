import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

# dataset
data = np.random.randn(200)

sns.distplot(data, kde=True, hist=True, rug=False)
plt.show()

