import os
from flask import Flask, request, render_template, jsonify, redirect, url_for


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
response_dict = {"predictyear":1936,"message":"jinga is working"}

@app.route('/', methods=['GET'])
def index():
  return render_template("index.html", response=response_dict)

@app.route('/predict', methods=['POST'])
def prediction():
  print(request)

  if request.files.get('file'):
    # read the file
    file = request.files['file']

    # read the filename
    filename = file.filename

    # Save the file to the uploads folder
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

  return {"predictyear":1945, "message":"file uploaded!"}

if __name__ == "__main__":
    app.run(debug=True)