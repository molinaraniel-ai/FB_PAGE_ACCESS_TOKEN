import os
import requests

PAGE_ID = os.environ.get("FB_PAGE_ID")
ACCESS_TOKEN = os.environ.get("FB_PAGE_ACCESS_TOKEN")
VIDEO_PATH = "resultado_messi.mp4"

def publicar_video():
    url = f"https://graph-video.facebook.com/v26.0/{PAGE_ID}/videos"
    
    if not os.path.exists(VIDEO_PATH):
        print(f"Error: No se encuentra el archivo {VIDEO_PATH}")
        return

    payload = {
        'access_token': ACCESS_TOKEN,
        'description': 'Publicación automática del video de Messi - Trabajo Práctico Grupo 1 EEST N1'
    }
    
    files = {
        'source': open(VIDEO_PATH, 'rb')
    }
    
    print("Subiendo video a Facebook...")
    response = requests.post(url, data=payload, files=files)
    
    print("Respuesta de Facebook:", response.text)
    if response.status_code == 200:
        print("¡Video publicado con éxito en Facebook!")
    else:
        print("Error al publicar el video.")

if __name__ == "__main__":
    publicar_video()
