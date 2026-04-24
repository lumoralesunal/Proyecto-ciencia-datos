function simular_prediccion() {

    var edad = document.getElementById("input_edad").value;
    var calificacion = document.getElementById("input_calificacion").value;
    var clima = document.getElementById("input_clima").value;
    var trafico = document.getElementById("input_trafico").value;
    var vehiculo = document.getElementById("input_vehiculo").value;


    if (edad === "" || calificacion === "") {
        alert("Por favor, llena la edad y la calificación.");
        return; 
    }

   
    var caja = document.getElementById("caja_resultado");
    var texto = document.getElementById("texto_resultado");

   
    caja.style.display = "block";

    texto.innerHTML = "Tiempo estimado: x minutos.";
}