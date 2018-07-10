//  This javascript file contains script to render the data to the data table 

// Establish references to HTML
var $Rothko = document.getElementById("Rothko");
var $Morris = document.getElementById("Morris");

d3.csv("static/data/data.csv", function (data) {    
    for (var r=0;r<data.length;r++) {
        var row = data[r];
        var fields = Object.keys(row);
        
        // Insert New Row
        var $row = $Rothko.insertRow(r);
        for (var c=0; c<fields.length; c++){
            var field=fields[c];
            // Insert new cells for each field
            var $cell = $row.insertCell(c);
            $cell.innerText = row[field];
        }
    }
    console.log(data);
    
}
);

d3.csv("static/data/morrisdata.csv", function (data) {    
    for (var r=0;r<data.length;r++) {
        var row = data[r];
        var fields = Object.keys(row);
        
        // Insert New Row
        var $row = $Morris.insertRow(r);
        for (var c=0; c<fields.length; c++){
            var field=fields[c];
            // Insert new cells for each field
            var $cell = $row.insertCell(c);
            $cell.innerText = row[field];
        }
    }
    console.log(data);
    
}
);

