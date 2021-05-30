import logging
import sys

INITIALIZED = False

if not INITIALIZED:
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.DEBUG,
        format='%(asctime)s %(name)s %(levelname)s %(message)s',
    )

    INITIALIZED = True

logger = logging.getLogger()
