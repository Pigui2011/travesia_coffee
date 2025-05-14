from flask import Flask, render_template
import mercadopago

app = Flask(__name__)

# Configura tus credenciales de Mercado Pago aquí
sdk = mercadopago.SDK("TEST-ACCESS-TOKEN")  # Reemplaza con tu access token

@app.route("/")
def index():
    return render_template("index.html")

# @app.route("/catalogo")
# def catalogo():
#     return render_template("catalogo.html")

@app.route("/catalogo")
def catalogo():
    productos = [
        {
            "nombre": "Café Clásico",
            "precio": "$15.000",
            "imagen": "img/producto1.jpeg",
            "whatsapp": "https://wa.me/573002674845?text=Quiero%20comprar%20Café%20Clásico"
        },
        {
            "nombre": "Café Seleccionado",
            "precio": "$25.000",
            "imagen": "img/producto2.jpeg",
            "whatsapp": "https://wa.me/573002674845?text=Quiero%20comprar%20Café%20Seleccionado"
        },
        {
            "nombre": "Café Molido Lb",
            "precio": "$25.500",
            "imagen": "img/producto3.jpeg",
            "whatsapp": "https://wa.me/573002674845?text=Quiero%20comprar%20Café%20Seleccionado"
        },
        {
            "nombre": "Café najulu Lb",
            "precio": "$10.500",
            "imagen": "img/producto4.jpeg",
            "whatsapp": "https://wa.me/573002674845?text=Quiero%20comprar%20Café%20Seleccionado"
        },
        {
            "nombre": "Café mañanas Lb",
            "precio": "$18.500",
            "imagen": "img/producto5.jpeg",
            "whatsapp": "https://wa.me/573002674845?text=Quiero%20comprar%20Café%20Seleccionado"
        }
    ]
    return render_template("catalogo.html", productos=productos)

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
    from os import environ
    app.run(host="0.0.0.0", port=int(environ.get("PORT", 5000)))

