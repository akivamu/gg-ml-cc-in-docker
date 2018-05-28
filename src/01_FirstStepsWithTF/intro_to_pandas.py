import pandas as pd
import matplotlib.pyplot as plt

print "Panda version: " + pd.__version__

print "\n---- 1. Load Series and DataFrame from CSV file ----"
# Load data from csv
california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")

# Display some rows
print "Display some first rows..."
print california_housing_dataframe.head()

# And histogram
print "Display histogram from column housing_median_age"
california_housing_dataframe.hist('housing_median_age')
# Uncomment line below to show plot
#plt.show()

print "\n---- 2. Manually create Series and DataFrame ----"
# Create some Series (column data)
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

# Create DataFrame with above data
cities = pd.DataFrame({ 'City name': city_names, 'Population': population })

print cities.describe()

print "\n---- 3. Accessing data ----"
# Type of column
print "Type of column 'City name':", type(cities['City name'])
print "Value of column 'City name':"
print cities['City name']

# Type of item in column
print "\n"
print "Type of element in column 'City name':", type(cities['City name'][1])
print "Value of 1 element in column 'City name':", cities['City name'][1]

print "\n---- 4. Manipulating data ----"
print "Origin population column"
print population

print "\nDivide population column by 1000"
modified_population = population / 1000
print modified_population

print "\nModify DataFrame"
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
print cities

# Exercise #1
print "\n---- 5. Exercise #1 ----"
cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print cities

# Indexes of columns and rows
print "\n---- 6. Indexes ----"
print "Index of column 'City name': ", city_names.index
print "Index of DataFrame cities: ",cities.index

print "\nReindex: keep index, just change order"
print cities.reindex([2, 0, 1])

print "\nReindex with non-exist indexes"
print cities.reindex([0, 4, 5, 2])
