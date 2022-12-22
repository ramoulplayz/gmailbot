import logging


def logger(name, mode='w', file='log.log'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    formatter = logging.Formatter('%(asctime)s ~ %(levelname)s: %(message)s')
    fileHandler = logging.FileHandler(file, encoding='utf_8_sig', mode=mode)
    fileHandler.setLevel(logging.INFO)
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    return logger
