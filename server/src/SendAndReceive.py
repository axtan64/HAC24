from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import base64
from random import randint
import check

# 2D array and choice of image

images = [
    ["chart.png", "chart1.png"],
    ["2chart.png", "2chart1.png"],
    ["3chart.png", "3chart1.png"],
    ["if.png", "if1.png"],
    ["2if.png", "2if1.png"]
]
global otherPath

# sending the image to front end
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


# Define route handler to receive data from the frontend
@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    editorText = data.get('editorText')
    fileName = data.get('fileName')
    # Perform any actions or processing based on the received data
    # For example, you can print it or use it to trigger some backend operation
    print("Received data from frontend:", editorText)

    # Return a response indicating successful receipt of data
    return jsonify({"status": check.checkCode(editorText)})

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

@app.route('/get_base64_image')
def get_base64_image():
    # Assuming you have the image path available
    num = randint(0, len(images) - 1)
    path = images[num][1]
    otherPath = images[num][0]
    return jsonify({"image": encode_image_to_base64(path), "fileName": path})

if __name__ == '__main__':
    app.run(debug=True)