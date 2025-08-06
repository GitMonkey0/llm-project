from peft import get_peft_model, LoraConfig

def add_lora(model, cfg):
    return get_peft_model(
        model,
        LoraConfig(r=cfg.lora_rank, lora_alpha=cfg.lora_alpha),
    )
