import requests

class InterfazApiBodega:
    def obtenerActualizacionesVinos(self, bodega):
        url = f"https://apiBodegas.com/vinos?bodega={bodega}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
