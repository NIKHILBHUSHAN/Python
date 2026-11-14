from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler
import logging
"""logging.basicConfig(level=logging.DEBUG,format="%(asctime)s- %(name)s - %(levelname)s- %(message)s")
logging.debug("Debugging application")
logging.info("application started")
logging.warning("Low memory")
logging.error("Unable to process a request")
logging.critical("Database connectino failed")"""

logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

stream_h=logging.StreamHandler()
file_h=logging.FileHandler("file.log")
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter=logging.Formatter("%(name)s - %(levelname)s - %(message)s")
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.propagate=False

rothandler=RotatingFileHandler("rotate.log",maxBytes=2000,backupCount=5)
rothandler.setLevel(logging.DEBUG)
rothandler.setFormatter(formatter)
timehandler=TimedRotatingFileHandler("time.log",when="s",interval=5,backupCount=5)
timehandler.setLevel(logging.DEBUG)
rothandler.setFormatter(formatter)

logger.addHandler(rothandler)
logger.addHandler(timehandler)

logger.debug("Debug message")
logger.info("Application started")
logger.warning("Low memory")
logger.error("unale to process a request")
logger.critical("database conectino failed")






