{
  "filename": "README.json",
  "content": {
    "title": "Adventure Works – Complete Data and AI Pipeline",
    "description": "Questo repository dimostra un flusso end-to-end che integra Data Engineering, Data Analysis, Machine Learning e un’AI locale basata su FastAPI e Hugging Face. I dati provengono da quattro file Excel (Sales, Products, Region, Salesperson) e vengono uniti, puliti ed arricchiti per calcolare KPI, identificare outlier e prevedere le vendite trimestrali. Una sezione finale avanzata mostra un confronto tra lo scenario baseline e uno scenario con azioni (+10% vendite), illustrando in dettaglio le strategie per migliorare margini, brand awareness e soddisfazione clienti.",
    "structure": [
      {
        "section": "Contenuti Principali",
        "details": [
          "AdventureWorks_Complete.ipynb: Notebook principale (Data Engineering, EDA, ML, Forecasting, Sezione Avanzata)",
          "local_ai_api.py: Server FastAPI (POST /predict per sentiment, GET /deep_analysis per raccomandazioni su trend)",
          "Products.xlsx, Region.xlsx, Sales.xlsx, Salesperson.xlsx: File Excel originali",
          "AdventureWorksLogo.png: Logo aziendale",
          "sales_merged.csv: Dataset unificato generato dal notebook"
        ]
      },
      {
        "section": "Requisiti",
        "details": [
          "Python 3.8+",
          "Librerie: pandas, numpy, matplotlib, seaborn, plotly, scikit-learn, xgboost, statsmodels, prophet, transformers, torch, fastapi, uvicorn, pydantic"
        ]
      },
      {
        "section": "Istruzioni di Esecuzione",
        "details": [
          "Aprire il file .ipynb con Jupyter Notebook/Lab",
          "Eseguire le celle in ordine (verranno generati sales_merged.csv e local_ai_api.py)",
          "In un secondo terminale, lanciare: uvicorn local_ai_api:app --host 0.0.0.0 --port 8000 --reload",
          "Testare: GET / (status), POST /predict (sentiment), GET /deep_analysis (raccomandazioni storiche)"
        ]
      },
      {
        "section": "Sezione Avanzata",
        "details": [
          "Utilizza Prophet per generare uno scenario baseline e uno scenario +10% vendite",
          "Confronto grafico dei due scenari sui prossimi 4 trimestri",
          "Analisi testuale di come aumentare margini, brand awareness e soddisfazione clienti",
          "Tempistiche stimate per consolidare i benefici"
        ]
      },
      {
        "section": "Come Caricare su GitHub",
        "details": [
          "Creare un nuovo repository su GitHub",
          "Inizializzare Git nella cartella locale (git init, git add ., git commit -m ...)",
          "git remote add origin https://github.com/<USERNAME>/<REPO>.git",
          "git push -u origin main",
          "Verificare che notebook, file Excel, local_ai_api.py e README siano presenti"
        ]
      },
      {
        "section": "Autore",
        "details": [
          "Raffaele Schiavone - Data Scientist & Data Analyst | Business Intelligence & Automation Expert"
        ]
      }
    ],
    "closing": "Questo progetto dimostra come unire Data Engineering, Analysis, ML e AI locale in un’unica pipeline, fornendo analisi predittive avanzate e raccomandazioni strategiche per Adventure Works."
  }
}
