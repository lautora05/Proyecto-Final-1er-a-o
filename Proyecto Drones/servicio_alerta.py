from PyQt5.QtCore import QDateTime
from configuracion import UMBRALES_ALERTA

class AlertService:
    def __init__(self):
        self.historial_alertas = []
    
    def registrar_alerta(self, mensaje):
        timestamp = QDateTime.currentDateTime().toString("hh:mm:ss")
        alerta = f"[{timestamp}] {mensaje}"
        self.historial_alertas.append(alerta)
        
        if len(self.historial_alertas) > 50:
            self.historial_alertas.pop(0)
        
        return self.historial_alertas[-10:]  
    
    def analizar_riesgos_dron(self, dron):
        alertas_dron = []
        
        if dron['temperatura'] > UMBRALES_ALERTA['temperatura_critica']:
            alertas_dron.append(f"Temperatura CRÍTICA: {dron['temperatura']:.1f}°C")
            dron['estado'] = "ALERTA"
        elif dron['temperatura'] > UMBRALES_ALERTA['temperatura_alta']:
            alertas_dron.append(f"Temperatura ALTA: {dron['temperatura']:.1f}°C")
            dron['estado'] = "ADVERTENCIA"
        
        if dron['velocidad_viento'] > UMBRALES_ALERTA['velocidad_viento_critica']:
            alertas_dron.append(f"Viento CRÍTICO: {dron['velocidad_viento']:.1f} km/h")
            dron['estado'] = "ALERTA"
        elif dron['velocidad_viento'] > UMBRALES_ALERTA['velocidad_viento_alta']:
            alertas_dron.append(f"Viento ALTO: {dron['velocidad_viento']:.1f} km/h")
            dron['estado'] = "ADVERTENCIA"
        
        if not alertas_dron and dron['estado'] != "ACTIVO":
            dron['estado'] = "ACTIVO"
        
        return alertas_dron
    
    def determinar_nivel_riesgo(self, drones):
        if any(dron['estado'] == "ALERTA" for dron in drones):
            return "ALTO", "color: #DC3545; background-color: #F8D7DA; padding: 10px; border: 1px solid #DC3545;"
        elif any(dron['estado'] == "ADVERTENCIA" for dron in drones):
            return "MEDIO", "color: #FFA500; background-color: #FFF3CD; padding: 10px; border: 1px solid #FFA500;"
        else:
            return "BAJO", "color: #28A745; background-color: #D4EDDA; padding: 10px; border: 1px solid #28A745;"