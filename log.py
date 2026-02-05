import logging
import sys

def get_logger(name: str):
  
  logger = logging.getLogger(name)
  logger.setLevel(logging.INFO)

  # format: [INFO] 29-12-2026 13:59:59: 
  formatter = logging.Formatter(
    '[%(name)s] [%(levelname)s] [%(asctime)s]: %(message)s',
    datefmt = '%d-%m-%y %H:%M:%S'
  )

  handler = logging.StreamHandler(sys.stdout)
  handler.setFormatter(formatter)

  if not logger.handlers:
    logger.addHandler(handler)

  return logger
