from plotnine import *
from plotnine.data import mtcars
import matplotlib.pyplot as plt 
p=(

(ggplot(data=mtcars)
 + geom_point(mapping=aes(x="wt", y="mpg", color="factor(gear)"))
 + facet_wrap("~gear"))
)

print(p)
plt.show() 