import pandas as pd

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])
abbr = pd.Series(['SF', 'SJ', 'SA'])

dataFrame = pd.DataFrame({
     'City name': city_names, 
     'Population': population,
     'Abbr':abbr })


print ("- Single bracket to refer to a Series in DataFrame: print type(dataFrame['City name'])")
print type(dataFrame['City name'])

print ("- Double bracket to get a new DataFrame, collect Series listed in inner bracket")
print ("print type(dataFrame[['City name', 'Abbr']])")
print type(dataFrame[['City name', 'Abbr']])

newDataFrame = dataFrame[['City name', 'Abbr']]
print newDataFrame