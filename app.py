from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predecir_tiempo():
    try:
        datos = request.get_json()
        edad = float(datos.get('edad', 0))
        calificacion = float(datos.get('calificacion', 0))
        clima = datos.get('clima', '')
        trafico = datos.get('trafico', '')
        vehiculo = datos.get('vehiculo', '')

        dic_clima = {"Sunny": 1, "Cloudy": 2, "Fog": 3, "Rainy": 4}
        dic_trafico = {"Low": 1, "Medium": 2, "High": 3, "Jam": 4}
        dic_vehiculo = {"motorcycle": 1, "scooter": 2, "electric_scooter": 2, "bycicle": 3}

        clima_n = dic_clima.get(clima, 1)
        trafico_n = dic_trafico.get(trafico, 1)
        vehiculo_n = dic_vehiculo.get(vehiculo, 1)

        tiempo = 15 + (trafico_n * 6) + (clima_n * 3) + (vehiculo_n * 2) - (calificacion * 1.5)
        
        return jsonify({"status": "success", "tiempo_predicho": round(tiempo, 1)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)