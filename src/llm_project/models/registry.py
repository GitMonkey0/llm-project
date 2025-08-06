from transformers import AutoModelForCausalLM, AutoTokenizer

def get_model_tokenizer(cfg):
    return AutoModelForCausalLM.from_pretrained(**cfg), AutoTokenizer.from_pretrained(**cfg)
