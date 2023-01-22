import logging
import sys


def get_new_logger():
    log = logging.getLogger()
    level = logging.INFO
    log.setLevel(level)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    log.addHandler(handler)

    return log


logger = get_new_logger()
