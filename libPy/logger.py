import logging
import sys

def new(name: str = 'app', exclude_name: bool = False):
  
  logger = logging.getLogger(name)
  logger.setLevel(logging.INFO)

  # format: [INFO] 29-12-2026 13:59:59: 
  regularFormat = '[%(name)s] [%(levelname)s] [%(asctime)s]: %(message)s'
  excludeNameFormat = '[%(levelname)s] [%(asctime)s]: %(message)s'
  format = regularFormat if exclude_name == False else excludeNameFormat
  formatter = logging.Formatter(
    format,
    datefmt = '%d-%m-%y %H:%M:%S'
  )

  handler = logging.StreamHandler(sys.stdout)
  handler.setFormatter(formatter)

  if not logger.handlers:
    logger.addHandler(handler)

  return logger
