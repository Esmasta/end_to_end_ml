import logging
import os
from datetime import datetime

# Step 1: Create filename based on date
log_filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

# Step 2: Create logs directory and full path
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)
log_file_path = os.path.join(logs_dir, log_filename)

# Step 3: Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)