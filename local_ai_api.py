import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import pandas as pd
import os

MODEL_NAME_SENTIMENT = "nlptown/bert-base-multilingual-uncased-sentiment"

app = FastAPI(
    title="Adventure Works Local AI API",
    description="API che analizza testo (sentiment) e fornisce raccomandazioni sui dati storici.",
    version="1.2"
)

class TextInput(BaseModel):
    text: str

sentiment_pipeline = None

@app.on_event("startup")
def load_model():
    global sentiment_pipeline
    print("[INFO] Caricamento del modello di sentiment...")
    sentiment_pipeline = pipeline("sentiment-analysis", model=MODEL_NAME_SENTIMENT)
    print("[INFO] Modello caricato correttamente!")

@app.get("/")
def root():
    return {"message": "Local AI API Avviata. POST /predict per sentiment, GET /deep_analysis per analisi storica."}

@app.post("/predict")
def predict_sentiment(item: TextInput):
    global sentiment_pipeline
    if not sentiment_pipeline:
        return {"error": "Pipeline non caricata."}
    result = sentiment_pipeline(item.text)
    return {
        "input_text": item.text,
        "analysis": result
    }

@app.get("/deep_analysis")
def deep_analysis():
    path_data = "sales_merged.csv"
    if not os.path.exists(path_data):
        return {"error": "File sales_merged.csv non trovato. Salva i dati dal Notebook prima di /deep_analysis."}

    df = pd.read_csv(path_data)
    total_sales = df['Total Sales'].sum()
    total_profit = df['Profit'].sum()
    margin_avg = df['Profit Margin'].mean()

    df_sorted = df.sort_values(by=['Year','Quarter'])
    if df_sorted.shape[0] < 2:
        return {"warning": "Dataset insufficiente per valutare un trend."}

    last_sales = df_sorted.iloc[-1]['Total Sales']
    prev_sales = df_sorted.iloc[-2]['Total Sales']

    if last_sales < prev_sales:
        trend = "negativo"
        scenario_msg = (
            "Le vendite sono in calo rispetto al trimestre precedente. "
            "Se non si cambia strategia, il profitto potrebbe diminuire ulteriormente. "
            "Suggerisco investimenti in marketing, formazione venditori e azioni mirate a "
            "migliorare il sentiment dei clienti."
        )
    elif last_sales > prev_sales:
        trend = "positivo"
        scenario_msg = (
            "Le vendite sono in crescita! Continuate le azioni intraprese, "
            "monitorando i KPI e valutando ulteriori investimenti mirati per "
            "brand awareness e soddisfazione clienti."
        )
    else:
        trend = "stabile"
        scenario_msg = (
            "Le vendite sono stabili rispetto al periodo precedente. Potrebbe essere "
            "una fase di transizione, valutate possibili interventi se volete spingere "
            "di più sul fatturato e la fidelizzazione clienti."
        )

    return {
        "TotaleVendite": float(total_sales),
        "ProfittoTotale": float(total_profit),
        "MargineMedio": float(margin_avg),
        "TrendRecente": trend,
        "Raccomandazione": scenario_msg
    }
