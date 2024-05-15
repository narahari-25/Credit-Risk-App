from flask import Flask, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# Load the data from CSV
df = pd.read_csv('synthetic_credit_data.csv')

# Split data into features (X) and target (y)
X = df.drop(columns=['CreditScore'])
y = df['CreditScore']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the trained model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Define API endpoint for credit score prediction
@app.route('/predict_credit_score', methods=['POST'])
def predict_credit_score():
    logging.debug(f'BOO')
    try:
        # Get data from JSON request
        data = request.json
        new_applicant_features = pd.DataFrame(data)
        logging.debug(f'Received: {data}')

        # Predict credit score
        credit_score = model.predict(new_applicant_features)

        # Return prediction as JSON response
        return jsonify({'credit_score': credit_score.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
