from plotnine.data import mpg
from plotnine import ggplot, aes, geom_point

p = (
    ggplot(mpg)
    + aes(x="class", y="hwy")
    + geom_point()
)

# Save the plot as an image
p.save("mpg.png", width=6, height=4, dpi=100)

