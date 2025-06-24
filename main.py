import os
import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Carregar modelo
try:
    model = joblib.load(os.path.join('artefatos', 'diabetes_model.joblib'))
except Exception:
    model = None

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok', 'model_loaded': model is not None})

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Modelo não carregado.'}), 503

    data = request.get_json()
    if not data or 'features' not in data:
        return jsonify({'error': 'A chave "features" é obrigatória.'}), 400

    features = data['features']
    if len(features) != 8:
        return jsonify({'error': 'Esperado 8 características.'}), 400

    try:
        prediction = model.predict([features])
        probability = model.predict_proba([features])[0][1]
        return jsonify({
            'prediction': int(prediction[0]),
            'probability': round(probability, 3)
        })
    except Exception:
        return jsonify({'error': 'Erro ao processar a predição.'}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)