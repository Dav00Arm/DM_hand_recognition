We have started by training the model in English letter signs 

the dataset for training was 
we have not considered augmenting the dataset at this point because the dataset was not bad

first 
we have converted the dataset into an "understandable for the model" format because there was an already ready training code for this 
the model was also edited because it was too small
we have made it a bit bigger with different logic, just to help it learn all the gestures 
but because the meaning of the program is to teach a sign we need our detection to be as precise as possible and that's when 
confidence score will come in handy 
currently, we are adding a confidence score calculation section, and because we are getting a probability distribution as an output from our model, with 27 classes one of them none, we are going to play with it
 
 As a good practice, we are going to use the validation set to understand which confidence threshold will provide the best information 
 quality 

 Calculating Confidence Score
Output Type:

Our model's output is a probability distribution over the 27 classes (softmax activation).
Confidence Score:

The confidence score for a prediction is the probability assigned to the predicted class.
After obtaining the output probabilities, the confidence score is the maximum value among them.
Setting a Threshold
Evaluate Model Performance:

Evaluate our model on a validation set to obtain the confidence scores for correct and incorrect predictions.
Analyze Confidence Distribution:

Plot the distribution of confidence scores for correct and incorrect predictions.
This helps to understand where to set the threshold.
Set Threshold:

Choose a threshold that balances precision and recall based on our application needs. A common approach is to use the point where the distributions of correct and incorrect predictions overlap the least.
Next Steps
Evaluate Model:
 what metrics did we obtain?
Plot Confidence Distribution:

Can we plot the distribution of confidence scores for correct and incorrect predictions? This will help in setting an appropriate threshold.
