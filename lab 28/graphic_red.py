from plotnine import *
from plotnine.data import mtcars

p = (
    ggplot(mtcars)
    + geom_point(aes("wt", "mpg"), color='red')
    + labs(
    )
)

p.save("graphics_red.png", width=6, height=4, dpi=100)
