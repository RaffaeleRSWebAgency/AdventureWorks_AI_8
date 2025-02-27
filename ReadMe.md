# Adventure Works - Progetto Completo di Data Engineering, Data Analysis, Machine Learning, Forecasting & AI

Mi chiamo **Raffaele Schiavone** e in questo repository metto a disposizione un progetto end-to-end che integra Data Engineering, Data Analysis, Machine Learning, Time Series Forecasting e AI. L'obiettivo è mostrare come unire, analizzare e prevedere i dati, fornendo anche un'API locale per l'analisi del sentiment e per raccomandazioni basate sui dati storici.

---

## Indice

- [Descrizione](#descrizione)
- [Requisiti e Setup](#requisiti-e-setup)
- [Data Engineering](#data-engineering)
- [Data Analysis (EDA)](#data-analysis-eda)
- [Machine Learning e Forecasting](#machine-learning-e-forecasting)
- [API AI Locale](#api-ai-locale)
- [Analisi Avanzata](#analisi-avanzata)
- [Conclusioni](#conclusioni)
- [Contatti](#contatti)

---

## Descrizione

Questo progetto dimostra come:
- **Unire** dati provenienti da più file Excel.
- **Analizzare** i dati per estrarre KPI, individuare outlier e comprendere le tendenze.
- **Prevedere** l’andamento delle vendite mediante modelli di Machine Learning (RandomForest e XGBoost) e tecniche di Time Series Forecasting (ARIMA e Prophet).
- **Integrare** un'API AI locale con FastAPI e Hugging Face per effettuare analisi di sentiment e fornire raccomandazioni basate sui trend storici.
- **Confrontare** scenari futuri, evidenziando l'effetto di possibili azioni strategiche (es. aumento del 10% nelle vendite).

---

## Requisiti e Setup

### Requisiti

- **Python 3.8+** (si consiglia l'uso di un ambiente virtuale)
- Le seguenti librerie Python:
  - `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`
  - `scikit-learn`, `xgboost`
  - `statsmodels`, `prophet`
  - `transformers`, `torch`
  - `fastapi`, `uvicorn`, `pydantic`

### File Necessari

Assicurarsi di avere i seguenti file nella **stessa cartella** del notebook:
- `Products.xlsx`
- `Region.xlsx`
- `Sales.xlsx`
- `Salesperson.xlsx`
- `AdventureWorksLogo.png`

### Installazione delle Librerie

Utilizzare il seguente comando per installare tutte le dipendenze:
```bash
pip install pandas numpy matplotlib seaborn plotly scikit-learn xgboost statsmodels prophet transformers torch fastapi uvicorn pydantic
Data Engineering
In questa fase vengono:

Caricati i file Excel.
Convertita la colonna OrderDate in formato datetime, con creazione di nuove colonne (Year e Quarter).
Unite le tabelle per ottenere il dataframe sales_merged.
Calcolato il Profit e il Profit Margin.
Individuati gli outlier in Total Sales.
Data Analysis (EDA)
Si eseguono analisi esplorative dei dati per:

Calcolare statistiche descrittive e KPI globali (es. Vendite Totali, Costo Totale, Profitto Totale, Margine Medio).
Visualizzare la distribuzione dei dati con istogrammi e boxplot.
Analizzare le vendite per dimensioni quali Paese, Categoria e Venditori.
Machine Learning e Forecasting
Il progetto include due componenti principali:

Machine Learning
Creazione di un dataset trimestrale con la colonna Lag1 (valore del trimestre precedente).
Applicazione di modelli di regressione:
RandomForest
XGBoost
Time Series Forecasting
ARIMA per previsioni mensili.
Prophet per previsioni trimestrali.
API AI Locale
È stata implementata un'API con FastAPI che offre due endpoint:

POST /predict: Accetta un JSON con un campo text e restituisce l'analisi del sentiment tramite un modello pre-addestrato di Hugging Face.
GET /deep_analysis: Legge il file sales_merged.csv e fornisce raccomandazioni basate sull'analisi dei trend storici.
Avvio del Server
Per lanciare il server API, utilizzare il comando:

bash
Copia
uvicorn local_ai_api:app --host 0.0.0.0 --port 8000 --reload
È possibile testare l'API utilizzando strumenti come curl o Postman.

Analisi Avanzata
Una sezione dedicata del notebook fornisce un'analisi dettagliata:

Scenario Baseline: Previsione del trend naturale delle vendite.
Scenario +10%: Simulazione dell'impatto di azioni di marketing, brand awareness e miglior supporto al cliente che portano ad un aumento ipotetico del 10% delle vendite.
Viene mostrato un confronto grafico tra i due scenari e fornito un testo descrittivo estremamente dettagliato che:
Analizza lo stato attuale e le previsioni per i prossimi 4 trimestri.
Suggerisce azioni strategiche per migliorare margini, vendite, brand awareness e soddisfazione dei clienti.
Conclusioni
Il progetto dimostra come integrare:

Data Engineering: Unione e pulizia dei dati.
Data Analysis: Estrazione di KPI e analisi delle distribuzioni.
Machine Learning & Forecasting: Previsioni dei trend di vendita con modelli statistici e ML.
API AI Locale: Implementazione di un servizio di analisi del sentiment e raccomandazioni basate sui dati.
Analisi Avanzata: Scenari futuri e suggerimenti strategici per decisioni aziendali mirate.
Questo flusso completo è pensato per essere un esempio pratico e d'ispirazione per colleghi, recruiter e appassionati del settore.

Contatti
Raffaele Schiavone
Data Scientist & Data Analyst | Business Intelligence & Automation Expert
GitHub Repository

Grazie per l'attenzione!

css
Copia

Questo README in formato Markdown verrà visualizzato correttamente su GitHub, facilitando la consultazione e la comprensione del progetto.