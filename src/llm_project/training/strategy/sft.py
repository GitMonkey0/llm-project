# src/llm_project/training/trainers/sft.py
from trl import SFTTrainer as TRLSFTTrainer
from trl import SFTConfig

class SFTTrainer(TRLSFTTrainer):
    """
    Drop-in replacement for the generic Trainer.
    All cfg.train keys are forwarded to SFTConfig.
    """
    def __init__(self, model, train_dataset, eval_dataset, **kwargs):
        cfg_keys = {k: kwargs.pop(k) for k in list(kwargs) if hasattr(SFTConfig, k)}
        args = SFTConfig(**cfg_keys)
        super().__init__(
            model=model,
            args=args,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            **kwargs
        )