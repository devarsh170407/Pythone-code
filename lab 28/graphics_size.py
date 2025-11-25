from plotnine import *
from plotnine.data import mtcars

p = (
    ggplot(mtcars)
    + geom_point(aes("wt", "mpg", size="factor(gear)"))
    + labs(
        title="MPG vs Weight using Point Size by Gear",
        x="Weight (1000 lbs)",
        y="Miles per Gallon",
        size="Gears"
    )
)

p.save("graphics_size.png", width=6, height=4, dpi=100)

