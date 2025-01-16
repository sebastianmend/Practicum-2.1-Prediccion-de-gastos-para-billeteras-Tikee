from flask import Flask, render_template, request
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from geopy.distance import geodesic
import joblib

app = Flask(__name__)

# Cargar modelo KNN y datos
modelo_knn = joblib.load("recomendador_knn.pkl")
train_path = "dataset/transacciones_train.json"
df_train = pd.read_json(train_path, lines=True)

# Pesos para las características
pesos = {"latitud": 0.3, "longitud": 0.3, "hora": 0.3, "dia_semana": 0.1}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Obtener datos del formulario
            cedula = int(request.form["cedula"])
            latitud = float(request.form["latitud"])
            longitud = float(request.form["longitud"])
            hora = int(request.form["hora"])
            dia_semana = int(request.form["dia_semana"])
            radio_haversine = float(request.form["radio_haversine"])

            # Filtrar historial por cédula
            historial_usuario = df_train[df_train["ordenante_cedula"] == cedula]
            if historial_usuario.empty:
                return render_template("index.html", error="No se encontró historial para esta cédula")

            # Preparar datos del cliente
            cliente_datos = [latitud, longitud, hora, dia_semana]
            cliente_datos = [
                cliente_datos[0] * pesos["latitud"],
                cliente_datos[1] * pesos["longitud"],
                cliente_datos[2] * pesos["hora"],
                cliente_datos[3] * pesos["dia_semana"],
            ]

            # Obtener vecinos más cercanos
            X_train = historial_usuario[["latitud", "longitud", "hora", "dia_semana"]].copy()
            for columna, peso in pesos.items():
                X_train[columna] *= peso
            modelo_knn.fit(X_train)
            distancias, indices = modelo_knn.kneighbors([cliente_datos])

            # Obtener recomendaciones iniciales
            recomendaciones = historial_usuario.iloc[indices[0]].copy()

            # Calcular distancia Haversine
            cliente_coords = (latitud, longitud)
            recomendaciones["distancia_haversine"] = recomendaciones.apply(
                lambda row: geodesic(
                    (row["latitud_original"], row["longitud_original"]),
                    cliente_coords
                ).kilometers,
                axis=1
            )

            # Filtrar por distancia Haversine
            recomendaciones_filtradas = recomendaciones[recomendaciones["distancia_haversine"] <= radio_haversine]
            if recomendaciones_filtradas.empty:
                return render_template("index.html", error="No se encontraron recomendaciones dentro del radio")

            # Preparar resultados
            resultados = recomendaciones_filtradas[[
                "local_nombre", "latitud_original", "longitud_original", 
                "hora", "dia_semana", "distancia_haversine"
            ]].to_dict(orient="records")

            return render_template("index.html", resultados=resultados)

        except Exception as e:
            return render_template("index.html", error=f"Error: {str(e)}")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
