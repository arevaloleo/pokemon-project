# app.py
from flask import Flask
from src.controllers.pokemon_controller import pokemon_bp

app = Flask(__name__)

# Registra el blueprint
app.register_blueprint(pokemon_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
