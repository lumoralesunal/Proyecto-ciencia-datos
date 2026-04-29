from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

@app.route('/predict', methods=['POST'])
def predecir_tiempo():
    
    datos = request.get_json()
    edad = float(datos.get('edad'))
    calificacion = float(datos.get('calificacion'))
    clima = datos.get('clima')
    trafico = datos.get('trafico')
    vehiculo = datos.get('vehiculo')
    
    diccionario_trafico = {
        "Low": 1, 
        "Medium": 2, 
        "High": 3, 
        "Jam": 4
    }
    trafico_num = diccionario_trafico.get(trafico, 2)
    
    diccionario_clima = {
        "Sunny": 1,
        "Cloudy": 2,
        "Fog": 3,
        "Rainy": 4
    }
    clima_num = diccionario_clima.get(clima, 1)

    diccionario_vehiculo = {
        "motorcycle": 1,
        "scooter": 2,
        "electric_scooter": 2,
        "bycicle": 3
    }
    vehiculo_num = diccionario_vehiculo.get(vehiculo, 1)

    
    # Tiempo base de 20 min + ajustes por variables
    tiempo_calculado = 20 + (trafico_num * 5) + (clima_num * 3) + (vehiculo_num * 4) - (calificacion * 2)

    tiempo_final = round(tiempo_calculado, 1)
    
    return jsonify({
        "mensaje": "Preprocesamiento y conexión exitosa",
        "tiempo_predicho": tiempo_final
    })

if __name__ == '__main__':
    app.run(debug=True)