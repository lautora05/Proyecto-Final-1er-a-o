import sys
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QLabel, QTabWidget, QMessageBox, QInputDialog)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont

from config2 import CONFIG, UMBRALES_ALERTA, CIUDADES_ARGENTINA
from drone_model3 import Drone
from weather_service4 import WeatherService
from email_service5 import EmailService
from alert_service6 import AlertService
from monitoring_tab7 import MonitoringTab
from config_tab8 import ConfigTab
from control_tab9 import ControlTab

class VentanaMonitoreoDrones(QMainWindow):
    def __init__(self):
        super().__init__()
        self.drones = []
        self.umbrales = UMBRALES_ALERTA.copy()
        self.weather_service = WeatherService()
        self.email_service = EmailService()
        self.alert_service = AlertService()
        
        self.inicializar_interfaz()
        self.inicializar_temporizador()
    
    def inicializar_interfaz(self):
        self.setWindowTitle("Sistema de Monitoreo de Drones - Cuerpo de Bomberos")
        self.setGeometry(100, 100, 1200, 800)
        
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        layout_principal = QVBoxLayout(widget_central)
        
        
        titulo = QLabel("CENTRO DE CONTROL DE DRONES - MONITOREO DE INCENDIOS")
        titulo.setFont(QFont("Arial", 16, QFont.Bold))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("background-color: #2E4057; color: white; padding: 10px;")
        layout_principal.addWidget(titulo)
        
        
        self.tabs = QTabWidget()
        layout_principal.addWidget(self.tabs)
        
        self.monitoring_tab = MonitoringTab(self)
        self.config_tab = ConfigTab(self)
        self.control_tab = ControlTab(self)
        
        self.tabs.addTab(self.monitoring_tab, "Monitoreo en Tiempo Real")
        self.tabs.addTab(self.config_tab, "Configuración")
        self.tabs.addTab(self.control_tab, "Control de Drones")
    
    def inicializar_temporizador(self):
        self.temporizador = QTimer()
        self.temporizador.timeout.connect(self.actualizar_datos_tiempo_real)
        self.temporizador.start(5000)
    
    def agregar_nuevo_dron(self):
        ciudad, ok = QInputDialog.getItem(self, 
                                         'Nuevo Dron - Seleccionar Ciudad', 
                                         'Seleccione una ciudad de Argentina:',
                                         CIUDADES_ARGENTINA, 
                                         0, 
                                         False)
        
        if ok and ciudad:
            if any(dron['ubicacion'].lower() == ciudad.lower() for dron in self.drones):
                QMessageBox.warning(self, "Ubicación duplicada", 
                                  f"Ya existe un dron monitoreando la ciudad de {ciudad}.\n"
                                  "Por favor seleccione una ciudad diferente.")
                return
            
            datos_clima = self.weather_service.obtener_datos_climaticos(ciudad)
            
            if datos_clima:
                temperatura = datos_clima.get("temperatura", random.uniform(30, 70))
                viento = datos_clima.get("viento", random.uniform(10, 50))
                direccion = datos_clima.get("direccion", random.choice(["N", "S", "E", "O", "NE", "NO", "SE", "SO"]))
            else:
                temperatura = random.uniform(30, 70)
                viento = random.uniform(10, 50)
                direccion = random.choice(["N", "S", "E", "O", "NE", "NO", "SE", "SO"])
            
            coordenadas = self.weather_service.obtener_coordenadas(ciudad)
            
            nuevo_dron = {
                'id': f"DRONE-{len(self.drones)+1:02d}",
                'ubicacion': ciudad,
                'lat': coordenadas['lat'],
                'lon': coordenadas['lon'],
                'temperatura': temperatura,
                'velocidad_viento': viento,
                'direccion_viento': direccion,
                'estado': "ACTIVO"
            }
            
            self.drones.append(nuevo_dron)
            self.actualizar_tabla_drones()
            self.control_tab.actualizar_combo_drones()
            self.registrar_alerta(f"✓ Nuevo dron agregado: {nuevo_dron['id']} en {ciudad}")
    
    def actualizar_datos_tiempo_real(self):
        for dron in self.drones:
            dron['temperatura'] += random.uniform(-2, 3)
            dron['temperatura'] = max(20, min(100, dron['temperatura']))
            
            dron['velocidad_viento'] += random.uniform(-3, 4)
            dron['velocidad_viento'] = max(5, min(80, dron['velocidad_viento']))
            
            if random.random() < 0.2:
                dron['direccion_viento'] = random.choice(["N", "S", "E", "O", "NE", "NO", "SE", "SO"])
            
            dron['lat'] += random.uniform(-0.01, 0.01)
            dron['lon'] += random.uniform(-0.01, 0.01)
        
        self.actualizar_tabla_drones()
        self.actualizar_metricas_generales()
        self.analizar_riesgos()
        self.generar_prediccion()
        self.control_tab.actualizar_combo_drones()
    
    def actualizar_tabla_drones(self):
        self.monitoring_tab.actualizar_tabla_drones(self.drones)
    
    def actualizar_metricas_generales(self):
        if not self.drones:
            return
            
        temperaturas = [dron['temperatura'] for dron in self.drones]
        vientos = [dron['velocidad_viento'] for dron in self.drones]
        estados = [dron['estado'] for dron in self.drones]
        
        temp_max = max(temperaturas)
        viento_max = max(vientos)
        area_estimada = len(self.drones) * 3.8
        drones_activos = sum(1 for estado in estados if estado == "ACTIVO")
        
        self.monitoring_tab.metrica_temp.setText(f"Temperatura Máxima: {temp_max:.1f}°C")
        self.monitoring_tab.metrica_viento.setText(f"Viento Máximo: {viento_max:.1f} km/h")
        self.monitoring_tab.metrica_area.setText(f"Área Afectada: {area_estimada:.1f} ha")
        self.monitoring_tab.metrica_drones_activos.setText(f"Drones Activos: {drones_activos}/{len(self.drones)}")
    
    def analizar_riesgos(self):
        alertas_detectadas = False
        drones_alerta = []
        
        for dron in self.drones:
            alertas_dron = self.alert_service.analizar_riesgos_dron(dron)
            
            if alertas_dron:
                mensaje_alerta = f"ALERTA en {dron['id']} ({dron['ubicacion']}): " + ", ".join(alertas_dron)
                self.registrar_alerta(mensaje_alerta)
                alertas_detectadas = True
                if dron['estado'] == "ALERTA":
                    drones_alerta.append(dron)
        
        nivel_riesgo, estilo = self.alert_service.determinar_nivel_riesgo(self.drones)
        self.monitoring_tab.etiqueta_riesgo.setText(f"NIVEL DE RIESGO: {nivel_riesgo}")
        self.monitoring_tab.etiqueta_riesgo.setStyleSheet(estilo)
        
        if alertas_detectadas and drones_alerta:
            self.email_service.enviar_alerta_incendio(drones_alerta)
            self.registrar_alerta("✓ Alerta enviada por correo electrónico")
    
    def generar_prediccion(self):
        if not self.drones:
            return
            
        direcciones = [dron['direccion_viento'] for dron in self.drones]
        direccion_predominante = max(set(direcciones), key=direcciones.count)
        
        temp_promedio = sum(dron['temperatura'] for dron in self.drones) / len(self.drones)
        
        if temp_promedio > 60:
            severidad = "severo"
        elif temp_promedio > 45:
            severidad = "alto"
        else:
            severidad = "moderado"
        
        prediccion = f"El incendio muestra comportamiento {severidad} y se espera que se expanda hacia el {direccion_predominante} en las próximas 2 horas debido a vientos favorables."
        self.monitoring_tab.etiqueta_prediccion.setText(prediccion)
    
    def registrar_alerta(self, mensaje):
        alertas_actualizadas = self.alert_service.registrar_alerta(mensaje)
        self.monitoring_tab.registro_alertas.clear()
        self.monitoring_tab.registro_alertas.append("\n".join(alertas_actualizadas))