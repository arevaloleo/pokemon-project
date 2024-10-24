import requests
from datetime import datetime

class OpenMeteoService:
    latitud = "-31.4135"
    longitud = "-64.181"
    def get_current_temperature(self):
        # Obtener el pronóstico por hora (incluyendo la temperatura)
        url = f"https://api.open-meteo.com/v1/forecast?latitude={self.latitud}&longitude={self.longitud}&hourly=temperature_2m&timezone=auto"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            current_time = datetime.now().strftime("%Y-%m-%dT%H:00")
            if current_time in data["hourly"]["time"]:
                index = data["hourly"]["time"].index(current_time)
                current_temperature = data["hourly"]["temperature_2m"][index]
                return {"temperature": current_temperature, "time": current_time}
            else:
                return {"error": "No temperature data available for the current time"}
        else:
            return {"error": "Unable to fetch weather data"}
