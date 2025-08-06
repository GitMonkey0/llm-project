import hydra
from llm_project import get_model_tokenizer, build_dataloader, apply_formatting, Trainer

@hydra.main(config_path="../configs", config_name="config", version_base=None)
def main(cfg):
    model, tokenizer = get_model_tokenizer(cfg.model)
    raw_dataset = build_dataloader(cfg.data)
    dataset = apply_formatting(raw_dataset)
    Trainer(cfg).train(model, dataset)

if __name__ == "__main__":
    main()
