from PyQt5.QtWidgets import (QWidget, QGridLayout, QGroupBox, QVBoxLayout, 
                             QHBoxLayout, QLabel, QTextEdit, QPushButton, 
                             QTableWidget, QTableWidgetItem, QHeaderView)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt


class MonitoringTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.parent = parent
   
        self.inicializar_ui()
    
    def inicializar_ui(self):
        layout = QGridLayout(self)
        
        
        grupo_estado = QGroupBox("Estado General del Incendio")
        layout_estado = QVBoxLayout()
        
        self.etiqueta_riesgo = QLabel("NIVEL DE RIESGO: MEDIO")
        self.etiqueta_riesgo.setFont(QFont("Arial", 14, QFont.Bold))
        self.etiqueta_riesgo.setStyleSheet("color: #FFA500; background-color: #FFF3CD; padding: 10px; border: 1px solid #FFA500;")
        self.etiqueta_riesgo.setAlignment(Qt.AlignCenter)
        layout_estado.addWidget(self.etiqueta_riesgo)
        
        layout_metricas = QHBoxLayout()
        self.metrica_temp = QLabel("Temperatura Máxima: --°C")
        self.metrica_viento = QLabel("Viento Máximo: -- km/h")
        self.metrica_area = QLabel("Área Afectada: -- ha")
        self.metrica_drones_activos = QLabel("Drones Activos: --/--")
        
        for metrica in [self.metrica_temp, self.metrica_viento, self.metrica_area, self.metrica_drones_activos]:
            metrica.setStyleSheet("font-size: 12px; padding: 5px;")
            layout_metricas.addWidget(metrica)
        
        layout_estado.addLayout(layout_metricas)
        grupo_estado.setLayout(layout_estado)
        layout.addWidget(grupo_estado, 0, 0, 1, 2)
        
        
        grupo_drones = self.crear_grupo_drones()
        layout.addWidget(grupo_drones, 1, 0, 1, 2)
        
        
        grupo_alertas = self.crear_grupo_alertas()
        layout.addWidget(grupo_alertas, 2, 0, 1, 2)
        
        
        grupo_prediccion = self.crear_grupo_prediccion()
        layout.addWidget(grupo_prediccion, 3, 0, 1, 2)
    
    def crear_grupo_drones(self):
        grupo = QGroupBox("Flota de Drones")
        layout = QVBoxLayout()
        
        layout_botones = QHBoxLayout()
        btn_actualizar = QPushButton("Actualizar Datos")
        btn_actualizar.clicked.connect(self.parent.actualizar_datos_tiempo_real)
        btn_agregar = QPushButton("Agregar Nuevo Dron")
        btn_agregar.clicked.connect(self.parent.agregar_nuevo_dron)
        
        layout_botones.addWidget(btn_actualizar)
        layout_botones.addWidget(btn_agregar)
        layout.addLayout(layout_botones)
        
        self.tabla_drones = QTableWidget()
        self.tabla_drones.setColumnCount(6)
        self.tabla_drones.setHorizontalHeaderLabels(["ID Dron", "Ubicación", "Temperatura (°C)", "Viento (km/h)", "Dirección Viento", "Estado"])
        self.tabla_drones.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.tabla_drones)
        
        grupo.setLayout(layout)
        return grupo
    
    def crear_grupo_alertas(self):
        grupo = QGroupBox("Alertas y Notificaciones")
        layout = QVBoxLayout()
        self.registro_alertas = QTextEdit()
        self.registro_alertas.setReadOnly(True)
        self.registro_alertas.setMaximumHeight(200)
        layout.addWidget(self.registro_alertas)
        grupo.setLayout(layout)
        return grupo
    
    def crear_grupo_prediccion(self):
        grupo = QGroupBox("Predicción de Comportamiento del Incendio")
        layout = QVBoxLayout()
        self.etiqueta_prediccion = QLabel("El incendio se espera que se expanda hacia el NORTE en las próximas 2 horas debido a vientos favorables.")
        self.etiqueta_prediccion.setWordWrap(True)
        self.etiqueta_prediccion.setStyleSheet("padding: 10px; background-color: #E8F4FD; border: 1px solid #B8D4E8;")
        layout.addWidget(self.etiqueta_prediccion)
        grupo.setLayout(layout)
        return grupo
    
    def actualizar_tabla_drones(self, drones):
        self.tabla_drones.setRowCount(len(drones))
        
        for fila, dron in enumerate(drones):
            self.tabla_drones.setItem(fila, 0, QTableWidgetItem(dron['id']))
            self.tabla_drones.setItem(fila, 1, QTableWidgetItem(dron['ubicacion']))
            
            item_temp = QTableWidgetItem(f"{dron['temperatura']:.1f}")
            if dron['temperatura'] > self.parent.umbrales['temperatura_critica']:
                item_temp.setBackground(QColor(220, 53, 69))
            elif dron['temperatura'] > self.parent.umbrales['temperatura_alta']:
                item_temp.setBackground(QColor(255, 193, 7))
            self.tabla_drones.setItem(fila, 2, item_temp)
            
            item_viento = QTableWidgetItem(f"{dron['velocidad_viento']:.1f}")
            if dron['velocidad_viento'] > self.parent.umbrales['velocidad_viento_critica']:
                item_viento.setBackground(QColor(220, 53, 69))
            elif dron['velocidad_viento'] > self.parent.umbrales['velocidad_viento_alta']:
                item_viento.setBackground(QColor(255, 193, 7))
            self.tabla_drones.setItem(fila, 3, item_viento)
            
            self.tabla_drones.setItem(fila, 4, QTableWidgetItem(dron['direccion_viento']))
            item_estado = QTableWidgetItem(dron['estado'])
            if dron['estado'] == "ALERTA":
                item_estado.setBackground(QColor(220, 53, 69))
            elif dron['estado'] == "ADVERTENCIA":
                item_estado.setBackground(QColor(255, 193, 7))
            self.tabla_drones.setItem(fila, 5, item_estado)