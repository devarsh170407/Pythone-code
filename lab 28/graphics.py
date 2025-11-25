from plotnine import *
from plotnine.data import mtcars

p = (
    ggplot(mtcars)
    + geom_point(aes("wt", "mpg", color="factor(gear)"))
    + facet_wrap("~gear")
    + labs(
        title="MPG vs Weight by Gear",
        x="Weight (1000 lbs)",
        y="Miles per Gallon",
        color="Gears"
    )
)

p.save("ggplot.png", width=6, height=4, dpi=100)

