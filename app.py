from flask import Flask, request, jsonify
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)

def calcular_distancia(lat1, lon1, lat2, lon2):
    R = 6371.0
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = R * c
    return round(distancia, 2)

@app.route('/predict', methods=['POST'])
def predecir_tiempo():
    datos = request.get_json()
    
    edad = float(datos.get('edad'))
    calificacion = float(datos.get('calificacion'))
    rest_lat = float(datos.get('rest_lat'))
    rest_lon = float(datos.get('rest_lon'))
    del_lat = float(datos.get('del_lat'))
    del_lon = float(datos.get('del_lon'))
    orden = datos.get('orden').strip()
    vehiculo = datos.get('vehiculo').strip()
    
    distancia_km = calcular_distancia(rest_lat, rest_lon, del_lat, del_lon)
    
    dic_vehiculo = {
        "motorcycle": 1, 
        "scooter": 2, 
        "electric_scooter": 3, 
        "bycicle": 4
    }
    vehiculo_num = dic_vehiculo.get(vehiculo, 1)

    tiempo = 10 + (distancia_km * 3) + (edad * 0.5) - (calificacion * 2) + vehiculo_num
    
    return jsonify({
        "distancia_km": distancia_km,
        "tiempo_predicho": round(tiempo, 1)
    })

if __name__ == '__main__':
    app.run(debug=True)
