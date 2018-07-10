/**
 * This javascript file contains the code to use the models to predict test images
 * 
 * @author Rupali Mayekar
 */


var resultText1 = "Decision Tree Model Predicted Year : ";
var resultText2 = "<br>Decision Tree Model Classification : ";
var resultText3 = "<br><br>Random Forest Model Predicted Year : ";
var resultText4 = "<br>Random Forest Model Classification : ";

// A dictionary of the year ranges and their corresponding names as specified on the 
// artist-gallery page
var rothkoClassification = {"(1935, 1940]":"Figurative", "(1940, 1947]": "Surrealism",
        "(1947, 1950]":"Multiform", "(1950, 1968]":"Mature", "(1968, 1971]":"Late"};
// bins = [1935, 1940, 1947, 1950, 1968, 1971]

/**
 * 
 * @param {string} art  is the name of the image file used to test the model. The flask route
 * will look for this file in the static/images/test/rothko folder and use it to classify using
 * the models
 */
function classifyRothko (art) {
    // Call the flask route to classify this rothko art image
    var route = '/classify_rothko/'+art;
    d3.json(route, function(error, response) {
        console.log(response);
        var treePrediction = response.tree_predicted_year_bin[0]
        var forestPrediction = response.random_forest_predicted_year_bin[0]
        console.log(treePrediction);
        console.log(forestPrediction);

        // populate the value in the result panel
        var panelText = resultText1 + treePrediction + resultText2 + rothkoClassification[treePrediction]
            + resultText3 + forestPrediction + resultText4 + rothkoClassification[forestPrediction];
        d3.select("#result-panel").html(panelText);
    });

};

/**
 * This function is called when the Predict button on the Test Gallery page is clicked
 */
function predictRothko() {
    //d3.select("#year-text").html("Showing data for the year range: " + yearSelection);

    console.log(d3.select(".radio-inline"));

    if (document.getElementById('inlineRadio1').checked) {
        // Get the name of the selected image
        var art = document.getElementById('inlineRadio1').value;
        console.log(art);
        classifyRothko(art);
    } else if (document.getElementById('inlineRadio2').checked) {
        // Get the name of the selected image
        var art = document.getElementById('inlineRadio2').value;
        console.log(art);
        classifyRothko(art);
    } else if (document.getElementById('inlineRadio3').checked) {
        // Get the name of the selected image
        var art = document.getElementById('inlineRadio3').value;
        console.log(art);
        classifyRothko(art);
    } else if (document.getElementById('inlineRadio4').checked) {
        // Get the name of the selected image
        var art = document.getElementById('inlineRadio4').value;
        console.log(art);
        classifyRothko(art);
    } else {
        alert("Please select an image to classify.");
    };

}