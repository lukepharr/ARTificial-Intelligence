###########################################################################################
# This is the main flask application script for the website
###########################################################################################
import os
from flask import Flask
from flask import render_template, jsonify
import pandas as pd

from sklearn import tree
import pickle

import metrics

app = Flask(__name__)

# The path to the Rothko Decision Tree model
rothko_tree_model_file = "../Rothko/models/TREE/RothkoDecisionTree.pkl"
rothko_linear_model_file = "../Rothko/models/linear_regression/RothkoLinearModel.pkl"

#########################################################
# Flask route for the root/index page
#########################################################
@app.route('/')
def home():
    return render_template('index.html', title='Home')

#########################################################
# Flask route to classify a Rothko Image. The <imagefile> 
# is expected to exist in the uploads folder
#########################################################
@app.route('/classify_rothko/<imagefile>')
def classify_rothko(imagefile):
    # load the rothko decision tree model from disk
    decision_tree_model = pickle.load(open(rothko_tree_model_file, "rb"))

    # get the metrics for the image that we need for the input features for the model
    d = metrics.get_image_data("uploads/"+imagefile)
    features = [[d["shannon_entropy"][0], d["mean_color_r"][0], d["luminance"][0], d["contrast"][0], d["contour"][0] ]]

    # use the model to predict the year bin
    predicted = decision_tree_model.predict(features)

    # load the linear model from disk
    linear_model = pickle.load(open(rothko_linear_model_file, "rb"))

    # predict the years and put them into the correct bins
    linear_predictions = linear_model.predict(features)
    linear_predictions = linear_predictions.round().astype(int)
    linear_pred_df = pd.DataFrame(data = {"predicted": linear_predictions})
    bins = [1935, 1940, 1947, 1950, 1968, 1971]
    linear_pred_df['predicted_year_bin']=pd.cut(linear_pred_df['predicted'], bins).astype(str)
    linear_bins = linear_pred_df['predicted_year_bin'].tolist()

    # create the dictionary to return
    image_info = {"image_data": d, "tree_predicted_year_bin":predicted.tolist(), 
                    "linear_predicted_year_bins": linear_bins}
    return jsonify(image_info)


@app.route('/about')
def thesis():
    return render_template('about.html', title='Water We Doing? - A Summary')


if __name__ == "__main__":
    app.run(debug=True)

