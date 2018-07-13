# ARTificial Intelligence
## Overview
Throughout an artist's lifetime, changes in method, subject matter, and even style are to be expected. This is certainly true for the artists we've selected for this project - Marko Rothko and Morris Louis. Inspired by their paintings, the goal of this application is to identify the time period of each artist's paintings using machine learning techniques. The initial intention was to use a neural network to predict the year painted for each painter's works, but this was not the best model due to a need for a larger dataset. We explored various models like Linear Regression, clustering models like K Means, and classification models like Decision Tree and Random Forest. We found that predicting a year timeframe using the Decision Tree Model yielded the best results.

## Team Members
* Luke Pharr
* Rupali Mayekar
* Andrea Karaffa
* David Richter
* Jen Vacanti

## How does the Application Work?
The website is powered by a Python Flask Application. Machine learning models were explored in Jupyter Notebook using Python's scikit-learn library to extract specific metrics from each artist's paintings and then test the correlation of these metrics with the year of the painting. These models were saved and reused by the Test Gallery via FLask. The Test Gallery has images from different time periods of each artist's career. These are not a part of the dataset that the models were trained on. On clicking the Classify button, the metrics for the selected image are calculated, corresponding models are loaded and used to predict the time period for the selected image. 

Tools used are:
* Python Flask App
* Python SciKit Library: some of the API's utilized were skikit-image, sklearn.linear_model, sklearn.model_selection, sklearn.decomposition, sklearn.ensemble
* HTML, CSS, Bootstrap
* Javascript, D3

## The Process
The digital images for each artist's paintings were collected through online searches. While web scraping was used for all of the Morris Louis image collection, the Mark Rothko images were gathered manually. In total, 166 Rothko paintings and 660 Louis paintings were collected to build the prediction models.

#### Extract Painting Metrics
Every image is made of many pixels. Instead of running a prediction using the individual pixels from each image, image properties summarizing different pixel patterns and characteristics were extracted from each image providing a more efficient dataset to build the prediction model.

The image properties (metrics) below were extracted from each painting and can be found in the Data Tables
* Contour: Extracting the contour is essentially extracting the general shape of the pixel pattern. A pattern can be identified when boundary pixels show an ordered sequence.
* Contrast: This property describes the difference in color and brightness within the digital image.
* Mean Color: Each pixel is measured for a red, green and blue value. From there, each red, green and blue value is averaged to achieve an overall average value for the painting.
* Mean Color-Red: The red mean color value for each painting was used to correlate time period predictions because the red colors appears to change the most over time with Rothko and Morris' paintings.
* Luminance: This shows the brightness of color and is calculated by using the averaged red, green and blue values to calculate a luminance value: =(0.2126*R + 0.7152*G + 0.0722*B). This shows the difference in how the human eye perceives red, green and blue colors. For instance, green light is most intensively perceived by the human eye.
* Shannon Entropy: This measures the business of an image. Greater entropy means a more complex image resulting in a larger flattened file.

#### Model Testing and Selection
Three different types of models were evaluated to build the Rothko and Morris prediction models. 

##### Regression
Linear regression was the first model evaluated as this is the most straightforward type of model with one independent variable - year and one or more dependent variables - the above metrics. The metrics were checked individually and together for a linear relationship, with highest correlation resulting from shannon entropy. Multilinear relationships were also explored using multiple metrics but proved not much more successful than using shannon entropy individually. Scores for the regression models were at 0.5 or less. 

##### Clustering K-Means
K-means models seek to cluster data into "k" number of groups that are each well represented by their means. It is successfully use when datasets are distinct and separated in a linear way. K-means models should result in visible clusters grouping the data points together, but when applied to the paintings, the resulting clusters overlapped significantly with indistinct boundaries. This was not surprising because the linear regression did not prove a strong correlation. 

##### Classification: Decision Tree and Random Forest
Decision trees are used to classify datasets visually, going through a series of decisions based on a selected set of features until each branch is no longer split to achieve the final classification decision. The features in this case are: Shannon entropy, mean red color, luminance, contrast and contour, and the final decision is which year bin to classify the painting. This model proved the best for both painter's but especially Rothko. 

##### Model Scores:
* Rothko Decision Tree: 80%
* Rothko Random Forest: 83%
* Louis Decision Tree: 60%.
* Louis Random Forest: 59%
* Links to the code can be found here.
* Rothko: Rothko Models
* Louis: Louis Models

## Project Presentation
The tool and project information is organized on this [website] (https://rothkoapp.herokuapp.com).

## Conclusions
Classification models scored the highest for Rothko and Morris time period predictions and both the Decision Tree and Random Forest were more or less similar in performance. The works of Mark Rothko and Morris Louis visibly change over time and now this is quantified and predictable using machine learning models.

## Additional Considerations
It may be of interest to test the model against Rothko's close colleagues like Adolf Gottlieb and Barnet to determine similarity and influence. 

