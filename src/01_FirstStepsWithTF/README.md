# First steps

## Core concepts

- Feature
- Label
- Example
- Prediction

**Linear Regression**  
Predict model is represented by linear function `y' = w0 + w1*x`  
`w1` is weight of feature 1.  

**Loss (or Cost) function**  
When training a model, loss function represents the difference between Predicted
vs Actual value, based on the same input in example data set.  
Loss function is a function with variables `weight` of features, e.g. `w1`, `w2`  

To optimize model, we need minimize loss. So we need to solve loss function for those variables `weight` so that the loss is minimum.  

**Mean Squared Error**  
A popular loss function, is the average squared loss per example over the whole dataset.

**Gradient Descent**
A iterative method to find optimal `weight` so that loss is minimized.  

## How to train model

Assume this is single feature model, single weight `w1`.

First, initialize model weight `w1 = 0` or any value.

Iterate throw N steps, at each step:

- Choose a batch of data, consists of 1 or more examples.  
- With current model, calculate loss.  
- Use Gradient Descent to find more optimal weight `w1`.  
- Update model with new `w1`.  
- Repeat next step.  

### Questions

Q: Why multiple steps? Why not single step with big batch?  
A: With single step, the updated weight may be not good enough (not converged), because we update model base on the learning rate. The point is we continuosly update model until the model converged.  
About batch size, we can use whole dataset as a batch (traditional way) or split it up (Stochastic or mini-batch way). It deals with very big dataset - computation expensiveness.

Q: Why choose batch with 1 example?  
A: That is Stochastic Gradient Descent way. If you choose multiple examples by updating step, it becomes mini-batch way.

## Intro to pandas

`pandas` is python API for data analysis. Main data structures:

- DataFrame: just like table, but in column-oriented  
- Series: is a single column  

You can imagine those are just like table and row in relational database, but in column-oriented instead of rows.

For example code, see `intro_to_pandas.py`

## First steps with TensorFlow

In this exercise, we will build a model to predict **median house value**, using the California's housing data.

The technique here is running Linear Regression with Gradient Descent as optimizer.

First, we start with using only 1 single feature as input: `total_rooms`. And the output is `median_house_value`.  
Our model will use `total_rooms` and `median_house_value` as training set `(x,y)`.

Looking at the code, there is a complicated in `my_input_fn`. At this time, just consider it as an transformer original data into the structure that TF can use - from `pandas` to TensorFlow `Dataset`.  
The parameters `features`, `targets`, `batch_size` are easy to understand. But what about `num_epochs`.

While training, we need data to be fetched into optimizer continuosly. What if all examples in training data is used?  
We repeat them, by instruct `Dataset` to repeat data `num_epochs` of times.  
Specifically, when training, we need the `Dataset` repeats infinitely.
When making prediction, we need the `Dataset` repeats just once.

The important steps here are:

- `linear_regressor.train`: which trains the model by using our dataset `total_rooms` and `median_house_value`  
- `linear_regressor.predict`: which predicts the output according to the input `total_rooms`  
- `metrics.mean_squared_error`: calculate the error between predicts and real value `median_house_value`  

Then, we can examine the error, the parameters of our model after training `weight` and `bias`.  
We can plot the regression line to see that our model performs very bad.

Time to improve our model!

### Tweaking the model

We refactor the training process into a function `train_model`, so we can easily try various configurations:

- Learning rate  
- Steps  
- Batch size  

To recall, in the original code, our configuration is:  

- Learning rate: 0.0000001  
- Steps: 100  
- Batch size: 1  

You can see the learning rate is too low. And with batch size is 1 and steps is 100, we just use 100 examples in training dataset.

We need to try various combinations to find best result.

What we do in `train_model` function:

Basically the same as before, but breaking all steps into 10 periods.  
After each period done, we evaluate the current model, calculating the error and plot.

A good configuration:

- Learning rate: 0.00002  
- Steps: 500  
- Batch size: 5  

See the plot, you can see after each period, the straight line (represents our model) become better. And the errors are also reduced after each period.

## Synthetic features

Recall our last code, we use `total_rooms` as a single feature for training process. We can use other features too, such as `population`.  
But we can also create new feature base on original feature and use it in training process. We call it synthetic feature.

In this exercise, we create new feature: `rooms_per_person` by the formula: `rooms_per_person = total_rooms / population`

Train the model, then plot it.  

Now plot the comparation between predictions and real labels:  
`plt.scatter(calibration_data["predictions"], calibration_data["targets"])`  
If our model works perfectly, we should see a perfect diagonal line, means `x = y` line.  
But it isn't here, because of some outliers.

Now we remove all outliers in input by taking only `rooms_per_person` minimum at 5: `min(x, 5)`  
Again train model with new processed input, and plot.