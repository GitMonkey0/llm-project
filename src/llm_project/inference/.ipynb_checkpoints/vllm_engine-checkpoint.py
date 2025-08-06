from vllm import LLM

class VLLMEngine:
    def __init__(self, cfg):
        self.llm = LLM(model=cfg.pretrained_model_name_or_path)

    def generate(self, prompts):
        return [o.outputs[0].text for o in self.llm.generate(prompts)]
