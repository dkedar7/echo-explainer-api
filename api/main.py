from fastapi import FastAPI
from explainer import explainer

app = FastAPI()

@app.get('/explain/')
def explain_echo(text: str):
    try:
        return {"explanation": explainer(text)}
    except Exception as e:
        return {"explanation": str(e)}