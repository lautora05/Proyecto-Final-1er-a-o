import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    'WEATHER_API_KEY': '44390f5f756c4a2fa7e203233251110',
    'EMAIL_SMTP_SERVER': '',
    'EMAIL_SMTP_PORT': ,
    'EMAIL_FROM': '',
    'EMAIL_PASSWORD': '',
}

UMBRALES_ALERTA = {
    'temperatura_alta': 45,
    'temperatura_critica': 60,
    'velocidad_viento_alta': 25,
    'velocidad_viento_critica': 40
}

CIUDADES_ARGENTINA = [
    "Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata", "San Miguel de Tucumán",
    "Mar del Plata", "Salta", "Santa Fe", "San Juan", "Resistencia", "Santiago del Estero",
    "Corrientes", "Posadas", "San Salvador de Jujuy", "Neuquén", "Formosa", "San Luis",
    "La Rioja", "Catamarca", "Río Gallegos", "Ushuaia", "Bahía Blanca", "Paraná", 
    "Merlo", "Godo Cruz", "Quilmes", "Pilar", "San Nicolás", "Vicente López",
    "Concordia", "San Rafael", "Tandil", "San Carlos de Bariloche", "Comodoro Rivadavia",
    "Río Cuarto", "Junín", "Zárate", "Olavarría", "Tres Arroyos", "Villa María"
]

COORDENADAS_CIUDADES = {
    "Buenos Aires": {"lat": -34.6037, "lon": -58.3816},
    "Córdoba": {"lat": -31.4201, "lon": -64.1888},
    "Rosario": {"lat": -32.9468, "lon": -60.6393},
    "Mendoza": {"lat": -32.8895, "lon": -68.8458},
    "La Plata": {"lat": -34.9205, "lon": -57.9536},
    "San Miguel de Tucumán": {"lat": -26.8083, "lon": -65.2176},
    "Mar del Plata": {"lat": -38.0055, "lon": -57.5426},
    "Salta": {"lat": -24.7821, "lon": -65.4232},
    "Santa Fe": {"lat": -31.6107, "lon": -60.6973},
    "San Juan": {"lat": -31.5375, "lon": -68.5364},
    "Resistencia": {"lat": -27.4512, "lon": -58.9866},
    "Santiago del Estero": {"lat": -27.7951, "lon": -64.2615},
    "Corrientes": {"lat": -27.4692, "lon": -58.8304},
    "Posadas": {"lat": -27.3621, "lon": -55.9009},
    "San Salvador de Jujuy": {"lat": -24.1858, "lon": -65.2995},
    "Neuquén": {"lat": -38.9516, "lon": -68.0591},
    "Formosa": {"lat": -26.1849, "lon": -58.1731},
    "San Luis": {"lat": -33.3017, "lon": -66.3378},
    "La Rioja": {"lat": -29.4135, "lon": -66.8565},
    "Catamarca": {"lat": -28.4696, "lon": -65.7795},
    "Río Gallegos": {"lat": -51.6230, "lon": -69.2168},
    "Ushuaia": {"lat": -54.8019, "lon": -68.3030},
    "Bahía Blanca": {"lat": -38.7183, "lon": -62.2664},
    "Paraná": {"lat": -31.7333, "lon": -60.5333},
    "Merlo": {"lat": -34.6667, "lon": -58.7333},
    "Godo Cruz": {"lat": -32.8833, "lon": -68.8333},
    "Quilmes": {"lat": -34.7167, "lon": -58.2667},
    "Pilar": {"lat": -34.4589, "lon": -58.9142},
    "San Nicolás": {"lat": -33.3333, "lon": -60.2167},
    "Vicente López": {"lat": -34.5333, "lon": -58.4833},
    "Concordia": {"lat": -31.3925, "lon": -58.0206},
    "San Rafael": {"lat": -34.6175, "lon": -68.3356},
    "Tandil": {"lat": -37.3167, "lon": -59.1333},
    "San Carlos de Bariloche": {"lat": -41.1333, "lon": -71.3000},
    "Comodoro Rivadavia": {"lat": -45.8667, "lon": -67.5000},
    "Río Cuarto": {"lat": -33.1333, "lon": -64.3500},
    "Junín": {"lat": -34.5833, "lon": -60.9500},
    "Zárate": {"lat": -34.1000, "lon": -59.0333},
    "Olavarría": {"lat": -36.9000, "lon": -60.2833},
    "Tres Arroyos": {"lat": -38.3833, "lon": -60.2833},
    "Villa María": {"lat": -32.4167, "lon": -63.2500}

}
