from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Advertising API!"

@app.route('/api/v1/predict', methods=['POST'])
def predict():
    with open('ad_model.pkl', 'rb') as f:
        model = pickle.load(f)

    data = request.get_json()
    input_df = pd.DataFrame([data])
    prediction = model.predict(input_df)[0]

    return jsonify({'prediction': prediction})

@app.route('/api/v1/retrain', methods=['POST'])
def retrain():
    file = request.files['file']
    df = pd.read_csv(file)

    X = df.drop(columns=['sales'])
    y = df['sales']

    from sklearn.linear_model import Lasso
    model = Lasso(alpha=6000)
    model.fit(X, y)

    with open('ad_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    return jsonify({'message': 'Model retrained successfully'})

if __name__ == '__main__':
    app.run(debug=True)
