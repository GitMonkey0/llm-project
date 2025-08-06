install:
	poetry install
train:
	poetry run python scripts/train.py experiment=sft_llama3_qlora
serve:
	poetry run python scripts/serve.py
test:
	poetry run pytest tests/
