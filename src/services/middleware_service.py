# src/services/mediador_service.py
from .openMeteo_service import OpenMeteoService
from .pokemon_service import PokemonService

class MiddlewareService:
    def __init__(self):
        self.open_meteo_service = OpenMeteoService()
        self.pokemon_service = PokemonService()

    def obtener_pokemon_por_clima(self):
        clima_data = self.open_meteo_service.get_current_temperature()
        print(clima_data)
        if "error" in clima_data:
            return clima_data

        temperatura = clima_data['temperature']
        tipo_fuerte = self.determinar_tipo_fuerte(temperatura)
        return self.pokemon_service.get_random_pokemon(tipo_fuerte, ['I', 'A', 'M'])

    def determinar_tipo_fuerte(self, temperatura):
        if temperatura >= 30:
            return "fire"
        elif 20 <= temperatura < 30:
            return "ground"
        elif 10 <= temperatura < 20:
            return "normal"
        elif 0 <= temperatura < 10:
            return "water"
        else:
            return "ice"
