# Classification

We're done with one type of ML: Regression (which predicts continuous output values).

Now it's time for: Classification (used to predicts discrete output values, like `spam` and `not spam`).

## Modeling

For convenience, we use Sigmoid function to represent our model, because this function outputs values in range [0,1].  
Think of it as probability of the output to be.

Our problem can be interpretted as:

- Value >= 0.5 (means probability >= 50%) : spam
- Value <  0.5 (means probability <  50%) : not spam

## Threshold

In a binary classification problem (either `YES` or `NO`), we can choose the threshold to be 0.5.  
But it really depends on the nature of the problem.

An example: spam filter.  
Falsely classify an email as spam can be very dangerous, we need to be very sure about that.  
So we raise the threshold to 0.9, means that we mark as spam only if 90% sure.

## TP, FP, TN and FN

Assume we are in the classification problem which detect `spam` and `not spam`. Assume `spam` is rare, about 10% of examples.  
So here are the terms:

- Positive: spam
- Negative: not spam
- True Positive: correct prediction as spam
- False Positive: incorrect prediction as spam
- True Negative: correct prediction as non spam
- False Negative: incorrect prediction as non spam

We can derive from those:

- Total number of real positives: True Positives + False Negatives
- Total number of real negatives: True Negatives + False Positives

## Accuracy

Accuracy is simple: `number of correct predictions / total number of predictions`  
And it could went very wrong.

Assume our dataset has 100 emails, 90 of those are not spam.  
We make a stupid model, which predicts all emails as `not spam`.  
So for 100 emails, we got 90 emails that are correctly predicted (as not spam).  
And the accuracy is 90%, which give use very wrong evaluation about the model.

## Precision - Recall

Precision: how many predicted positives are real positive.  
Recall: how many real positives are predicted.

Explain in spam detectors:  
Precision: how many detected spams are real spam.  
Recall: how many real spams are detected.

