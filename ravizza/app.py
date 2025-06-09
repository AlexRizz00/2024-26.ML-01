from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/infer', methods=['POST'])
def hello():
    data = request.get_json()
    name = data.get('name', 'Stranger')
    return jsonify({"message": "Hello {}!".format(name)})

@app.route('/infer', methods=['POST'])
def returnModel():
    import pickle
    import pandas as pd

    # Load the model from the .pkl file
    with open("best_model.pkl", "rb") as file:
        model = pickle.load(file)

    # Load test data from a CSV file
    test_data_path = "mushrooms.csv"
    test_data = pd.read_csv(test_data_path)

    # Perform evaluation
    if hasattr(model, "predict"):
        predictions = model.predict(test_data)
        return jsonify(predictions)
    else:
        print("Loaded object is not a model.")



if __name__ == '__main__':
    app.run(debug=True)