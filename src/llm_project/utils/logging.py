import logging

def setup_logger(name="llm"):
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)
