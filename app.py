from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return "ML API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json["features"]
    prediction = model.predict([data]).tolist()
    return jsonify({"prediction": prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)