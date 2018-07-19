# Validation

After trying many configurations (learning rate, batch size), we finally got our best model, which has very good predictions, very low error compared to our data labels.

Now we collect more data, and test if our model can still predict best with new data.  
Turns out our model works not so well.

It's because of our model was tweaked so much on original dataset. When new data come in, which different from original dataset, our model failed to work. It's called overfitting (to original dataset).

To prevent it, we split original dataset into 3 parts:

- Training set
- Validation set
- Test set

First we train model based on data Training set, make it best fit to that set.  
Second, we use model to make predictions on Validation set. We will see our model won't work well anymore. Now make changes in model's configuration, until it best fits to both Training set and Validation set.  
Finally, use our latest model to make predictions on Test set. Now we can evaluate if our model is good or bad.

## Programing exercise

This exercise is based on the last exercise: predicting house value in California.

And we apply the theory of validation to it.

### Task 1 & 2 & 3

First, splitting data set into Training set (12000 examples) and Validation set (5000 examples).
Remember to shuffling whole dataset before hand. So that when we plot those sets, they seems similar.

### Task 4: train the model

Now, we modify the `train_model` function.  
At each period, we still update model, make prediction on Training set and calculate the error.  
In additional, at each period, we also make prediction based on Validation set, to see the error in the Validation set if we use the mode.  

Tweaking configurations until you can get both RMSE under 180.

### Task 5: use Test set to evaluate our model
