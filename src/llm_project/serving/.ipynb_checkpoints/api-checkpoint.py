from fastapi import FastAPI
from pydantic import BaseModel
from ..inference.predictor import Predictor

app = FastAPI()
predictor = None

class Req(BaseModel):
    prompt: str

@app.post("/generate")
def generate(req: Req):
    return {"text": predictor.predict(req.prompt)}

@app.on_event("startup")
def startup():
    global predictor
    from hydra import compose, initialize
    with initialize(config_path="../../../configs"):
        cfg = compose(config_name="config")
        predictor = Predictor(cfg.model)