Adventure Works - Progetto Completo di Data Engineering, Data Analysis, Machine Learning, Forecasting & AI
Benvenuti! Questo repository contiene un progetto end-to-end che integra Data Engineering, Data Analysis, Machine Learning, Forecasting e AI, applicato ai dati aziendali di Adventure Works.

🚀 Obiettivi del Progetto
Questo progetto dimostra come:

Unire dati provenienti da più file Excel (📊 Data Engineering).
Analizzare tali dati (Exploratory Data Analysis, KPI, outlier).
Prevedere le vendite (Machine Learning trimestrale con RandomForest/XGBoost, Forecasting con ARIMA e Prophet).
Integrare un'AI locale (FastAPI + Hugging Face) per sentiment analysis e raccomandazioni storiche.
Realizzare una sezione avanzata di analisi AI, che fornisce:
Stato attuale e storico 📈
Previsioni per i prossimi 4 trimestri 📊
Azioni alternative per migliorare margini, vendite, brand awareness e customer satisfaction 💡
Il tutto per fornire un framework di analisi dati utile a colleghi, recruiter e appassionati. 🔍

⚙️ Setup & Requisiti
Per eseguire il progetto, assicurati di avere:

Un ambiente Python 3.8+ (es. venv_new) con i seguenti pacchetti:

pip install pandas numpy matplotlib seaborn plotly scikit-learn xgboost statsmodels prophet \
            transformers torch fastapi uvicorn pydantic

I seguenti file nella stessa cartella del notebook:
Products.xlsx, Region.xlsx, Sales.xlsx, Salesperson.xlsx
AdventureWorksLogo.png

Esegui tutte le celle del notebook in ordine.
Quando verrà generato local_ai_api.py, avvialo in un altro terminale:


uvicorn local_ai_api:app --host 0.0.0.0 --port 8000 --reload

Per testare le chiamate API, puoi usare:
Uno script Python (test_api.py)

📌 Struttura del Progetto
Il notebook guida l'utente attraverso i seguenti step:

🔹 1. Data Engineering
Caricamento dei 4 file Excel (Sales, Products, Region, Salesperson).
Conversione della data OrderDate, creazione delle colonne Year, Quarter.
Merge delle tabelle per ottenere un dataset completo (sales_merged).
Calcolo di Profit, Profit Margin e identificazione degli outlier.
🔹 2. Data Analysis (EDA)
Statistiche descrittive e distribuzioni 📊
KPI globali: vendite totali, costi, profitti, margine medio.
Analisi delle vendite per Paese, Categoria, Venditori.
Visualizzazioni interattive con seaborn e plotly.
🔹 3. Machine Learning (Previsione Trimestrale)
Creazione dataset trimestrale (Year, Quarter, Total Sales).
Aggiunta di Lag1 per catturare il valore del trimestre precedente.
Training di RandomForestRegressor e XGBoostRegressor.
Valutazione dei modelli tramite MSE, MAE, R².
Confronto previsioni vs. valori reali con grafici.
🔹 4. Time Series Forecasting
ARIMA su base mensile.
Prophet su base trimestrale.
Previsione dell’andamento delle vendite per i prossimi 4 trimestri.
🔹 5. Creazione di un'API AI Locale con FastAPI
L'API fornisce due endpoint:

POST /predict → Sentiment analysis su testo 📢
GET /deep_analysis → Lettura dei dati storici e raccomandazioni.
Esempi di chiamata:


# Controllo dello stato
curl http://127.0.0.1:8000/

# Sentiment Analysis
curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"text":"Amo i prodotti Adventure Works!"}'

# Analisi avanzata
curl http://127.0.0.1:8000/deep_analysis

🔹 6. Analisi AI Avanzata (Previsioni & Azioni Alternative)
Scenario Baseline (Prophet su dati trimestrali)
Scenario +10% (Simulazione di azioni su marketing e customer satisfaction)
Testo descrittivo dettagliato su trend, margini, vendite e azioni da intraprendere.
Grafico comparativo tra le due previsioni.
📊 Risultati & Conclusioni
Questo progetto dimostra un flusso completo di analisi dati che combina: ✅ Data Engineering per strutturare il dataset
✅ Data Analysis per ottenere insight dai dati
✅ Machine Learning per previsioni a breve termine
✅ Forecasting per proiezioni a lungo termine
✅ AI & Automazione per sentiment analysis e raccomandazioni

Il tutto in un unico progetto integrato. 🧠📈

⚡ Raffaele Schiavone
📍 Data Scientist & Data Analyst | Business Intelligence & Automation Expert

📌 Repository: AdventureWorks_AI_8
🌎 Connettiti con me su LinkedIn: Raffaele Schiavone

🚀 Se ti piace il progetto, lascia una ⭐ su GitHub! 🚀

📥 Contribuisci!
Se vuoi migliorare questo progetto o aggiungere nuove funzionalità, forka il repository e proponi una pull request! 🚀
