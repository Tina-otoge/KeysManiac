import logging
import pathlib

logger = logging.getLogger(pathlib.PurePath(__file__).parent.name)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(
    '{levelname}: {message}',
    style='{'
))
logger.addHandler(stream_handler)
logger.setLevel(logging.INFO)
