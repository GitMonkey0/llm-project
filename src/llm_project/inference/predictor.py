from .vllm_engine import VLLMEngine

class Predictor:
    def __init__(self, cfg):
        self.engine = VLLMEngine(cfg)

    def predict(self, text):
        return self.engine.generate([text])[0]
