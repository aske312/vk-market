# -*- coding: utf-8 -*-

import logging
from datetime import datetime

log = logging.getLogger('VkBot')
data_now = datetime.now().strftime("%m-%d-%Y-")


def config_logging():
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(logging.Formatter(f'%(levelname)s %(message)s'))
    stream_handler.setLevel(logging.INFO)
    log.addHandler(stream_handler)

    file_handler = logging.FileHandler(f'logs/{data_now}bot_worker.log')
    file_handler.setFormatter(logging.Formatter(f'%(asctime)s %(name)s %(funcName)s %(levelname)s %(message)s',
                                                datefmt='%Y-%m-%d %H:%M'))
    file_handler.setLevel(logging.DEBUG)
    log.addHandler(file_handler)
    log.setLevel(logging.DEBUG)
