import os
import sys
import logging


logging_src = "[%(asctime)s: %(levelname)s: %(module)s: %(lineno)d: %(message)s]"
log_dir="logs"
log_file_path = os.path.join(log_dir, "text_summarizer.log")
os.makedirs(log_dir, exist_ok=True)

logging_config = logging.basicConfig(
    level=logging.INFO,
    format=logging_src,
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("textSummarizerLogger")