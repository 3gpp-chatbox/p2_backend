import logging

<<<<<<< HEAD
=======

>>>>>>> 4555043bb0ffe470fc876bae43cd576bf033c15d
def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
<<<<<<< HEAD
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
=======
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
>>>>>>> 4555043bb0ffe470fc876bae43cd576bf033c15d
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
