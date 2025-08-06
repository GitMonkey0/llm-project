from transformers import TrainerCallback

class LoggingCallback(TrainerCallback):
    def on_log(self, *args, **kwargs):
        print("LOG:", kwargs["logs"])
