function simular_prediccion() {
    var edad = document.getElementById("input_edad").value;
    var calificacion = document.getElementById("input_calificacion").value;
    var rest_lat = document.getElementById("rest_lat").value;
    var rest_lon = document.getElementById("rest_lon").value;
    var del_lat = document.getElementById("del_lat").value;
    var del_lon = document.getElementById("del_lon").value;
    var orden = document.getElementById("input_orden").value;
    var vehiculo = document.getElementById("input_vehiculo").value;

    if (edad === "" || calificacion === "") {
        alert("Por favor, llena la edad y la calificación.");
        return; 
    }

    fetch("http://localhost:5000/predict", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            edad: parseFloat(edad),
            calificacion: parseFloat(calificacion),
            rest_lat: parseFloat(rest_lat),
            rest_lon: parseFloat(rest_lon),
            del_lat: parseFloat(del_lat),
            del_lon: parseFloat(del_lon),
            orden: orden,
            vehiculo: vehiculo
        })
    })
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        var caja = document.getElementById("caja_resultado");
        var texto = document.getElementById("texto_resultado");
        
        caja.style.display = "block";
        texto.innerHTML = "Distancia: " + data.distancia_km + " km <br> Tiempo estimado: " + data.tiempo_predicho + " minutos.";
    })
    .catch(function(error) {
        alert("El error real es: " + error.message);
        console.error("Detalle del error:", error);
    });
}

