import hydra
from llm_project.inference.predictor import Predictor

@hydra.main(config_path="../configs", config_name="config")
def main(cfg):
    predictor = Predictor(cfg.model)
    print("evaluate stub")

if __name__ == "__main__":
    main()
