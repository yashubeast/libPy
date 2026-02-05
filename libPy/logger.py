import colorlog
import logging
import sys

def new(name: str = 'app', exclude_name: bool = False):
  
  logger = logging.getLogger(name)
  logger.setLevel(logging.INFO)

  # format: [app] [INFO] 29-12-2026 13:59:59: message
  regularFormat = '%(log_color)s[%(name)s] [%(levelname)s] [%(asctime)s]: %(message)s%(reset)s'
  # format: [INFO] 29-12-2026 13:59:59: message
  excludeNameFormat = '%(log_color)s[%(levelname)s] [%(asctime)s]: %(message)s%(reset)s'
  format = regularFormat if exclude_name == False else excludeNameFormat

  formatter = colorlog.ColoredFormatter(
    format,
    datefmt = '%d-%m-%Y %H:%M:%S',
    log_colors={
      'DEBUG': 'purple',
      'INFO': 'green',
      'WARNING': 'yellow',
      'ERROR': 'red',
      'CRITICAL': 'red, bg_white',
    }
  )

  # handler
  handler = logging.StreamHandler(sys.stdout)
  handler.setFormatter(formatter)
  if not logger.handlers:
    logger.addHandler(handler)

  return logger
