from flask import Flask, jsonify, request
import base64
from random import randint

# 2D array and choice of image

images = [
    ["chart.png", "chart1.png"],
    ["2chart.png", "2chart1.png"],
    ["3chart.png", "3chart1.png"],
    ["if.png", "if1.png"],
    ["2if.png", "2if1.png"]
]



# sending the image to front end
app = Flask(__name__)


# Define route handler to receive data from the frontend
@app.route('/receive_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    button_data = data.get('button_data')

    # Perform any actions or processing based on the received data
    # For example, you can print it or use it to trigger some backend operation

    print("Received data from frontend:", button_data)



    # Return a response indicating successful receipt of data
    return jsonify({"status": "success"})

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string

@app.route('/get_base64_image')
def get_base64_image():
    # Assuming you have the image path available
    num = randint(0, len(images) - 1)
    path = images[num][1]
    return jsonify({"image": encode_image_to_base64(path)})

if __name__ == '__main__':
    app.run(debug=True)