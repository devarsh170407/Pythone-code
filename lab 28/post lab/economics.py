from plotnine.data import economics
from plotnine import ggplot, aes, geom_line

p = (
    ggplot(economics)               # dataset
    + aes(x="date", y="pop")        
    + geom_line()                   
)

p.save("economics.png", width=6, height=4, dpi=100)

