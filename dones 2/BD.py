import mysql.connector
import csv
import os
from tabulate import tabulate
class DatabaseProvincias:
    def __init__(self):
        self.connection = None
        self.cursor = None
    
    def connect(self, host='localhost', user='root', password='sharktopus12', database='provincias_db'):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor()
            print("✅ Conexión exitosa a la base de datos")
            return True
        except mysql.connector.Error as err:
            print(f"❌ Error de conexión: {err}")
            return False
    
    def create_database(self):
        try:
            temp_conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='sharktopus12'
            )
            temp_cursor = temp_conn.cursor()
            temp_cursor.execute("CREATE DATABASE IF NOT EXISTS provincias_db")
            print("✅ Base de datos 'provincias_db' creada/existe")
            temp_cursor.close()
            temp_conn.close()
            return True
        except mysql.connector.Error as err:
            print(f"❌ Error creando base de datos: {err}")
            return False
    
    def create_table(self):
        try:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS provincias (
                id INT AUTO_INCREMENT PRIMARY KEY,
                ciudad VARCHAR(100) NOT NULL UNIQUE,
                latitud DECIMAL(10,6) NOT NULL,
                longitud DECIMAL(10,6) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            self.cursor.execute(create_table_query)
            self.connection.commit()
            print("✅ Tabla 'provincias' creada/existe")
            return True
        except mysql.connector.Error as err:
            print(f"❌ Error creando tabla: {err}")
            return False
    
    def insert_provincias_directo(self):
        
        PROVINCIAS_DATA = {
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
        
        try:
            inserted_count = 0
            for nombre, coordenadas in PROVINCIAS_DATA.items():
                insert_query = """
                INSERT IGNORE INTO provincias (nombre, latitud, longitud)
                VALUES (%s, %s, %s)
                """
                self.cursor.execute(insert_query, (
                    nombre,
                    coordenadas['lat'],
                    coordenadas['lon']
                ))
                inserted_count += 1
            
            self.connection.commit()
            print(f"✅ Datos insertados directamente: {inserted_count} provincias/ciudades")
            return True
                
        except Exception as e:
            print(f"❌ Error insertando datos: {e}")
            return False
    
    def get_all_provincias(self):
       
        try:
            self.cursor.execute("SELECT id, nombre, latitud, longitud FROM provincias ORDER BY id")
            provincias = self.cursor.fetchall()
            
            
            headers = ["ID", "Nombre", "Latitud", "Longitud"]
            table_data = []
            
            for provincia in provincias:
                table_data.append([
                    provincia[0],
                    provincia[1],
                    f"{provincia[2]:.4f}",
                    f"{provincia[3]:.4f}"
                ])
            
            print("\n🏛️  TABLA DE PROVINCIAS/CIUDADES")
            print("=" * 80)
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
            print(f"\nTotal: {len(provincias)} registros")
            
            return provincias
        except mysql.connector.Error as err:
            print(f"❌ Error obteniendo provincias: {err}")
            return []
    
    def search_by_name(self, ciudad):
        
        try:
            query = "SELECT id, ciudad, latitud, longitud FROM provincias WHERE nombre LIKE %s ORDER BY id"
            self.cursor.execute(query, (f'%{ciudad}%',))
            resultados = self.cursor.fetchall()
            
            if resultados:
                headers = ["ID", "Nombre", "Latitud", "Longitud"]
                table_data = []
                
                for resultado in resultados:
                    table_data.append([
                        resultado[0],
                        resultado[1],
                        f"{resultado[2]:.4f}",
                        f"{resultado[3]:.4f}"
                    ])
                
                print(f"\n🔍 RESULTADOS PARA: '{ciudad}'")
                print("=" * 60)
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
            else:
                print(f"\n❌ No se encontraron resultados para '{ciudad}'")
            
            return resultados
        except mysql.connector.Error as err:
            print(f"❌ Error en búsqueda: {err}")
            return []
    
    def get_total_count(self):
        
        try:
            self.cursor.execute("SELECT COUNT(*) FROM provincias")
            count = self.cursor.fetchone()[0]
            print(f"\n📊 Total de provincias/ciudades en la base de datos: {count}")
            return count
        except mysql.connector.Error as err:
            print(f"❌ Error obteniendo conteo: {err}")
            return 0
    
    def close(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print("✅ Conexión cerrada")


def main():
    db = DatabaseProvincias()
    
    try:
        
        if not db.create_database():
            return
        
       
        if not db.connect():
            return
        
       
        if not db.create_table():
            return
        
        
        if not db.insert_provincias_directo():
            return
        
        
        db.get_total_count()
        
        
        db.get_all_provincias()
        
        
    finally:
        db.close()

if __name__ == "__main__":
    main()