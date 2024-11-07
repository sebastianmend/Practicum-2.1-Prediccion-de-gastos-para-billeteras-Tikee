from flask import Flask, render_template

app = Flask(__name__)

# Ruta para renderizar el mapa en el navegador
@app.route('/')
def index():
    return render_template('mapa.html')

if __name__ == '__main__':
    app.run(debug=True)
