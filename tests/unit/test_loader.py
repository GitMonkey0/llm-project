from llm_project.data.loader import build_dataloader

def test_loader():
    cfg = {"path": "tatsu-lab/alpaca", "streaming": True}
    ds = build_dataloader(cfg)
    assert ds is not None
