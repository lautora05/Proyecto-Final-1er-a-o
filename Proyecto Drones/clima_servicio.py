import requests
import random
from configuracion import CONFIG, COORDENADAS_CIUDADES

class WeatherService:
    
    def obtener_datos_climaticos(self, ciudad):
        try:
            url = "http://api.weatherapi.com/v1/current.json"
            params = {
                "key": CONFIG['WEATHER_API_KEY'],
                "q": f"{ciudad}, Argentina",
                "aqi": "no",
                "lang": "es"
            }
            response = requests.get(url, params=params, timeout=5)
            data = response.json()

            if "error" in data:
                print("Error de API:", data["error"]["message"])
                return None

            return {
                "temperatura": data["current"]["temp_c"],
                "viento": data["current"]["wind_kph"],
                "direccion": data["current"]["wind_dir"]
            }

        except Exception as e:
            print("Error al obtener datos climáticos:", e)
            return None
    
    
    def obtener_coordenadas(self, ciudad):
        return COORDENADAS_CIUDADES.get(ciudad, {"lat": random.uniform(-55, -22), "lon": random.uniform(-73, -54)})