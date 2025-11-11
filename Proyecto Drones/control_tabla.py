from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QGroupBox, QGridLayout, 
                             QLabel, QPushButton, QComboBox,QHBoxLayout)
from PyQt5.QtCore import Qt
import random

class ControlTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.inicializar_ui()
    
    def inicializar_ui(self):
        layout = QVBoxLayout(self)
        
       
        grupo_info = QGroupBox("Información de Drones")
        layout_info = QGridLayout()
        
        layout_info.addWidget(QLabel("Seleccionar Dron:"), 0, 0)
        self.combo_drones = QComboBox()
        self.combo_drones.currentTextChanged.connect(self.actualizar_info_dron)
        layout_info.addWidget(self.combo_drones, 0, 1)
        
        self.info_dron = QLabel("Selecciona un dron para ver información detallada")
        self.info_dron.setStyleSheet("padding: 10px; background-color: #E8F4FD; border: 1px solid #B8D4E8;")
        self.info_dron.setWordWrap(True)
        layout_info.addWidget(self.info_dron, 1, 0, 1, 2)
        
        grupo_info.setLayout(layout_info)
        layout.addWidget(grupo_info)
        
        
        grupo_acciones = QGroupBox("Acciones Masivas")
        layout_acciones = QHBoxLayout()
        
        btn_normalizar_temp = QPushButton("Normalizar Temperaturas")
        btn_normalizar_temp.clicked.connect(self.normalizar_temperaturas)
        layout_acciones.addWidget(btn_normalizar_temp)
        
        btn_reiniciar_estados = QPushButton("Reiniciar Estados")
        btn_reiniciar_estados.clicked.connect(self.reiniciar_estados_drones)
        layout_acciones.addWidget(btn_reiniciar_estados)
        
        btn_simular_mejora = QPushButton("Simular Mejora Condiciones")
        btn_simular_mejora.clicked.connect(self.simular_mejora_condiciones)
        layout_acciones.addWidget(btn_simular_mejora)
        
        grupo_acciones.setLayout(layout_acciones)
        layout.addWidget(grupo_acciones)
    
    def actualizar_combo_drones(self):
        self.combo_drones.clear()
        for dron in self.parent.drones:
            self.combo_drones.addItem(f"{dron['id']} - {dron['ubicacion']}", dron)
    
    def actualizar_info_dron(self):
        current_data = self.combo_drones.currentData()
        if current_data:
            dron = current_data
            info = f"""
            <b>{dron['id']}</b> - {dron['ubicacion']}<br>
            <b>Temperatura:</b> {dron['temperatura']:.1f}°C<br>
            <b>Viento:</b> {dron['velocidad_viento']:.1f} km/h - {dron['direccion_viento']}<br>
            <b>Estado:</b> {dron['estado']}
            """
            self.info_dron.setText(info)
    
    def normalizar_temperaturas(self):
        for dron in self.parent.drones:
            dron['temperatura'] = max(25, dron['temperatura'] * 0.7)
            dron['velocidad_viento'] = max(5, dron['velocidad_viento'] * 0.8)
        
        self.parent.actualizar_tabla_drones()
        self.actualizar_combo_drones()
        self.parent.registrar_alerta("✓ Temperaturas y vientos normalizados en toda la flota")
    
    def reiniciar_estados_drones(self):
        for dron in self.parent.drones:
            dron['estado'] = "ACTIVO"
        
        self.parent.actualizar_tabla_drones()
        self.actualizar_combo_drones()
        self.parent.registrar_alerta("✓ Estados de todos los drones reiniciados a ACTIVO")
    
    def simular_mejora_condiciones(self):
        for dron in self.parent.drones:
            dron['temperatura'] = random.uniform(25, 40)
            dron['velocidad_viento'] = random.uniform(5, 15)
            dron['estado'] = "ACTIVO"
        
        self.parent.actualizar_tabla_drones()
        self.actualizar_combo_drones()
        self.parent.registrar_alerta("✓ Condiciones simuladas mejoradas en toda la flota")