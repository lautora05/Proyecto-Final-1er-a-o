from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QGroupBox, QGridLayout, 
                             QLabel, QPushButton, QSpinBox, QHBoxLayout, QMessageBox)
from PyQt5.QtCore import Qt

class ConfigTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.inicializar_ui()
    
    def inicializar_ui(self):
        layout = QVBoxLayout(self)
        
        
        grupo_umbrales = QGroupBox("Umbrales de Alerta")
        layout_umbrales = QGridLayout()
        
        layout_umbrales.addWidget(QLabel("Temperatura Alta (°C):"), 0, 0)
        self.spin_temp_alta = QSpinBox()
        self.spin_temp_alta.setRange(30, 100)
        self.spin_temp_alta.setValue(self.parent.umbrales['temperatura_alta'])
        layout_umbrales.addWidget(self.spin_temp_alta, 0, 1)
        
        layout_umbrales.addWidget(QLabel("Temperatura Crítica (°C):"), 1, 0)
        self.spin_temp_critica = QSpinBox()
        self.spin_temp_critica.setRange(40, 120)
        self.spin_temp_critica.setValue(self.parent.umbrales['temperatura_critica'])
        layout_umbrales.addWidget(self.spin_temp_critica, 1, 1)
        
        layout_umbrales.addWidget(QLabel("Viento Alto (km/h):"), 2, 0)
        self.spin_viento_alto = QSpinBox()
        self.spin_viento_alto.setRange(10, 80)
        self.spin_viento_alto.setValue(self.parent.umbrales['velocidad_viento_alta'])
        layout_umbrales.addWidget(self.spin_viento_alto, 2, 1)
        
        layout_umbrales.addWidget(QLabel("Viento Crítico (km/h):"), 3, 0)
        self.spin_viento_critico = QSpinBox()
        self.spin_viento_critico.setRange(20, 100)
        self.spin_viento_critico.setValue(self.parent.umbrales['velocidad_viento_critica'])
        layout_umbrales.addWidget(self.spin_viento_critico, 3, 1)
        
        grupo_umbrales.setLayout(layout_umbrales)
        layout.addWidget(grupo_umbrales)
        
        
        layout_botones = QHBoxLayout()
        
        boton_simular_alerta = QPushButton("Simular Alerta de Prueba")
        boton_simular_alerta.clicked.connect(self.simular_alerta_prueba)
        layout_botones.addWidget(boton_simular_alerta)
        
        boton_enviar_email = QPushButton("Probar Email")
        boton_enviar_email.clicked.connect(self.probar_email)
        layout_botones.addWidget(boton_enviar_email)
        
        layout.addLayout(layout_botones)
        
        
        grupo_info = QGroupBox("Información del Sistema")
        layout_info = QVBoxLayout()
        
        info = QLabel(
            "Este sistema monitorea incendios forestales utilizando una flota de drones.\n"
            "Los drones recopilan datos de temperatura, velocidad del viento y dirección.\n"
            "El sistema analiza estos datos para predecir el comportamiento del incendio\n"
            "y envía alertas automáticas por correo electrónico cuando se detectan riesgos."
        )
        info.setWordWrap(True)
        info.setStyleSheet("padding: 10px; background-color: #F8F9FA;")
        layout_info.addWidget(info)
        
        grupo_info.setLayout(layout_info)
        layout.addWidget(grupo_info)
    
    def actualizar_umbrales(self):
        self.parent.umbrales = {
            'temperatura_alta': self.spin_temp_alta.value(),
            'temperatura_critica': self.spin_temp_critica.value(),
            'velocidad_viento_alta': self.spin_viento_alto.value(),
            'velocidad_viento_critica': self.spin_viento_critico.value()
        }
        self.parent.registrar_alerta("✓ Umbrales de alerta actualizados")
    
    def simular_alerta_prueba(self):
        self.parent.registrar_alerta("🚨 ALERTA DE PRUEBA: Simulación de condiciones críticas")
        self.parent.registrar_alerta("✓ Sistema de alertas funcionando correctamente")
    
    def probar_email(self):
        if self.parent.email_service.enviar_prueba():
            self.parent.registrar_alerta("✓ Correo de prueba enviado exitosamente")
            QMessageBox.information(self, "Prueba de Email", "Correo de prueba enviado exitosamente")
        else:
            error_msg = "✗ Error al enviar correo de prueba"
            self.parent.registrar_alerta(error_msg)

            QMessageBox.critical(self, "Error", error_msg)
