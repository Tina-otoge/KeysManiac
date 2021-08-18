import logging
from pyglet import font


logger = logging.getLogger(__name__)

def setup_logger():
    logger.setLevel(logging.DEBUG)
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter('{levelname}:{message}', style='{'))
    logger.addHandler(console)


def setup_fonts():
    font.add_directory('resources/fonts')
    for name in ['Symtext']:
        if not font.have_font(name):
            logger.warning(f'Missing font "{name}"')

from . import scenes
