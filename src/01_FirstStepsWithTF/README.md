# Core concepts

**Feature, Label, Example, Prediction**  

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

# How to train model

Assume this is single feature model, single weight `w1`.

First, initialize model weight `w1 = 0` or any value.

Iterate throw N steps, at each step:  
  - Choose a batch of data, consists of 1 or more examples.  
  - With current model, calculate loss.  
  - Use Gradient Descent to find more optimal weight `w1`.  
  - Update model with new `w1`.  
  - Repeat next step.  

**Questions**

  - Why multiple steps? Why not single step with big batch?
  - Is learning_rate related to steps?
  - Why choose batch with 1 example?
