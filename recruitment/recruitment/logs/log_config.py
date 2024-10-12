"""Logger settings"""
import logging
from sys import stderr
LOGGER = logging.getLogger('logger')
FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

STREAM_HANDLER = logging.StreamHandler(stderr)
STREAM_HANDLER.setFormatter(FORMATTER)
STREAM_HANDLER.setLevel(logging.INFO)
LOGGER.addHandler(STREAM_HANDLER)
LOGGER.setLevel(logging.INFO)
