import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Sales': [100, 200, 150, 300, 250],
    'Profit': [30, 70, 50, 120, 90]
})

fig = px.bar(df, x='Product', y='Sales',
             title='Sales by Product',
             color='Profit',
             text='Sales')

fig.update_layout(xaxis_title='Product',
                  yaxis_title='Sales',
                  legend_title='Profit',
                  template='plotly_dark')

fig.show()
fig.write_html('sales_by_product.html')
fig.write_image('sales_by_product.png')

# Save the figure as an HTML file
fig.write_html('sales_by_product.html')

# Save the figure as a PNG file (you may need to install kaleido)
fig.write_image('sales_by_product.png')