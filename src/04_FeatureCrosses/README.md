# Feature Crosses

`Cross` means you make new features by using cross product of exist features.  
Add cross producted new features will make our model **non-linear**.  
Why?

Suppose we have model with 2 features x1 and x2: `y = b + w1*x1 + w2*x2`  
This model is linear.

Now add new features `x3 = x1 * x2`: `y = b + w1*x1 + w2*x2 + w3*x1*x2`  
The model become non-linear.  

Now try new features `x3 = x1^2`: `y = b + w1*x1 + w2*x2 + w3*(x1^2)`  
It's obviously non-linear.  

## Crossing One-hot vectors

For example these 2 features:

```python
binned_latitude(lat) = [
  0  < lat <= 10
  10 < lat <= 20
  20 < lat <= 30
]

binned_longitude(lon) = [
  0  < lon <= 15
  15 < lon <= 30
]
```

Crossing:

```python
binned_latitude_X_longitude(lat, lon) = [
  0  < lat <= 10 AND 0  < lon <= 15
  0  < lat <= 10 AND 15 < lon <= 30
  10 < lat <= 20 AND 0  < lon <= 15
  10 < lat <= 20 AND 15 < lon <= 30
  20 < lat <= 30 AND 0  < lon <= 15
  20 < lat <= 30 AND 15 < lon <= 30
]
```

## Programming exercise

This time, we feed all features to optimizer, and the training time should be longer.

Run `feature_crosses_multifeatures.py` to know how could we improved if using all features.  
The final RMSE = 176. Worse than previous exercises.

### FtrlOptimizer

Now, we will get rid of `GradientDescentOptimizer`, and use new optimizer instead: `FtrlOptimizer`

Run `feature_crosses_ftrl.py` to know how good new optimizer works.  
The final RMSE = 106.77. Better than last exercise

### Bucketizing

We also transform `numeric_column` features into `bucketized_column` features, using **quantile-based** technique.  
Quantile-based technique is used for choosing bucket's range.  
By that, all buckets have the same number of examples.

Run `feature_crosses_bucketized.py` to train model with bucketized features, we got RMSE = 88.87

So, bucketizing improved our result. But why?

### Feature cross

Now, we create cross feature of longitude and latitude. It used TF data structure `crossed_column`.

Why should I create cross feature of long and lat?  
In reality, long and lat separately couldn't tell much. But the combination of long and lat give us exact location on map, which is easier to imagine.

Run `feature_crosses.py` to train model with new cross feature, we got RMSE = 79.57

Feature crossing did improved the model.