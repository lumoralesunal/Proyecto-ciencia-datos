# Sistema de Predicción de Tiempo de Entrega

## 1. Descripción del dataset
* **Justificación:** Se eligió este dataset porque optimizar los tiempos de entrega es un problema crítico en logística. Permite aplicar modelos de Regresión para estimar el tiempo en minutos basándose en las condiciones del entorno y del repartidor.
* **Fuente:** El dataset fue obtenido de Kaggle y corresponde a registros reales de tiempos de entrega de pedidos.
* **Número de instancias:** 45593 instancias
* **Variables de entrada principales:** `Delivery_person_Age` (Edad), `Delivery_person_Ratings` (Calificación), `Weatherconditions` (Clima), `Road_traffic_density` (Tráfico), `Type_of_vehicle` (Vehículo).
* **Variable objetivo:** `Time_taken(min)` (Tiempo de entrega en minutos). Es un problema de Aprendizaje Supervisado.

## 2. Análisis preliminar de los datos

| Estadística | Delivery_person_Age | Delivery_person_Ratings | Time_taken(min) |
| :--- | :--- | :--- | :--- |
| **count** | 45593.000000 | 45593.000000 | 45593.000000 |
| **mean** | 29.544075 | 4.632367 | 26.294607 |
| **std** | 5.696793 | 0.327708 | 9.383806 |
| **min** | 15.000000 | 1.000000 | 10.000000 |
| **25%** | 25.000000 | 4.600000 | 19.000000 |
| **50%** | 29.000000 | 4.700000 | 26.000000 |
| **75%** | 34.000000 | 4.800000 | 32.000000 |
| **max** | 50.000000 | 6.000000 | 54.000000 |

<img width="800" height="500" alt="imagen1" src="https://github.com/user-attachments/assets/274545d3-0948-4345-9e9a-727f1c1f1251" />

<img width="800" height="500" alt="imagen2" src="https://github.com/user-attachments/assets/e75eb0ca-2fb8-4ab8-8cba-611900824d76" />

<img width="800" height="500" alt="imagen3" src="https://github.com/user-attachments/assets/f583f0cc-8c4b-41ca-9eb9-6ea182daa1d9" />


