# Regularization

When we do tuning too much, increase the degree of hypothesis function, our model becomes overfitting, and more complex.  
If we visualize the model, we can see a complicated curve that fits every points in the training set, or with very small error.

It's bad when predicting new input, that curve may not fit or close to the new points.  
We don't want the model that has small error on training set, but high error on new input.  
It's best if both errors are close.

That why we apply Regularization.

Regularization is a method to reduce the fitting level of our model, by reduce the effect of some **weights**, i.e. decreasing their values.

## How we do regularization

Q: Can we just scale down all the weights?  
A: Not all weights contribute to overfitting. We have to select the right ones to reduce.

Q: Can we just remove high order weights?  
A: You can, if you understand the model so well. But it seems like a manual job, why don't we use a general method?

## General formula

Let's recall, our objective is minimize the cost function `J(theta)`, which is a function of weights `theta`.  
Using Gradient Descent or anything, we can find its minimal point `Jmin`, and the corresponding `theta` at that minimal point.

Now add a new regularization term to cost function, it becomes: `J(theta) + R(theta)`.  
The objective is still the same: minimizing that function.  
But now we do 2 things at the same time:

- Minimizing Cost
- Minimizing the size of weights

That's why we should put regularization term to Cost function.

Q: Why addition, not multiplication?  
A: ![Explained here](https://stats.stackexchange.com/questions/347530/why-is-the-regularization-term-added-to-the-cost-function-instead-of-multipli)

## Regularization methods

### L1 Regularization - Lasso Regression

Penalize absolute value of weights - force them to zero

### L2 Regularization - Ridge Regression

Penalize squared value of weights - force them to small

![Read this to know why](https://towardsdatascience.com/regularization-in-machine-learning-76441ddcf99a)

## Programming exercise (Sparsity)

In this exercise, we add L1 regularization into optimizer.  
It's quite simple, just use the API:

`my_optimizer = tf.train.FtrlOptimizer(learning_rate=learning_rate, l1_regularization_strength=regularization_strength)`

Think `l1_regularization_strength` as lambda.