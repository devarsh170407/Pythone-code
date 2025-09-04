import pandas as pd
# print(pd.__version__)

# l1=[1,2,3,43]
# data=pd.Series(l1)#series means print number with its index but in list it print without index
# print(data)
# print(data+10)# it add 10 in all data
# print(data.loc[[0]])

# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# print(series)

# Series2 = series + 10
# print(Series2)
# # Filtering
# filtered_series = series[series > 2]
# print(filtered_series)
# # Statistical Calculations
# mean_value = series.mean()
# print(mean_value)


# data={"name":['shivam','divy','mit'],"city":['rajkot','upleta','kenya']}
# data1=pd.DataFrame(data)
# print(data1)


# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# }
# df = pd.DataFrame(data)
# # print(df)
# # print(df[['Name']])

# df['Salary'] = [70000, 80000, 90000]
# print(df)


# # s1=pd.read_csv("data.csv")
# df = df.drop('City', axis=1)
# print(df)

# print(df.loc[[0]])
# print(df.loc[[0, 1]])

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# print(df)

# dat = pd.read_csv("data.csv")
# print(dat)

# Biodata = {'Name': ['John', 'Emily', 'Mike', 'Lisa'],
#         'Age': [28, 23, 35, 31],
#         'Gender': ['M', 'F', 'M', 'F']
#         }
# df = pd.DataFrame(Biodata)
# # Save the dataframe to a CSV file
# print(df.to_csv('Biodata.csv', index=False))
# print(df)

# dat = pd.read_csv("data.csv")
# # print(dat.info())
# # # shows first and last five rows
# # print(dat.head())
# # print(dat.tail())
# # print(dat.describe())
# print(dat[['Name']])
# print(dat[['Name','Number']])
# print(dat.loc[[1]])
# import numpy as np
# data = {
#     'A': [np.nan, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     'B': np.random.normal(50, 15, 10),
#     'C': np.random.rand(10) * 100,
#     'D': np.linspace(1, 10, 10),
#     'E': np.logspace(1, 2, 10)
# }
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# data=[5,6,7,8,9]
# series2 = pd.Series(data)
# # addition
# print(series+series2)
# #subtraction
# print(series-series2)
# #multiplication
# print(series*series2)
# #divide
# print(series2/series)


# import pandas as pd
# import numpy as np
# data= [10, 20, 30, 40]
# da= np.array([50, 60, 70, 80])
# dd = {
#     'a': 10,
#     'b': 20,
#     'c': 30,
#     'd': 40
# }
# sl = pd.Series(data)
# print(sl)
# sa=pd.Series(da)
# print(sa)
# series = pd.Series(dd)
# print(series)

import pandas as pd
s1 = pd.Series([10, 20, 30], name='Series1')
s2 = pd.Series([40, 50, 60], name='Series2')

vertical = pd.concat([s1,s2], axis=0)

print("vertical Stack:")
print(vertical)

horizontal= pd.concat([s1,s2], axis=1)
print("horizontal stack")
print(horizontal)
