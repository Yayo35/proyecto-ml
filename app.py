from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Leer el archivo CSV que subió el usuario
        f = request.files['file']
        df = pd.read_csv(f)

        # Sacar datos útiles
        columnas = df.columns.tolist()
        primeras_filas = df.head().to_html()
        resumen = df.describe().to_html()

        # Mostrar todo como HTML
        return f"""
        <h1>¡Archivo recibido!</h1>
        <h2>Columnas:</h2>
        <ul>{"".join(f"<li>{col}</li>" for col in columnas)}</ul>
        <h2>Primeras filas del archivo:</h2>
        {primeras_filas}
        <h2>Estadísticas básicas (solo numéricas):</h2>
        {resumen}
        <br><a href="/">⬅️ Subir otro archivo</a>
        """

    # Si no han subido nada, mostrar el formulario
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)