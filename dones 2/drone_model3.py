import random


class Drone:
    def __init__(self, drone_id, ubicacion, lat, lon, temperatura, velocidad_viento, direccion_viento, estado="ACTIVO"):
        self.id = drone_id
        self.ubicacion = ubicacion
        self.lat = lat
        self.lon = lon
        self.temperatura = temperatura
        self.velocidad_viento = velocidad_viento
        self.direccion_viento = direccion_viento
        self.estado = estado
    
    def actualizar_datos_aleatorios(self):
        self.temperatura += random.uniform(-2, 3)
        self.temperatura = max(20, min(100, self.temperatura))
        
        self.velocidad_viento += random.uniform(-3, 4)
        self.velocidad_viento = max(5, min(80, self.velocidad_viento))
        
        if random.random() < 0.2:
            self.direccion_viento = random.choice(["N", "S", "E", "O", "NE", "NO", "SE", "SO"])
        
        self.lat += random.uniform(-0.01, 0.01)
        self.lon += random.uniform(-0.01, 0.01)
    
    def to_dict(self):
        return {
            'id': self.id,
            'ubicacion': self.ubicacion,
            'lat': self.lat,
            'lon': self.lon,
            'temperatura': self.temperatura,
            'velocidad_viento': self.velocidad_viento,
            'direccion_viento': self.direccion_viento,
            'estado': self.estado
        }