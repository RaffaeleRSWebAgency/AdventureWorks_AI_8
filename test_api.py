# test_api.py

"""
Questo script Python effettua tre chiamate HTTP alla nostra AI locale basata su FastAPI.
Deve essere eseguito in un ambiente in cui sia installata la libreria 'requests'.
Assicurarsi che il server FastAPI sia già avviato con:
uvicorn local_ai_api:app --host 0.0.0.0 --port 8000 --reload

Funzionalità testate:
1) GET /             -> Verifica che l'API risponda e restituisca un messaggio iniziale.
2) POST /predict     -> Invia un testo per l'analisi di sentiment.
3) GET /deep_analysis -> Esegue l'analisi storica su sales_merged.csv e fornisce raccomandazioni.

Esecuzione dallo stesso prompt (cmd) o terminale:
python test_api.py
"""

import requests

def main():
    # Indirizzo di base del server FastAPI locale
    base_url = "http://127.0.0.1:8000"

    print("=== 1) GET / ===")
    try:
        resp_root = requests.get(base_url)
        print("Status:", resp_root.status_code)
        print("Risposta:", resp_root.json())
    except requests.exceptions.ConnectionError as e:
        print("[ERRORE] Impossibile connettersi all'API. Assicurarsi che il server sia avviato.")
        return

    print("\n=== 2) POST /predict ===")
    payload = {"text": "Amo i prodotti AW!"}  # Test di sentiment
    try:
        resp_predict = requests.post(f"{base_url}/predict", json=payload)
        print("Status:", resp_predict.status_code)
        print("Risposta:", resp_predict.json())
    except requests.exceptions.ConnectionError as e:
        print("[ERRORE] Impossibile connettersi all'API. Assicurarsi che il server sia avviato.")
        return

    print("\n=== 3) GET /deep_analysis ===")
    try:
        resp_deep = requests.get(f"{base_url}/deep_analysis")
        print("Status:", resp_deep.status_code)
        print("Risposta:", resp_deep.json())
    except requests.exceptions.ConnectionError as e:
        print("[ERRORE] Impossibile connettersi all'API. Assicurarsi che il server sia avviato.")
        return

if __name__ == "__main__":
    main()
