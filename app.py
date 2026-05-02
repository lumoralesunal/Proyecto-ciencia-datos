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

        dic_orden = { "Snack": 5,"Drinks": 3,"Buffet": 15,"Meal": 10}
        dic_vehiculo = {"motorcycle": 1, "scooter": 2, "electric_scooter": 2, "bycicle": 3}

        tiempo_preparacion = dic_orden.get(orden, 5)
        vehiculo_n = dic_vehiculo.get(vehiculo, 1)

        tiempo = 10 + tiempo_preparacion + (vehiculo_n * 4) - (calificacion * 1.2)
        
        return jsonify({"status": "success", "tiempo_predicho": round(tiempo, 1)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
