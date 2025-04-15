import requests


WORKFLOW_URL = "https://prod-145.westeurope.logic.azure.com:443/workflows/5644cb48853244798651ccbcc1f09f6d/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=DxbGXZqEZNUFgL2mniKHUtTJTCoD9dGEJoblXkk0GBE"


data = {"text": "Ahoj, toto je automatická zpráva z Power Automate přes Python! 🚀"}


headers = {"Content-Type": "application/json"}

try:
    
    response = requests.post(WORKFLOW_URL, json=data, headers=headers)

    
    if response.status_code == 200:
        print("✅ Workflow byl úspěšně spuštěn!")
    elif response.status_code == 202:
        print("✅ Požadavek byl přijat, workflow se zpracovává...")
    else:
        print(f"❌ Chyba: {response.status_code}, {response.text}")

except requests.exceptions.RequestException as e:
    print(f"❌ Chyba při odesílání požadavku: {e}")




