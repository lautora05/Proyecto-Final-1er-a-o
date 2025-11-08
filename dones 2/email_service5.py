import smtplib
from email.message import EmailMessage
from datetime import datetime
from config2 import CONFIG

class EmailService:
    @staticmethod
    def enviar_alerta_incendio(drones_alerta):
        try:
            msg = EmailMessage()
            msg['Subject'] = '🚨 ALERTA DE INCENDIO - Sistema de Monitoreo de Drones'
            msg['From'] = CONFIG['EMAIL_FROM']
            msg['To'] = CONFIG['EMAIL_FROM']
            
            cuerpo = "SE HA DETECTADO UNA SITUACIÓN DE RIESGO EN EL MONITOREO DE INCENDIOS\n\n"
            cuerpo += "Drones en estado de ALERTA:\n"
            
            for dron in drones_alerta:
                cuerpo += f"- {dron['id']} en {dron['ubicacion']}: "
                condiciones = []
                if dron['temperatura'] > CONFIG['UMBRALES_ALERTA']['temperatura_critica']:
                    condiciones.append(f"Temperatura crítica ({dron['temperatura']:.1f}°C)")
                if dron['velocidad_viento'] > CONFIG['UMBRALES_ALERTA']['velocidad_viento_critica']:
                    condiciones.append(f"Viento crítico ({dron['velocidad_viento']:.1f} km/h)")
                cuerpo += ", ".join(condiciones) + "\n"
            
            cuerpo += f"\nHora de detección: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            cuerpo += "\nSe recomienda movilizar recursos adicionales y evaluar evacuaciones preventivas."
            
            msg.set_content(cuerpo)
            
            with smtplib.SMTP(CONFIG['EMAIL_SMTP_SERVER'], CONFIG['EMAIL_SMTP_PORT']) as server:
                server.starttls()
                server.login(CONFIG['EMAIL_FROM'], CONFIG['EMAIL_PASSWORD'])
                server.send_message(msg)
            
            return True
            
        except Exception as e:
            print(f"Error al enviar email: {str(e)}")
            return False
    
    @staticmethod
    def enviar_prueba():
        try:
            msg = EmailMessage()
            msg['Subject'] = 'Prueba del Sistema de Monitoreo de Drones'
            msg['From'] = CONFIG['EMAIL_FROM']
            msg['To'] = CONFIG['EMAIL_FROM']
            msg.set_content("Esta es una prueba del sistema de alertas por correo electrónico.\n\nEl sistema está funcionando correctamente.")
            
            with smtplib.SMTP(CONFIG['EMAIL_SMTP_SERVER'], CONFIG['EMAIL_SMTP_PORT']) as server:
                server.starttls()
                server.login(CONFIG['EMAIL_FROM'], CONFIG['EMAIL_PASSWORD'])
                server.send_message(msg)
            
            return True
            
        except Exception as e:
            print(f"Error al enviar correo de prueba: {str(e)}")
            return False