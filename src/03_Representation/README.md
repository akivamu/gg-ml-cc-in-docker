# Representation

Machine Learning includes 25% coding effort & 75% data engineering effort.

## Raw data to feature data

Map numberic values  
Map categorical values (one-hot encoding)  

## Qualities of Good Features

Avoid rarely used discrete feature values.  
Prefer clear and obvious meanings.  
Don't mix "magic" values with actual data.  
Account for upstream instability.  

## Cleaning Data

Scaling feature values  
Handling extreme outliers  
Binning  
Scrubbing  

## Feature Sets programming exercise

### Task 1: select features

To identify good features to use, we can use correlation matrix. List all correlations between features and targets by `correlation_dataframe.corr()`.

Select features that have non-zero correlation to targets: `'latitude', 'housing_median_age', 'total_rooms','households','median_income','rooms_per_person'`

Because `median_income` has strongest correlation to targets, we choose it first.  
In this task, we can only choose 2 features, so let check among those features, and find the pair that least correlated to each other. Means choose feature that least correlated to `median_income`, here is the list:

- latitude: -0.1
- housing_median_age: -0.1
- total_rooms: 0.2
- households: 0.0
- rooms_per_person: 0.2

We can easily pick `households` for the least correlated with `median_income`.  
But the correct solution is `latitude`, and I don't know why yet???

Just take `median_income` and `latitude` as our features for now. With these parameters:  
learning_rate=0.01, steps=500, batch_size=5  
We can get RMSE = 113.40

### Task 2: Make Better Use of Latitude

In this task, we transform `latitude` feature into multiple features `latitude_32_to_33`, `latitude_33_to_34`...  
Each of those features has value 1 or 0, depends on if the example belongs to the latitude or not.

So after transformation, we have these features: `median_income`, `latitude_32_to_33`, `latitude_33_to_34`...  
Feed them to model, we got RMSE = 139.57
