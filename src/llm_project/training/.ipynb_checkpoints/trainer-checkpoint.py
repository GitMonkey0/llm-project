# src/llm_project/training/trainer.py
from hydra.utils import instantiate
from typing import Any

class Trainer:
    """
    Thin router: `cfg.train._target_` decides the real trainer.
    All other keys are forwarded as **kwargs.
    """
    def __init__(self, cfg: Any):
        self.cfg = cfg

    def train(self, model, dataset):
        trainer = instantiate(self.cfg.train, model=model, train_dataset=dataset["train"], eval_dataset=dataset["validation"])
        trainer.train()