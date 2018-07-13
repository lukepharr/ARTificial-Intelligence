###########################################################################################
# This is the main flask application script for the website
###########################################################################################
import os
from flask import Flask
from flask import render_template, jsonify, request
import pandas as pd

from sklearn import tree
import pickle

import metrics

app = Flask(__name__)

# The path to the Rothko and Morris models
rothko_tree_model_file = "./models/RothkoDecisionTree.pkl"
rothko_linear_model_file = "./models/RothkoLinearModel.pkl"
rothko_random_forest_model_file = "./models/RothkoRandomForestModel.pkl"
morris_tree_model_file = "./models/MorrisDecisionTree.pkl"
morris_random_forest_model_file = "./models/MorrisRandomForestModel.pkl"

app.config['UPLOAD_FOLDER'] = 'uploads'

#########################################################
# Flask route for the root/index page
#########################################################
@app.route('/')
def go_home():
    return render_template('index.html', title='Home')

#########################################################
# Flask route to classify a Rothko Image. The <imagefile> 
# is expected to exist static/images/test/rothko folder and the uploadfile
# in the uploads folder
#########################################################
@app.route('/classify_rothko/<imagefile>/<uploadfile>')
def classify_rothko(imagefile=None, uploadfile=None):
    d = {}
    # if the first parameter is "upload" then the uploadfile exists and we need to look
    # into the uploads folder, else the corresponding test folder. 
    if (imagefile=="upload"):
        print("uploads/"+uploadfile)
        d = metrics.get_image_data("uploads/"+uploadfile)
    else :
        d = metrics.get_image_data("static/images/test/rothko/"+imagefile)
    

    # load the rothko decision tree model from disk
    decision_tree_model = pickle.load(open(rothko_tree_model_file, "rb"))

    # get the metrics for the image that we need for the input features for the model
    features = [[d["shannon_entropy"][0], d["mean_color_r"][0], d["luminance"][0], d["contrast"][0], d["contour"][0] ]]

    # use the model to predict the year bin
    tree_predicted = decision_tree_model.predict(features)

    # load the rothko decision tree model from disk
    random_forest_model = pickle.load(open(rothko_random_forest_model_file, "rb"))

    # use the model to predict the year bin
    random_predicted = random_forest_model.predict(features)

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
    image_info = {"image_data": d, "tree_predicted_year_bin":tree_predicted.tolist(), 
                    "random_forest_predicted_year_bin":random_predicted.tolist(),
                    "linear_predicted_year_bins": linear_bins}
    return jsonify(image_info)

#########################################################
# Flask route to classify a Morris Louis Image. The <imagefile> 
# is expected to exist static/images/test/morris folder and the uploadfile
# in the uploads folder
#########################################################
@app.route('/classify_morris/<imagefile>/<uploadfile>')
def classify_morris(imagefile=None, uploadfile=None):

    # if the first parameter is "upload" then the uploadfile exists and we need to look
    # into the uploads folder, else the corresponding test folder. 
    if (imagefile=="upload"):
        print("uploads/"+uploadfile)
        d = metrics.get_image_data("uploads/"+uploadfile)
    else :
        d = metrics.get_image_data("static/images/test/morris/"+imagefile)
    
    # get the metrics for the image that we need for the input features for the model
    features = [[d["shannon_entropy"][0], d["mean_color_r"][0], d["luminance"][0], d["contrast"][0], d["contour"][0] ]]

    # load the morris decision tree model from disk
    decision_tree_model = pickle.load(open(morris_tree_model_file, "rb"))

    # use the model to predict the year bin
    tree_predicted = decision_tree_model.predict(features)

    # load the morris decision tree model from disk
    random_forest_model = pickle.load(open(morris_random_forest_model_file, "rb"))

    # use the model to predict the year bin
    random_predicted = random_forest_model.predict(features)


    # create the dictionary to return
    image_info = {"image_data": d, "tree_predicted_year_bin":tree_predicted.tolist(), 
                    "random_forest_predicted_year_bin":random_predicted.tolist()}
    print("############  Morris Louis Response ###############")
    print(image_info)
    return jsonify(image_info)

#########################################################
# Flask route for the specific section of the Artist Gallery page
#########################################################
@app.route('/artist_gallery/<ref>')
def show_artist_gallery(ref):
    return render_template('artist_gallery.html', section = ref)
    
#########################################################
# Flask route for the Artist Gallery page
#########################################################
@app.route('/artist_gallery')
def artist_gallery():
    return render_template('artist_gallery.html')

#########################################################
# Flask route for the Test Gallery page
#########################################################
@app.route('/test_gallery', methods=['GET', 'POST'])
def show_test_gallery():

    # If it is a POST then we need to save the file to the uploads folder
    if request.method == 'POST':
        # if the post is via the rothkofile upload button
        if request.files.get('rothkofile'):
            print("GOT ROTHKO FILE !!!!!!!!!!!!!!!!!!!!!!")
            # read the file
            file = request.files['rothkofile']

            # read the filename
            filename = file.filename

            # Save the file to the uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('test_gallery.html', msg=" saved!", artist="rothko", filename=filename)
        
        # if the post is via the louisfile upload button
        if request.files.get('louisfile'):
            print("GOT LOUIS FILE !!!!!!!!!!!!!!!!!!!!!!")
            # read the file
            file = request.files['louisfile']

            # read the filename
            filename = file.filename

            # Save the file to the uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template('test_gallery.html', msg=" saved!", artist="louis", filename=filename)

    # for a GET  request there are no files to upload
    return render_template('test_gallery.html', msg="", artist="", filename="")

#########################################################
# Flask route for the Data page
#########################################################
@app.route('/data')
def show_data():
    return render_template('data.html')

#########################################################
# Flask route for the About Us page
#########################################################
@app.route('/about')
def show_about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)

