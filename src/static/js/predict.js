/**
 * This javascript file contains the code to use the models to classify test images in the Test Gallery
 * page. This code is used by test_gallery.html
 * 
 * @author Rupali Mayekar
 */


var resultText1 = "Decision Tree Model Predicted Year : ";
var resultText2 = "<br>Decision Tree Model Classification : ";
var resultText3 = "<br><br>Random Forest Model Predicted Year : ";
var resultText4 = "<br>Random Forest Model Classification : ";
var waitText = "Please wait while we classify your the image: ";
var clearText = "Select/upload an image and click the Classify button to see how the models classifies it.";
var alertText = "Please select/upload an image to classify.";

var artistlink1 = '<a target="_blank" href="../artist_gallery/';
var artistlink2 = '">'
var artistlink3 = '</a>';

// A dictionary of the year ranges and their corresponding names as specified on the 
// artist-gallery page
var rothkoClassification = {"(1935, 1940]":"Figurative", "(1940, 1947]": "Surrealism",
        "(1947, 1950]":"Multiform", "(1950, 1968]":"Mature", "(1968, 1971]":"Late"};

/**
 * 
 * @param {string} art  is the name of the image file used to test the model. The flask route
 * will look for this file in the static/images/test/rothko folder and use it to classify using
 * the models
 * @param filename is the name of the uploaded file in the uploads folder
 */
function classifyRothko (art, filename="") {
    // Call the flask route to classify this rothko art image
    var route = "";

    // if a file is uploaded then classify it, otherwise classify the selection
    if (filename==""){
        route = '/classify_rothko/'+ art + "/none";
    } else {
        route = '/classify_rothko/upload/'+filename;
    }
    console.log("This is the rothko route===========", route);

    d3.json(route, function(error, response) {
        console.log(response);
        var treePrediction = response.tree_predicted_year_bin[0]
        var forestPrediction = response.random_forest_predicted_year_bin[0]
        console.log(treePrediction);
        console.log(forestPrediction);

        // populate the value in the result panel
        var panelText = resultText1 + treePrediction + resultText2 + artistlink1 + rothkoClassification[treePrediction] + artistlink2 + rothkoClassification[treePrediction] + artistlink3 +
            resultText3 + forestPrediction + resultText4 + artistlink1 + rothkoClassification[forestPrediction] + artistlink2 + rothkoClassification[forestPrediction] + artistlink3;
        d3.select("#result-panel").html(panelText);
    });

};

/**
 * Clear the upload file name for Rothko.
 */
function clearRothkoUpload() {
    d3.select("#rothkoFile").html("");
    d3.select("#rothkoFile").attr("data","");
}

/**
 * This function is called when the Classify button on the Test Gallery page is clicked
 */
function predictRothko() {

    var filename = document.getElementById("rothkoFile").getAttribute("data");
    console.log(filename);

    if (filename!= ""){
        d3.select("#result-panel").html(waitText + filename + "...");
        classifyRothko("", filename)
    } else {
        if (document.getElementById('inlineRadio1').checked) {
            // Get the name of the selected image
            var art = document.getElementById('inlineRadio1').value;
            d3.select("#result-panel").html(waitText + art + "...");
            classifyRothko(art);
        } else if (document.getElementById('inlineRadio2').checked) {
            // Get the name of the selected image
            var art = document.getElementById('inlineRadio2').value;
            d3.select("#result-panel").html(waitText + art + "...");
            classifyRothko(art);
        } else if (document.getElementById('inlineRadio3').checked) {
            // Get the name of the selected image
            var art = document.getElementById('inlineRadio3').value;
            d3.select("#result-panel").html(waitText + art + "...");
            classifyRothko(art);
        } else if (document.getElementById('inlineRadio4').checked) {
            // Get the name of the selected image
            var art = document.getElementById('inlineRadio4').value;
            d3.select("#result-panel").html(waitText + art + "...");
            classifyRothko(art);
        } else {
            alert(alertText);
        };
    }
}

/**
 * 
 * @param art  is the name of the image file used to test the model. The flask route
 * will look for this file in the static/images/test/morris folder and use it to classify using
 * the models for Morris Louis
 * @param filename is the name of the uploaded file in the uploads folder
 */
function classifyMorris (art, filename="") {
    // Call the flask route to classify this morris art image
    var route = "";

    // if a file is uploaded then classify it, otherwise classify the selection
    if (filename==""){
        route = '/classify_morris/'+ art + "/none";
    } else {
        route = '/classify_morris/upload/'+filename;
    }
    console.log("This is the rothko route===========", route);

    d3.json(route, function(error, response) {
        console.log(response);
        var treePrediction = response.tree_predicted_year_bin[0]
        var forestPrediction = response.random_forest_predicted_year_bin[0]
        console.log(treePrediction);

        // populate the value in the result panel
        var panelText = resultText2 + artistlink1 + treePrediction + artistlink2 + treePrediction + artistlink3
         + resultText4 + artistlink1 + forestPrediction + artistlink2 + forestPrediction + artistlink3;
        d3.select("#result-panel-morris").html(panelText);
    });

};

/**
 * Clear the upload file name for Morris.
 */
function clearLouisUpload() {
    d3.select("#louisFile").html("");
    d3.select("#louisFile").attr("data","");
}

/**
 * This function is called when the Classify button on the Test Gallery page is clicked
 */
function predictMorris() {
    var filename = document.getElementById("louisFile").getAttribute("data");
    console.log(filename);

    if (filename!= ""){
        d3.select("#result-panel-morris").html(waitText + filename + "...");
        classifyMorris("", filename)
    } else {
        if (document.getElementById('inlineRadioMorris1').checked) {
            // Get the name of the selected image
            var art = document.getElementById('inlineRadioMorris1').value;
            d3.select("#result-panel-morris").html(waitText + art + "...");
            classifyMorris(art);
        } else if (document.getElementById('inlineRadioMorris2').checked) {
            // Get the name of the selected image
            var art = document.getElementById('inlineRadioMorris2').value;
            d3.select("#result-panel-morris").html(waitText + art + "...");
            classifyMorris(art);
        } else if (document.getElementById('inlineRadioMorris3').checked) {
            // Get the name of the selected image
            var art = document.getElementById('inlineRadioMorris3').value;
            d3.select("#result-panel-morris").html(waitText + art + "...");
            classifyMorris(art);
        } else if (document.getElementById('inlineRadioMorris4').checked) {
            // Get the name of the selected image
            var art = document.getElementById('inlineRadioMorris4').value;
            d3.select("#result-panel-morris").html(waitText + art + "...");
            classifyMorris(art);
        } else {
            alert(alertText);
        };
    };
}
