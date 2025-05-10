from flask import Flask, render_template
import mercadopago

app = Flask(__name__)

# Configura tus credenciales de Mercado Pago aquí
sdk = mercadopago.SDK("TEST-ACCESS-TOKEN")  # Reemplaza con tu access token

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/catalogo")
def catalogo():
    return render_template("catalogo.html")

@app.route("/galeria")
def galeria():
    return render_template("galeria.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

if __name__ == "__main__":
    app.run(debug=True)
